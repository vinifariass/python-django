from django.test import TestCase
from django.urls import reverse


class BasicAppUrlTests(TestCase):
	def test_special_url_is_namespaced_and_index_renders(self):
		self.assertEqual(reverse('basic_app:special'), '/special/')
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
