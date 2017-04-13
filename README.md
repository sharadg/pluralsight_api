# pluralsight_api
Pluralsight Reporting API - Python Client

Simple python program to download reporting data from [Pluralsight API](https://app.pluralsight.com/plans/api/reports/docs). You need to have python3 installed alongwith optional packages (requests, argparse). 

Before using the program, please set couple of environment variables PLURALSIGHT_PLAN_ID and PLURALSIGHT_TOKEN_ID. You can find the values of these variables from your plan administration screen (https://app.pluralsight.com/plans/account/<plan_id>/integrations)

```/bin/bash
export PLURALSIGHT_PLAN_ID=<plan_id>
export PLURALSIGHT_TOKEN_ID=<token_id>
```

## Usage for python script

```
usage: reporting_api.py [-h] [-o OUTPUT_FOLDER] [-d [DELTA_DAYS]]
                        [-s [START_DATE]] [-e [END_DATE]] [-u] [-c] [-g]

Python script for interacting with Pluralsight Reporting APIs

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_FOLDER, --output_folder OUTPUT_FOLDER
                        Path to where the data files will go (default: current
                        folder)

Reporting Period:
  Start and End dates to pull the data for

  -d [DELTA_DAYS], --delta_days [DELTA_DAYS]
                        Incremental data based on last X days (default: 1)
  -s [START_DATE], --start_date [START_DATE]
                        Filter records by specifying start date in mm-dd-yyyy
                        format
  -e [END_DATE], --end_date [END_DATE]
                        Filter records by specifying end date in mm-dd-yyyy
                        format

Asset types to pull:
  Choice of assets to pull: Users, Course Completion, Course Usage

  -u, --users           Get All Users (note: start_date and end_date have no
                        effect on this option)
  -c, --course_completion
                        Get Course Completion data
  -g, --course_usage    Get Course Usage data
```

## Examples of script usage:
### Download last 30 days worth of data from users, course completion and course usage APIs.

```
python reporting_api.py -d 30 -u -c -g -o /tmp
Pulling Pluralsight Reporting data starting from 2017-03-13 and ending at 2017-04-12
Pulling users
Created file: /tmp/adventureworks_users_20170413_180853.csv
Pulling course completion
Created file: /tmp/adventureworks_course_completion_20170413_180855.csv
Pulling course usage
Created file: /tmp/adventureworks_course_usage_20170413_180858.csv
```

### Download data from course completion APIs based on specific start and end dates.

```
python reporting_api.py -s 01-01-2017 -e 03-01-2017 -c -o /tmp
Pulling Pluralsight Reporting data starting from 2017-01-01 and ending at 2017-03-01
Pulling course completion
Created file: /tmp/adventureworks_course_completion_20170413_180947.csv
```

### Download all available data (last 1 year) from users, course completion and course usage APIs.
```
python reporting_api.py -o /tmp -ucg
Pulling Pluralsight Reporting data starting from 2016-04-12 and ending at 2017-04-12
Pulling users
Created file: /tmp/adventureworks_users_20170413_181024.csv
Pulling course completion
Created file: /tmp/adventureworks_course_completion_20170413_181026.csv
Pulling course usage
Created file: /tmp/adventureworks_course_usage_20170413_181030.csv
```
