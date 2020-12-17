import re

from bs4 import BeautifulSoup
from config import DOU_GENERAL_URL, LOCALHOST


def modify_links(content):
    soup = BeautifulSoup(content, "html.parser")

    for tag in soup.findAll('a', href=True):
        if tag['href'].startswith(DOU_GENERAL_URL):
            tag.attrs['href'] = tag['href'].replace(DOU_GENERAL_URL, LOCALHOST)

    return soup


def modify_content(content):
    start_article = content.find('<article')
    stop_article = content.find('</article>') + 10
    article_content = content[start_article:stop_article]

    regex = r'(\s|^)([А-Яа-я]{6})([.!?,;:\\-]|\s|$)'
    article_content = re.sub(regex, r'\1\2™\3', article_content)

    result = content[:start_article] + article_content + content[stop_article:]
    return result
