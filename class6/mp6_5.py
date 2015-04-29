#!/usr/bin/env python

import sys
from mp6_3 import check_ip
from mp6_4 import dec_to_bin


ip_addr = raw_input("Please enter an IP address: ")

if check_ip(ip_addr) is False:
	print "Bad IP address."
	sys.exit()
else:

