# FileSave
CLI script that helps secure private folders

### Prerequisites
Python 3.0 > needs to be installed and make sure you can use the pip command.
To check if you have python and correct version, open terminal and enter.
```
python --version
```
### How to install
Give exceutable permission to install.sh
```
chmod +x install.sh
```
Run install.sh
```
./install.sh
```
You're set

### How to secure folder
Replace "exfolder" with your folder name
```
filesave hide exfolder
```
Be sure to create a password and phone number if you wish for 2-auth

### How to reveal folder
```
filesave show exfolder
```
Enter password and complete phone verificaton if set up.
