import subprocess
import crypt

sudopwd = "codud0724"

def adduser(username, pwd):
    
    command = 'sudo -S useradd -m -s /bin/bash -p'
    command = command.split()

    password = crypt.crypt(pwd, "22")

    p = subprocess.Popen(commane + [password, username], stdin=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    p.communicate(sudopwd + '\n')[1]

def deluser(username):

    command = 'sudo -S userdel -r'
    command = command.split()

    p = subprocess.Popen(command + [username], stdin=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    p.communicate(sudopwd + '\n')[1]


    
