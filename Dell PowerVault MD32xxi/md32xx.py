import subprocess
import sys
import getopt
import json
from pyzabbix import ZabbixMetric, ZabbixSender
ipa = ''
ipb = ''
host = ''
try:
    opts, args = getopt.getopt(sys.argv[1:], "ha:b:n:")
except getopt.GetoptError:
    print 'md32xx.py -a <IPControlerA> -b <IPControlerB> -n <HostNameInZabbix>'
    sys.exit(2)
for opt, arg in opts:
    if opt == "-h":
        print 'md32xx.py -a <IPControlerA> -b <IPControlerB> -n <HostNameInZabbix>'
        print 'Parameters:'
        print '-a\t\tIP Controler A'
        print '-b\t\tIP Controler B'
        print '-n\t\tHostName in Zabbix'
        print '-h\t\tThis help'
        sys.exit()
    elif opt == "-a":
        ipa = arg
    elif opt == "-b":
        ipb = arg
    elif opt == "-n":
        host = arg
#    else
#        print 'md32xx.py -a <IPControlerA> -b <IPControlerB> -n <HostNameInZabbix>'
#        sys.exit(2)
SMCLI = "/opt/IBM_DS/client/SMcli"
CONN = ipa + " " + ipb
cmd = SMCLI + " " + CONN + " -S -c \"set session performanceMonitorInterval=3 performanceMonitorIterations=1;show allLogicalDrives performanceStats;\""
#print cmd
proc =  subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
strings = out.split("\n",7)[7]
#print strings
packet = []
output = []
for str in strings.splitlines():
    arr = str.split(',')
    output.append({"{#VALUE}": arr[0].replace("\"","")})
    packet.append(ZabbixMetric(host, 'total.ios['+arr[0].replace("\"","")+']',arr[1].replace("\"", "")))
    packet.append(ZabbixMetric(host, 'read['+arr[0].replace("\"","")+']',arr[2].replace("\"", "")))
    packet.append(ZabbixMetric(host, 'read.cache.hit['+arr[0].replace("\"","")+']',arr[3].replace("\"", "")))
    packet.append(ZabbixMetric(host, 'write.cache.hit['+arr[0].replace("\"","")+']',arr[4].replace("\"", "")))
    packet.append(ZabbixMetric(host, 'ssd.cache.hit['+arr[0].replace("\"","")+']',arr[5].replace("\"", "")))
    packet.append(ZabbixMetric(host, 'current.MBs['+arr[0].replace("\"","")+']',arr[6].replace("\"", "")))
    packet.append(ZabbixMetric(host, 'max.MBs['+arr[0].replace("\"","")+']',arr[7].replace("\"", "")))
    packet.append(ZabbixMetric(host, 'current.ios['+arr[0].replace("\"","")+']',arr[8].replace("\"", "")))
    packet.append(ZabbixMetric(host, 'max.ios['+arr[0].replace("\"","")+']',arr[9].replace("\"", "")))
    if arr[0].replace("\"","") == "STORAGE SUBSYSTEM TOTALS":
      break
#print packet
ZabbixSender(zabbix_server='192.168.10.45', zabbix_port=10051).send(packet)
print '{"data":'
print json.dumps(output)
print '}'
