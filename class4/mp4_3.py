uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'

list = [uptime1, uptime2, uptime3, uptime4]
output = {}

for string in list:
	device_name = string.split()[0]

	parse_time = ((string.split("is "))[1].split(", "))
	print parse_time

	seconds = 0
	for time_unit in parse_time:
		if "years" in time_unit:
			years = time_unit.split()[0]
			seconds = int(years) * 31560000000
		if "weeks" in time_unit:
			weeks = time_unit.split()[0]
			seconds = seconds + (int(weeks) * 604800)
		if "days" in time_unit:
			days = time_unit.split()[0]
			seconds = seconds + (int(days) * 86400)
	print seconds

#	output[device_name] = parse_time

