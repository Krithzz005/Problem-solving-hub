n="1214"
if len(n)!=4:
    print(n , "is not a valid car number")
else:
    num=int(n)
    og_n=num
s=0
for i in range(0,4):
    s+= og_n%10
    og_n//=10
if s%3==0 or s%5==0 or s%7==0 :
    print(n, " is the Lucky number")
else:
    print("Sorry its not my lucky number")
