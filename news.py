import requests
from bs4 import BeautifulSoup
import time


class NewsParser:
    url = "https://www.coindesk.com/livewire"
    old_news = []
    
    def get_news(self):
        ''' Получает заголовок последней новости с coindesk. при необходимости удаляет заголовки старых новостей '''
        for _ in range(5):
            try:
                response = requests.get(self.url)
                break
            except:
                time.sleep(5)
        else:
            return False
        
        if response.status_code != 200:
            return False

        soup = BeautifulSoup(response.text, "html.parser")
        post = soup.find("h3").get_text().strip()       # берём только последнюю новость
        if post in self.old_news:
            return False
        self.old_news.append(post)
        if len(self.old_news) >= 15:                    # чтобы не хранить кучу данных - храним только 15 последних новостей
            self.old_news = self.old_news[:12]
        return post


if __name__ == '__main__':
    p = NewsParser()
    p.get_news()
