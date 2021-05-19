import os
import random


def custom_pass(alpha,nums,schars):
    str_pass =""
    a= "abcdefghijklmnoprstuvwxyz"
    b= "1234567890"
    c= "!@#$%^&*()"

    length = alpha + nums + schars
    list_pass =['']*length 
    indices = [index for index in range(length)]

    while alpha!=0:
        num =  random.choice(indices)
        indices.remove(num)
        list_pass[num] =random.choice(a) 
        alpha = alpha -1

    while nums!=0:
        num =  random.choice(indices)
        indices.remove(num)
        list_pass[num] =random.choice(b) 
        nums = nums -1
    
    while schars!=0:
        num =  random.choice(indices)
        indices.remove(num)
        list_pass[num] =random.choice(c) 
        schars=schars -1

    str_pass = str.join("",list_pass)
    #str_pass = ''.join(list_pass)
    return str_pass




if __name__ =="__main__":
    print(custom_pass(alpha=3,nums=3,schars=3))

