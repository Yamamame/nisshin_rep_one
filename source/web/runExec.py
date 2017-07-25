#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import subprocess
import re
import pprint

args   = sys.argv
cmd    = ''
option = ''
try:
    cmd  = args[1]
except IndexError:
    print "not process!!"

#arg1が無ければ終了
if not cmd :
	sys.exit()

sprited = re.split('\s+',cmd,0)
#pprint.pprint(sprited)
cmd    = sprited[0]
option =  sprited[1]
print "start!!"
check = subprocess.call(sprited)
#print check
