import requests
from bs4 import BeautifulSoup


def get_usd_eur() -> None:
    url = "https://www.x-rates.com/table/?from=RUB&amount=1"
    r = requests.get(url)

    soup = BeautifulSoup(r.content, "html.parser")
    rate_list = soup.findAll("table", {"class": "ratesTable"})[0].findAll("tbody")
    for table_val in rate_list:
        for tr_val in table_val.findAll("tr")[:2]:
            print(tr_val.text)


get_usd_eur()
