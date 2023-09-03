from pathlib import Path
import netifaces
import re
import sys
import os
import ipaddress

myDir = os.getcwd()
sys.path.append(myDir)

path = Path(myDir)
a = str(path.parent.absolute())
sys.path.append(a)
from data.ifaces import ifaces

def calculate_network_address(ip_address, subnet_mask):
    network = ipaddress.ip_interface(f"{ip_address}/{subnet_mask}")
    return network.network



def ip_setter(interface, data, inet):
    if inet == '4':
        inet = netifaces.AF_INET
    elif inet == '6':
        inet = netifaces.AF_INET6
    elif inet == 'mac':
        inet = netifaces.AF_LINK
    addrs = netifaces.ifaddresses(interface)
    print(addrs)
    if inet in addrs:
        addresses = addrs[inet]
        for addr in addresses:
            if data in addr:
                return addr[data]
    return None

def ip_data(list, data, inet):
    ip4_pattern = r"^(?:\d{1,3}\.){3}\d{1,3}$"
    ip6_pattern1 = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}/\d{1,3}$"
    ip6_pattern2 = r"^fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]+$"
    mac_pattern = r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$"

    for element in list:
        try:
            target = ip_setter(element, data, inet)
            if target and re.match(ip4_pattern, target):
                return target
            elif target and (re.match(ip6_pattern1, target) or re.match(ip6_pattern2, target)):
                return target
            elif target and re.match(mac_pattern, target):
                return target
            else:
                print(f"Invalid IP address for {element}: {target}")
        except:
            pass


# SPECIALIZED FUNCTIONS
'''
NOTE - these functions are specialized for no reason more than the fact that it is easier to 
extract the data needed by defining the funcs in this way rather than in the ip_data func
'''

def get_iface(list):
    iface = ip_data(list, 'addr', '6')
    return iface.split('%')[-1]


def get_ip6_mask():
    mask_info = netifaces.ifaddresses("enp0s3")
    ipv6_info = mask_info.get(netifaces.AF_INET6)
    if 'netmask' in ipv6_info[0]:
        return ipv6_info[0]['netmask']
    else:
        print("IPv6 netmask could not be found")
        return None
    

def get_localhost_ip():
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        if interface == 'lo':
            addresses = netifaces.ifaddresses(interface)
            if netifaces.AF_INET in addresses:
                return addresses[netifaces.AF_INET][0]['addr']




'''
TODO - ip_data function is to be imported to hostoptionsbox
NOTE - this is how to initialize the functions


ip4_addr = ip_data(ifaces, 'addr', '4')
print(ip4_addr)

ip4_mask = ip_data(ifaces, 'netmask', '4')
print(ip4_mask)

net_addr = calculate_network_address(ip4_addr, ip4_mask)
print("NETWORK ADDR -> ",net_addr)

ip4_broadcast = ip_data(ifaces, 'broadcast', '4')
print(ip4_broadcast)

ip6_addr = ip_data(ifaces, 'addr', '6')
print(ip6_addr)

mac_addr = ip_data(ifaces, 'addr', 'mac')
print(mac_addr)

mac_broadcast = ip_data(ifaces, 'broadcast', 'mac')
print(mac_broadcast)

iface = get_iface(ifaces)
print(iface)

ip6_mask = get_ip6_mask()
print(ip6_mask)

localhost_ip = get_localhost_ip()
print("Localhost IP:", localhost_ip)
'''




