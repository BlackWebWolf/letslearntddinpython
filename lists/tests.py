from django.test import TestCase
from django.core.urlresolvers import resolve
from  lists.views import home_page

# Create your tests here.

class HomePageTest(TestCase):
    def test_root_urls_resolve_to_home_page(self):
        found = resolve("/")
        self.assertEqual(found.func, home_page)