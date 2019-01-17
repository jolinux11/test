import string
import random

a=string.ascii_letters
a=a+string.digits
b=random.sample(a,8)
otp=''
count=0
while count < len(b):
    otp=otp+str(b[count])
    count+=1
print('captcha:',otp)
c=0
while c<3:

    x=input('enter the captcha:')
    if x==otp:
        print('correct captcha')
        break;
    else:
        print('incorrect captcha')
    c+=1
#print ('max guess finished reset captcha')
