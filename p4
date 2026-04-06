#RSA
import random
import math
msg=input("Enter the message to encrypt: ").replace(" ","")
def gen_primes(n1, n2):
    primes=[]
    for num in range(n1,n2+1):
        if num>1:
            for j in range(2,num):
                if num%j==0:
                    break
            else:
                primes.append(num)
    return primes
def gen_PUPRkeys():
    p=random.choice(gen_primes(20,50))
    q=random.choice(gen_primes(60,90))
    n=p*q
    phi=(p-1)*(q-1)
    #1<e<phi
    e=2
    while (e<phi):
        if math.gcd(e,phi)==1:
            break
        e+=1
    i=1
    while True:
        d=((phi*i)+1)/e
        if int(d)==d:
            break
        i+=1
    return [e,d,n]
def RSA_encrypt(e, n, pt):
    codes=[ord(symbol) for symbol in pt]
    ct=[chr((msg**e) % n) for msg in codes]
    return "".join(ct)
def RSA_decrypt(d, n, ct):
    char_codes=[ord(symbol) for symbol in ct]
    pt=[chr((msg**int(d))%n) for msg in char_codes]
    return "".join(pt)
keys=gen_PUPRkeys()
e=keys[0]
d=keys[1]
n=keys[2]
ctxt=RSA_encrypt(e,n, msg)
print("Roll Number TCS2526062")
print("Cipher Text: ",ctxt)
print("Original Text: ",RSA_decrypt(d,n,ctxt))
