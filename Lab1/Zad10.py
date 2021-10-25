#zad10
a = "asa12bb3bb21asa"

def palindrom(x):
    y = int(len(x))
    for i in range(0, y):
        if x[y-i-1] != x[0+i]:
            return "nie"
    return "tak"

print(palindrom(a))