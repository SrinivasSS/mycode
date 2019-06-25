#!/usr/bin/env python3

import os
import paramiko

def commandissue(command_to_issue):
    #listOut = []
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(command_to_issue)
    #listOut.append(ssh_stdout.read(), ssh_stderr.read())
    return [ssh_stdin,ssh_stdout,ssh_stderr]

sshsession=paramiko.SSHClient()

mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sshsession.connect(hostname = "10.10.2.3", username = "bender", pkey=mykey)

our_commands=["touch sshworked.txt","touch create.txt", "touch file3.txt", "ls"]

for x in our_commands:
    out = commandissue(x)
    print(out)
    print(out[1].read().decode('utf-8'))
    print(out[0])

print(dir(sshsession))
