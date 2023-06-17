import logging

from scrapers import base
from scrapers import constants
from scrapers import tags
from scrapers.deel import constants as deel_constants

from models import dtos


logger = logging.getLogger(__name__)


class DeelClient(base.BaseScrapeClient):
    scraper = constants.Scraper.DEEL
    log_prefix = 'DEEL-SCRAPE-CLIENT'

    BASE_URL = deel_constants.BASE_URL
    SCRAPE_PATH = deel_constants.SCRAPE_PATH

    def crawl(self):
        response = self._request(
            url=self.BASE_URL + self.SCRAPE_PATH, method='GET'
        )
        self.init_beautiful_soup(content=response)

        for article in self.find_articles():
            header = article.find(tags.ElementTag.HEADING_2.value)
            url = article.find(tags.ElementTag.A.value)
            image = article.find(tags.ElementTag.IMG.value)

            yield dtos.CompanyDTO(
                name=header.text.strip(),
                url=url[tags.ElementTagProperty.HREF.value].strip(),
                logo=image[tags.ElementTagProperty.SRC.value],
            )
