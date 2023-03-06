import sys
import time

from ip_file_valid import ip_file_valid
from inventory_reach import ip_reach
from ssh_connect import ssh_connection
from Threads import create_threads

ip_list = ip_file_valid()

try:
    ip_reach(ip_list)

except KeyboardInterrupt:
    print("\n\n* Program aborted by user. Exiting...\n")
    sys.exit()

while True:
    create_threads(ip_list, ssh_connection)
    time.sleep(10)

#End