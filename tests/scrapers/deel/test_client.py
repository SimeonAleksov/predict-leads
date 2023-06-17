from unittest import mock


from models import dtos
from scrapers.deel.client import DeelClient
from tests.data.responses import DEEL_HTML_RESPONSE


class TestDeelScrapeClient:
    @mock.patch(
        'scrapers.base.BaseScrapeClient._request',
        return_value=DEEL_HTML_RESPONSE,
    )
    def test_crawl(self, mocked_request):
        client = DeelClient()
        for data in client.crawl():
            assert isinstance(data, dtos.CompanyDTO)
            assert data.name
            assert data.url
            assert data.logo
