#!/usr/bin/env python3.8

from argparse import ArgumentParser
import os
import subprocess

parser = ArgumentParser(description="kill the running process on a given port")
parser.add_argument('port', type=int, help='port you want the process to be killed')

port = parser.parse_args().port

try:
    result = subprocess.run(
            ["lsof", "-n", "-i4TCP:%s" % port],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
except subprocess.CalledProcessError:
    print (f"no process listening on port {port}")
else:
    listening = None
    for line in result.stdout.splitlines():
        if "LISTEN" in str(line):
            listening = line
            break

    if listening:
        pid = int(listening.split()[1])
        os.kill(pid, 9)
        print(f"process with pid {pid} killed")
    else:
        print(f"no process listening on port {port}")


