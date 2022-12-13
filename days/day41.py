# get user input and store a website info in a dict

myDict = {"name": None, "url": None, "desc": None, "raintg": None}

print("Add the followintg details for the website:")
print()
myDict["name"] = input("Name: ")
myDict["url"] = input("Url: ")
myDict["desc"] = input("Description: ")
myDict["rating"] = input("Rating: ")
print()

for key, value in myDict.items():
    print(f"{key}: {value}")
