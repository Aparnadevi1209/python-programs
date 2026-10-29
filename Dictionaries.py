'''student={"name":"aparna","age":21,"course":"MCA","age":21}
print(student["name"])
print(student.get("age"))
print(student.get("city","not found"))
print(student)
student["city"]="pithapuram"
print(student)
student.update({"age":22})
print(student)
student.pop("age")
print(student)'''
student={"name":["aparna","appu"],"age":[21,23],"course":["MCA","MBA"]}
print(student)    #adding munltiple elements in single key[
print(student.keys()) #all the keys of dictionaries
print(student.values())
print(student.items())
