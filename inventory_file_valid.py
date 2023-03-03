import os.path
import sys

#Check for inventory file validity and existance
def ip_file_valid():
    ip_file = input("\n# Enter inventory file path and name (e.g. C:\\username\\myfile.txt): ")

    if os.path.isfile(ip_file) == True:
        print("\n* Inventory file is valid :)\n")

    else:
        print("\n* File {} does not exist :( Please check and try again.\n".format(ip_file))
        sys.exit()

    #Open file for reading
    selected_inventory_file = open(ip_file, 'r')

    #Set to start reading from beginning
    selected_inventory_file.seek(0)

    #Read in IP's one line at a time
    inventory_list = selected_inventory_file.readlines()

    #Close file
    selected_inventory_file.close()

    return inventory_list