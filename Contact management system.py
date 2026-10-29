print(" 1.Add contact 2.search contact  3.update contact 4.Delete contact 5.Display contact 6.Exit")
contact={}
menu=int(input("enter menu number:"))
while(menu<=6):
    if menu==1:
        print("give the detalis to add in contact")
        name=input("enter your name")
        branch=input("enter your branch")
        roll=int(input("enter your roll number:"))
        cgpa=int(input("enter your cgpa:"))
        contact.append                   #appaend the all the values to  ontact 
        print("succesfuly add contacts")
    elif menu==2:
        s=input("enter search contact:")
        if s in contact:
            print(s[s])
        else:
            print("not found")
    elif menu==3:
        print("updateing contact")
        contact["cgpa"]=int(input("enter the updated cgpa:"))
        print("updated succesfuly")
    elif menu==4:
        print("deleting contact")
        del contact[input(" enter the deleting contact")]
        print("succesfuly deleted")
    elif menu==5:
        print("Display the contact")
        print("The contact is",contact)
    else:
        print("succesfuly exited")
        break;
    menu=int(input("enter menu number"))

    
    
    
    
