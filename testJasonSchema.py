import jsonschema
import json


class TestJsonSchema:

    def __init__(self):
        print("init TestJsonSchema")

        self.data = {
            "glossary": {
                "title": "example glossary",
                "GlossDiv": {
                    "title": "S",
                    "GlossList": {
                        "GlossEntry": {
                            "ID": "SGML",
                            "SortAs": "SGML",
                            "GlossTerm": "Standard Generalized Markup Language",
                            "Acronym": "SGML",
                            "Abbrev": "ISO 8879:1986",
                            "GlossDef": {
                                "para": "A meta-markup language, used to create markup languages such as DocBook.",
                                "GlossSeeAlso": ["GML", "XML"]
                            },
                            "GlossSee": "markup"
                        }
                    }
                }
            }
        }

        self.schema = {
            "type": "object",
            "properties": {
                "price": {"type": "number"},
                "name": {"type": "string"},
                },
            }

    def saveJsonFile(self):
        with open("sample_json.json", "w") as write_file:
            json.dump(self.data, write_file)

    def openJsonFile(self):
        with open("sample_json.json", "r") as read_file:
            data = json.load(read_file)
        print(data)
        print(type(data))
        testJson = {"name" : "Eggs", "price" : 34.99}
        validationTest = jsonschema.validate(testJson, self.schema)
        print(validationTest)

testJsonSchema = TestJsonSchema()
testJsonSchema.saveJsonFile()
testJsonSchema.openJsonFile()
