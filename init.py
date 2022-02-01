from typing import Text, List
import google.auth
from google.auth.transport.requests import AuthorizedSession
import argparse


def enable_service(projectNumber: int, services: List[Text]):
    try:
        credentials, _ = google.auth.default()

        authed_session = AuthorizedSession(credentials)

        for service in services:
            response = authed_session.post(
                "https://serviceusage.googleapis.com/v1/projects/{number}/services/{service}.googleapis.com:enable".format(
                    number=projectNumber,
                    service=service,
                )
            )
            print("status code {}".format(response.status_code))
            print(response.text)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--project", type=int, help="target project number")
    args = parser.parse_args()

    enable_service(args.project, ["artifactregistry", "appengine"])
