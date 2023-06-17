from unittest import mock


from models import dtos
from scrapers.webflow.client import WebflowClient
from tests.data.responses import WEBFLOW_HTML_RESPONSE


class TestWebflowScrapeClient:
    @mock.patch(
        'scrapers.base.BaseScrapeClient._request',
        return_value=WEBFLOW_HTML_RESPONSE,
    )
    def test_crawl(self, mocked_request):
        client = WebflowClient()
        for data in client.crawl():
            assert isinstance(data, dtos.CompanyDTO)
            assert data.name
            assert data.url
            assert data.logo
