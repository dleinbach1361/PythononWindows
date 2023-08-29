from netmiko import ConnectHandler
from netmiko import NetMikoAuthenticationException
import os.path
import time
import sys
import re

#get username and password
username = input("\n# Enter your username please: ")
password = input("\n# Enter your password please: ")

#Check command file
cmd_file = input("\n# Enter command file path and name (C:\\user\\filepath\\filename.txt): ")

#Verify validity
if os.path.isfile(cmd_file) == True:
    print("\n* Command file valid :)\n")

else:
    print("\n* File {} does not exist :( \n".format(cmd_file))
    sys.exit

def ssh_connection(ip):

    global cmd_file

    #Establish ssh session
    try:

        session = ConnectHandler(device_type = "cisco_ios", ip = ip.rstrip('\n'), username = username, password = password)

        #Do not use next line in prod environment
        #session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        #Start sending commands
        selected_cmd_file = open(cmd_file, 'r')
        selected_cmd_file.seek(0)
        command_list = selected_cmd_file.readlines()
        cfg_out = session.send_config_set(command_list)

        #for each_line in selected_cmd_file.readlines():
        #    cfg_out = session.send_command(each_line + '\n')
        #    time.sleep(2)
            
        print(cfg_out)

        #Close files
        #selected_cmd_file.close()

        #checking for errors
        #router_output = session.remote_conn.recv(65535)

        #if re.search(b"% Invalid input", router_output):
        #   print('* There was at least one IOS syntax error on device {} :('.format(ip))
            
        #else:
        #   print('\nDone for device {} :)\n'.format(ip))
            
            
        #print(str(router_output) + "\n")


        session.remote_conn.close()


    except NetMikoAuthenticationException:
        print('* Invalid username or password :( \n* Please check the username/password')
        print('* Closing program')
