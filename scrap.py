import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []


def scrap_by_url(link):
    print('scrap on link ' + link)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    url = link
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')
    # print(soup)
    table = soup.find('table', {'class': 'top-table__content'})
    # print(table)
    body = table.find('tbody')
    # print(body)
    rows = body.find_all('tr')
    print(rows)
    for row in rows:
        if row != []:
            tds = row.find_all('td')
            alink = tds[1].find('a')
            # print(alink.text, tds[2].text)
            data.append(
                [alink.text, tds[2].text])


scrap_by_url('https://www.similarweb.com/top-websites/indonesia/')

df = pd.DataFrame(
    data, columns=['Website', 'Traffic'])

print('data done')

print('create a excel file')

df.to_excel("webscrapper.xlsx")
