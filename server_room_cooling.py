#!/usr/local/bin/python3.8

import subprocess
import sys

def main():
#check if argument defined
    if len(sys.argv) > 1:
        rc_num = int(sys.argv[1])
    else:
        rc_num = int(input("Enter raw_column number: "))
    n = 1
    server_room_list = []

    while n <= rc_num:
        line1_str = str(n)
        rc_num_str = str(rc_num)
        n += 1

#get all server room raw and col for each n
        l1 = ("s1_"+line1_str)
        l2 = ("s"+rc_num_str+"_"+line1_str)
        l3 = ("s"+line1_str+"_1")
        l4 = ("s"+line1_str+"_"+rc_num_str)

#set server rooms into the list
        server_room_list.extend([l1, l2, l3, l4])

#get rid of duplicated (corner) values in the list
    unique_list = list(dict.fromkeys(server_room_list))
    print(unique_list)

#connect to each server to change config
    for server in unique_list:
#        cmd = ('./remote_give_more_work.sh', server)   #commented not to get error
        cmd = ('touch', server)                         #for test
        proc = subprocess.Popen(cmd)


if __name__ == "__main__":
        main();
