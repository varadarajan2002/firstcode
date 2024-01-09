i=0
word="Hello world!"
while i < len(word):
    if word[i]=='e' or word[i]=='l':
        i+=1
        continue
    print("changed word:",word[i])
    i+=1

