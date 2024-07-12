a="WIPRO"
sum=0
l=[]
l2=[]
val=""
for i in a:
     
    l.append(ord(i))
    
for j in range(1,len(l)):
    if l[j]%j==0:
        l2.append(l[j])
        sum+=l[j]

for k in l2:
    val=val+chr(k)
print(val,sum)
 
    
