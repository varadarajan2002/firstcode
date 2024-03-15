print("program that counts the number of characters")

def countchar(string):
    unique={}

    for i in string:
        chaar = unique.keys()

        if i in chaar:
            unique[i] +=1
        else:
            unique[i] = 1

    return unique
print(countchar("varadarajan"))

