from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    # h5_tags = soup.find_all('h5')
    # for h5 in h5_tags:
    #     print(h5.text)
    cards = soup.find_all('div', class_='card')
    for card in cards:
        name = card.h5.text
        price = card.a.text.split()[-1]
        print(name)
        print(price)

