from create_target import sys_lock, end_name, final_path
from sys_lock_internals import cmd_lock
from sys_lock_internals import cmd_pw
import os



end_final_path = os.path.join(final_path, end_name)

temp_pw = 'PW.txt'

if( os.path.exists(final_path)==False ):
    os.mkdir(final_path)
    to_sys_lock = os.path.join(final_path, sys_lock)
    f = open(to_sys_lock, 'a+', encoding='utf_8')
    f.write(cmd_lock)
    f.close()
    to_temp_pw = os.path.join(final_path, temp_pw)
    final_pw = os.path.join(final_path, 'How To Use.bat')
    f_pw = open(to_temp_pw, 'a+', encoding='utf_8')
    f_pw.write(cmd_pw)
    f_pw.close()
    os.rename(to_sys_lock, end_final_path)
    os.path.join(end_final_path, final_pw)
    os.rename(to_temp_pw, final_pw)
else:
    exit('File structure has been previously created\nContact owner for troubleshooting')


