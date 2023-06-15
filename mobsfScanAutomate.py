#!/usr/bin/python3
import requests
import json
import sys
import os
import hashlib


def autoScanFile(file_path):
    url = 'http://localhost:8000/api/v1/scan'
    scan_type = input("Enter scan type (apk/ipa): ")
    file_name = os.path.basename(file_path)
    hash_obj = hashlib.md5()
    
    api_key = 'e68b24efbcf78495f93873d887110117eacea9e412b86f894b5eca2df7ab7121'
    headers = {'Authorization': api_key}
    
    with (open(file_path, 'rb')) as f:
        file_contents = f.read()
        files = {'file': (file_name, file_contents)}
        hash_obj.update(file_contents)
        hash = hash_obj.hexdigest()
        params = {'scan_type': scan_type, 'file_name': file_name, 'hash': hash}

        response = requests.post(url, headers=headers, files=files, data=params)
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
            print("Error Response: {}".format(response.text))


if __name__ == "__main__":
    args = sys.argv

    if len(args) < 2:
        print("You need to pass file name/file path as argument")
    else:
        for i in range(1, len(args)):
            fle = args[i]
            autoScanFile(fle)
