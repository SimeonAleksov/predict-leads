import logging
from abc import ABC
from abc import abstractmethod

import requests

from scrapers.constants import Scraper
from observer import base
from models import dtos


logger = logging.getLogger(__name__)



class BaseScrapeClient(ABC):
    scraper: Scraper = None
    log_prefix: str = None

    def __init__(self):
        self.observers: list[base.ObserverBase] = []

    @abstractmethod
    def crawl(self) -> None:
        pass

    def _request(self, url: str, method: str ) -> str:
        response = requests.request(method=method, url=url)
        logger.debug(f'[{self.log_prefix}] URL: {url}, Status code: {response.status_code}, Content: {response.content}')
        if response.status_code != requests.codes.ok:
            raise Exception('Request not ok.')

        return response.text

    def execute_scrape(self):
        self.crawl()
        self.notify(data=dtos.ObserverDTO(scraper=self.scraper, dto=dtos.CompanyDTO(**{'url': 'https:deel.com', 'name': 'Shigoto'})))

    def attach(self, observer: base.ObserverBase):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, data: dtos.BaseDTO):
        for observer in self.observers:
            observer.execute(data)