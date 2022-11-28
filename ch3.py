class GetValue(dict):
    def get(self, keySet, default=None):
        keys = keySet.split("/")
        value = None

        for key in keys:
            if value:
                if isinstance(value, list):
                    value = [v.get(key, default) if v else None for v in value]
                else:
                    value = value.get(key, default)
            else:
                value = dict.get(self, key, default)

            if not value:
                break

        return value
        
object1 = {'a':{'b':{'c':'d'}}}
key='a/b/c'
print(GetValue(object1).get(key))
