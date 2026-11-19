import random

f=open("words.txt","r")
count = {}
wordlist=[]
for word in f:
    word = word.strip()
    wordlist.append(word)
    for a,b in zip(word, word[1:]):
        group = a+b
        if group not in count:
            count[group]=0
        count[group]+=1
    for a,b,c in zip(word, word[1:], word[2:]):
        group = a+b+c
        if group not in count:
            count[group]=0
        count[group]+=1

print(count)

groups = []
for group in count:
    groups.append((count[group],group))
groups.sort(reverse=True)
print(groups)
i=0
while i<len(groups):
    word=None
    n,group = groups[i]
    while word not in wordlist or group not in word:
        word=input("Write a word with "+group+":").lower()
    i+=random.randint(1,10)