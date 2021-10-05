# Folder_Locker

----- GENERAL -----

After using my Mac(Apple), I noticed how odd it is that Windows does not have a method of easily password "locking" folders. So, I automated this here and now have this capability on my Windows device(and, now, so do you). The code in the project/repo must only be run one single time and, then, can be used easily after this without access to the file, GitHub or even the internet. This is a work in progress - it is intended to manipulate "Desktop" within C drive, was tested/developed using Windows 10 and assumes that your current "User" is your desired selection. Python is used. Libraries "subprocess" and "os" are imported/used.
-------------------



----- create_target.py -----

This file access's/computes the local users file path options and configures the correct file path "route" to work within. The users "Desktop" on the C drive is chosen by default so that the "VAULT" can easily be found. The drive that the user is operating on will be used for this entire process.
----------------------------



----- run_me.py -----

This file(and only this file) must be run in order for the tool/process to operate successfully and as intended. It deals with the path existence and/or non-existence as well as the file/folder creation, and document type conversions. 
---------------------



----- sys_lock_internals.py -----

Here is where my terminal commands are created. There are two of these variables declared here and they are stored as multi-line strings. One is for the locking and and unlocking mechanism and utilizes the user input from "create_target.py". The other variable declared is used for the "walkthrough" when use/operation is explained via the users actual device terminal.
---------------------------------
