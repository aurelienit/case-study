
## Welcome to Get Disk Usage
This program has been written using Python.

### Motivation
To be able to check disk usage by listing all the files of a specific mount point in any Unix Environment. Print size of file in bytes in a JSON format.

### Output Example

$ ./getdiskusage.py /tmp

List of files in: /tmp<br />
{<br />
      "files": {<br />
            "/tmp/unity_support_test.0": 0, <br />
            "/tmp/config-err-RAozv0": 0, <br />
            "/tmp/.s.PGSQL.5432.lock": 63, <br />
            "/tmp/.X0-lock": 11<br />
      }<br />
}<br />

### Installation
Use the file named "getdiskusage.py"
Depending on your Unix environment runs the python file with an argument. The argument must be a mount point or Directory.
the following example shows how to run on Ubuntu 14.04.<br />
$ ./getdiskusage.py /tmp<br />
You can run the file as an administrator by adding the sudo command:<br />
$sudo ./getdiskusage.py /root<br />
The program will list of the file under the specify directory. If the directory contains any sub-directory the program will prompt the user to choose if he/she would like to list the files under the sub-directory(ies).<br />

The program returns error if:
 errno.EACCES
 # Display Error Message if access required
 errno.ENOENT
 # Display Error Message if Mount point does not exist
 errno.ENOTDIR
 # Display Error Message if not a valid Directory

### Requirements
Python module os, sys, json and errno.<br />
At least Python 2.6<br />

### Tests
