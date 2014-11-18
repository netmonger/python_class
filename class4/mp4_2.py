import pprint

show_version = '''
>>>>> show version data <<<<<
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
B
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
ROM: System Bootstrap, Version 12.4(22r)YB5, RELEASE SOFTWARE (fc1)

twb-sf-881 uptime is 7 weeks, 5 days, 19 hours, 23 minutes
System returned to ROM by reload at 15:33:36 PST Fri Feb 28 2014
System restarted at 15:34:09 PST Fri Feb 28 2014
System image file is "flash:c880data-universalk9-mz.150-1.M4.bin"
Last reload type: Normal Reload
Last reload reason: Reload Command

Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX1000038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)

License Info:
    License UDI:
    -------------------------------------------------
    Device#   PID                   SN
    -------------------------------------------------
    *0        CISCO881-SEC-K9       FTX1000038X

    License Information for 'c880-data'
        License Level: advipservices   Type: Permanent
            Next reboot license Level: advipservices

            Configuration register is 0x2102
            >>>>> end <<<<<'''

show_version = show_version.split("\n")

show_version_out = {}

for line in show_version:

    if "Cisco IOS Software" in line:
        show_version_out['vendor'] = line.split(", ")[0]
        show_version_out['os_version'] = line.split(", ")[2]

    if "bytes of memory" in line:
        show_version_out['model'] = line.split(" ")[1]

    if "Processor board ID" in line:
        show_version_out['serial_number'] = line.split(" ")[3]

    if "uptime" in line:
        show_version_out['uptime'] = line.split("is ")[1]

pprint.pprint(show_version_out)


