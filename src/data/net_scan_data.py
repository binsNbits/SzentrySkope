from data.ifaces import ifaces
from ops.net.get_ip_info import (
    ip_data, get_iface, get_ip6_mask, get_localhost_ip, calculate_network_address
)

scan_init = "nmap"
#########################################################################################

udp_protocols = {
    "UDP" : "-sU"
}
#########################################################################################

scan_techniques = {
    "TCP SYN - Techinique"          : "-sS", 
    "TCP CON - Techinique"          : "-sT", 
    "TCP SYN ACK - Techinique"      : "-sA",
    "TCP Window - Techinique"       : "-sW",
    "TCP Maimon - Techinique"       :  "-sM", 
    "TCP NULL - Techinique"         : "-sN", 
    "TCP FIN - Techinique"          :  "-sF", 
    "TCP XMAS - Techinique"         : "-sX", 
    "Zombie - Techinique"           : "-sI",  
    "SCTP INIT - Techinique"        : "-sY",  
    "COOKIE-ECHO - Techinique"      : "-sZ", 
    "FTP Bounce - Techinique"       : "-b",
    "Consecutive ports - Port Spec" : "-r",
    "Ping Scan - Host"              : "-sn",
    "All Hosts Online"              : "-Pn",
    "TCP SYN - Host"                : "-PS",
    "ACK - Host"                    : "-PA",
    "UDP Discovery - Host"          : "-PU",
    "SCTP Discovery - Host"         : "-PY",
    "ICMP echo - Host"              : "-PE",
    "Timestamp - Host"              : "-PP",
    "netmask request - Host"        : "-PM",
    "No DNS Resolve - Host"         : "-n",
    "DNS Resolve - Host"            : "-R"
}

scan_technique_options_gui = list(scan_techniques.keys())

scan_technique_options = list(scan_techniques.values())
#########################################################################################

scan_service_detection = {
    "Service Detection"             : "-sV", 
    "+Debug Info"                    : "-sV --version-trace",
    "Intensity"                     : "-sV --version-intensity "
}
#########################################################################################

scan_os_detection = {
    "OS Detection"                  : "-O", 
    "+Limited"                       : "-O osscan-limit", 
    "+Aggressive"                    : "-O --osscan-guess"
}
#########################################################################################

scan_scripts = {
    "script="                       : "-sC", 
    "script_trace"                  : "--script-trace",
    "script_db_update"              : "--script-updatedb"
}
#########################################################################################

scan_ports = {
    "First 1000"                    : "-p 1000",
    "All Ports"                     : "-p-", 
    "Custom"                        : None
}
#########################################################################################

ipv4_info = {
    "Localhost"                     : get_localhost_ip, 
    "IPv4 Address"                  : ip_data,
    "IPv6 Netmask"                  : ip_data,
    "IPv4 Broadcast"                : ip_data,
    "Network Address"               : calculate_network_address
}

ipv4_info_keys = list(ipv4_info.keys())
ipv4_info_values = list(ipv4_info.values())
#########################################################################################

ipv6_info = {
    "IPv6 Address"                  : ip_data,
    "IPv6 Netmask"                  : get_ip6_mask,
}

ipv6_info_keys = list(ipv6_info.keys())
ipv6_info_values = list(ipv6_info.values())
#########################################################################################

nic_info = {
    "Network Interface"             : get_iface,
    "MAC Address"                   : ip_data,
    "MAC Broadcast"                 : ip_data
}

nic_info_keys = list(nic_info.keys())
nic_info_values = list(nic_info.values())
#########################################################################################

stealth_info = {
    "Stealth"                        : "-T ", 

}