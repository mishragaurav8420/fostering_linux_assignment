from django.test import TestCase, Client
from django.urls import reverse

class BookTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_books(self):
        response = self.client.get(reverse('get_books'))
        self.assertEqual(response.status_code, 200)

    def test_get_book_by_id(self):
        response = self.client.post(reverse('get_book'), {'id': 1})
        self.assertEqual(response.status_code, 200)

    def test_create_book(self):
        response = self.client.post(reverse('create_book'), {
            'id': 1,
            'title': 'Test Book',
            'description': 'Test Description',
            'pageCount': 100,
            'excerpt': 'Test Excerpt',
            'publishDate': '2023-05-28T16:16:11.012Z'
        })
        self.assertEqual(response.status_code, 200)

    def test_delete_book(self):
        response = self.client.post(reverse('delete_book', kwargs={'book_id': 1}))
        self.assertEqual(response.status_code, 302)
