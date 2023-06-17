import logging

from scrapers import base
from scrapers import constants
from scrapers import tags
from scrapers.webflow import constants as webflow_constants
from models import dtos

logger = logging.getLogger(__name__)
_LOG_PREFIX = 'DEEL-SCRAPE-CLIENT'


class WebflowClient(base.BaseScrapeClient):
    scraper = constants.Scraper.WEBFLOW
    log_prefix = _LOG_PREFIX

    BASE_URL = webflow_constants.BASE_URL
    SCRAPE_PATH = webflow_constants.SCRAPE_URL

    def crawl(self):
        response = self._request(
            url=self.BASE_URL + self.SCRAPE_PATH, method='GET'
        )
        self.init_beautiful_soup(content=response)

        divs = self.find_divs_by_property(div_property={'role': 'listitem'})
        for div in divs:
            try:
                image = div.find(
                    tags.ElementTag.IMG.value, {'class': 'customer-grid_logo'}
                )
                yield dtos.CompanyDTO(
                    name=image[tags.ElementTagProperty.ALT.value],
                    url=div.a[tags.ElementTagProperty.HREF.value],
                    logo=image[tags.ElementTagProperty.SRC.value],
                )
            except TypeError:
                # logger.error(f'[{_LOG_PREFIX}] Tag(div={div} does not contain href.')
                continue
