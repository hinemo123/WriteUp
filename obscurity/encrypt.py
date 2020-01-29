with open("check64.txt") as f:
    check=f.read()
with open('out64.txt') as f:
    out=f.read()
def encrypt(text, crypto):
    key=""
    i=0
    for x in text:
        key+=chr(ord(crypto[i])-ord(x))
        i+=1
    print(key)
def decrypt(text,key):
    keylen = len(key)
    keyPos = 0
    decrypted = ""
    for x in text:
        keyChr = key[keyPos]
        newChr = ord(x)
        newChr = chr((newChr - ord(keyChr)) % 255)
        decrypted += newChr
        keyPos += 1
        keyPos = keyPos % keylen
    return decrypted
with open('passre.txt') as f:
    password=f.read()
with open('key.txt') as f:
    key=f.read()
print(decrypt(password,key='alexandrovich'))
#encrypt(check,out)
