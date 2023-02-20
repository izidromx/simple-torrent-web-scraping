import requests
from bs4 import BeautifulSoup
import time

animation = "|/-\\"

movie_title = input("Please enter a title: ")
text_message = "please wait..."
# Show the loading animation
for i in range(10):
    time.sleep(0.1)  # Add a small delay to make the animation visible
    print(f"\r{animation[i % len(animation)]} {text_message}", end="", flush=True)

page = requests.get(f'https://solidtorrents.to/search?q={movie_title}+yg')
soup = BeautifulSoup(page.content, 'html.parser')

container = soup.find('div', class_='w3-col s12 mt-1')
movie_elements = container.find_all('li', class_='card')

movies = []
for movie_element in movie_elements:
    title_node = movie_element.find('h5', class_='title w-100 truncate')
    title = title_node.find('a').text
    category = movie_element.find('a', class_='category').text
    stats = movie_element.find('div', class_='stats')
    size = stats.contents[3].text
    seeds_node = stats.contents[5]
    seeds = seeds_node.find('font').text
    leecher_nodes = stats.contents[7]
    leecher = leecher_nodes.find('font').text
    date = stats.contents[9].text

    link_node = movie_element.find('div', class_='links center-flex hide-on-small px-3')
    torrent = link_node.find('a', class_='dl-torrent').get('href')
    magnet = link_node.find('a', class_='dl-magnet').get('href')

    movie = {
        'title': title,
        'category': category,
        'size': size,
        'seeds': seeds,
        'leecher': leecher,
        'date': date,
        'torrent': torrent,
        'magnet': magnet
    }

    movies.append(movie)

for movie in movies:
    print(movie)

# Print a message to indicate that the loading is complete
print("\nLoading complete!")
