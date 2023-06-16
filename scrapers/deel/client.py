import logging

from scrapers import base
from scrapers import constants


logger = logging.getLogger(__name__)


class DeelClient(base.BaseScrapeClient):
    scraper = constants.Scraper.DEEL
    log_prefix = 'DEEL-SCRAPE-CLIENT'

    BASE_URL = 'https://deel.com'

    def crawl(self):
        self._request(url=self.BASE_URL, method='GET')