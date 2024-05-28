import os
import time
os.system('cls')

print("==========================================")
print ("----------------LOGO VISA----------------")
print("==========================================\n")

from termcolor import colored, cprint
time.sleep(0.5)
for i in range (2):
    cprint (" "*40, 'white', "on_blue")
print (" ")

time.sleep (0.5)
print(colored("  |||      |||   |||   |||||    ||||||","blue"))
print(colored("   ||      ||    |||   ||       ||  ||","blue"))
print(colored("    ||    ||     |||   |||||    ||||||","blue"))
print(colored("     ||  ||      |||      ||    ||  ||","blue"))
print(colored("       ||        |||   |||||    ||  ||","blue"))
print (" ")

time.sleep(0.5)
for i in range (2):
    cprint(" "*40, 'white', "on_light_yellow")
print (" ")