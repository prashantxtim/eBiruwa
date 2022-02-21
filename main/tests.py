from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import *
# Create your tests here.


class TestUrls(TestCase):
    def test_index_url(self):
        url = reverse('main:index')
        self.assertEquals(resolve(url).func, index)

    def test_signin_url(self):
        url = reverse('main:signin')
        self.assertEquals(resolve(url).func, signin)

    def test_logout_url(self):
        url = reverse('main:logout')
        self.assertEquals(resolve(url).func, logout)

    def test_update_url(self):
        url = reverse('main:update', args=[1])
        self.assertEquals(resolve(url).func, update)

    def test_donate_url(self):
        url = reverse('main:donate')
        self.assertEquals(resolve(url).func, donate)

    def test_adminlogin_url(self):
        url = reverse('main:AdminLogin')
        self.assertEquals(resolve(url).func, loginadmin)

class Testviews(TestCase):
    def test_views_index(self):
        client = Client()
        url = reverse('main:index')
        response = client.post(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_views_indbhex(self):
        client = Client()
        url = reverse('main:index')
        response = client.post(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "iindex.html")