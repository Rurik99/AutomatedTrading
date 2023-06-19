from traiding import BinanceTrader
import model
from news import NewsParser
import yaml
import logging
import time
import database

def main():
    with open("config.yml") as f:
        params = yaml.load(f, Loader=yaml.FullLoader)
    parser = NewsParser()
    traider = BinanceTrader()

    if traider.traiding_type == 'GRID':
        last_news = 'neutral'
    while True:
        last_post = parser.get_news()
        if last_post:
            text_analyse = model.analyze_text(last_post)
            database.insert_news(last_post, text_analyse)
            logging.info(f'News: {last_post}. {text_analyse}')
            if float(text_analyse['Negative']) >= 0.7:

                if traider.traiding_type == 'GRID':
                    if last_news == 'pozitive':
                        traider.close_grid_from_main()
                        
                        last_news = 'neutral'
                    else:
                        last_news = 'negative'
                else:
                    traider.ema_trade("SELL")
            elif float(text_analyse['Positive']) >= 0.7:
                
                if traider.traiding_type == 'GRID':
                    if last_news == 'negative':
                        traider.close_grid_from_main()
                        last_news = 'neutral'
                    else:
                        last_news = 'pozitive'
                else:
                    traider.ema_trade("BUY")
        else:
            logging.info('No new news')
        for i in range(15):
            traider.polling()
            time.sleep(20)


if __name__ == '__main__':
    logging.basicConfig(filename='log.log', level=logging.INFO,
                        format="%(asctime)s:%(levelname)s:%(message)s")
    database.init_db()
    main()
