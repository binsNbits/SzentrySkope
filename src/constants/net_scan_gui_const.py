# Scan Techniques
sS = "TCP SYN - Techinique"
sT = "TCP CON - Techinique"
sA = "TCP SYN ACK - Techinique"
sW = "TCP Window - Techinique"
sM = "TCP Maimon - Techinique"
sU = "UDP"
sN = "TCP NULL - Techinique"
sF = "TCP FIN - Techinique"
sX = "TCP XMAS - Techinique"
sI = "Zombie - Techinique"
sY = "SCTP INIT - Techinique"
sZ = "COOKIE-ECHO - Techinique"
b = "FTP Bounce - Techinique"
r = "Consecutive ports - Port Spec"

# Host Discovery
sn = "Ping Scan - Host"
Pn = "All Hosts Online"
PS = "TCP SYN - Host"
PA = "ACK - Host"
PU = "UDP Discovery - Host"
PY = "SCTP Discovery - Host"
PE = "ICMP echo - Host"
PP = "Timestamp - Host"
PM = "netmask request - Host"
n = "No DNS Resolve - Host"
R = "DNS Resolve - Host"



####################################################

scan_techniques_txt = [
    sS, sT, sA, sW, sM, sU, sN, sF, sX, sI, sY, sZ, b, sn, Pn, PS, PA, PU, PY, PE, PP, 
    PM, n, R, r
]

# Menu
PRANGE_1 = "Protocol"
PRANGE_1_VAL_1 = "TCP"
PRANGE_1_VAL_2 = "UDP"
PRANGE_2 = "Services"
PRANGE_2_VAL_NONE = "None"
PRANGE_2_VAL_1 = "Services"
PRANGE_2_VAL_2 = "Operating System"
PRANGE_2_VAL_3 = "ALL"
PRANGE_3 = "Operating Systems"
PRANGE_4 = "Vulns"

# SERVICE/VERSION DETECTION
sV = "Service Detection"# OS Detection
os_detect = "-O"
aggressive_os_detect = "--osscan-guess"

# Advanced Script Scanning
script = "-sC"
script_trace = "--script-trace" # Show all data sent and received
script_updatedb = "--script-updatedb" #Update the script database.

# Script Scans
sC = "Advanced Scan Running"

# Scan Intensity Constants
SCAN_1_INT = "Stealth"
SCAN_2_INT = "Aggression"
SCAN_3_INT = "Evasion"

# OS Detection
os_detect = "-O"
aggressive_os_detect = "--osscan-guess"

# Advanced Script Scanning
script = "-sC"
script_trace = "--script-trace" # Show all data sent and received
script_updatedb = "--script-updatedb" #Update the script database.