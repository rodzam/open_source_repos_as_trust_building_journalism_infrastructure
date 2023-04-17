#!/usr/bin/python3
## Load libraries
import pandas as pd
import glob, json, re, yaml, os

## Load variables
with open("config.yml", "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)
save_dir = cfg["directories"]["data_directory"]
master_repo_list = os.path.normpath("%s/%s" % (save_dir, cfg["files"]["list_of_repositories"]))
analysis_csv_dir = os.path.normpath("%s/%s" % (save_dir, cfg["directories"]["analysis_directory"]))

## Create function for generating a master CSV file for analysis
def create_analysis_csv(data_file, extension, select_columns=False, sort_by="id", filename_as_id=False, rename_columns=False, infer_from_url=False, check_exist=False):
    file_path = "%s/%s/*%s" % (save_dir, data_file, extension)
    file_list = glob.glob(file_path)
    file_list_len = len(file_list)
    dfs = []
    for i, file in enumerate(file_list):
        print("Working on %s (%s of %s in %s)" % (file, i+1, file_list_len, data_file))
        if extension == ".json":
            with open(file, "r") as f:
                file_contents = pd.json_normalize(json.load(f))
                f.close()
        elif extension == ".csv":
            with open(file, "r") as f:
                file_contents = pd.read_csv(f)
                f.close()
        if filename_as_id is not False:
            file_contents["filename_id"] = file.split("/")[-1].split(".")[0]
        dfs.append(file_contents)
    print("Starting dataframe concatenation...")
    df_master = pd.concat(dfs, ignore_index=True)
    if rename_columns is not False:
        print("Renaming columns...")
        df_master.rename(columns=rename_columns, inplace=True)
    if filename_as_id is not False:
        print("Setting the filename as the id...")
        df_master["id"] = df_master["filename_id"]
    if infer_from_url is not False:
        print("Inferring information from URL...")
        df_master["full_name"] = [re.match(infer_from_url["regex"], x)[1] for x in df_master[infer_from_url["variable"]].values.tolist()]
    if check_exist is not False:
        print("Checking is certain variables exist...")
        for item in check_exist:
            for row in df_master.itertuples():
                try:
                    if pd.isna(row.__getattribute__(item)):
                        df_master.loc[df_master.index == row.__getattribute__("Index"), item] = "FALSE"
                    else:
                        df_master.loc[df_master.index == row.__getattribute__("Index"), item] = "TRUE"
                except:
                    df_master.loc[df_master.index == row.__getattribute__("Index"), item] = "FALSE"
    print("Selecting columns...")
    if select_columns is not False and "id" in select_columns:
        df_master = df_master[select_columns]
    elif filename_as_id is not False and select_columns is not False:
        df_master = df_master[["id"] + select_columns]
    elif select_columns is not False:
        df_master = df_master[select_columns]
    elif filename_as_id is not False and select_columns is False:
        df_master = df_master.loc[:, df_master.columns != 'filename_id']
    print("Sorting dataframe...")
    df_master = df_master.sort_values(by=sort_by)
    print("Saving dataframe to CSV...")
    df_master.to_csv("%s/%s.csv" % (analysis_csv_dir, data_file), index=False)
    return


## Create CSV files
# Repo
create_analysis_csv(data_file="repo", extension=".json", select_columns=["id", "full_name", "owner.login", "name", "fork", "created_at", "pushed_at", "size", "stargazers_count", "watchers_count", "forks_count", "subscribers_count", "license.name", "parent.owner.login", "parent.name"])

# Fork Parent
create_analysis_csv(data_file="fork_parent", extension=".json", select_columns=["fork_status", "fork_ahead_by", "fork_behind_by", "fork_total_commits"], filename_as_id=True, rename_columns={"status":"fork_status", "ahead_by":"fork_ahead_by", "behind_by":"fork_behind_by", "total_commits":"fork_total_commits"})

# Fork Descendants
create_analysis_csv(data_file="fork_descendants", extension=".json", select_columns=["descendant_full_name", "parent_full_name", "descendant_created_at"], filename_as_id=True, rename_columns={"full_name":"descendant_full_name", "parent.full_name":"parent_full_name", "created_at":"descendant_created_at"})

# Issues
create_analysis_csv(data_file="issues", extension=".json", select_columns=["full_name", "issue_id", "issue_number", "issue_user_login", "issue_created_at", "issue_updated_at", "issue_closed_at", "issue_author_association", "pull_request"], sort_by=["full_name", "issue_id"], rename_columns={"id":"issue_id", "number":"issue_number", "user.login":"issue_user_login", "created_at":"issue_created_at", "updated_at":"issue_updated_at", "closed_at":"issue_closed_at", "author_association":"issue_author_association", "pull_request.url":"pull_request"}, infer_from_url={"variable":"repository_url", "regex":"https://api.github.com/repos/(.*)"}, check_exist=["pull_request"])

# Contributors
create_analysis_csv(data_file="contributors", extension=".csv", sort_by=["id", "contributor_id"], filename_as_id=True)

# Pulls
create_analysis_csv(data_file="pulls", extension=".json", select_columns=["full_name", "pull_id", "pull_number", "pull_state", "pull_user_login", "pull_author_association", "pull_created_at", "pull_updated_at", "pull_closed_at", "pull_merged_at", "pull_merged"], sort_by=["full_name", "pull_id"], rename_columns={"id":"pull_id", "number":"pull_number", "state":"pull_state", "user.login":"pull_user_login", "author_association":"pull_author_association", "created_at":"pull_created_at", "updated_at":"pull_updated_at", "closed_at":"pull_closed_at", "merged_at":"pull_merged_at", "merged":"pull_merged"}, infer_from_url={"variable":"html_url", "regex":"https://github.com/(.*)/pull"})
