# -*- coding: utf-8 -*-
"""
Task 7.1

Process the lines from the ospf.txt file and print information for each line
in this form to the stdout:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""

output = "\n{:20} {}" * 5

with open('ospf.txt', 'r') as f:
	for line in f:
		line = line.split()
		
		print(output.format(
        "Prefix", line[1],
        "AD/Metric", line[2].replace("[", "").replace("]", ""),
        "Next-Hop", line[4].replace(",", ""),
        "Last update", line[5].replace(",", ""),
        "Outbound Interface", line[6],
))
				
