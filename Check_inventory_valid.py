import os.path
import sys

#Declare function to check validity of inventory file.
def inventory_file_valid():

    #Prompt user for input of inventory file location.
    inventory_file = input("\n# Enter IP file path and name (e.g. d:\MyApps\myfile.txt): ")
    
    #Check if file exists.
    if os.path.isfile(inventory_file) == True:
        print("\n* IP file is valid :) \n")
    
    else:
        print("\n* File [] does not exist :( Please check and try again.\n".format(inventory_file))
        sys.exit()
        
    #Open inventory file for reading
    selected_inventory_file = open(inventory_file, 'r')
    
    #Start reading from beginning of file
    selected_inventory_file.seek(0)
    
    #Read each line in the file
    ip_inventory = selected_inventory_file.readlines()
    
    #Close file
    selected_inventory_file.close()
    
    return ip_inventory
    