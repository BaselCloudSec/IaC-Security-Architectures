# https://www.goodreads.com/quotes
import requests
import bs4


web_site = requests.get("https://www.goodreads.com/quotes")
html = web_site.text




html_parser= bs4.BeautifulSoup(html, "html.parser")
quote = html_parser.findAll("div", attrs={"class": "quoteText"})

print(quote)
