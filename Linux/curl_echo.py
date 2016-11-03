#!/usr/bin/env python
import os
import sys
import linecache

file_temp = open("file_path",'r')
while True:
	line = file_temp.readline()
	if line:
		cmd = 'curl -i '+ line
		result = os.popen(cmd).read()
		temp = open("temp.txt",'w')
		temp.write(result)
		temp.close()
		line = linecache.getline("temp.txt",line_number)
		print('========================================')
		print line
		print('========================================')
		os.system("curl -i ")+ line[start:end]
	else:
		break
file_temp.close()
