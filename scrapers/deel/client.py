import logging

from scrapers import base
from scrapers import constants

from models import dtos


logger = logging.getLogger(__name__)


class DeelClient(base.BaseScrapeClient):
    scraper = constants.Scraper.DEEL
    log_prefix = 'DEEL-SCRAPE-CLIENT'

    BASE_URL = 'https://www.deel.com'
    SCRAPE_PATH = '/case-studies'

    def crawl(self):
        response = self._request(
            url=self.BASE_URL + self.SCRAPE_PATH, method='GET'
        )
        self.init_beautiful_soup(content=response)

        for article in self.find_articles():
            header = article.find('h2')
            url = article.find('a')
            image = article.find('img')

            yield dtos.CompanyDTO(
                name=header.text.strip(),
                url=url['href'].strip(),
                logo=image['src'],
            )
