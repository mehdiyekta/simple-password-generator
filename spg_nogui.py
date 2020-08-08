import random
import re
import time
realtimeofuser=time.asctime(time.localtime(time.time()))
a=input('len: ')
if not re.match('[0-9]',a):
    print('Just number')
    a=input('len: ')
n=input('name for password\nforexample:instagram\n:')
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(s,int(a) ))
print(p)
print('save?')
b=input('[Y,N]')
if b.startswith(('Y','y','O','o')):
    with open('pass.txt','a') as file_name:
        c=n+': '+'\n'+('-'*15)+str(realtimeofuser)+('-'*15)+'\n'+str(p)+'\n'+('-'*54)+'\n'
        file_name.write(c)
        file_name.close
        print('Done!')
else:
    exit()
