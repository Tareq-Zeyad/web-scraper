from web_scraper import __version__
from web_scraper.web_scraper import get_citations_needed_count, germany_wiki_url


def test_version():
    assert __version__ == '0.1.0'


def test_citation_needed():
    # Arange
    expected = 5

    # Actual
    actual = get_citations_needed_count(germany_wiki_url)

    # Assert
    assert actual == expected
