#!/usr/local/bin/python3

import os
import sys
import time

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} program_name program_args")
    sys.exit(1)

args = sys.argv
args.pop(0)
program = " ".join(args)

print(f"\n==========STARTING {program}==========\n")

start_time = time.time()

os.system(program)

end_time = time.time()

print(f"\n==========FINISHING {program}==========\n")

elapsed_time = end_time - start_time

print(f"[*] \"{program}\" took {round(elapsed_time, 4)} seconds to run")