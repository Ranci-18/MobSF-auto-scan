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
    
    api_key = '831b0baf2b718bb0216a40b2a8a4ef115d5d58830182ec059cc048571f0edd5d'
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
            critical_issues = 0
            warning = 0
            for key, val in data.items():
                if key == "permissions":
                    if type(val) == dict:
                        for k, v in val.items():
                            if type(v) == dict:
                                for ky, vl in v.items():
                                    if v[ky] == 'dangerous':
                                        critical_issues += 1
                                    if v[ky] == 'warning':
                                        warning += 1
            print("{} dangerous warnings in permissions analysis".format(critical_issues))
            print("=================")
            print("{} warnings in permissions analysis".format(warning))
            print("-----------------")

            for key, val in data.items():    
                if key == "certificate_analysis":
                    if type(val) == dict:
                        for k, v in val.items():  
                            if type(v) == dict:
                                for ky, vl in v.items():
                                    if ky == 'warning':
                                        warning += v[ky]
                                        print("{} warnings in certificate analysis".format(warning))
                                        print("-----------------")
                                    if ky == 'high':
                                        print("{} high/critical warnings in certificate analysis".format(v[ky]))
                                        print("=================")
                if key == "manifest_analysis":
                    if type(val) == dict:
                        for k, v in val.items():
                            if type(v) == dict:
                                for ky, vl in v.items():
                                    if ky == 'high':
                                        print("{} high/critical warnings in manifest analysis".format(v[ky]))
                                        print("=================")
                                    if ky == 'warning':
                                        warning += v[ky]
                                        print("{} warnings in manifest analysis".format(warning))
                                        print("-----------------")
                if key == "code_analysis":
                    if type(val) == dict:
                        for k, v in val.items():
                            if type(v) == dict:
                                for ky, vl in v.items():
                                    if ky == 'high':
                                        print("{} high/critical warnings in code analysis".format(v[ky]))
                                        print("=================")
                                    if ky == 'warning':
                                        warning += v[ky]
                                        print("{} warnings in code analysis".format(warning))
                                        print("-----------------")                
                                    
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
            print("File: {}".format(args[i]))
            print("+++++++++++++++++++++++++++++++++++++")
