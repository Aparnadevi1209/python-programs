'''names=["appu","uma","bhavani"]
it=iter(names)
while True:
    try:
        iteam=next(it)
        print(iteam)
    except StopIteration:
        break


sum=range(1,5)
it=iter(sum)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))


#unpacking
f=[10,20,30,40]
a,b,c,d=f
print(a)
print(b)
print(c)
print(d)

#tuple

marks=(40,50,30,40)
colors=("red","green","blue")
single=(5,)
empty=()
print(marks[0])
#marks[0]=99
print(colors[1])
print(marks[:2])
print(marks.count(40))
print(marks.index(30))
print(len(colors))


languages=("python","java","c","R")
print(languages)
print(languages[1])
print(languages[1:3])
print(len(languages))

student=101,"aparna","MCA"

marks=[[75,80],[82,90],[91,88]]
print(marks)
print(marks[0])
print(marks[1][1])


marks=[[75,80],[82,90],[91,88]]
for i in marks:
    for j in i:
        print(j,end=" ")
    print()    



 #matrix addition
A=[[1,2],[3,4]]
B=[[5,6],[7,8]]
c=[]
for i in range(2):
    row=[]
    for j in range(2):
        row.append(A[i][j]+B[i][j])
    c.append(row)
print(c)
for i in c:
    for j in i:
        print(j,end=" ")
    print()

#sum and average
    
num=[25,30,45,20,10]
total=sum(num)
avg=total/len(num)
c=[]
print("sum=",total)
print("Average=",avg)

#even numbers 
for i in num:
    if i%2==0:
       c.append(i)   # print(i)
print(c)

# printing vowels 
name="aditya"
c=[]
for i in name :
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
       c.append(i)
print(c) '''      

name="aditya"
o=['a','e','i','o','u']
for i in name:
    if i in o:
        name.append(i)
print(name)        
    


         
    


























       





