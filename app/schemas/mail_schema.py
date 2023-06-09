from marshmallow import Schema, ValidationError, fields, validate

from app.models import StatusContact, StatusMail


class CreateMailSchema(Schema):
    name = fields.Str(required=True)
    from_name = fields.Str(required=True)
    from_mail = fields.Email(required=True)
    subject = fields.Str(required=True)
    preview_line = fields.Str(required=True)
    design = fields.Str(required=True)
    recipients = fields.List(fields.Int(), required=True)
    status = fields.Enum(StatusMail)
    template_id = fields.Int()
    scheduled = fields.DateTime()


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
    recipients = fields.List(fields.Int())
    status = fields.Enum(StatusMail)
    template_id = fields.Int()
    scheduled = fields.DateTime()


def validate_update(data):
    try:
        schema = UpdateMailSchema()
        validated_data = schema.load(data)
        fields_to_update = {}

        # Cek setiap field yang ada dalam data
        for field in schema.fields:
            if field in validated_data:
                fields_to_update[field] = validated_data[field]

        if fields_to_update:
            return True, fields_to_update
        else:
            return False, "No fields to update"
    except ValidationError as e:
        return False, str(e)
