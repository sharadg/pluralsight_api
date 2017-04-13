# pluralsight_api
Pluralsight Reporting API - Python Client

Simple python program to download reporting data from [Pluralsight API](https://app.pluralsight.com/plans/api/reports/docs). You need to have python3 installed alongwith optional packages (requests, argparse). 

```
usage: reporting_api.py [-h] [-d [DELTA_DAYS]] [-s [START_DATE]]
                        [-e [END_DATE]] [-u] [-c] [-g]

Python script for interacting with Pluralsight Reporting APIs

optional arguments:
  -h, --help            show this help message and exit

Reporting Period:
  Start and End dates to pull the data for

  -d [DELTA_DAYS], --delta_days [DELTA_DAYS]
                        Incremental data based on last X days (default 1)
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
1. Download last 30 days worth of data from users, course completion and course usage APIs.

```
python reporting_api.py -d 30 -u -c -g
Pulling Pluralsight Reporting data starting from 2017-03-13 and ending at 2017-04-12
Pulling users
Pulling course completion
Pulling course usage
```

2. Download data from course completion APIs based on specific start and end dates.

```
python reporting_api.py -s 01-01-2017 -e 03-01-2017 -c
Pulling Pluralsight Reporting data starting from 2017-01-01 and ending at 2017-03-01
Pulling course completion
```

3. Download all available data (last 1 year) from users, course completion and course usage APIs.
```
python reporting_api.py -ucg
Pulling Pluralsight Reporting data starting from 2016-04-12 and ending at 2017-04-12
Pulling users
Pulling course completion
Pulling course usage
```
