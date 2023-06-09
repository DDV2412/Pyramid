from marshmallow import Schema, ValidationError, fields
from app.models import StatusContact


class CreateContactSchema(Schema):
    email = fields.Email(required=True)
    firstname = fields.Str(required=True)
    lastname = fields.Str()
    status = fields.Enum(StatusContact)
    lists = fields.List(fields.Int())


def validate_data(data, schema):
    try:
        schema.load(data)
        return True, None
    except ValidationError as e:
        return False, str(e)


class UpdateContactSchema(Schema):
    email = fields.Email()
    firstname = fields.Str()
    lastname = fields.Str()
    status = fields.Enum(StatusContact)
    lists = fields.List(fields.Int())


def validate_update(data):
    try:
        schema = UpdateContactSchema()
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
