# Folder_Locker

----- GENERAL -----

After using my Mac(Apple), I noticed how odd it is that Windows does not have a method of "locking" folders. So, I 
automated this here and now have this capability on my Windows device(and, now, so do you). My program only requires 
this project's code to be run one single time and can be used easily after this without code/internet etc. This is
a work in progress, is intended to manipulate "Desktop" within C drive, was tested using Windows 10 and assumes that
your current "User" is your selection. This is written in Python and uses "subprocess" and "os" imports.
-------------------

----- create_target.py -----

----- run_me.py -----

This file must be run in order for the tool/process to operate successfully. It 

----- sys_lock_internals.py -----

Here is where my terminal commands are created. There are two of these variables declared here and they are stored as
multi-line strings. One is for the locking and and unlocking mechanism and utilizes the user input from "create_target.py". 
The other variable declared is used for the "walkthrough" when use/operation is explained.
