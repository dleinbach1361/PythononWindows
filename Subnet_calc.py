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
        #print(network_address_binary)

        broadcast_address_binary = binary_ip[:(no_of_ones)] + '1' * no_of_zeros
        #print(broadcast_address_binary)


        net_ip_octets = []

        for bit in range(0, 32, 8):
            net_ip_octet = network_address_binary[bit: bit + 8]
            net_ip_octets.append(net_ip_octet)

        #print(net_ip_octets)

        net_ip_address = []

        for each_octet in net_ip_octets:
            net_ip_address.append(str(int(each_octet, 2)))

        network_address = '.'.join(net_ip_address)

        #print(network_address)

        bst_ip_octets = []

        for bit in range(0, 32, 8):
            bst_ip_octet = broadcast_address_binary[bit: bit + 8]
            bst_ip_octets.append(bst_ip_octet)

        bst_ip_address = []

        for each_octet in bst_ip_octets:
            bst_ip_address.append(str(int(each_octet, 2)))

        broadcast_address = '.'.join(bst_ip_address)

        #print(broadcast_address)

        #Print all the results
        print('\n')
        print('Network Address is: %s' % network_address)
        print('Broadcast Address is: %s' % broadcast_address)
        print('Number of valid hosts per subnet: %s' % no_of_hosts)
        print('Wildcard Mask: %s' % wildcard_mask)
        print('Mask bits: %s' % no_of_ones)
        print('\n')


        while True:
            generate = input('Would you like to generate a random IP from this subnet? (y/n): ')

            if generate == 'y':

                generated_ip = []

                for indexb, oct_bst in enumerate(bst_ip_address):
                    for indexn, oct_net in enumerate(net_ip_address):
                        if indexb == indexn:
                            if oct_bst == oct_net:
                                generated_ip.append(oct_bst)
                            else:
                                generated_ip.append(str(random.randint(int(oct_net), int(oct_bst))))
                
                y_iaddr = '.'.join(generated_ip)

                print('Random IP address is: %s' % y_iaddr)
                print('\n')
                continue

            else:
                print('See ya later!\n')
                break
            


    except KeyboardInterrupt:
        print("\n\nProgram aborted by user. Exiting...\n")
        sys.exit()      


subnet_calc()


