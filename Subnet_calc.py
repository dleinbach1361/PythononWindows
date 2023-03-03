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

        #convert mask to bin
        mask_octets_binary = []

        for octet in mask_octets:
            binary_octet = bin(int(octet)).lstrip('0b')

            #append to list mask_octets_binary
            mask_octets_binary.append(binary_octet.zfill(8))

        #print mask as long binary
        binary_mask = ''.join(mask_octets_binary)

        no_of_zeros = binary_mask.count('0')
        no_of_ones = 32 - no_of_zeros
        no_of_hosts = abs(2 ** no_of_zeros - 2)

        #print(no_of_zeros)
        #print(no_of_ones)
        #print(no_of_hosts)


        #create wildcard mask
        wildcard_octets = []

        for octet in mask_octets:
            wild_octet = 255 - int(octet)
            wildcard_octets.append(str(wild_octet))

        #put it all back together
        wildcard_mask = '.'.join(wildcard_octets)

        #convert the IP to binary
        ip_octets_binary = []

        for octet in ip_octets:
            binary_octet = bin(int(octet)).lstrip('0b')

            ip_octets_binary.append(binary_octet.zfill(8))

        binary_ip = ''.join(ip_octets_binary)

        network_address_binary = binary_ip[:(no_of_ones)] + '0' * no_of_zeros
        print(network_address_binary)

        broadcast_address_binary = binary_ip[:(no_of_ones)] + '1' * no_of_zeros
        print(broadcast_address_binary)

        



    except KeyboardInterrupt:
        print("\n\nProgram aborted by user. Exiting...\n")
        sys.exit()      


subnet_calc()