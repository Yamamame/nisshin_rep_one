#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import subprocess
import re
import pprint
sys.path.append('./lib')

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

#コマンドとオプションを分割して投げる必要があるため分割
sprited = re.split('\s+',cmd,0)
#pprint.pprint(sprited)
# cmd    = sprited[0]
# option =  sprited[1]
# print "start!!"
# check = subprocess.check_call(sprited)
# print "end  !!"
# print check

buf = []
prcss1 = subprocess.Popen(sprited,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# stdoutput_out , stderr_out = prcss1.communicate()
# print "{} : {} : {}".format("prcss1",stdoutput_out,stderr_out)

while True:
    # バッファから1行読み込む.
    line = prcss1.stdout.readline()
    buf.append(line)
    sys.stdout.write(line)

    # バッファが空 + プロセス終了.
    if not line and prcss1.poll() is not None:
        break
