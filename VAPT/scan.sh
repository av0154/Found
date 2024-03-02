echo "Enter the IP address :"
read ip
nmap -sV -p 1-1000 $ip -v >> ~/foundathon/results/open_ports.txt
nmap --script=vuln -p $ip >> ~/foundathon/results/results.txt
identity = grep -R "MS%" ~/foundathon/results/results.txt
