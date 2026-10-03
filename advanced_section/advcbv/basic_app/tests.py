from django.test import TestCase
from django.urls import reverse
from .models import School, Student

class StudentListViewTests(TestCase):
	def setUp(self):
		self.school = School.objects.create(
			name='Central School',
			location='Springfield',
			principal='A. Principal',
		)
		self.student = Student.objects.create(
			name='Taylor Student',
			age=15,
			school=self.school,
		)

	def test_homepage_renders_student_navigation_link(self):
		response = self.client.get('/')

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, reverse('basic_app:student_list'))

	def test_student_list_displays_students(self):
		response = self.client.get(reverse('basic_app:student_list'))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, self.student.name)

	def test_school_list_links_to_school_detail(self):
		response = self.client.get(reverse('basic_app:list'))

		self.assertEqual(response.status_code, 200)
		self.assertContains(
			response,
			reverse('basic_app:detail', kwargs={'pk': self.school.pk}),
		)

	def test_school_detail_displays_school_and_students(self):
		response = self.client.get(
			reverse('basic_app:detail', kwargs={'pk': self.school.pk}),
		)

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, self.school.name)
		self.assertContains(response, self.school.principal)
		self.assertContains(response, self.school.location)
		self.assertContains(response, self.student.name)

	def test_school_create_page_displays_form(self):
		response = self.client.get(reverse('basic_app:create'))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Create New School')
		self.assertContains(response, 'name="name"')
		self.assertContains(response, 'name="location"')
		self.assertContains(response, 'name="principal"')
