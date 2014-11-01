import sys

ip_addr = sys.argv.pop()

octets = ip_addr.split(".")
binary_ip = range(4)
x = 0

# Iterate through octets to remove first two characters and pad with 0's
for element in octets:
  binary_ip[x] = ('0000000' + (bin(int(element))[2:]))[-8:]
  x += 1

binary_ip = '.'.join(binary_ip)


print "\n%-20s %-20s" % ("IP address","Bindary")
print "%-20s %-20s" % (ip_addr,binary_ip)
print "\n"
