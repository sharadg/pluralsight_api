# Python script for building out usage and command line parser

import datetime as dt
import argparse


def mk_date(date_string):
    return dt.datetime.strptime(date_string, '%m-%d-%Y').date()


def build_parser():
    yesterday = dt.date.today() - dt.timedelta(1)
    default_start_date = yesterday - dt.timedelta(365)
    default_end_date = yesterday

    parser = argparse.ArgumentParser(description='Python script for interacting with Pluralsight Reporting APIs')

    date_group = parser.add_argument_group('Reporting Period', 'Start and End dates to pull the data for')
    date_group.add_argument("-d", "--delta_days", help="Incremental data based on last X days (default 1)",
                            nargs='?', const=1, type=int)
    date_group.add_argument("-s", "--start_date", help="Filter records by specifying start date in mm-dd-yyyy format",
                            nargs='?', default=default_start_date, const=default_start_date, type=mk_date)
    date_group.add_argument("-e", "--end_date", help="Filter records by specifying end date in mm-dd-yyyy format",
                            nargs='?', default=default_end_date, const=default_end_date, type=mk_date)

    objects_group = parser.add_argument_group('Asset types to pull',
                                              'Choice of assets to pull: Users, Course Completion, Course Usage')
    objects_group.add_argument("-u", "--users",
                               help="Get All Users (note: start_date and end_date have no effect on this option)",
                               action="store_true", default=False)
    objects_group.add_argument("-c", "--course_completion", help="Get Course Completion data", action="store_true",
                               default=False)
    objects_group.add_argument("-g", "--course_usage", help="Get Course Usage data", action="store_true", default=False)

    args = parser.parse_args()

    if args.delta_days is not None:
        args.start_date = yesterday - dt.timedelta(args.delta_days)
        args.end_date = yesterday

    return parser, args
