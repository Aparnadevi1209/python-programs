#write a programm to desine a calculater on user chosies?

print("1.add\n 2.sub\n 3.mul\n 4.div\n 5.exit\n")
chosie=int(input("enter the chosie"))
while(chosie<=4):
    n1=int(input("enter number1:"))
    n2=int(input("enter number2:"))
    if chosie==1:
        print(n1+n2)
    elif (chosie==2):
        print(n1-n2)
    elif chosie==3:
       print(n1*n2)
    elif chosie==4:
       print(n1%n2)
    else:
       break;
    chosie=int(input("enter the chosie"))   
        
        


         
           

