import sys
import subprocess

#Checking IP reachability
def ip_reach(iplist):

    for ip in iplist:
        ip = iprstrip("\n")
        
        ping_reply = subprocess.call('ping %s /n 3' % (ip), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
        
        if ping-reply == 0:
            print("\n* {} is reachable :)\n".format(ip))
            continue
        
        else:
            print('\n* {} not reachable :( Check connectivity and try again.'.format(ip))
            sys.exit()
            