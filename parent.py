#!/usr/bin/python3
import os
import random
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-n")
args = parser.parse_args()
n = int(args.n)

for i in range(n):
  child = os.fork()
  if (child == 0):
    break

if child > 0:
  ret = os.wait()

  print("Child process with PID {} is finished. Finish status is {}.".format(child, ret))
elif child == 0:
  os.execl("child.py", "child.py", str(random.randint(5, 10)))
else:
  print("Error happens")
