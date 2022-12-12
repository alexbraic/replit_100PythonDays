# create a contact card using a dictionary
# print the details of it
details = {
    "name": "Alex B",
    "dob": "01/01/1944",
    "phone_nr": "0876444444",
    "email": "alex.b@mymail.com",
    "address": "Middle of Nowhere, Apt. 1, Random Spot"
}

n = "Name: "
d = "Date of Birth: "
p = "Phone Number: "
e = "Email: "
a = "Address: "

print(
    f'{n:<15}{details["name"]}\n{d:<15}{details["dob"]}\n{p:<15}{details["phone_nr"]}\n{e:<15}{details["email"]}\n{a:<15}{details["address"]}'
)
