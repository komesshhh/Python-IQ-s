a=input()
b=""
for i in range(len(a)):
    ch=int(ord(a[i]))+1       # convert charater to ascii value.
    b=b+chr(ch)                # chr() - is used to convert int to character.
print(b.replace("!"," "))