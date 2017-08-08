from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from .views import home_page


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_can_save_a_POST_request(self):

        expected_html = render_to_string(
            'home.html',
            {'new_item_text': 'A new list item'}
        )
        self.assertIn('A new list item', expected_html)
