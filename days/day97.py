import requests, os, openai
from bs4 import BeautifulSoup

#url = input("Paste wiki url: ")
url = "https://en.wikipedia.org/wiki/Cloud_computing"
response = requests.get(url)
html = response.text
#print(html)

soup = BeautifulSoup(html, "html.parser")
#div
#mw-parser-output
#p

article = soup.find_all("div", {"class": "mw-parser-output"})[0]

content = article.find_all("p")
print(len(article))

text = ""
for p in content:
  text += p.text

print(text)

# openai part
# this is just there as a part of the solution,
#+as i do not have credit on openai
###################################################
# instantiate the secret env vars
openai.api_key = os.environ["openai"]
openai.organization = os.environ["organizationID"]
openai.Model.list()

prompt = f"Summarise the text below in no more than 3 paragraphs. {text}"

response = openai.Completion.create(model="text-davinci-002",
                                    prompt=prompt,
                                    temperature=0,
                                    max_tokens=150)

print(response["choices"][0]["text"].strip())

refs = soup.find_all("ol", {"class": "references"})
for ref in refs:
  print(ref.text.replace("^ ", ""))
