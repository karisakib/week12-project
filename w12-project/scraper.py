import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Top_contributors_to_greenhouse_gas_emissions"

req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')
table = soup.find('table')
lst = []
full = []

def scrape():
    for item in table.find_all('td'):
        lst.append(item.text[:-1])

    i = 0
    j = 0
    k = 1
    m = 2
    n = 3
    try:
        for i in range(0, len(lst)-3):
            full.append(f"{lst[j]} {lst[k]} {lst[m]} {lst[n]}")
            i += 1
            j += 4
            k += 4
            m += 4
            n += 4
    except IndexError:
        print('e')
        
    print(full[:20])

    # for i in full[:20]:
    #     print(i)

if __name__ == "__main__":
    scrape()