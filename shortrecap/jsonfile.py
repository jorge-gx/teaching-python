"""

JSON - JavaScript Object Notation
inspired by a subset of JavaScript, dealing with object literal syntax

{
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}


Python comes with a built-in package called json for encoding and decoding JSON data.
"""

import json

data = {
    "superman": {
        "name": "Clark Kent",
        "species": "Kryptonian"
    }
}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

