import requests

from app import app
from app.service import modify_links, modify_content
from config import DOU_GENERAL_URL


@app.route('/', methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def dou_pages(path=None):
    if path is not None:
        url = DOU_GENERAL_URL + path
    else:
        url = DOU_GENERAL_URL

    response = requests.get(url=url, headers={'User-Agent': 'egoo'})

    pars_text = modify_content(response.text)
    result = modify_links(pars_text)
    return str(result)
