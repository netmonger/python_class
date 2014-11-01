import sys

if len(sys.argv) != 2:
    # Exit the script
    sys.exit("Usage: ./ex1_binary_converter.py <ip_address>")


ip_addr = sys.argv.pop()
octets = ip_addr.split(".")

# create a blank list (needed because I use .append() method below)
ip_addr_bin = []

if len(octets) == 4:

    for octet in octets:

        bin_octet = bin(int(octet))

        # strip off '0b' from front of string (you can slice a string also)
        bin_octet = bin_octet[2:]

        # prepend '0' to number until 8 chars long
        while True:
            if len(bin_octet) >= 8:
                break
            bin_octet = '0' + bin_octet

        # add octet to new list
        ip_addr_bin.append(bin_octet)


    # join binary number in dotted-binary format
    ip_addr_bin = ".".join(ip_addr_bin)

    # print the output
    print "\n%-15s %-45s" % ("IP address", "Binary")
    print "%-15s %-45s\n\n" % (ip_addr, ip_addr_bin)

else:
    sys.exit("Invalid IP address entered")
