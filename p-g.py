import string
import random
import os


yellow = '\033[93m'
green = '\033[92m'
red = '\033[91m'
b = '\033[1m'
print (green+b+"""


         ██████╗        ██████╗ 
         ██╔══██╗      ██╔════╝ 
         ██████╔╝█████╗██║  ███╗
         ██╔═══╝ ╚════╝██║   ██║
         ██║           ╚██████╔╝
         ╚═╝            ╚═════╝        coded by Asif lone
"""+b+red)

print (green+b+"              <===[ coed by Asif lone]===>"+b+green)
print (" ")
print (yellow+b+"             <===( YOUTUBE==> Techno Lone )===>"+b+yellow)
print("")
plength = int(input("Please enter password length\n"))
if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
random.shuffle(s)
print("".join(s[0:plength]))
print (yellow+b+"====> password  generated :) save the password<===="+b+yellow)