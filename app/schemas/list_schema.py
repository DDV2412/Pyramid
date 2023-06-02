from marshmallow import Schema, ValidationError, fields


class CreateListSchema(Schema):
    name = fields.Str(required=True)


def validate_data(data, schema):
    try:
        schema.load(data)
        return True, None
    except ValidationError as e:
        return False, str(e)


class UpdateListSchema(Schema):
    name = fields.Str()


def validate_update(self, request):
    list_id = request.matchdict['list_id']
    list_data = request.json

    # Validate data
    try:
        validated_data = UpdateListSchema().load(list_data)
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
        contact = self.contact_repository.update_contact(list_id, fields_to_update)

        if contact:
            return {
                'success': True,
                'message': 'List updated successfully'
            }
        else:
            return {
                'success': False,
                'error': 'List not found'
            }
    else:
        return {
            'success': False,
            'error': 'No fields to update'
        }
