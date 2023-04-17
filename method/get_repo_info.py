#!/usr/bin/python3
## Load libraries
from github import Github
import pandas as pd
import csv, time, datetime, json, os, traceback, yaml

## Load variables
with open("config.yml", "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)
initiate = cfg["user_config"]["initiate_files"]
reset_error_log = cfg["user_config"]["reset_error_log"]
github_access_token = cfg["user_config"]["github_token"]
api_call_safety = cfg["user_config"]["api_call_safety"]
save_dir = cfg["directories"]["data_directory"]
org_spreadsheet = os.path.normpath("%s/%s" % (save_dir, cfg["files"]["list_of_organizations"]))

## Get a list of the organizations
org_df = pd.read_csv(org_spreadsheet)
accounts = org_df[org_df['Has GitHub Account'] == "Y"][['Organization Name', 'Accounts']].values.tolist()
#accounts = org_df[org_df['Scrape'] == "Y"][['Organization Name', 'Accounts']].values.tolist() # Use this if you want to be explicit about which accounts to scrape
accounts_list = []
for organization, account in accounts:
    if "," in account:
        accounts_list += [[organization, x] for x in account.split(", ")]
    else:
        accounts_list += [[organization, account]]

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


## Get information for each account
i_account = 0
total_accounts = len(accounts_list)
account_response = [["repo_id", "repo_owner", "repo_name", "repo_json"]]
for organization, account in accounts_list:
    if account.startswith("https://github.com/"):
        account = account[len("https://github.com/"):]

    repo_listing = []
    try:
        account_repos = g.get_user(account).get_repos()
        total_repos = account_repos.totalCount
        i_repo = 0
        for repo in account_repos:
            # Get repo id
            try:
                check_limits()
                repo_id = repo.id
                repo_name = repo.name
                print("Working on %s/%s (%s of %s accounts, %s of %s repos)" % (account, repo_name, i_account+1, total_accounts, i_repo+1, total_repos))
            except:
                record_error(account=account, repo_id=repo_id, error_msg=traceback.format_exc())
                continue

            # Create JSON for repo data
            #print("Getting repo data... [%s/%s (%s of %s accounts, %s of %s repos)]" % (account, repo_name, i_account+1, total_accounts, i_repo+1, total_repos))
            try:
                repo_json = repo.raw_data
                with open("%s/repo/%s.json" % (save_dir, repo_id), "w") as f:
                    json.dump(repo_json, f)
                    f.close()
            except:
                record_error(account=account, repo_id=repo_id, error_msg=traceback.format_exc())
                continue

            # Proceed to next repo
            i_repo += 1

        # Proceed to next account
        i_account += 1
    except:
        record_error(account=account, repo_id=repo_id, error_msg=traceback.format_exc())
        continue

# Report completion
print("We're done getting the repo information!")
