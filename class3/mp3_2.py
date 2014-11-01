bgp_table = []

bgp_table.append("*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i")
bgp_table.append("*  1.1.1.0/24      157.130.10.233         0 701 1299 15169 i")
bgp_table.append("*  1.1.42.0/24     157.130.10.233        0 701 9505 17408 2.1465 i")
bgp_table.append("*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i")

print "\n%-20s %-50s" % ("ip_prefix", "as_path")

for element in bgp_table:
  entry_split = element.split()
  ip_prefix = entry_split[1]
  as_path = entry_split[4:-1]
  print "%-20s %-50s" % (ip_prefix, as_path)

print "\n"
