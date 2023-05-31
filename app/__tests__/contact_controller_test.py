import unittest
from unittest.mock import Mock
from app.controllers.contact_controller import ContactController


class TestContactController(unittest.TestCase):
    def setUp(self):
        self.mock_request = Mock()
        self.controller = ContactController(self.mock_request)

    def test_get_all_contact(self):
        mock_service = Mock()
        mock_contacts = [
            Mock(id=1, email='john@example.com', firstname='John'),
            Mock(id=2, email='jane@example.com', firstname='Jane')
        ]
        mock_service.get_all_contacts.return_value = mock_contacts
        self.controller.contact_service = mock_service

        response = self.controller.get_all_contact()

        self.assertEqual(response['status'], 'success')
        self.assertEqual(len(response['data']), 2)
        self.assertEqual(response['data'][0], mock_contacts[0].to_dict())
        self.assertEqual(response['data'][1], mock_contacts[1].to_dict())

    def test_get_contact_by_id(self):
        mock_service = Mock()
        mock_contact = Mock(id=1, email='john@example.com', firstname='John')
        mock_service.get_contact_by_id.return_value = mock_contact
        self.controller.contact_service = mock_service

        self.mock_request.matchdict = {'id': '1'}
        response = self.controller.get_contact_by_id()

        self.assertEqual(response['status'], 'success')
        self.assertEqual(response['data'], mock_contact.to_dict())

    def test_create_contact(self):
        mock_service = Mock()
        mock_contact = Mock(id=1, email='john@example.com', firstname='John')
        mock_service.create_contact.return_value.to_dict.return_value = mock_contact.to_dict()
        self.controller.contact_service = mock_service

        self.mock_request.json_body = {'email': 'john@example.com', 'firstname': 'John'}
        response = self.controller.create_contact()

        self.assertEqual(response['status'], 'success')
        self.assertEqual(response['data'], mock_contact.to_dict())

    def test_update_contact(self):
        mock_service = Mock()
        mock_contact = Mock(id=1, email='john@example.com', firstname='John')
        mock_service.update_contact.return_value.to_dict.return_value = mock_contact.to_dict()
        self.controller.contact_service = mock_service

        self.mock_request.matchdict = {'id': '1'}
        self.mock_request.json_body = {'email': 'john@example.com', 'firstname': 'John'}
        response = self.controller.update_contact()

        self.assertEqual(response['status'], 'success')
        self.assertEqual(response['data'], mock_contact.to_dict())

    def test_delete_contact(self):
        mock_service = Mock()
        mock_service.delete_contact.return_value = True
        self.controller.contact_service = mock_service

        self.mock_request.matchdict = {'id': '1'}
        response = self.controller.delete_contact()

        self.assertEqual(response['status'], 'success')
        self.assertEqual(response['message'], 'Contact deleted successfully')

    def test_import_contacts(self):
        mock_service = Mock()
        mock_contacts = [
            Mock(id=1, name='John Doe'),
            Mock(id=2, name='Jane Smith')
        ]
        mock_service.import_contacts.return_value = mock_contacts
        self.controller.contact_service = mock_service

        self.mock_request.json_body = {'file_path': 'contacts.csv'}
        response = self.controller.import_contacts()
        self.assertEqual(response['status'], 'success')
        self.assertEqual(len(response['data']), 2)
        self.assertEqual(response['data'][0], mock_contacts[0].to_dict())
        self.assertEqual(response['data'][1], mock_contacts[1].to_dict())


if __name__ == '__main__':
    unittest.main()
