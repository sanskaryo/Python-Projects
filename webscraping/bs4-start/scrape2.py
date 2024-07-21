import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")
yc_page = response.text
BeautifulSoup("yc_page", "html.parser")

soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.find("a")["href"]
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

max_upvote = max(article_upvotes)
print(max_upvote)
max_index = article_upvotes.index(max_upvote)
print(article_texts[max_index])
print(article_links[max_index])