# input table
show_ip_int_brief = '''
Interface            IP-Address      OK?     Method      Status     Protocol
FastEthernet0   unassigned      YES     unset          up          up
FastEthernet1   unassigned      YES     unset          up          up
FastEthernet2   unassigned      YES     unset          down      down
FastEthernet3   unassigned      YES     unset          up          up
FastEthernet4    6.9.4.10          YES     NVRAM       up          up
NVI0                  6.9.4.10          YES     unset           up          up
Tunnel1            16.25.253.2     YES     NVRAM       up          down
Tunnel2            16.25.253.6     YES     NVRAM       up          down
Vlan1                unassigned      YES    NVRAM       down      down
Vlan10              10.220.88.1     YES     NVRAM       up          up
Vlan20              192.168.0.1     YES     NVRAM       down      down
Vlan100            10.220.84.1     YES     NVRAM       up          up
'''

# Prepare table for itteration
table = show_ip_int_brief.split('\n')[2:-1]
table_output = []

# Iterrate through table
for element in table:
  interface = element.split()
  if interface[4] == "down":
    continue 
  elif interface[5] == "down":
    continue
  else:
    table_output.append((interface[0], interface[1], interface[4], interface[5]))
    
print "\n"
print table_output
print "\n"
