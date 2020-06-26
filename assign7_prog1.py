rows = 4
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
 
    print("")

n=int(input("Enter the number of integers : "))
a=[]
for i in range(0,n):
    elem=int(input("Enter integers: "))
    a.append(elem)
avg=sum(a)/n
print("Average of integers in the list",round(avg,2))