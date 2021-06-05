from django.test import TestCase
from django.urls import reverse, resolve

from . import views


class HomePageViewTests(TestCase):
    def test_uses_correct_html(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, views.HomePageView.template_name)

    def test_uses_correct_view(self):
        response = resolve(reverse('home'))
        self.assertEqual(
            response.func.__name__, views.HomePageView.as_view().__name__
        )


class AboutPageViewTests(TestCase):
    def test_uses_correct_html(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, views.AboutPageView.template_name)

    def test_uses_correct_view(self):
        response = resolve(reverse('about'))
        self.assertEqual(
            response.func.__name__, views.AboutPageView.as_view().__name__
        )
