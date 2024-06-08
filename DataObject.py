from Schema import Schema


class DataObject:

    def __init__(self, data, schema):
        if not isinstance(schema, Schema):
            raise ValueError('Schema must be of type Schema')
        schema.validate(data)

        self.schema = schema
        self.data = data
        self.applySchema()

    def applySchema(self):
        schema = self.schema
        data = self.data
        functions = schema.listOfKeysToApply(data)

        for key in functions:
            data[key] = schema.schema[key]['apply'](data[key])

    def getData(self):
        return self.data
