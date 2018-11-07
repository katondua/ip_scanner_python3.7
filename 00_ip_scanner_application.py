import subprocess
import ipaddress
import string

print ("########################################################")
print ("##            IP Scanner application ver.1.0          ##")
print ("########################################################")
print ("##                    BY : zhadowsong                 ##")
print ("##                    7-November-2018                 ##")
print ("##          Open Source Application (python3.7)       ##")
print ("########################################################")
print ("")
print ("Example -> 192.168.1.1/24 ")
print ("")

ipinput = ipaddress.ip_interface(input ("Input ip address and network  : "))

from subprocess import Popen, PIPE

ipadd1 = ipaddress.ip_interface(ipinput)
#ipadd1.network
network = ipadd1.network 	
#network = ipaddress.ip_network('10.101.98.1/24')
for i in network.hosts():
	i=str(i)
	toping = Popen(['ping','-c','3',i], stdout=PIPE)
	output = toping.communicate()[0]
	hostalive = toping.returncode
	if hostalive == 0:
		print (i,"is reachable")
	else :
		print (i, "is unreachable")


print (ipadd1)




