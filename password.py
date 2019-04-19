import random

password = 'enocpass'


def leetmode(a):
    b = [{'o': '0'}, {'i': '1'}, {'s': '5'}, {'s', '$'}, {'i', '1'}]
    for i in b:
        if a in i:
            return i[a]
        elif a=='a':
            return '@'
    return a


def toCapital(a):
    return a.upper()


def addSuffix(a):
    b = ['', '123', '1@', '!', '#']
    return a + b[random.randrange(0, len(b))]


result = []
result.append(password)
while 1:
    new_password = password
    for i in range(random.randrange(0, 100)):
        a = random.randrange(0, len(password))
        b = random.randrange(0, 2)
        new_password = list(new_password)
        if b == 0:
            new_password[a] = leetmode(password[a])
        if b == 1:
            new_password[a] = toCapital(password[a])

        new_password = ''.join(new_password)
        if len(new_password) == len(password):
            new_password = addSuffix(new_password)
    if new_password not in result:
        result.append(new_password)
        print(new_password)
        print(len(result))
