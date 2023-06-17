from __future__ import annotations

from attr import define

from scrapers import constants


@define
class BaseDTO:
    pass


@define
class CompanyDTO(BaseDTO):
    name: str
    url: str
    logo: str


@define
class ObserverDTO(BaseDTO):
    scraper: constants.Scraper
    dto: BaseDTO
