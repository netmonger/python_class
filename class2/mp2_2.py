ip_address = raw_input("\n\nPlease enter an IP address: ")

octets = ip_address.split('.')

first_octet = bin(int(octets[0]))
second_octet = bin(int(octets[1]))
third_octet = bin(int(octets[2]))
fourth_octet = bin(int(octets[3]))

print "\n\n"
print "%-20s %-20s %-20s %-20s" % ("first_octet", "second_octet", "third_octet", "fourth_octet")
print "%-20s %-20s %-20s %-20s" % (first_octet, second_octet, third_octet, fourth_octet)
print "\n\n"
