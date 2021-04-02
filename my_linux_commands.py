

#This program takes an input and displays useful Linux commands with a quick description of what those commands do

#INPUT OPTIONS: 'all' = show all useful commands, 'net' = show networking commands, 
# 'proc' = show process monitoring commands, "sys' = show system, hardware, software commands

#commands for networking
ping = "ping: tests connectivity between 2 nodes (ping google.com)"
ifconfig = "ifconfig: shows interface ip address, mac address, and maximum transmission unit size"
traceroute = "traceroute: shows number of router hops and path to a destination"
netstat = "netstat: shows connection info, routing table info"
dig = "dig: queries DNS related info"
nslookup = "nslookup: queries DNS related info"
host = "host: finds name to IP or IP to name (host google.com)"
arp = "arp: shows ARP table contents"
hostname = "hostname: shows info about your system/network (hostname -I shows your IPv4 and IPv6 address)"

#commands for processes
top = "top: monitor processes and PIDs" 
ps_aux = "ps aux: full processes and PIDs list"
pidof = "pidof: view the PID of a running process (pidof firefox)"
kill = "kill <pid>: kill process (kill 9378) or you can kill multiple processes:(kill 9378 297 5467) - sigkill (9) forces a process to stop immediately (kill -9 9378)"

#commands for system info (hardware/sofware)
uname = "uname -a: -shows basic system and OS info"
lscpu = "lscpu: shows info about the cpu and processing units"
lshw = "lshw: lists hardware info"
df = "df: disk space of file systems"
fdisk = "fdisk: lists partition info"
free = "free: check RAM"

net = [ping, ifconfig, traceroute, netstat, dig, nslookup, host, arp, hostname]
proc = [top, ps_aux, pidof, kill]
sys = [uname, lscpu, lshw, df, fdisk, free]


options = input("Please input: 'net' for useful networking commands, 'sys' for system commands, 'proc' for process commands, or 'all' for all useful commands (without the quotation marks of course): ")
print(options)

if options == 'net':
    print(*net, sep="\n")
elif options == 'sys':
    print(*sys, sep="\n")
elif options == 'proc':
    print(*proc, sep="\n")
elif options == 'all':
    print(*net, *proc, *sys, sep="\n")
else:
    print("please type the exact words: 'net', 'proc', 'sys', or 'all': ")

