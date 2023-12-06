# scraper.py

# Scrape news headlines using BeautifulSoup
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

def get_latest_news():
    url = "https://finviz.com/news.ashx" # Link to news webpage
    req = Request(url=url, headers={"user-agent": "my-app"})
    response = urlopen(req)
    html_content = response.read()
    soup = BeautifulSoup(html_content, "html.parser")
    headline_elements = soup.find_all("td", class_="news_link-cell")
    latest_headlines = [headline_element.find("a", class_="tab-link").text.strip() for headline_element in headline_elements[:15]]
    return latest_headlines
