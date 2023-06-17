import logging

from scrapers import base
from scrapers import constants
from scrapers import tags
from scrapers.scale import constants as scale_constants

from models import dtos

logger = logging.getLogger(__name__)


class ScaleClient(base.BaseScrapeClient):
    scraper = constants.Scraper.SCALE
    log_prefix = 'SCALE-SCRAPE-CLIENT'

    BASE_URL = scale_constants.BASE_URL
    SCRAPE_PATH = scale_constants.SCRAPE_PATH

    def crawl(self):
        response = self._request(
            url=self.BASE_URL + self.SCRAPE_PATH, method='GET'
        )
        self.init_beautiful_soup(content=response)
        for article in self.find_articles():
            image = article.find(tags.ElementTag.IMG.value)
            name = image['alt'].strip().split('|')[0].split(':')[-1].strip()
            next_image = image.find_next().find(tags.ElementTag.IMG.value)
            yield dtos.CompanyDTO(
                name=name,
                url=self.BASE_URL
                + article.parent[tags.ElementTagProperty.HREF.value],
                logo=next_image[tags.ElementTagProperty.SRC.value].strip(),
            )
