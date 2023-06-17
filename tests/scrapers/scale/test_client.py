from unittest import mock


from models import dtos
from scrapers.scale.client import ScaleClient
from tests.data.responses import SCALE_HTML_RESPONSE


class TestDeelScrapeClient:
    @mock.patch(
        'scrapers.base.BaseScrapeClient._request',
        return_value=SCALE_HTML_RESPONSE,
    )
    def test_crawl(self, mocked_request):
        client = ScaleClient()
        for data in client.crawl():
            assert isinstance(data, dtos.CompanyDTO)
            assert data.name
            assert data.url
            assert data.logo
