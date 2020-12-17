import unittest

from app.service import modify_links


class ModifyLinksTests(unittest.TestCase):
    def test_modify_links(self):
        url = '<li><a href="https://dou.ua/lenta/articles/' \
               'jobs-and-trends-2019/?from=doufp">Рынок труда</a></li>'
        expected_url = '<li><a href="http://127.0.0.1:8888/lenta/articles/' \
                       'jobs-and-trends-2019/?from=doufp">Рынок труда</a></li>'

        response_url = modify_links(url)
        self.assertEqual(str(expected_url), str(response_url))
