import nmap
import pyfiglet
import sys
import socket
from datetime import datetime
from tqdm import tqdm
import time
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)
scanned = 0
# Defining a target


def res():
    if (len(main_array) != 0):
        print("PORT\tSERVICE")
        for p in main_array:
            try:
                serv = socket.getservbyport(p)
            except:
                serv = "unknown"
            print(str(p)+"\t"+serv)


if len(sys.argv) == 2:

    # translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of Argument")

# Add Banner
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)
main_array = []
main_array2 = []
socket.setdefaulttimeout(0.01)
for i in tqdm(range(100)):
    time.sleep(0.21)

try:
    # global scanned
    # scanned=scanned+1
    # will scan ports between 1 to 65,535
    for port in range(1, 500):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # global scanned
        scanned = scanned+1
        s.close
        # returns an error indicator
        result = s.connect_ex((target, port))
        if result == 0:
            print("Port {} is open".format(port))
            main_array.append(port)
        elif result == 11:
            print(f"Port {port} is  closed")
        else:
            print(f"Port {port} is  filtered")
            main_array2.append(port)
    print("-"*40)
    for i in tqdm(range(100)):
        time.sleep(0.01)  # Simulate some latency
    print("The scanning is done.....")
    if (len(main_array2)):
        print("the ports which are filtered are:")
        print(main_array2)
    if (len(main_array)):
        print("the ports which are open are:")
        print(main_array)
    else:
        print("------------------------------NO PORTS ARE OPEN IN THE RANGE SPECIFIED---------------------------")
    res()
    # s.close()

except KeyboardInterrupt:
    print("\n Exiting Program !!!!")
    sys.exit()
except socket.gaierror:
    print("\n Hostname Could Not Be Resolved !!!!")
    sys.exit()
except socket.error:
    print("\ Server not responding !!!!")
    sys.exit()
