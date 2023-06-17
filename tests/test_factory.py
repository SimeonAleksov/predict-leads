from contextlib import nullcontext as does_not_raise

import pytest

from scrapers import constants
from scrapers import exceptions
from scrapers.factory import ScraperFactory


class TestScraperFactory:
    @pytest.mark.parametrize(
        "client, expectation",
        [
            (constants.Scraper.SCALE, does_not_raise()),
            (constants.Scraper.DEEL, does_not_raise()),
            (constants.Scraper.WEBFLOW, does_not_raise()),
            (
                'random_non_existant_client',
                pytest.raises(exceptions.FactoryClientNotFoundError),
            ),
        ],
    )
    def test_create_scraper(self, client, expectation):
        with expectation:
            ScraperFactory.create_scraper(client=client)
