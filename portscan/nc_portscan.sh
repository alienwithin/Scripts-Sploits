#!/bin/bash
#Script to conduct portscans via netcat when Nmap is not working in environments for some reason
#By Munir Njiru

##Config Elements
output_file='top_1000_ports_found.txt' # File that will contain the ports found
port_range='ports_1000.txt' #File that contains various port ranges or individual ports to check
ip_addresses='scan_ips.txt' #file containing IP addresses to scan
## End Config
while read ip; do 
  while read portrange; do
  echo "Working on... $ip and $portrange"
    nc -zvw 1 $ip $portrange 2>&1 |grep succeeded | tee -a $output_file
  done <$port_range
done <$ip_addresses
