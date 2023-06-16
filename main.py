from observer.storage import Storage
from settings import setup_logging
from scrapers import constants
from scrapers.factory import ScraperFactory


if __name__ == '__main__':
    setup_logging()

    scraper = ScraperFactory.create_scraper(client=constants.Scraper.DEEL)
    storage = Storage()
    scraper.attach(observer=storage)
    scraper.execute_scrape()
