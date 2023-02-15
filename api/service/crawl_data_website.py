import logging
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from datetime import datetime, timedelta
logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO)

weather_day=[]
class Crawler:
    def __init__(self, urls=[]):
        self.visited_urls = []
        self.urls_to_visit = urls

    def download_url(self, url):
        return requests.get(url).text

    def get_linked_urls(self, url, html):
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a'):
            path = link.get('href')
            if path and path.startswith('/'):
                path = urljoin(url, path)
            yield path

    def add_url_to_visit(self, url):
        if url not in self.visited_urls and url not in self.urls_to_visit:
            self.urls_to_visit.append(url)

    def crawl(self, url):
        html = self.download_url(url)
        for url in self.get_linked_urls(url, html):
            self.add_url_to_visit(url)

    def run(self):
        while self.urls_to_visit:
            url = self.urls_to_visit.pop(0)
            logging.info(f'Crawling: {url}')
            try:
                self.crawl(url)
            except Exception:
                logging.exception(f'Failed to crawl: {url}')
            finally:
                self.visited_urls.append(url)
                

def convert_time(time, year):
    date = datetime.strptime(time, '%d/%m %H:%M')
    new_date = date.replace(year=int(year))
    new_date = new_date.strftime('%Y-%m-%d %H:%M:%S')
    return new_date

def convert_string(string: str, year):
    if not string.strip(): 
        return {
            'start_time': '',
            'weather': ''
        }
    new_string = string.split('-')
    return {
        'start_time': convert_time(new_string[0].strip(), year),
        'weather': new_string[1].strip()
    }

def end_time(time: str):
    date = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
    new_date = date - timedelta(minutes=1)
    new_date = new_date.strftime('%Y-%m-%d %H:%M:%S')
    return new_date

def craw_website(url):
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'html.parser')
    for table in soup.find_all('table'):
        try:
            year = table.find_all('b')[0].get_text()
            for tr in table.find_all('tr'):
                td = tr.find_all('td')
                b = td[0].find_all('b')
                if not b:
                    squirrel_date: str = td[0].get_text()
                    squirrel_time = None
                    if squirrel_date.strip():
                        squirrel_time = convert_time(squirrel_date, year)  
                    date_weather: str = td[1].get_text()
                    if date_weather.strip():
                        new_date_weather = convert_string(date_weather, year)
                        tiet_khi = {
                            'gio_soc': squirrel_time,
                            'year': year,
                            'start_time': new_date_weather['start_time'],
                            'tiet_khi': new_date_weather['weather'],
                            'end_time': None
                        }
                        if weather_day:
                            weather_day[-1]['end_time'] = end_time(new_date_weather['start_time'])
                        weather_day.append(tiet_khi)
        except:
            pass

            
            
                
def craw_tiet_khi():

    urls = 'https://www.informatik.uni-leipzig.de/~duc/amlich/DuLieu/list.html'
    data = requests.get(urls).text
    href = []
    soup = BeautifulSoup(data, 'html.parser')
    for link in soup.find_all('a'):
        path = link.get('href')
        if 'zip' not in path and 'http' not in path:
            href.append(urls.replace('list.html', path))
    for hr in href:
        craw_website(hr)
    return weather_day
