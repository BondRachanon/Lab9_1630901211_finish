#L=List
#N=Num
#M=Mid
def search(L,N):
    l = 0
    V = len(L)-1
    while l<=V:
       M = (l+V) //2
       if L[M] == N:
          globals()['pos'] = M
          return True
       else:
           if L[M] < N:
              l = M;
           else:
              V = M;
pos = -1
N = 14
L = [7,10,12,14,16,20,29,37]
if search(L,N):
   print("L Found Is : ",pos+1)
else:
   print("L Not Found Is :")
N = 29
if search(L,N):
   print("L Found at Is :",pos+1)
else:
   print("L Not Found Is :")