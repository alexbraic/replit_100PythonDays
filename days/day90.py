import requests, json

result = requests.get("https://randomuser.me/api/")
if result.status_code != 200:
  print("Error! Could not get API")
else:
  user = result.json()
#print(json.dumps(user, indent=2))

#name = f"""{user["results"][0]["name"]["first"]} {user["results"][0]["name"]["last"]}"""
#print(name)
#image = f"""{user["results"][0]["picture"]["large"]}"""

#picture = requests.get(image)

#f = open("image.jpg", "wb")
#f.write(picture.content)
#f.close()

#print(image)

#for person in user["results"]:
#  name = f"""{person["name"]["first"]} {person["name"]["last"]}"""
#  print(name)

# access the site: https://randomuser.me/api/
# get the user fname and lname
# get the user picture
# create an image file and save their picture as their 'first last'.jpg names

i = 0
while i < 10:
  result = requests.get("https://randomuser.me/api/")
  if result.status_code != 200:
    print("Error! Could not get API")
  else:
    user = result.json()

  for person in user["results"]:
    fname = f"""{user["results"][0]["name"]["first"]}"""
    lname = f"""{user["results"][0]["name"]["last"]}"""
    fullname = f"{fname} {lname}"

    image = f"""{user["results"][0]["picture"]["medium"]}"""
    picture = requests.get(image)

    f = open(f"{fullname}.jpg", "wb")
    f.write(picture.content)
    f.close()
    print(f"Saved {fullname}.jpg")
  i += 1
