#!/usr/bin/env python3
# -*- coding: utf-8 -*

#廖雪峰网站 多进程

import os 

print('Process (%s) start ....' % os.getpid())
pid = os.fork()
print(pid)
if pid == 0:
	print('I am child process (%s) and my parent is %s.' %(os.getpid(), os.getppid()))
else:
	print('I (%s) just created a child a child process (%s).' %(os.getpid(),pid))

