entry1 = "*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i"
entry2 = "*  1.1.1.0/24       157.130.10.233        0 701 1299 15169 i"
entry3 = "*  1.1.42.0/24     157.130.10.233        0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i"

entry1_prefix = entry1.split(' ')[2]
entry2_prefix = entry2.split(' ')[2]
entry3_prefix = entry3.split(' ')[2]
entry4_prefix = entry4.split(' ')[2]

entry1_as_path = ('701' + (entry1.split('701')[1])[:-2]).split(' ')
entry2_as_path = ('701' + (entry2.split('701')[1])[:-2]).split(' ')
entry3_as_path = ('701' + (entry3.split('701')[1])[:-2]).split(' ')
entry4_as_path = ('701' + (entry4.split('701')[1])[:-2]).split(' ')

print "%-20s %-20s" % ("ip_prefix", "as_path")
print "%-20s %-20s" % (entry1_prefix, entry1_as_path)
print "%-20s %-20s" % (entry2_prefix, entry2_as_path)
print "%-20s %-20s" % (entry3_prefix, entry3_as_path)
print "%-20s %-20s" % (entry4_prefix, entry4_as_path)
