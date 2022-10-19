import random
import sys

def getencdict(characters,seed):
    random.seed(seed)
    ret={}
    s=set()
    n=len(characters)-1
    for c in characters:
        while True:
            d=characters[random.randint(0,n)]
            if d in s:
                continue
            else:
                s.add(d)
                ret[c]=d
                break
    return ret

def getdecdict(characters,seed):
    d=getencdict(characters,seed)
    ret={}
    for k in d:
        ret[d[k]]=k
    return ret

allowed=" .?!ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-*/()_:@"
seed=int(input("Enter the seed: "))
ed=input("Enter e to encrypt or d to decrypt: ")
if ed=='e':
    pad=getencdict(characters=allowed, seed=seed)
elif ed=='d':
    pad=getdecdict(characters=allowed, seed=seed)
else:
    print("Unrecognized option.")
    exit()
text=input("Enter the text: ")
ot=""
for c in text:
    try:
        ot+=pad[c]
    except:
        ot+=c
sys.stdout.write('"'+ot+'"\n')
