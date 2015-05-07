#!/usr/bin/env python

import sys
from mp6_3 import check_ip
from mp6_4 import dec_to_bin


ip_addr = raw_input("Please enter an IP address: ")

if check_ip(ip_addr) is True:
	print dec_to_bin(ip_addr)
	sys.exit()
else:
	print "Bad IP address"
