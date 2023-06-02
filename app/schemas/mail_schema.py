from marshmallow import Schema, ValidationError, fields


class CreateMailSchema(Schema):
    name = fields.Str(required=True)
    from_name = fields.Str(required=True)
    from_mail = fields.Email(required=True)
    subject = fields.Str(required=True)
    preview_line = fields.Str(required=True)
    design = fields.Str(required=True)


def validate_data(data, schema):
    try:
        schema.load(data)
        return True, None
    except ValidationError as e:
        return False, str(e)


class UpdateMailSchema(Schema):
    name = fields.Str()
    from_name = fields.Str()
    from_mail = fields.Email()
    subject = fields.Str()
    preview_line = fields.Str()
    design = fields.Str()


def validate_update(self, request):
    mail_id = request.matchdict['mail_id']
    mail_data = request.json

    # Validate data
    try:
        validated_data = UpdateMailSchema().load(mail_data)
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
        contact = self.contact_repository.update_contact(mail_id, fields_to_update)

        if contact:
            return {
                'success': True,
                'message': 'Mail updated successfully'
            }
        else:
            return {
                'success': False,
                'error': 'Mail not found'
            }
    else:
        return {
            'success': False,
            'error': 'No fields to update'
        }
