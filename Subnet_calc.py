import random
import sys

def subnet_calc():
    try:
        print("\n")

        while True:
            ip_address = input("Enter an IP address: ")

            #check valid octets
            ip_octets = ip_address.split('.')

            if (len(ip_octets) == 4) and (1 <= int(ip_octets[0]) <= 223) and (int(ip_octets[0]) != 127) and (int(ip_octets[0]) != 169 or int(ip_octets[1] != 254) and (0 <= int(ip_octets)[1]) <= 255 and 0 <= (ip_octets[2]) <= 255 and 0 <= int(ip_octets[3]) <= 255):
                break

            else:
                print("\nThe IP address is INVALID! Please try again dumbass\n")
                continue

        masks = [255, 254, 252, 248, 240, 224, 192,128, 0]

        while True:

            subnet_mask = input("Enter subnet mask: ")

            mask_octets = subnet_mask.split('.')

            if (len(mask_octets) == 4) and (int(mask_octets[0]) == 255) and (int(mask_octets[1]) in masks) and (int(mask_octets[2]) in masks) and (int(mask_octets[3]) in masks) and (int(mask_octets[0]) >= int(mask_octets[1]) >= int(mask_octets[2]) >= int(mask_octets[3])):
                break

            else:
                print("\nThe subnet mask is INVALID dumbass! Try again\n")
                continue
            