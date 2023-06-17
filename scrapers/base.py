import typing
import logging
from abc import ABC
from abc import abstractmethod

import requests
from bs4 import BeautifulSoup
from bs4 import element

from scrapers.constants import Scraper
from observer import base
from models import dtos

logger = logging.getLogger(__name__)


class BaseScrapeClient(ABC):
    scraper: Scraper = None
    log_prefix: str = None

    BASE_URL = None
    SCRAPE_PATH = None

    def __init__(self):
        self.soup: BeautifulSoup = None
        self.observers: list[base.ObserverBase] = []

    @abstractmethod
    def crawl(self) -> None:
        pass

    @classmethod
    def _request(cls, url: str, method: str) -> str:
        response = requests.request(method=method, url=url)
        logger.debug(
            f'[{cls.log_prefix}] URL: {url}, Status code:'
            f' {response.status_code}, Content: {response.content}'
        )
        if response.status_code != requests.codes.ok:
            raise Exception('Request not ok.')

        return response.text

    def init_beautiful_soup(self, content: str):
        self.soup = BeautifulSoup(content, 'html.parser')

    def find_article(
        self,
    ) -> typing.Union[element.Tag, element.NavigableString]:
        return self.soup.find('article')

    def find_image(self) -> typing.Union[element.Tag, element.NavigableString]:
        return self.soup.find('img')

    def find_link(self) -> typing.Union[element.Tag, element.NavigableString]:
        return self.soup.find('a')

    def find_articles(self) -> element.ResultSet:
        return self.soup.find_all('article')

    def find_images(self) -> element.ResultSet:
        return self.soup.find_all('img')

    def find_links(self) -> element.ResultSet:
        return self.soup.find_all('a')

    def execute_scrape(self):
        logger.info(
            f'[{self.log_prefix}] Initiating ScrapeClient(url={self.BASE_URL},'
            f' scraping_path={self.SCRAPE_PATH}).'
        )

        for data in self.crawl():
            self.notify(data=dtos.ObserverDTO(scraper=self.scraper, dto=data))

    def attach(self, observer: base.ObserverBase):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, data: dtos.BaseDTO):
        for observer in self.observers:
            observer.execute(data)
