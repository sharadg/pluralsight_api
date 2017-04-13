# Scratch Python script for GETting Pluralsight Reporting API

import os
import requests
import datetime as dt
from parser import build_parser
import pluralsight as psapi

plan_id = os.getenv('PLURALSIGHT_PLAN_ID', '')
token_id = os.getenv('PLURALSIGHT_TOKEN_ID', '')


def valid_env_vars():
    if len(plan_id) == 0 or len(token_id) == 0:
        print(
            "Please set Environment variables. " +
            "Current values for PLURALSIGHT_PLAN_ID: ({}) and PLURALSIGHT_TOKEN_ID: ({})".format(
                plan_id, token_id))
        print("")
        return False
    else:
        return True


def extract_filename(headers):
    return headers["Content-Disposition"].split("=")[1]


def mk_path(output_folder, filename):
    # with open("./users_{}.csv".format(datetime.now().strftime("%d-%m-%Y_%H%M%S")), 'w') as file:
    name, dot, extension = str(filename).partition(".")
    output_file = os.path.join(os.path.abspath(output_folder),
                               name + "_" + dt.datetime.now().strftime("%H%M%S") + dot + extension)
    return output_file


def write_file(response, output_folder=None):
    if output_folder is None:
        output_folder = os.getcwd()

    with open(mk_path(output_folder, extract_filename(response.headers)), 'w', encoding='utf-8') as file:
        file.write(response.text)
        print("Created file: {}".format(file.name))


def get_users(output_folder=None):
    try:
        resp = psapi.get_users(plan_id, token_id)
        if resp.status_code != requests.codes.ok:
            print("Pluralsight API Get Users: Status Code {}".format(resp.status_code))
        write_file(resp, output_folder)
    except Exception as e:
        print("Couldn't complete the request")
        exit(1)


def get_course_completion(start_date, end_date, output_folder=None):
    try:
        resp = psapi.get_course_completion(plan_id, token_id, start_date, end_date)
        if resp.status_code != requests.codes.ok:
            print("Pluralsight API Course Completion {}".format(resp.status_code))

        write_file(resp, output_folder)
    except Exception as e:
        print("Couldn't complete the request")
        exit(1)


def get_course_usage(start_date, end_date, output_folder=None):
    try:
        resp = psapi.get_course_usage(plan_id, token_id, start_date, end_date)
        if resp.status_code != requests.codes.ok:
            print("Pluralsight API Course Usage {}".format(resp.status_code))

        write_file(resp, output_folder)
    except Exception as e:
        print("Couldn't complete the request")
        exit(1)


def main():
    parser, args = build_parser()

    if not (valid_env_vars()):
        parser.print_help()
        exit(1)

    print(
        "Pulling Pluralsight Reporting data starting from {0} and ending at {1}".format(args.start_date, args.end_date))

    if args.users:
        print("Pulling users")
        get_users(args.output_folder)

    if args.course_completion:
        print("Pulling course completion")
        get_course_completion(args.start_date, args.end_date, args.output_folder)

    if args.course_usage:
        print("Pulling course usage")
        get_course_usage(args.start_date, args.end_date, args.output_folder)


if __name__ == "__main__":
    main()
