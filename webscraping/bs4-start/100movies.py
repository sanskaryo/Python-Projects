import requests
from bs4 import BeautifulSoup

url = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url)

wesbsite_html = response.text
soup = BeautifulSoup(wesbsite_html, "html.parser")



all_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")

movie_title = [movie.getText() for movie in all_movies]

for n in range(len(movie_title) - 1, -1, -1):
    with open("movies.txt", mode="a") as file:
        file.write(f"{movie_title[n]}\n")