#!/usr/bin/python3
import requests
import json
import sys


def autoScanFile(file):
    url = 'http://localhost:8000/api/v1/scan'
    api-key = None
    header = {"Authorization:" api-key}
    files = {'file': open(file, 'rb')}

    response = requests.post(url, headers=header, files=files)
    if response.status_code == 200:
        data = json.loads(response.content)

        issues = data.get('issues', [])

        critical_issues = [issue for issue in
                           issues if issue.get('severity') == 'Critical']
        high_issues = [issue for issue in
                       issues if issue.get('severity') == 'High']
        medium_issues = [issue for issue in
                         issues if issue.get('severity') == 'Medium']

        print("Critical issues: {}, "
              "High issues: {}, "
              "Medium issues: {}".format(len(critical_issues),
                                         len(high_issues),
                                         len(medium_issues)))
    else:
        print("Error Response")


if __name__ == "__main__":
    args = sys.argv

    for i in range(1, len(args)):
        fle = args[i]
        autoScanFile(fle)