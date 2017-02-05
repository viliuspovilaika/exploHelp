import argparse
import socket
import csv
from time import gmtime, strftime
from netaddr import *
parser = argparse.ArgumentParser(description='Cross-Origin Resource Sharing scanner')
parser.add_argument('-t', action="store", help="target range", required=True)
port = 80
vulnerable = []
invulnerable = []
broken = []
def getRange(x):
	result = []
	for part in x.split("."):
		if "-" in part:
			a, b = part.split("-")
			a, b = int(a), int(b)
			result.extend(range(a, b + 1))
		else:
			a = int(part)
			result.append(a)
	return result
print "[*] Scanning IP range " + parser.parse_args().t
IP = IPNetwork(parser.parse_args().t)
for item in IP:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(5)
	try:
		s.connect((str(item), port))
		s.send("HEAD / HTTP/1.1\r\nHost: "+str(item)+"\r\nOrigin: csrftestorigin\r\nConnection: close\r\n\r\n")
		received = s.recv(1024)
		if "Access-Control-Allow-Origin: csrftestorigin" in received or "Access-Control-Allow-Origin: *" in received or received == "":
			vulnerable.append(item)
			print "[+] Host "+item+" has CSRF implementation!"
		else:
			invulnerable.append(item)
	except:
		broken.append(item)
	s.close()
reportName = "csrf_" + strftime("%Y-%m-%d_%H-%M-%S", gmtime()) + ".csv"
with open(reportName, "w+") as csvFile:
	csvWriter = csv.writer(csvFile, dialect='excel')
	csvWriter.writerow(["CSRF implemented: "])
	for item in vulnerable:
		csvWriter.writerow([item])
	csvWriter.writerow("")
	csvWriter.writerow(["CSRF not implemented: "])
	for item in invulnerable:
		csvWriter.writerow([item])
	csvWriter.writerow("")
	csvWriter.writerow(["Couldn't connect: "])
	for item in broken:
		csvWriter.writerow([item])
print "[*] Report saved to '"+reportName+"'!"
print "[*] Exiting.."
