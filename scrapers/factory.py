from scrapers import constants
from scrapers import exceptions
from scrapers import base
from scrapers.deel import client as deel_client
from scrapers.scale import client as scale_client
from scrapers.webflow import client as webflow_client


class ScraperFactory:
    @staticmethod
    def create_scraper(client: constants.Scraper) -> base.BaseScrapeClient:
        _mapping = {
            constants.Scraper.DEEL: deel_client.DeelClient(),
            constants.Scraper.SCALE: scale_client.ScaleClient(),
            constants.Scraper.WEBFLOW: webflow_client.WebflowClient(),
        }

        try:
            return _mapping[client]
        except KeyError:
            raise exceptions.FactoryClientNotFoundError(
                f'[CLIENT-FACTORY] Scraping client not found for {client}.'
            )
