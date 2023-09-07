import sys

from ip_file_valid import ip_file_valid
from inventory_reach import ip_reach
from ssh_netmiko import ssh_connection
from Threads2 import create_threads

ip_list = ip_file_valid()

try:
    ip_reach(ip_list)

except KeyboardInterrupt:
    print("\n\n* Program aborted by user. Exiting...\n")
    sys.exit()

create_threads(ip_list, ssh_connection)

#End