def Lisearch(L, N):
    Found = False
    pos = 0
    while pos < len(L) and not Found:
        if L[pos] == N:
            Found = True
        else:
            pos = pos + 1
    return Found, pos

print("LinearSearch :")
print(Lisearch([7,10,12,14,16,20,29,37], 14))
print("LinearSearch :")
print(Lisearch([7,10,12,14,16,20,29,37], 29))