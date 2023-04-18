# Open-Source Repositories as Trust-Building Journalism Infrastructure: Examining the Use of GitHub by News Outlets to Promote Transparency, Innovation, and Collaboration

## Description

This repository contains all of the source files, data collection scripts, codebook, final datasets, and the data analysis reports for the study titled, ["Open-Source Repositories as Trust-Building Journalism Infrastructure: Examining the Use of GitHub by News Outlets to Promote Transparency, Innovation, and Collaboration."](https://doi.org/10.1080/21670811.2023.2202873) A free preprint of the paper is [available here](https://rodrigozamith.com/pubs/open-source-repositories-as-trust-building-journalism-infrastructure.pdf).

### Citation

Zamith, R. (2023). Open-Source Repositories as Trust-Building Journalism Infrastructure: Examining the Use of GitHub by News Outlets to Promote Transparency, Innovation, and Collaboration. *Digital Journalism*. Advance Online Publication. https://doi.org/10.1080/21670811.2023.2202873

A BibTeX citation is [available here](citation.bib).

## Features

* The `supplemental` directory contains two appendices to the study:
    * The list of organizations and accounts studied ([`supplemental/list_of_organizations.md`](supplemental/list_of_organizations.md)).
    * The codebook used for the manual content analysis ([`supplemental/codebook.md`](supplemental/codebook.md)).

* The `data` directory contains all of the *processed* data used in the study.
    * These files are effectively slices of the GitHub API data, converted to CSV format, to make analysis easier.
    * The directory also includes the human-coded data ([`data/analysis_data/coded_repos.csv`](data/analysis_data/coded_repos.csv)) and a CSV version of the list of organizations and accounts that were analyzed ([`data/list_of_orgs.csv`](data/list_of_orgs.csv)).
    * The JSON files containing the raw API responses from GitHub (at the time of data collection) are available upon request.

* The `method` directory contains all of the data collection scripts used in the study.
    * Only a partial replication is possible because some repositories or users may have been deleted from GitHub since the study data were collected in August, 2002. In other words, the resulting files/results are likely to differ from those reported in the study.

* The `analysis` directory contains the R Notebook files necessary to replicate the analysis with the data provided in this repository.
    * The file [`analysis/data_analysis.html`](analysis/data_analysis.html) contains a rendered version of the main data analysis notebook. This is the file you're most likely to be interested in if you want to see every step of the analysis.

## Usage Details

If you wish to replicate the analysis or conduct a follow-up study, please follow the following steps. By performing the steps below, you will overwrite the data that came with your download of this repository.

1. Download [the latest release](releases/latest) and unzip the file. Alternatively, you can just clone this repository if you already have `git` installed.

2. Create a CSV file in the `data` directory called `list_of_orgs.csv`. That file should contain the following variables:
    * `Organization Name`: The name of the news organization.
    * `Parent Organization`: If you wish to relate one organization to another (e.g., a subsidiary), enter the `Organization Name` of the parent organization.
    * `Has GitHub Account`: Enter "Y" if the organization has a GitHub account.
    * `Accounts`: List all of the accounts associated with that organization, separated by a comma and a space (`, `).
    * You may include additional fields; these *should* be ignored by the data collection and analysis pipeline by default.

3. Download [Python](https://www.python.org/) (version 3.0 or higher), in case it is not already installed on your computer. *(Python 3.9.13 was used to collect the data.)*
    * The following libraries were used and may be installed using a Python library manager like `pip3` (that comes with a typical Python installation):
        * [Pandas](https://pypi.org/project/pandas/) (`pip3 install pandas`)
        * [PyGithub](https://pypi.org/project/PyGithub/) (`pip3 install PyGithub`)
        * [PyYAML](https://pypi.org/project/PyYAML/) (`pip3 install PyYAML`)

3. Get [a personal access token from GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token). Then, edit the `config.yml` file in the `method` directory, replacing the `github_token` value with your token.

4. Open your Terminal (MacOS/Linux) or Command Prompt (Windows), go into the directory go into the `method` directory (`cd method/`).

5. Get the list of GitHub repositories (and general repository data) from the desired organizations by executing `python3 get_repo_info.py` in your terminal. This will create a file called `list_of_repos.csv` in your `data` directory. It will also create a JSON file with the raw API response for each repository queried and place that file in the `data/repo` subdirectory.

6. Get detailed repository information by executing `python3 get_repo_details.py`. This will create several new subdirectories in your `data` directory containing the JSON files with raw API responses from different API endpoints for each of the repositories listed in the `list_of_repos.csv` file. *(This will take a few days to fully execute due to API limitations and will produce a large number of files.)*

7. Create consolidated CSV files containing subsets of the JSON files generated in the previous step by executing `python3 create_csv_for_analysis.py`. This will create a new subdirectory of `data` called `analysis_data`, which will contain the CSV files that will be used by the data analysis R Notebooks.
    * The JSON files are not required for the subsequent data analysis steps. Only the `data/list_of_orgs.csv` file and the files in the `data/analysis_data/` files are needed for the subsequent step.

8. Using [RStudio](https://www.rstudio.com/) (which depends on [R](https://www.r-project.org/)), create a project with a working directory rooted in the `analysis/` directory (`File` --> `New Project` --> `Existing Directory` --> the `analysis` subdirectory of the directory containing the project files). Alternatively, you may open each .Rmd file separately within RStudio.
    * The [`analysis/generate_samples.Rmd`](analysis/generate_samples.Rmd) file contains the R code used to generate the samples for the intercoder reliability assessment and the eventual human content analysis.
    * The [`analysis/intercoder_reliability.Rmd`](analysis/intercoder_reliability.Rmd) file contains the R code used to perform the intercoder reliability assessment.
    * The [`analysis/data_analysis.Rmd`](analysis/data_analysis.html) file contains the R code used to perform all of the data analysis reported in the paper and to generate the associated Figure images.
    * To execute the R Notebooks, be sure to install all of the required packages first. You may do so by executing the following code in the RStudio console: `install.packages(c("jsonlite", "tidyverse", "lubridate", "scales", "gridExtra", "irr"))`

## License

All of the data collection scripts, codebook, and data analysis reports are made available through a Creative Commons Attribution 4.0 International license. For more information, see the [LICENSE](LICENSE) file. Data collected from the GitHub API may be subject to different copyright restrictions.
