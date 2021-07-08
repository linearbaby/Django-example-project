from django.test import TestCase, Client


class ShopViewTestCase(TestCase):
    test_domains = 'parapapa.ru'

    def setUp(self):
        self.c = Client()

    def test_url_allowed_hosts(self):
        request = self.c.get('/', SERVER_NAME=self.test_domains)
        self.assertNotEqual(request.status_code, 200)

        request = self.c.get('/')
        self.assertEqual(request.status_code, 200)
