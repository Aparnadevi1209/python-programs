'''#String Concatenation
frist = input("enter frist name ")
last = input("enter last name")
fullname = frist+ " "+last
print("Full Name:",fullname)

#String Methods
print("upper:" ,fullname.upper())
print("lower:" ,fullname.lower())
print("title" ,fullname.title())
print("length:" ,len(fullname))
#String sclicing
name = input("entaer th name:")
print("frist 5 characters:",name[:5])
print("last 5 characters:",name[-5:])
print("reverse:",name[::-1])
#count words
sentence = input("enter any sentence :")
words = sentence.split()
print("number of words:",len(words))
for ch in sorted(set(sentence)): 
    print(ch, "=", sentence.count(ch))'''

roll_no="MCA070"
print(roll_no.isalnum())
print(roll_no.isdigit())
print("course",roll_no[:3])
print("number",roll_no[3:])
text = input(" enter age : ")
if text.isdigit():
    age =int(text)
    print("valid number:",age)
else:
    print("digits only,please")




