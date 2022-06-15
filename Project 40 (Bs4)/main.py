import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
all_html = response.text

soup = BeautifulSoup(all_html, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")   
all_movies_titles = [i.getText() for i in all_movies]
sort_movies = all_movies_titles[::-1]

with open("movies.txt", "w", encoding="utf-8") as file:
    for i in sort_movies:
        file.write(f"{i}\n")