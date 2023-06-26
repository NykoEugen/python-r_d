import random

import requests


def request_web():
    web_url = ['https://google.com', 'https://facebook.com', 'https://twitter.com',
               'https://amazon.com', 'https://apple.com']
    random_url = random.choice(web_url)
    res = requests.get(url=random_url, stream=True)
    html_text = res.text
    print(f"Status code: {res.status_code}, URL: {res.url}, length html code: {len(html_text)}")


request_web()
