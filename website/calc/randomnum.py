from numpy import random
def password_gen():
    x = "abcdefghijkjlmopqrstuvwxyz1234567890!@#$%^&*()"
    password=""
    random_nums =random.randint(10,15)
    while random_nums!=0:

        password = password + x[int(random.randint(len(x)))]
        random_nums = random_nums - 1

    return password

