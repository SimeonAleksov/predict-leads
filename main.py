import click

from observer.storage import Storage
from settings import setup_logging
from scrapers import constants
from scrapers.factory import ScraperFactory


def run_scrape(client: str):
    scraper = ScraperFactory.create_scraper(client=constants.Scraper[client])
    storage = Storage()
    scraper.attach(observer=storage)
    scraper.execute_scrape()


@click.command()
@click.option('--client', type=click.Choice(constants.Scraper.as_list() + ['ALL']))
def run_scrapers(client: constants.Scraper):
    if client == 'ALL':
        for scraping_client in constants.Scraper:
            run_scrape(client=scraping_client.name)
    else:
        run_scrape(client=client)


if __name__ == '__main__':
    setup_logging()

    run_scrapers()
