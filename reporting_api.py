# Scratch Python script for GETting Pluralsight Reporting API

import os
import requests
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


def attachment_name(headers):
    return headers["Content-Disposition"].split("=")[1]


def write_file(response):
    # with open("./users_{}.csv".format(datetime.now().strftime("%d-%m-%Y_%H%M%S")), 'w') as file:
    with open(attachment_name(response.headers), 'w', encoding='utf-8') as file:
        file.write(response.text)


def get_users():
    try:
        resp = psapi.get_users(plan_id, token_id)
        if resp.status_code != requests.codes.ok:
            print("Pluralsight API Get Users: Status Code {}".format(resp.status_code))
        write_file(resp)
    except Exception:
        print("Couldn't complete the request")
        exit(1)


def get_course_completion(start_date, end_date):
    try:
        resp = psapi.get_course_completion(plan_id, token_id, start_date, end_date)
        if resp.status_code != requests.codes.ok:
            print("Pluralsight API Course Completion {}".format(resp.status_code))

        write_file(resp)
    except Exception:
        print("Couldn't complete the request")
        exit(1)


def get_course_usage(start_date, end_date):
    try:
        resp = psapi.get_course_usage(plan_id, token_id, start_date, end_date)
        if resp.status_code != requests.codes.ok:
            print("Pluralsight API Course Usage {}".format(resp.status_code))

        write_file(resp)
    except Exception:
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
        get_users()

    if args.course_completion:
        print("Pulling course completion")
        get_course_completion(args.start_date, args.end_date)

    if args.course_usage:
        print("Pulling course usage")
        get_course_usage(args.start_date, args.end_date)


if __name__ == "__main__":
    main()
