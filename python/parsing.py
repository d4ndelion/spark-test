from bs4 import BeautifulSoup, ResultSet
from chrome_driver import ChromeDriver
from models import Quote, Author
from logging import info

_PAGES_START = 1
_PAGES_END = 11
_AUTHOR_URL = "http://quotes.toscrape.com/author/"


def _quote_url_generator() -> str:
    def url_helper(page: int):
        return f"https://quotes.toscrape.com/page/{page}/"

    for i in range(_PAGES_START, _PAGES_END):
        info(f"Parsed page {i}")
        yield url_helper(i)


def _quote_generator(raw_quotes: ResultSet) -> Quote:
    for raw_quote in raw_quotes:
        yield Quote(
            text=raw_quote.find("span", attrs={"class": "text"}).text[1:-1],
            author=raw_quote.find("a", string="(about)")["href"][8:],
            tags=[tag.text for tag in raw_quote.find_all("a", attrs={"class": "tag"})],
        )


def parse_quotes() -> list[Quote]:
    quotes: list[Quote] = []
    for page in _quote_url_generator():
        with ChromeDriver() as driver:
            driver.get(page)
            soup: BeautifulSoup = BeautifulSoup(driver.page_source, "lxml")
        for quote in _quote_generator(soup.find_all("div", attrs={"class": "quote"})):
            quotes.append(quote)
    return quotes


def parse_author(author_name: str) -> Author:
    def _author_url_helper() -> str:
        info(f"Parsed author: {author_name}")
        return f"{_AUTHOR_URL}{author_name}/"

    with ChromeDriver() as driver:
        driver.get(_author_url_helper())
        soup: BeautifulSoup = BeautifulSoup(driver.page_source, "lxml")
    return Author(
        name=author_name,
        readable_name=soup.find("h3", attrs={"class": "author-title"}).text,
        birthdate=soup.find("span", attrs={"class": "author-born-date"}).text,
        birthplace=soup.find("span", attrs={"class": "author-born-location"}).text[3:],
        description=soup.find("div", attrs={"class": "author-description"}).text,
    )
