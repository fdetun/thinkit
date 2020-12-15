A =[1, 1, 1,0,0]
b=[]
rslt= 0
for i in range(0,len(A), 2):
    if A[0] == 1:
        b.extend([1, 0])
    if A[0] == 0:
        b.extend([0, 1])
if len(b) != len(A):
    b.pop()
for i in range(len(A)):
    if A[i] != b[i]:
        rslt += 1
print(rslt)    
print(b)