
# beautifulsoup
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://pyshop.net'
page = urlopen(url)
html = page.read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")

print(soup.title)

# Urllib

start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
print(title)

x = "Belajar"
y = "Python"
result = x > y
print(result)