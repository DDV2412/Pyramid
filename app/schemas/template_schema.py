from marshmallow import Schema, ValidationError, fields


class CreateTemplateSchema(Schema):
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


class UpdateTemplateSchema(Schema):
    name = fields.Str()
    from_name = fields.Str()
    from_mail = fields.Email()
    subject = fields.Str()
    preview_line = fields.Str()
    design = fields.Str()


def validate_update(data):
    try:
        schema = UpdateTemplateSchema()
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
