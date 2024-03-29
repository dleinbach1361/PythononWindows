import paramiko
import os.path
import time
import sys
import re

#check username/password file
user_file = input(r"\n# Enter user file path and name (e.g. C:\username\filename.txt): ")

#verify file
if os.path.isfile(user_file) == True:
    print("\n* Username\password file is valid :) \n")

else:
    print(r"\n* File {} does not exist :( Please check and try again.\n".format(user_file))
    sys.exit()

#Check command file
cmd_file = input(r"\n# Enter command file path and name (C:\user\filepath\filename.txt): ")

#Verify validity
if os.path.isfile(cmd_file) == True:
    print("\n* Command file valid :)\n")

else:
    print(r"\n* File {} does not exist :( \n".format(cmd_file))
    sys.exit
    

def ssh_connection(ip):

    global user_file
    global cmd_file

    #Establish ssh session
    try:

        selected_user_file = open(user_file, 'r')

        selected_user_file.seek(0)

        username = selected_user_file.readlines()[0].split(',')[0].rstrip('\n')

        selected_user_file.seek(0)

        password = selected_user_file.readlines()[0].split(',')[1].rstrip('\n')

        session = paramiko.SSHClient()

        #Do not use next line in prod environment
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        session.connect(ip.rstrip('\n'), username = username, password = password)

        connection = session.invoke_shell()

        connection.send('enable\n')
        connection.send('terminal length 0\n')
        time.sleep(1)

        connection.send('\n')
        connection.send('conf t\n')
        time.sleep(1)

        #Start sending commands
        selected_cmd_file = open(cmd_file, 'r')

        selected_cmd_file.seek(0)

        for each_line in selected_cmd_file.readlines():
            connection.send(each_line + '\n')
            time.sleep(2)

        #Close files
        selected_user_file.close()
        selected_cmd_file.close()

        #checking for errors
        router_output = connection.recv(65535)

        if re.search(b"% Invalid input", router_output):
            print('* There was at least one IOS syntax error on device {} :('.format(ip))
            
        else:
            print('\nDone for device {} :)\n'.format(ip))

        #print(str(router_output) + "\n")

        #Searching for the CPU utilization value within the output of "show processes top once"
        cpu = re.search(b'%Cpu\(s\):(\s) + (.+?)(\s) + us,', router_output)

        utilization = cpu.group(2).decode('utf-8')

        with open('C:\\Users\\e296631\\Desktop\\Python\\cpu.txt', 'a') as f:

            f.write(utilization + '\n')
        
        session.close()


    except paramiko.AuthenticationException:
        print('* Invalid username or password :( \n* Please check the username/password')
        print('* Closing program')

    


        