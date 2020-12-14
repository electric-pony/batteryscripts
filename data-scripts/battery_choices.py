import requests
import logging
import json
from bs4 import BeautifulSoup

def geturl():

    page = requests.get(url)

    # use this get request instead to extract cell data from the website
    # page = requests.get("https://www.imrbatteries.com/18650-batteries/")

    logging.info(page)
    soup = BeautifulSoup(page.content, 'html.parser')

    # for tag in soup.find_all(re.compile("t")):
    #     print(tag.name)

    # use this command if you want to see the output of the webpage in the command line
    html = soup.prettify()


    prod_list = soup.find_all('ul', {"class": "ProductList"})


    return html


if __name__ == '__main__':

    log = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG)
    contents = ''

    # url = "http://dataquestio.github.io/web-scraping-pages/simple.html"
    url = "https://www.imrbatteries.com/18650-batteries/"
    contents = geturl()
    print(contents)
    with open('18650.txt', 'w') as f:
        f.write(contents)

    my_details = {
        'name': 'rocket ros',
        'rating': 'BAMF'
    }

    with open('personal.json', 'w') as json_file:
        json.dump(my_details, json_file)

