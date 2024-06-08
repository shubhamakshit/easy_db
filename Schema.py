class Schema:

    def __init__(self,schema: dict):
        self.schema = schema

    def listToDict(self,values: list):
        if len(values) != len(self.schema):
            raise ValueError('Length of values does not match schema')
        keys = [key for key in self.schema.keys()]
        return dict(zip(keys,values))

    def validate(self,data: dict):
        for key in self.schema.keys():

            if key not in data:
                # Check if key is required

                # Case 'required' is set to True

                #  if required is present and True                                         or required is not present (default is True)
                if ( 'required' in self.schema[key] and self.schema[key]['required'] ) or ( 'required' not in self.schema[key] ):
                    if 'default' in self.schema[key]: # Case 'default' is set
                        data[key] = self.schema[key]['default']
                    else: # Since this key is required and no default value is set, raise an error
                        raise ValueError(f'{key} is required')

                # Case 'required' is set to False
                elif 'required' in self.schema[key] and not self.schema[key]['required']:
                    continue



            if 'type' in self.schema[key] and not isinstance(data[key],self.schema[key]['type']):
                raise ValueError(f'{key} is not of type {self.schema[key]["type"]}')
        return True


    def listOfKeysToApply(self, data: dict):
        if self.validate(data):
            return [key for key in self.schema.keys() if 'apply' in self.schema[key] and self.schema[key]['apply'] ]
        else:
            return False