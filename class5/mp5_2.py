#!/usr/bin/env python

import pprint


sw1_show_cdp_neighbors = '''

SW1>show cdp neighbors

Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                                 S - Switch, H - Host, I - IGMP, r - Repeater,
P - Phone

Device ID            Local Intrfce        Holdtme        Capability        Platform    Port ID
R1                    Fas 0/11              153            R S I           881		Fas 1
R2                    Fas 0/12              123            R S I           881		Fas 1
R3                    Fas 0/13              129            R S I           881		Fas 1
R4                    Fas 0/14              173            R S I           881		Fas 1
R5                    Fas 0/15              144            R S I           881		Fas 1

'''

sw1_show_cdp_neighbors_detail = '''

SW1> show cdp neighbors detail
--------------------------
Device ID: R1
Entry address(es):
   IP address: 10.1.1.1
Platform: Cisco 881, Capabilities: Router Switch IGMP
Interface: FastEthernet0/11, Port ID (outgoing port): FastEthernet1
Holdtime: 153 sec

Version :
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4,
RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team

advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):

--------------------------
Device ID: R2
Entry address(es):
   IP address: 10.1.1.2
Platform: Cisco 881, Capabilities: Router Switch IGMP
Interface: FastEthernet0/12, Port ID (outgoing port): FastEthernet1
Holdtime: 123 sec

Version :
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4,
RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team

advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):

--------------------------
Device ID: R3
Entry address(es):
   IP address: 10.1.1.3
Platform: Cisco 881, Capabilities: Router Switch IGMP
Interface: FastEthernet0/13, Port ID (outgoing port): FastEthernet1
Holdtime: 129 sec

Version :
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4,
RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team

advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):

--------------------------
Device ID: R4
Entry address(es):
   IP address: 10.1.1.4
Platform: Cisco 881, Capabilities: Router Switch IGMP
Interface: FastEthernet0/14, Port ID (outgoing port): FastEthernet1
Holdtime: 173 sec

Version :
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4,
RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team

advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):

--------------------------
Device ID: R5
Entry address(es):
   IP address: 10.1.1.5
Platform: Cisco 881, Capabilities: Router Switch IGMP
Interface: FastEthernet0/15, Port ID (outgoing port): FastEthernet1
Holdtime: 144 sec

Version :
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4,
RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team

advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):

'''

r1_show_cdp_neighbors = '''

R1>show cdp neighbors 
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Fas 1              150          S I      WS-C2950- Fas 0/11

'''

r1_show_cdp_neighbors_detail = '''

R1>show cdp neighbors detail 
-------------------------
Device ID: SW1
Entry address(es): 
  IP address: 10.1.1.22
Platform: cisco WS-C2950-24,  Capabilities: Switch IGMP 
Interface: FastEthernet1,  Port ID (outgoing port): FastEthernet0/11
Holdtime : 145 sec

Version :
Cisco Internetwork Operating System Software 
IOS (tm) C2950 Software (C2950-I6Q4L2-M), Version 12.1(22)EA8a, RELEASE
SOFTWARE (fc1)
Copyright (c) 1986-2006 by cisco Systems, Inc.
Compiled Fri 28-Jul-06 15:16 by weiliu

advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27,
value=00000000FFFFFFFF010221FF0000000000000019E845CE80FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full

'''

r2_show_cdp_neighbors = '''

R2>show cdp neighbors 
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Fas 1              150          S I      WS-C2950- Fas 0/12

'''

r2_show_cdp_neighbors_detail = '''

R2>show cdp neighbors detail 
-------------------------
Device ID: SW1
Entry address(es): 
  IP address: 10.1.1.22
Platform: cisco WS-C2950-24,  Capabilities: Switch IGMP 
Interface: FastEthernet1,  Port ID (outgoing port): FastEthernet0/12
Holdtime : 145 sec

Version :
Cisco Internetwork Operating System Software 
IOS (tm) C2950 Software (C2950-I6Q4L2-M), Version 12.1(22)EA8a, RELEASE
SOFTWARE (fc1)
Copyright (c) 1986-2006 by cisco Systems, Inc.
Compiled Fri 28-Jul-06 15:16 by weiliu

advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27,
value=00000000FFFFFFFF010221FF0000000000000019E845CE80FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full

'''

r3_show_cdp_neighbors = '''

R3>show cdp neighbors 
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Fas 1              150          S I      WS-C2950- Fas 0/13

'''

r3_show_cdp_neighbors_detail = '''

R3>show cdp neighbors detail 
-------------------------
Device ID: SW1
Entry address(es): 
  IP address: 10.1.1.22
Platform: cisco WS-C2950-24,  Capabilities: Switch IGMP 
Interface: FastEthernet1,  Port ID (outgoing port): FastEthernet0/13
Holdtime : 145 sec

Version :
Cisco Internetwork Operating System Software 
IOS (tm) C2950 Software (C2950-I6Q4L2-M), Version 12.1(22)EA8a, RELEASE
SOFTWARE (fc1)
Copyright (c) 1986-2006 by cisco Systems, Inc.
Compiled Fri 28-Jul-06 15:16 by weiliu

advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27,
value=00000000FFFFFFFF010221FF0000000000000019E845CE80FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full

'''

r4_show_cdp_neighbors = '''

R4>show cdp neighbors 
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Fas 1              150          S I      WS-C2950- Fas 0/14

'''

r4_show_cdp_neighbors_detail = '''

R4>show cdp neighbors detail 
-------------------------
Device ID: SW1
Entry address(es): 
  IP address: 10.1.1.22
Platform: cisco WS-C2950-24,  Capabilities: Switch IGMP 
Interface: FastEthernet1,  Port ID (outgoing port): FastEthernet0/14
Holdtime : 145 sec

Version :
Cisco Internetwork Operating System Software 
IOS (tm) C2950 Software (C2950-I6Q4L2-M), Version 12.1(22)EA8a, RELEASE
SOFTWARE (fc1)
Copyright (c) 1986-2006 by cisco Systems, Inc.
Compiled Fri 28-Jul-06 15:16 by weiliu

advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27,
value=00000000FFFFFFFF010221FF0000000000000019E845CE80FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full

'''

r5_show_cdp_neighbors = '''

R5>show cdp neighbors 
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Fas 1              150          S I      WS-C2950- Fas 0/15

'''

r5_show_cdp_neighbors_detail = '''

R5>show cdp neighbors detail 
-------------------------
Device ID: SW1
Entry address(es): 
  IP address: 10.1.1.22
Platform: cisco WS-C2950-24,  Capabilities: Switch IGMP 
Interface: FastEthernet1,  Port ID (outgoing port): FastEthernet0/15
Holdtime : 145 sec

Version :
Cisco Internetwork Operating System Software 
IOS (tm) C2950 Software (C2950-I6Q4L2-M), Version 12.1(22)EA8a, RELEASE
SOFTWARE (fc1)
Copyright (c) 1986-2006 by cisco Systems, Inc.
Compiled Fri 28-Jul-06 15:16 by weiliu

advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27,
value=00000000FFFFFFFF010221FF0000000000000019E845CE80FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full

'''

network_devices = {}

devices = sw1_show_cdp_neighbors_detail.split("--------------------------")

for device in devices:
	device_details = device.split("\n")
	for item in device_details:
		if "Device ID:" in item:
                        device_name = item.split()[2]
			network_devices[device_name] = {}
		if "IP address" in item:
			device_ip = item.split()[2]
			network_devices[device_name]['ip'] = device_ip
		if "Platform" in item:
			device_model = (item.split()[2])[:-1]
			device_vendor = item.split()[1]
                        network_devices[device_name]['model'] = device_model
                        network_devices[device_name]['vendor'] = device_vendor
		if "Capabilities" in item:
			if "Router" in item:
				device_type = "router"
                                network_devices[device_name]['device_type'] = 'router'
			else:
				device_type = "switch"
                                network_devices[device_name]['device_type'] = 'switch'


device_details = r1_show_cdp_neighbors_detail.split("\n")

for item in device_details:
	if "Device ID:" in item:
                device_name = item.split()[2]
		network_devices[device_name] = {}
	if "IP address" in item:
		device_ip = item.split()[2]
		network_devices[device_name]['ip'] = device_ip
	if "Platform" in item:
		device_model = (item.split()[2])[:-1]
		device_vendor = item.split()[1]
                network_devices[device_name]['model'] = device_model
                network_devices[device_name]['vendor'] = device_vendor
	if "Capabilities" in item:
		if "Router" in item:
			device_type = "router"
			network_devices[device_name]['device_type'] = 'router'
		else:
			device_type = "switch"
                        network_devices[device_name]['device_type'] = 'switch'

# Take adjacency list and remove unnecessary characters
sw1_adjacent = sw1_show_cdp_neighbors.split("Port ID")[1].strip().split("\n")
r1_adjacent = r1_show_cdp_neighbors.split("Port ID")[1].strip().split("\n")
r2_adjacent = r2_show_cdp_neighbors.split("Port ID")[1].strip().split("\n")
r3_adjacent = r3_show_cdp_neighbors.split("Port ID")[1].strip().split("\n")
r4_adjacent = r4_show_cdp_neighbors.split("Port ID")[1].strip().split("\n")
r5_adjacent = r5_show_cdp_neighbors.split("Port ID")[1].strip().split("\n")


# Cycle through all adjacent devices for SW1
i = 0
network_devices["SW1"]['adjacent devices'] = []
while i < len(sw1_adjacent):
	network_devices["SW1"]['adjacent devices'].append(sw1_adjacent[i].split()[0])
	#sw1_adjacent = sw1_adjacent[1].split()[0]
	i+=1

# Adjacent devices for Routers
network_devices["R1"]['adjacent devices'] = [r1_adjacent[0].split()[0]]
network_devices["R2"]['adjacent devices'] = [r2_adjacent[0].split()[0]]
network_devices["R3"]['adjacent devices'] = [r3_adjacent[0].split()[0]]
network_devices["R4"]['adjacent devices'] = [r4_adjacent[0].split()[0]]
network_devices["R5"]['adjacent devices'] = [r5_adjacent[0].split()[0]]

pprint.pprint(network_devices)