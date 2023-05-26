from marshmallow import Schema, ValidationError, fields


class CreateContactSchema(Schema):
    email = fields.Email(required=True)
    firstname = fields.Str(required=True)


def validate_data(data, schema):
    try:
        schema.load(data)
        return True, None
    except ValidationError as e:
        return False, str(e)


class UpdateContactSchema(Schema):
    email = fields.Email()
    firstname = fields.Str()


def validate_update(self, request):
    contact_id = request.matchdict['contact_id']
    contact_data = request.json

    # Validate data
    try:
        validated_data = UpdateContactSchema().load(contact_data)
    except ValidationError as e:
        return {
            'success': False,
            'error': str(e)
        }

    # Check for fields that have changed
    fields_to_update = {}
    for field, value in validated_data.items():
        if value is not None:
            fields_to_update[field] = value

    # Perform update only if there are fields to update
    if fields_to_update:
        contact = self.contact_repository.update_contact(contact_id, fields_to_update)

        if contact:
            return {
                'success': True,
                'message': 'Contact updated successfully'
            }
        else:
            return {
                'success': False,
                'error': 'Contact not found'
            }
    else:
        return {
            'success': False,
            'error': 'No fields to update'
        }


