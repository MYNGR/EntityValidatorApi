from marshmallow import Schema, fields, post_load, INCLUDE
from entity_validator.serializer.models.finite_set_entity import FiniteSetEntity


class FiniteSetEntitySchema(Schema):
    """
    Schema for the FiniteSetEntity model in order to validate the incoming data before converting it into python object.
    If a value is set required and is missing, then ValidationError will be raised.
    If a value is not set required and is missing, then if the missing value is set then that will be used as it's value.
    """
    values = fields.List(fields.Dict(), required=True)
    invalid_trigger = fields.Str(required=True)
    key = fields.Str(required=True)
    support_multiple = fields.Bool(missing=True)
    pick_first = fields.Bool(missing=False)
    supported_values = fields.List(fields.Str(), required=True)

    @post_load()
    def make_entity_obj(self, data, **kwargs):
        """
        Deserialize JSON data into python object.
        :param data: data which we need to convert into python object based on FiniteSetEntity model
        :param kwargs: extra parameters (if any given)
        :return: FiniteSetEntity object
        """
        return FiniteSetEntity(**data)

    class Meta:
        """
        To include unknown fields ( those which were not defined in schema or model) in the schema otherwise a
        ValidationError will be raised.
        """
        unknown = INCLUDE
