from pprint import pprint 
import requests
import extruct
from w3lib.html import get_base_url


'''
Get raw HTML from a URL
'''
def get_html(url): 
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
    req = requests.get(url, headers = headers)
    return req.text

'''
Parse structured data from a target page
'''
def scrape(url):
    html = get_html(url)
    metadata = get_metadata(html, url)
    pprint(metadata, indent=2, width=150)
    return metadata


'''
Fetch JSON-LD structured data
'''
def get_metadata(html, url):
    metadata = extruct.extract(
        html,
        #base_url=get_base_url(html, url),
        syntaxes=['json-ld'],
    )['json-ld']
    scraped_data = []
    for data in metadata:
        if bool(metadata) and isinstance(metadata, list):
            scraped_data.append(data)
    return scraped_data

def main():
    url = input("Enter recipe url: ")
    scrape(url)

if __name__ == '__main__':
    main()
