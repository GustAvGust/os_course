#!/usr/bin/python3
import os
import random
import sys
import time

sec = int(sys.argv[1])

print("Child is running at process with PID {} with arg {}.".format(os.getpid(), sec))

time.sleep(sec)

print("Process with PID {} is finished".format(os.getpid()))

os._exit(random.randint(0, 1))
