import numpy as np
def cuss_pass_gen(alpha,nums,schars):

    str_pass=''
    a="abcdefghijkjlmopqrstuvwxyz"
    b='1234567890'
    c="!@#$%^&*()"
    length = alpha + nums + schars
    arr_pass = np.array([None]*length)
    
    while None  in arr_pass :
        while alpha!=0:
            num = np.random.randint(0,length)
            if arr_pass[num] == None:
                arr_pass[num] = a[np.random.randint(26)]
                alpha = alpha - 1
        while nums!=0:
            num = np.random.randint(0,length)
            if arr_pass[num] == None:
                arr_pass[num] = b[np.random.randint(10)]
                nums  = nums -1
        

        while schars!=0:
            num = np.random.randint(0,length)
            if arr_pass[num] == None:
                arr_pass[num] = c[np.random.randint(len(c))]
                schars = schars -1
    for i in range(length):
        str_pass = str_pass + str(arr_pass[i])
    return str_pass

if __name__ == "__main__":
    print(cuss_pass_gen(10,3,3))
