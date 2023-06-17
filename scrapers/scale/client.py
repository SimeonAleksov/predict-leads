import logging

from scrapers import base
from scrapers import constants

from models import dtos

logger = logging.getLogger(__name__)


class ScaleClient(base.BaseScrapeClient):
    scraper = constants.Scraper.SCALE
    log_prefix = 'SCALE-SCRAPE-CLIENT'

    BASE_URL = 'https://scale.com'
    SCRAPE_PATH = '/customers'

    def crawl(self):
        response = self._request(
            url=self.BASE_URL + self.SCRAPE_PATH, method='GET'
        )
        self.init_beautiful_soup(content=response)
        for article in self.find_articles():
            image = article.find('img')
            name = image['alt'].strip().split('|')[0].split(':')[-1].strip()
            next_image = image.find_next().find('img')
            yield dtos.CompanyDTO(
                name=name,
                url=self.BASE_URL + article.parent['href'],
                logo=next_image['src'].strip(),
            )
