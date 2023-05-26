import unittest
from pyramid.testing import DummyRequest
from app.controllers.contact_controller import ContactController


class ContactControllerTestCase(unittest.TestCase):
    def setUp(self):
        # Inisialisasi objek ContactController dengan dummy ContactService
        self.controller = ContactController(contact_service=None)

    def test_create_contact_invalid_data(self):
        # Menguji create_contact dengan data kontak tidak valid
        request = DummyRequest(json={
            'email': 'invalid_email',
            'firstname': 'John'
        })
        response = self.controller.create_contact(request)

        # Memeriksa bahwa response status code adalah 400 (kesalahan validasi)
        self.assertEqual(response.status_code, 400)

        # Memeriksa bahwa response berisi pesan kesalahan yang diharapkan
        expected_error = {'email': ['Not a valid email address.']}
        self.assertEqual(response.json['error'], 'Validation Error')



if __name__ == '__main__':
    unittest.main()
