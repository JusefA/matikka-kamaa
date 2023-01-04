def syt(a,b):
    if b==0:
        return a
    else:
        syt(b,a%b)

print(syt(24,60))
