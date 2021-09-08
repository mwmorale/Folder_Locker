import os
import subprocess


# ----- GATHERING PATH INFO -----
output = subprocess.getoutput( 'cd' )
full_path = '' + output


# ----- GETTING USERNAME -----
LHS_start = output.find('Users') + len('Users') + 1
user = output[LHS_start:]
RHS_end = user.find('\\')
user = user[:RHS_end]


# ----- GETTING PRE-USERNAME ------
n = full_path.find(user + '\\')
pre_user = full_path[:n]



target = pre_user + user + '\Desktop'




# ----------- CREATING OS PATHS FOR run_me -----------
i = 'LockedContent'

to_locked_dir = 'VAULT'

sys_lock = 'sys_lock.txt'

end_name = 'Lock & Unlock Vault.bat'

final_path = os.path.join(target,to_locked_dir)



# ----------- User input -----------
pw = input('Choose password\n...no spaces allowed\n...only letters and numbers please\n ---->input your password here: ')

