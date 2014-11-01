# break the long string into a list based on newlines.
show_ip_lines = show_ip_int_brief.split("\n")

# Initialize a blank list so that we can use .append() on it
show_ip_list = []


# Iterate over each of the lines in the 'show ip int brief'
for line in show_ip_lines:

    # Skip the header line
    if 'Interface' in line:
        continue

    # Break line into words
    line_split = line.split()

    # Filter out lines that don't have the correct number of fields
    if len(line_split) == 6:

        # map these variables to the fields in the line_split list
        if_name, ip_addr, discard1, discard2, line_status, line_proto = line_split

        if (line_status == 'up') and (line_proto == 'up'):
            show_ip_list.append( (if_name, ip_addr, line_status, line_proto) )


print "\n"

# Haven't told you about this, but this just prints the list out nicer
pprint.pprint(show_ip_list)
print "\n"
