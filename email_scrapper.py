import requests
from bs4 import BeautifulSoup
import re
at_replacables = ["[at]","-at-", "(at)", " at ",  " @ ", "@ ", " @"]
dot_replacables = ["[dot]", "-dot-", "(dot)", " dot ", " . ", " .", ". "] 
regex = "([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)"

def replaceObscure(txt):
  txt = txt.lower()
  for replacable in at_replacables:
    txt = txt.replace(replacable, "@")
  for replacable in dot_replacables:
    txt = txt.replace(replacable, ".")
  return txt

emails = []
quote_page = None
while type(quote_page) != str:
  quote_page = input("enter page to scrape:")

page = requests.get(quote_page)
soup = BeautifulSoup(page.content,"html5lib")
#for line in soup.get_text().splitlines():
txt = replaceObscure(soup.get_text())
#print(txt)
foundEmails = re.findall(regex,txt)  
print(foundEmails)
