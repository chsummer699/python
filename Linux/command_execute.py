# /usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'summer'
import os
import commands
import subprocess
import re
import string


def check_file_1(path):
    command = 'du -sh %s' % path
    print os.system(command)


def check_file_2(path):
    command = 'du -sh %s' % path
    status, output = commands.getstatusoutput(command)
    print status
    print output
    memory = 0
    m = re.search(r'(\d\.?\d)M',output)
    if m:
        memory = string.atof(m.group(1))
    print memory
    if memory > 0 :
        print 'tvod recording is normal'
    else:
        print 'tvod recording is abnormal'


def check_file_3(path):
    command = 'du -sh %s' % path
    p = os.popen(command)
    x = p.read()
    print x
    p.close()


def check_file_4(path):
    command = 'du -sh %s' % path
    print subprocess.call(command, shell=True)


#check_file_1('/home/summer/')
print '====================='
check_file_2('/home/summer/')
print '====================='
#check_file_3('/home/summer/')
#print '====================='
#check_file_4('/home/summer/')
#print '====================='
