"""DevNet High - Class of 2020 - Challenge 1"""

import random
import ipaddress

# TODO: Write a print statement that displays both the type and value of 'ip'
ip = "10.1.1.200"
print("The type of 'ip' is {} and the value of 'ip' is {}".format(type(ip), ip))

# TODO: Write a conditional to print out if `i` is less than or greater than 14
i = random.randint(12, 17)
print('i is {}'.format(i))
if i < 14:
    print("i is less than 14")
elif i > 14:
    print("i is greater than 14")
else:
    print("i is equal to 14")

# TODO: Write a conditional that prints the serial number of the device
devices = ({'CAT9300':'XVNM1245ERGC'}, {'ISR4331':'VNMM8742THBX'}, {'NGFW2120':'EAQP4900RTJO'})
device = random.sample(devices, 1)[0]

# Didn't use a conditional, approached this in a different way!
model = list(device.keys())[0]
serial = list(device.values())[0]
print("The", model, "serial number is", serial)

# Function for converting CIDR notation into 32-bit netmask (nothing to do here)
def cidr_to_netmask(ip_str):
    ip = ipaddress.IPv4Network(ip_str)
    return ip.with_netmask

'''
TODO: Call the function above few times so that the input of IP network with CIDR displays the IP network with 32-bit netmask
Example:
Input would be '10.1.1.0/24' and when printed out the output would be '10.1.1.0/255.255.255.0'
'''

address_input = input("Enter the IP network and mask in CIDR format: ")
address_output = cidr_to_netmask(address_input)
print("The IP network and mask in 32-bit format is:", address_output)
