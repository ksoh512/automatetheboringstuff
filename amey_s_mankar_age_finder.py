import requests
import bs4

print('Checking Amey\'s age...')

try:
    url = 'www.whitepages.com/name/Amey-Mankar/CA'
    page = requests.get('http://' + url)
    print(page.status_code)
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    print(soup.prettify("utf-8"))
    print([type(item) for item in list(soup.children)])
    html = list(soup.children)[2]
    print(list(html.children))
except requests.exceptions.RequestException as e:
    print # -*- coding: utf-8 -*-
    sys.exit(1)
