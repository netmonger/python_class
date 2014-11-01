#!/usr/bin/env python

import sys

ip_addr = sys.argv.pop()
octets = ip_addr.split(".")


# Check that IP address contains 4 octets
if len(octets) < 4:
  print "IP address %s is invalid" % (ip_addr)

# Check that first octet is between 1 - 223
elif int(octets[0]) > 223:
  print "IP address %s is invalid.  First octet has to be between 1 - 223." % (ip_addr)

# Check that the first octect is not 127
elif int(octets[0]) == 127:
  print "IP address %s is invalid.  First octet cannot be 127." % (ip_addr)

# Check that IP is not part of the 169.254.x.x address space
elif (int(octets[0]) == 169) and (int(octets[1]) == 254):
  print "IP address %s is invalid.  Cannot be 169.254.x.x address space." % (ip_addr)

# Check that the last three octets range between 0 - 255
elif (int(octets[1]) > 255) or (int(octets[2]) > 255) or (int(octets[3]) > 255):
  print "IP address %s is invalid.  Last three octets must range between 0 - 255" % (ip_addr)

# If all checks out, print IP address
else:
  print "IP address %s is valid." % (ip_addr)
