#dictionaries are used to store data values in key:value pair
#they r unorderedb , mutuable(changeable) & don't allow duplicate key
#dict are unorder
info={
    "key":"value",
    "name":"yanna",
    "learning":"coding",
    "age":19,
    "is_adult":True,
    "subjects":["dbms","os","itw","de","math","dsa"],
    "marks":9.17,
    "main_Subject":("dsa","os","dbms")
}
print(info)
print(type(info))
print(info["marks"])
print(info["main_Subject"])
info["name"]="yans"    #cahneg in name
print(info)
info["surname"]="patel"   #add another ket:value
print(info)

null_dict={}
print(null_dict)
null_dict["name"]="zaira"
print(null_dict)

#nested dictionary in python
student={
    "name":"zai",
    "subject":{
        "phy":98,
        "math":99,
        "chem":{
            "organic":15,
            "inorganic":25,
            "biochemestry":30,
        }
    }
}
print(student)
print(student["subject"])
print(student.keys())
print(list(student.keys()))   #typecast in list
print(len(student))
print(len(list(student.keys())))
print(student.values())
pairs=list(student.items())
print(pairs[0])
print(pairs[1])
print(student.get("name"))
print(student.get("subject"))
print("before")
#print(student["name2"])     #iss me error aayega and iss me iss ke baad vale sentences print nhi honge
#print(student.get("name2"))    #iss me error nhi aayega-->None aayega  iss me iss ke baad vale sentances print hoge
print("after")
new_dict={"city":"Delhi","age":19}
student.update(new_dict)
print(student)
