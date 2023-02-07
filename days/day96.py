# web scraping
# scrape kackernews
# display headlines that display python or Replit

# import required libraries
import requests
from bs4 import BeautifulSoup

# print the title in color
blue = "\033[94m"
white = "\033[0m"  # this reverts the writing back to white (default)

# loop through the first 10 pages
# and get any titles containing "replit" or "python"
for i in range(1, 11):
  # the website to be scraped containing the page to go to "i"
  url = f"https://news.ycombinator.com/news?p={i}"
  # get the response
  response = requests.get(url)
  html = response.text
  #print(html)

  # use BeautifulSoup to get the info
  soup = BeautifulSoup(html, "html.parser")
  # titles we are looking for located in <span> elements
  myLinks = soup.find_all("span", {"class": "titleline"})

  # loop through the links and to see if they contain our keywords
  for link in myLinks:
    if "python" in link.text.lower() or "replit" in link.text.lower():
      # output the title in blue color
      print(f"{blue}{link.text}{white}")
      # output the href link
      to_it = link.find("a", href=True)
      print(f"""\t{to_it["href"]}""")
      print()
