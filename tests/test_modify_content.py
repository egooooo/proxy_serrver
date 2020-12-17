import unittest

from app.service import modify_content


class ModifyContentTests(unittest.TestCase):
    def test_modify_content(self):
        content = '<article class="b-typo"><p>Всем привет. Случилась очень ' \
                  'неприятная ситуация, и, данной темой хотел предупредить ' \
                  'остальных об очередных новых идеях этого оператора о ' \
                  'том как нагреть.</p></article>'
        expected_content = '<article class="b-typo"><p>Всем привет™. ' \
                           'Случилась очень неприятная ситуация, и, данной™ ' \
                           'темой хотел предупредить остальных об очередных ' \
                           'новых идеях этого оператора о том как нагреть.' \
                           '</p></article>'

        response_content = modify_content(content)
        self.assertEqual(str(expected_content), str(response_content))
