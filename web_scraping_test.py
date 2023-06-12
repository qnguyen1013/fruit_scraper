from bs4 import BeautifulSoup

# r for read
with open("test_html.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

# print(doc.prettify())

# get by tag type
tag  = doc.title
print(tag)

#get string inside
print(tag.string)

#modify the string
tag.string = "Hello"
print(tag.string)

tags = doc.find_all("p")
print(tags)

#access nested tags
tags = doc.find_all("p")[0]
print(tags)


