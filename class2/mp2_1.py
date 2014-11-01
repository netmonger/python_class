network_input = raw_input("\n\nPlease enter and IP address: ")
octets = network_input.split('.')
three_octets = octets[0:3]
octets_padded = three_octets + ['0']
network_out = '.'.join(octets_padded)

print "\nYour network number is: %s" % network_out

binary = bin(int(octets_padded[0]))
hex = hex(int(octets_padded[0]))

print "\n\n"
print "%-20s %-20s %-20s" % ("NETWORK_NUMBER", "FIRST_OCTET_BINARY", "FIRST_OCTET_HEX")
print "%-20s %-20s %-20s" % (network_out, binary, hex)
print "\n\n"
