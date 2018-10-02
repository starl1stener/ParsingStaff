import csv
import requests
from bs4 import BeautifulSoup


def get_html(url):
    user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    r = requests.get(url, headers=user_agent)
    return r.text

def write_csv(data):
    with open('testimonials.csv', 'a') as f:
        order = ['author', 'since']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)

def get_articles(html):
    soup = BeautifulSoup(html, 'lxml')
    ts = soup.find('div', class_ = 'testimonial-container').find_all('article')
    return ts

def get_page_data(ts):
    for t in ts:
        try:
            since = t.find('p', class_ = 'traxer-since').text.strip()
        except:
            since = ''

        try:
            author = t.find('p', class_ = 'testimonial-author').text.strip()
        except:
            author = ''

        data = {'author': author, 'since': since}
        write_csv(data)


def main():
    page = 1

    while True:

        url = 'https://catertrax.com/why-catertrax/traxers/page/{}/'.format(str(page))
        print(url)
        articles = get_articles(get_html(url))

        if articles:
            get_page_data(articles)
            page += 1
        else:
            break


if __name__ == '__main__':
    main()