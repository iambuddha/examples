#!/usr/local/bin/python3.8
## more info https://gist.github.com/gregory-m/107e83cceb3009a080cec12c37e0a989

import sys

def main():
  convert_braille(input_srv_room())

# function to get room number value and check if it is valid
def input_srv_room():
  srv_room_num = int(input())

  if type(srv_room_num) == int and srv_room_num <= 999:    # cheking if entered value is integer and less than 999
    srv_room_num = (f"{srv_room_num:03}")    # adding leading 0s for digits less than 100
    return srv_room_num
  else:
    print((srv_room_num), ("is NOT a valid room number. Exiting..."))
    sys.exit(1)

# function to convert room number in to the braille string for the printer
def convert_braille(room_num):
  num_conv_braille = {
    "1" : "*^^^^^",
    "2" : "*^^*^^",
    "3" : "**^^^^",
    "4" : "***^^^",
    "5" : "*^*^^^",
    "6" : "**^*^^",
    "7" : "****^^",
    "8" : "*^**^^",
    "9" : "^*^*^^",
    "0" : "^***^^"
  }
  braille_tuple = []
  digit_str = str(room_num)

  for digit in digit_str:
    braille_str = str(num_conv_braille[digit])
    braille_devide = [(braille_str[i:i+2]) for i in range(0, len(braille_str), 2)]    # devide the braille string for each digit by 2 symbols
    braille_tuple.append(braille_devide)

  braille_list = [item for t in braille_tuple for item in t]    # converting a tuple of elements to a list of elements
  print (                              # print list of elements in the order the printer follows
    braille_list[0]+
    braille_list[3]+
    braille_list[6]+
    braille_list[7]+
    braille_list[4]+
    braille_list[1]+
    braille_list[2]+
    braille_list[5]+
    braille_list[8]
  )

if __name__ == "__main__":
  main();
