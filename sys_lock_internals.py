from create_target import pw




# ------------------- Lock/unlock mechanism -------------------
a = """cls

@ECHO OFF

title Folder Locked Content

if EXIST "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" goto UNLOCK

if NOT EXIST LockedContent goto MDLOCKER

:CONFIRM

echo Are you sure you want to lock the folder vault?

echo . . . . Confirm the secure lock by entering Y/N below 

set/p "cho=>"

if %cho%==Y goto LOCK

if %cho%==y goto LOCK

if %cho%==n goto END

if %cho%==N goto END

echo Invalid choice.

goto CONFIRM

:LOCK

ren LockedContent "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"

attrib +h +s "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"

echo Folder locked

goto End

:UNLOCK

echo Enter password to Unlock folder

set/p "pass=>"

if NOT %pass%=="""

b = str(pw)

c = """ goto FAIL

attrib -h -s "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"

ren "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" LockedContent

echo Folder Unlocked successfully

goto End

:FAIL

echo Invalid password

goto end

:MDLOCKER

md LockedContent

echo LockedContent created successfully

goto End

:End"""

cmd_lock = a + b + c








# ------------------- Explaining operation -------------------
cmd_pw = '''
cls

@ECHO OFF

title -------------------- HOW TO OPERATE --------------------

echo ----------------- This area will explain how to use this file vault/locker -----------------

echo .
echo   .
echo     .
echo       .

echo       . . . . . Feel free to delete if this is unneeded

echo       .
echo       .
echo       .
echo       . . . . . Would you like to continue? Enter Y/N

set /p "one=>"

if %one%==Y goto YINPUT

if %one%==y goto YINPUT

if %one%==N goto NINPUT

if %one%==n goto NINPUT

:YINPUT

echo You entered %one% so now usability will be explained

echo       .

echo       .

echo       .

echo       .

echo       .

echo       . . . . . Locking and unlocking?

echo             . 
echo             .
echo             .  

echo             . . . . Locking and unlocking?

echo             . . . . Would you like to continue? Enter Y/N

set /p "one=>"

if %one%==N goto END

if %one%==n goto END

echo       . . . . . What can I store in my Locked Folder?

echo             . 
echo             . 
echo             . 

echo             . . . . What can I store in my Locked Folder?

echo             . . . . Would you like to continue? Enter Y/N

set /p "one=>"

if %one%==N goto END

if %one%==n goto END

echo       . . . . . Do I need the python folder still?

echo             . 
echo             . 

echo             . . . . Do I need the python folder still?

echo             . . . . Would you like to continue? Enter Y/N

set /p "one=>"

if %one%==N goto END

if %one%==n goto END

goto :END

:NINPUT

echo       .

echo       .

echo       .

echo You entered %one% so have fun using my tool

goto :END

:END

echo Good Bye !!!'''
