import requests
from bs4 import BeautifulSoup

url = "https://mavrix.in/2012/12/the-top-100-bollywood-songs-of-2012/"
response = requests.get(url)

wesbsite_html = response.text
soup = BeautifulSoup(wesbsite_html, "html.parser")


all_movies = soup.find_all("li a")

movie_title = [movie.getText() for movie in all_movies]

for n in range(len(movie_title) - 1, -1, -1):
    with open("songs1.txt", mode="a") as file:
        file.write(f"{movie_title[n]}\n")