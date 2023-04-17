#!/usr/bin/python3
## Load libraries
from github import Github
import pandas as pd
import csv, time, datetime, json, base64, glob, os, traceback, yaml

## Load variables
with open("config.yml", "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)
initiate = cfg["user_config"]["initiate_files"]
reset_error_log = cfg["user_config"]["reset_error_log"]
github_access_token = cfg["user_config"]["github_token"]
api_call_safety = cfg["user_config"]["api_call_safety"]
save_dir = cfg["directories"]["data_directory"]
master_repo_list = os.path.normpath("%s/%s" % (save_dir, cfg["files"]["list_of_repositories"]))

## Load the access token
g = Github(github_access_token)

## Create function for checking rate limits
def check_limits():
    # Check Rate Limits
    rate_limit = g.get_rate_limit()
    rate_remaining = rate_limit.core.remaining
    rate_reset = rate_limit.core.reset
    print("We have %s API calls remaining" % rate_remaining)
    if rate_remaining < api_call_safety:
        sleep_lapse = (rate_reset - datetime.datetime.utcnow()).seconds + 60
        if sleep_lapse > 3600:
            sleep_lapse = 3660
        print("Because we are nearing the rate limit, we're going to pause until it resets at %s UTC (%s seconds from now)" % (rate_reset, sleep_lapse))
        time.sleep(sleep_lapse)
    return


## Create function for logging errors
def record_error(account, repo_id, error_msg, state="a"):
    entry = [account, repo_id, error_msg]
    with open("%s/error_log.csv" % (save_dir), state) as f:
        write = csv.writer(f)
        write.writerow(entry)
        f.close()
    return


## Check if error log needs to be created or should be reinitiated
if not os.path.isfile("%s/error_log.csv" % save_dir) or reset_error_log is True:
    print("The error log does not exist or should be re-initiated, so I will create it now...")
    record_error(account="account", repo_id="repo_id", error_msg="error_msg", state="w")
else:
    print("The error log exists, so appending to that file...")


## Check if master list of repos needs to be created or should be reinitiated
if not os.path.isfile(master_repo_list) or initiate is True:
    print("A master list of repos does not exist or should be re-initiated, so I will create it now...")

    ## Get list of repos to evaluate
    repo_json_file_list = glob.glob("%s/repo/*.json" % save_dir)

    ## Create a list of all the repos with the relevant information
    master_repo_list_contents = [["repo_id", "repo_owner", "repo_name", "repo_scraped"]]
    for json_file in repo_json_file_list:
        with open(json_file, "r") as f:
            json_contents = json.load(f)
            f.close()
        repo_id = json_contents["id"]
        repo_owner = json_contents["owner"]["login"]
        repo_name = json_contents["name"]
        repo_scraped = "No"
        master_repo_list_contents.append([repo_id, repo_owner, repo_name, repo_scraped])

    ## Convert list into pandas dataframe and randomize
    master_repo_list_df = pd.DataFrame(master_repo_list_contents[1:], columns=master_repo_list_contents[0])
    master_repo_list_df = master_repo_list_df.sample(frac=1)

    ## Create a CSV file with the repo info
    master_repo_list_df.to_csv(master_repo_list, index=False)
else:
    print("A master list of repos exists, so proceeding with that...")


## Open master list of repos
print("Opening master list of repos...")
master_repo_list_df = pd.read_csv(master_repo_list)
master_repo_list_df_toscrape = master_repo_list_df[master_repo_list_df['repo_scraped'] == "No"]
master_repo_list_total = len(master_repo_list_df_toscrape.index)


## Scrape each repo
i = 0
for row in master_repo_list_df_toscrape.itertuples():
    # Get repo id
    try:
        repo_id = row.repo_id
        repo_owner = row.repo_owner
        repo_name = row.repo_name
        repo_full_name = "%s/%s" % (repo_owner, repo_name)
        print("Working on %s (%s of %s)" % (repo_full_name, i+1, master_repo_list_total))
    except:
        print("!!!ERROR: Getting repo id/name")
        record_error(account=repo_full_name, repo_id=repo_id, error_msg=traceback.format_exc())
        pass

    # Open repo JSON data
    print("Getting repo data... [%s (%s of %s repos)]" % (repo_full_name, i+1, master_repo_list_total))
    try:
        with open("%s/repo/%s.json" % (save_dir, repo_id), "r") as f:
            repo_info = json.load(f)
            f.close()
    except:
        print("!!!ERROR: Reading repo data")
        record_error(account=repo_full_name, repo_id=repo_id, error_msg=traceback.format_exc())
        pass

    # Check if it is a fork or not (record but ignore subsequent info for forks)
    print("Checking if it's a fork... [%s (%s of %s repos)]" % (repo_full_name, i+1, master_repo_list_total))
    try:
        repo_fork = repo_info["fork"]
    except:
        print("!!!ERROR: Checking if repo was a fork")
        record_error(account=repo_full_name, repo_id=repo_id, error_msg=traceback.format_exc())
        pass

    # Collect some additional information only if the repo is _NOT_ a fork
    if repo_fork is False:
        # Create JSON for pull data
        print("Getting pull data... [%s (%s of %s repos)]" % (repo_full_name, i+1, master_repo_list_total))
        try:
            repo_pulls = g.get_repo(repo_id).get_pulls(state="all")
            repo_pulls_len = repo_pulls.totalCount
            for p, pull in enumerate(repo_pulls):
                print("Getting pull #%s (of %s) [%s (%s of %s repos)]" % (p+1, repo_pulls_len, repo_full_name, i+1, master_repo_list_total))
                check_limits()
                pull_id = pull.id
                pull_json = pull.raw_data
                with open("%s/pulls/%s.json" % (save_dir, pull_id), "w") as f:
                    json.dump(pull_json, f)
                    f.close()
        except:
            print("!!!ERROR: Getting pull data")
            record_error(account=repo_full_name, repo_id=repo_id, error_msg=traceback.format_exc())
            pass

        # Create CSVs with contributor data (unfortunately, anonymous contributions break some things)
        print("Getting contributor data... [%s (%s of %s repos)]" % (repo_full_name, i+1, master_repo_list_total))
        repo_contributors_listing = [["contributor_id", "contributor_type", "contributor_info", "contributor_contributions"]]
        try:
            repo_contributors = g.get_repo(repo_id).get_contributors(anon="1")
            try:
                repo_contributors_len = repo_contributors.totalCount
                for p, contributor in enumerate(repo_contributors):
                    print("Getting contributor #%s (of %s) [%s (%s of %s repos)]" % (p + 1, repo_contributors_len, repo_full_name, i+1, master_repo_list_total))
                    check_limits()
                    try:
                        contributor_id = contributor.id
                    except:
                        contributor_id = None
                    try:
                        contributor_info = json.dumps(contributor.raw_data)
                        contributor_type = contributor.type
                    except:
                        try:
                            contributor_info = json.dumps({"email": contributor.email, "name": contributor.name})  # The raw data fails for anonymous contributions, so manually set it
                            contributor_type = contributor.type
                        except:
                            contributor_info = "!!!ERROR!!!"
                    try:
                        contributor_contributions = contributor.contributions
                    except:
                        contributor_contributions = None
                    repo_contributors_listing += [[contributor_id, contributor_type, contributor_info, contributor_contributions]]
            except:
                repo_contributors_listing += [["!!!ERROR!!!", "!!!ERROR!!!", "!!!ERROR!!!"]]
        except:
            print("!!!ERROR: Writing contributor data")
            record_error(account=repo_full_name, repo_id=repo_id, error_msg=traceback.format_exc())
            pass
        try:
            print("Writing CSV file with contributor information [%s (%s of %s repos)]" % (
            repo_full_name, i + 1, master_repo_list_total))
            with open('%s/contributors/%s.csv' % (save_dir, repo_id), 'w') as f:
                write = csv.writer(f)
                write.writerows(repo_contributors_listing)
                f.close()
        except:
            print("!!!ERROR: Writing contributor data")
            record_error(account=repo_full_name, repo_id=repo_id, error_msg=traceback.format_exc())
            pass

        # Create JSON for issues data
        print("Getting issues data... [%s (%s of %s repos)]" % (repo_full_name, i+1, master_repo_list_total))
        try:
            repo_issues = g.get_repo(repo_id).get_issues(state="all")
            repo_issues_len = repo_issues.totalCount
            for p, issue in enumerate(repo_issues):
                print("Getting issue #%s (of %s) [%s (%s of %s repos)]" % (p + 1, repo_issues_len, repo_full_name, i+1, master_repo_list_total))
                check_limits()
                issue_id = issue.id
                issue_json = issue.raw_data
                with open("%s/issues/%s.json" % (save_dir, issue_id), "w") as f:
                    json.dump(issue_json, f)
                    f.close()
        except:
            print("!!!ERROR: Getting issues data")
            record_error(account=repo_full_name, repo_id=repo_id, error_msg=traceback.format_exc())
            pass

        # Create JSON for descendant forks
        try:
            print("Getting descendant fork data... [%s (%s of %s repos)]" % (repo_full_name, i+1, master_repo_list_total))
            repo_descendant_forks = g.get_repo(repo_id).get_forks()
            repo_descendant_forks_len = repo_descendant_forks.totalCount
            for p, fork in enumerate(repo_descendant_forks):
                try: # Forks may be registered in the API but no longer exist, which results in a 404 error we must bypass
                    print("Getting fork #%s (of %s) [%s (%s of %s repos)]" % (p + 1, repo_descendant_forks_len, repo_full_name, i + 1, master_repo_list_total))
                    check_limits()
                    fork_id = fork.id
                    fork_json = fork.raw_data
                    with open("%s/fork_descendants/%s.json" % (save_dir, fork_id), "w") as f:
                        json.dump(fork_json, f)
                        f.close()
                except:
                    print("This fork no longer exists, bypassing...")
        except:
            print("!!!ERROR: Getting fork descendant data")
            record_error(account=repo_full_name, repo_id=repo_id, error_msg=traceback.format_exc())
            pass

    elif repo_fork is True: # Collect _some_ additional information only _IF_ the repo is a fork
        # Compare state of master branch in relation to parent
        print("Comparing fork state... [%s (%s of %s repos)]" % (repo_full_name, i+1, master_repo_list_total))
        try:
            repo_default_branch = repo_info["default_branch"]
            repo_parent = "%s:%s:%s" % (repo_info["parent"]["owner"]["login"], repo_info["parent"]["name"], repo_info["parent"]["default_branch"])
            repo_compare = g.get_repo(repo_id).compare(base=repo_parent, head=repo_default_branch).raw_data
            with open("%s/fork_parent/%s.json" % (save_dir, repo_id), "w") as f:
                json.dump(repo_compare, f)
                f.close()
        except:
            print("!!!ERROR: Getting fork comparison data")
            record_error(account=repo_full_name, repo_id=repo_id, error_msg=traceback.format_exc())
            pass

    # Get README for archival purposes
    print("Getting README file... [%s (%s of %s repos)]" % (repo_full_name, i+1, master_repo_list_total))
    try:
        repo_readme = base64.b64decode(g.get_repo(repo_id).get_readme().content)
        with open("%s/readme_files/%s.md" % (save_dir, repo_id), "wb") as f:
            f.write(repo_readme)
            f.close()
    except:
        print("!!!ERROR: Getting README file")
        record_error(account=repo_full_name, repo_id=repo_id, error_msg=traceback.format_exc())
        pass


    # Record the fact that the scrape was successful
    print("Successfully scraped %s (%s of %s repos); updating the master list of repos..." % (repo_full_name, i+1, master_repo_list_total))
    master_repo_list_df.loc[row.Index, "repo_scraped"] = "Yes"
    master_repo_list_df.to_csv(master_repo_list, index=False)

    # Proceed to next row
    i += 1

# Report completion
print("We're done scraping the repo details!")
