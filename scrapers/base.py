import logging
from abc import ABC
from abc import abstractmethod

import requests
from bs4 import BeautifulSoup

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

    @classmethod
    def _request(cls, url: str, method: str ) -> str:
        response = requests.request(method=method, url=url)
        logger.debug(f'[{cls.log_prefix}] URL: {url}, Status code: {response.status_code}, Content: {response.content}')
        if response.status_code != requests.codes.ok:
            raise Exception('Request not ok.')

        return response.text

    def _parse_with_beautiful_soup(self, content: str) -> BeautifulSoup:
        return BeautifulSoup(content, 'html.parser')

    def find_article(self, content: str):
        bs = self._parse_with_beautiful_soup(content=content)
        return bs.find_all('article')

    def execute_scrape(self):
        for data in self.crawl():
            self.notify(data=dtos.ObserverDTO(scraper=self.scraper, dto=data))

    def attach(self, observer: base.ObserverBase):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, data: dtos.BaseDTO):
        for observer in self.observers:
            observer.execute(data)