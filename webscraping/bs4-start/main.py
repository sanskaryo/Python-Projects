from bs4 import BeautifulSoup

# Open and read the HTML file
with open(r'D:\Python Projects\webscraping\bs4-start\website.html', 'r', encoding='utf-8') as file:
    contents = file.read()
    

soup = BeautifulSoup(contents, "html.parser")

print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.prettify())
print(soup.a)
print(soup.find_all('a'))
print(soup.find(id="name"))
print(soup.get_text())
print(soup.get('h1'))

heading = soup.find(name="h1", id="name")       
print(heading) 

section_heading = soup.find(class_="heading")
print(section_heading)

company_url = soup.select_one(selector="p a")
print(company_url)\
    
    
heading =     soup.select(".heading")
print(heading)
    
