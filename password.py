import random, sys



if len(sys.argv) < 2:
    print("""
         _______________
    < Hello, world! >
     ---------------
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\
                    ||----w |
                    ||     ||
    """)
    sys.exit(0)

password = sys.argv[1]


def leetmode(a):
    b = [{'o': '0'}, {'i': ['1', '!']}, {'s': ['5', '$']}]
    for i in b:
        if a in i:
            if isinstance(i[a], list) == False:
                return i[a]
            else:
                return i[a][random.randint(0, len(i))]
        elif a == 'a':
            return '@'
    return a


def toCapital(a):
    return a.upper()


def addSuffix(a):
    b = ['', '123', '1@', '!', '#']
    return a + b[random.randrange(0, len(b))]

f = open('result.txt','a')
result = []
result.append(password)
while 1:
    new_password = password
    for i in range(random.randint(0, 100)):
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
        f.write(new_password)
        f.write('\n')
        print(new_password)
        print(len(result))
