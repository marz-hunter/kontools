#Open file and read data
f = open("dnsx2", "r")
data = f.read()

#Use regular expression to extract ipv4 strings
import re
ipv4_strings = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", data)

#Print extracted ipv4 strings
print("Extracted IPv4 strings:")
for ip in ipv4_strings:
    print(ip)
