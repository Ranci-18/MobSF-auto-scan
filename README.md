+ The script is designed to automate the scanning process of files uploaded on MobSF - the pen-testing app, also for static and dynamic analysis - and give an outlook of critical and high-level threats in the app.
+ It uses the MobSF scan api endpoint to send an http POST request using the hash of the file, file_name, scan_type, and API-key to receive a JSON file.

Running the script
-----------------
+ You can run the script with the target files in the current directory or other directories in the file system. Simply apply the right file path as shown.
+ you can scan multiple files at once to get a breakdown of the issues of the uploaded files.
```Bash
vboxuser@Frank-Ubuntu:~/Documents/Coding/Internship-Tasks$ ./mobsfScanAutomate.py /home/vboxuser/Downloads/'NBM merchant.apk' /home/vboxuser/Downloads/'Pen test.apk'
```
Prompt
------
+ Once you run the script, the following prompt shows. In the event, input the extension as shown.
```Bash
Enter scan type (apk/ipa): apk
```
Sample output
-------------
+ Here is what you can expect as output for the above scanned files
```Bash
3 dangerous warnings in permissions analysis
=================
0 warnings in permissions analysis
-----------------
0 high/critical warnings in certificate analysis
=================
1 warnings in certificate analysis
-----------------
0 high/critical warnings in manifest analysis
=================
3 warnings in manifest analysis
-----------------
0 high/critical warnings in code analysis
=================
5 warnings in code analysis
-----------------
File: /home/vboxuser/Downloads/NBM merchant.apk
+++++++++++++++++++++++++++++++++++++
Enter scan type (apk/ipa): apk
8 dangerous warnings in permissions analysis
=================
0 warnings in permissions analysis
-----------------
0 high/critical warnings in certificate analysis
=================
1 warnings in certificate analysis
-----------------
0 high/critical warnings in manifest analysis
=================
10 warnings in manifest analysis
-----------------
0 high/critical warnings in code analysis
=================
13 warnings in code analysis
-----------------
File: /home/vboxuser/Downloads/Pen test.apk
+++++++++++++++++++++++++++++++++++++
```
Author
======
+ Frank Ng'ang'a
+ wanyoike39@gmail.com
+ +254715353197

If you would like to contribute to this repository and make improvements, contact me. 
+ Let's do this!!!!