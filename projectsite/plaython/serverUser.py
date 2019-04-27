import subprocess
import crypt

#import pexpect

sudopwd = "default00"

def adduser(username, pwd):
    try:    
        command = 'sudo -S useradd -m -s /bin/bash -p'
        #command = 'mkdir ' + username 
        command = command.split()

        password = crypt.crypt(pwd, "22")
        p = subprocess.Popen(command + [password, username], stdin=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    
        #p = subprocess.Popen(command , stdin=subprocess.PIPE, stderr = subprocess.PIPE,  universal_newlines = True)
        p.communicate(sudopwd + '\n')[1]
        #p.communicate()        
       
    except Exception as ex:
        print('ERROR' , ex)


def deluser(username):

    command = 'sudo -S userdel -r'
    command = command.split()

    p = subprocess.Popen(command + [username], stdin=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    p.communicate(sudopwd + '\n')[1]


    
