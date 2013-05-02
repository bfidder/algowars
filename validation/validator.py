#!/usr/bin/python

import sys

input_filename = sys.argv[1]

output_filename = sys.argv[2]

time_output = "{0:.2f}"
input_file = open(input_filename, 'r')
numMachines = int(input_file.readline())
numTasks = input_file.readline()
tasks = input_file.readline().split()
machines = input_file.readline().split()

output_file = open(output_filename, 'r')

output = output_file.readlines()
machine_num = 0
totals = []

time  = float(output[len(output) -1 ])
output = output[:len(output)-1]
print "time: " , time_output.format(time)
given_total = 0
for line in output:
	tasks_per_machine = line.split()
	if tasks_per_machine != []:
		total_machine = 0.0
		for task in tasks_per_machine:
			total_machine += float(tasks[int(task)])
		total = total_machine/float(machines[machine_num])
		totals.append(total)
	else:
		totals.append(0.0)
	machine_num += 1

total_time_expected = max(totals)
print "calculated:", time_output.format(total_time_expected)
if abs(total_time_expected - time) <= .01:
	print "passed"
else:
	print "unexpected total"

