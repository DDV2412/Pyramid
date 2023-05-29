import unittest
from unittest.mock import Mock
from app.controllers.contact_controller import ContactController


class TestContactController(unittest.TestCase):
    def setUp(self):
        self.mock_request = Mock()
        self.controller = ContactController(self.mock_request)

    def test_get_all_contact(self):
        mock_service = Mock()
        mock_service.get_all_contacts.return_value = [
            {'id': 1, 'firstname': 'John', 'email': 'john@example.com'},
            {'id': 2, 'firstname': 'Jane', 'email': 'jane@example.com'}
        ]
        self.controller.contact_service = mock_service

        response = self.controller.get_all_contact()

        self.assertEqual(response, {
            'status': 'success',
            'data': [
                {'id': 1, 'firstname': 'John', 'email': 'john@example.com'},
                {'id': 2, 'firstname': 'Jane', 'email': 'jane@example.com'}
            ]
        })

    def test_get_contact_by_id(self):
        mock_service = Mock()
        mock_service.get_contact_by_id.return_value = {'id': 1, 'firstname': 'John', 'email': 'john@example.com'}
        self.controller.contact_service = mock_service

        self.mock_request.matchdict = {'id': '1'}
        response = self.controller.get_contact_by_id()

        self.assertEqual(response, {
            'status': 'success',
            'data': {'id': 1, 'firstname': 'John', 'email': 'john@example.com'}
        })

    def test_create_contact(self):
        mock_service = Mock()
        mock_service.create_contact.return_value = {'id': 1, 'firstname': 'John', 'email': 'john@example.com'}
        self.controller.contact_service = mock_service

        self.mock_request.json_body = {'firstname': 'John', 'email': 'john@example.com'}
        response = self.controller.create_contact()

        self.assertEqual(response, {
            'status': 'success',
            'data': {'id': 1, 'firstname': 'John', 'email': 'john@example.com'}
        })

    def test_update_contact(self):
        mock_service = Mock()
        mock_service.update_contact.return_value = {'id': 1, 'firstname': 'John', 'email': 'john@example.com'}
        self.controller.contact_service = mock_service

        self.mock_request.matchdict = {'id': '1'}
        self.mock_request.json_body = {'firstname': 'John', 'email': 'john@example.com'}
        response = self.controller.update_contact()

        self.assertEqual(response, {
            'status': 'success',
            'data': {'id': 1, 'firstname': 'John', 'email': 'john@example.com'}
        })

    def test_delete_contact(self):
        mock_service = Mock()
        mock_service.delete_contact.return_value = True
        self.controller.contact_service = mock_service

        self.mock_request.matchdict = {'id': '1'}
        response = self.controller.delete_contact()

        self.assertEqual(response, {
            'status': 'success',
            'message': 'Contact deleted successfully'
        })

    def test_import_contacts(self):
        # Mock the contact service
        mock_service = Mock()
        mock_service.import_contacts.return_value = [
            {'id': 1, 'name': 'John Doe'},
            {'id': 2, 'name': 'Jane Smith'}
        ]
        self.controller.contact_service = mock_service

        self.mock_request.json_body = {'file_path': 'contacts.csv'}
        response = self.controller.import_contacts()

        self.assertEqual(response['status'], 'success')
        self.assertEqual(len(response['data']), 2)


if __name__ == '__main__':
    unittest.main()
