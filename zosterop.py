import random, sys
import argparse
from xeger import Xeger
import pyfiglet
import base64
if len(sys.argv) < 2:
    print("""
         _______________
    < Hello, truongtn! >
     ---------------
            \   ^__^
             \  (oo)\_______
                (__)\       )\/
                    ||----w |
                    ||     ||
    Usage: zosterop.py -p [password] 
    """)
    sys.exit(0)

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--pass', help='password', dest='root')
parser.add_argument('-r', '--regex', help='Regex. Example: [aA]dmin[a-d1-3]{0,4}@[a-d1-6]{4,10}', dest='reg')
parser.add_argument('-l', '--limit', help='limit or length', dest='limit')
parser.add_argument('-m', '--mics', help='misc', dest='mics')
parser.add_argument('-b64', '--base64', help='base64 encode', dest='b64')
args = parser.parse_args()
result = []
x=Xeger()
#######################################
class passWord():
    def __init__(self,l,tempList):
        self.l=l
        self.tempList=tempList
        self.x=Xeger()

    def genPass2(self):
        result=[]
        f = open('result.txt','a')
        for i in range(0,self.l):
            temp=""
            for i in self.tempList:
                if i[1]=='0': temp+=self.x.xeger(i[0])
                elif i[1]=='1': 
                    temp+=''.join(sorted(self.x.xeger(i[0])))
                elif i[1]=='2': 
                    temp+=''.join(sorted(self.x.xeger(i[0]),reverse=True))
                elif i[1]=='3':
                    if bool(random.getrandbits(1)):
                        temp+=''.join(sorted(self.x.xeger(i[0]),reverse=True))
                    else:
                        temp+=''.join(sorted(self.x.xeger(i[0])))
            if temp not in result: 
                result.append(temp)
                f.write(temp)
                f.write('\n')
                print(temp)
        return result

    def genPass2WithBase64(self):
        result=[]
        f = open('result.txt','a')
        for i in range(0,self.l):
            temp=""
            for i in self.tempList:
                #print(i[0])
                if i[1]=='0': temp+=self.x.xeger(i[0])
                elif i[1]=='1': 
                    temp+=''.join(sorted(self.x.xeger(i[0])))
                elif i[1]=='2': 
                    temp+=''.join(sorted(self.x.xeger(i[0]),reverse=True))
                elif i[1]=='3':
                    if bool(random.getrandbits(1)):
                        temp+=''.join(sorted(self.x.xeger(i[0]),reverse=True))
                    else:
                        temp+=''.join(sorted(self.x.xeger(i[0])))
            if temp not in result: 
                result.append(temp)
                f.write(base64.b64encode(temp.encode('utf-8')).decode('utf-8'))
                f.write('\n')
                print(base64.b64encode(temp.encode('utf-8')).decode('utf-8'))
        return result

##########################################################################################
if args.root:
    print("")
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
        b = ['', '123', '1@', '!', '#', '@123']
        return a + b[random.randrange(0, len(b))]


    f = open('result.txt','a')
    result.append(password)
    try:
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
    except (KeyboardInterrupt, SystemExit):
        print('\n')
        print('[INFO]: The file result is saved in result.txt')
        sys.exit(0)
if args.reg:
    f = open('result.txt','a')
    x=Xeger()
    l= int(args.limit if args.limit else 1000)
    for i in range(0,l):
        a=x.xeger(args.reg)
        if a not in result:
            result.append(a)
            f.write(a)
            f.write('\n')
            print(a)
if args.mics:
    tempList=[]
    l= int((args.limit if args.limit else 1000))
    for i in range(0,int(args.mics)):
        a=input("Nhap vao regex  >>")
        b=input("Sort (0,1,2,3)? >>")
        tempList.append([a,b])
    pw=passWord(l,tempList)
    if args.b64:
        pw.genPass2WithBase64()
    else:
        pw.genPass2()