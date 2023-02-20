import requests
from bs4 import BeautifulSoup

page = requests.get('https://solidtorrents.to/search?q=shark+bait')
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
