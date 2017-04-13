# Python script for GETting Pluralsight Reporting API

import requests


def _url(path):
    return "https://app.pluralsight.com/plans/api/reports/v1" + path


def get_users(plan_id, token_id):
    return requests.get(_url('/users/{plan_id}?token={token_id}'.format(plan_id=plan_id, token_id=token_id)))


def get_course_completion(plan_id, token_id, start_date=None, end_date=None):
    if start_date is not None and end_date is not None:
        return requests.get(
            _url('/course-completion/{plan_id}?token={token_id}&startDate={start_date}&endDate={end_date}'.format(
                plan_id=plan_id, token_id=token_id, start_date=start_date, end_date=end_date)))
    else:
        return requests.get(
            _url('/course-completion/{plan_id}?token={token_id}'.format(plan_id=plan_id, token_id=token_id)))


def get_course_usage(plan_id, token_id, start_date=None, end_date=None):
    if start_date is not None and end_date is not None:
        return requests.get(_url(
            '/course-usage/{plan_id}?token={token_id}&startDate={start_date}&endDate={end_date}'.format(
                plan_id=plan_id, token_id=token_id, start_date=start_date, end_date=end_date)))
    else:
        return requests.get(_url('/course-usage/{plan_id}?token={token_id}'.format(plan_id=plan_id, token_id=token_id)))
