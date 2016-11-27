Title: Testing json responses in Flask REST apps with pytest
Author: SergeM
Date: 2016-11-27 22:47:00
Slug: testing-json-responses-in-Flask-REST-apps-with-pytest
Tags: python,flask,pytest


The code consists of two files: `sample_app.py` (productions) and `sample_app_test.py` (testing). Testing is run using py.test.

## Code of sample_app.py
Creating Flask application:
```
from flask import Flask, request, Response, json

app = Flask(__name__)
```
Helper class for JSON-based response:

```
class JsonResponse(Response):
    def __init__(self, json_dict, status=200):
        super().__init__(response=json.dumps(json_dict), status=status, mimetype="application/json")
```

Defining GET and POST endpoints. The puprose of the `/add` endpoint is to return doubled value.

```
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/add', methods=['POST'])
def add():
    json = request.json
    resp = JsonResponse(json_dict={"answer": json['key'] * 2}, status=200)
    return resp
```
Main section that prints help message. (Alternative launching procedure can be applied)

```
if __name__ == '__main__':
    script_name = __file__
    print("run:\n"
          "FLASK_APP={} python -m flask run --port 8000 --host 0.0.0.0".format(script_name))
    exit(1)

```


## Code of sample_app_test.py
Fixture for test client:
```
import json
import pytest
from sample_app import app

@pytest.fixture
def client(request):
    test_client = app.test_client()

    def teardown():
        pass # databases and resourses have to be freed at the end. But so far we don't have anything

    request.addfinalizer(teardown)
    return test_client
```
Helper functions for encoding and decoding jsons:
```
def post_json(client, url, json_dict):
    """Send dictionary json_dict as a json to the specified url """
    return client.post(url, data=json.dumps(json_dict), content_type='application/json')

def json_of_response(response):
    """Decode json from response"""
    return json.loads(response.data.decode('utf8'))

```

The simplest test for GET endpoint:
```
def test_dummy(client):
    response = client.get('/')
    assert b'Hello, World!' in response.data
```

Test for POST endpoint. Checking resulting json:
```
def test_json(client):
    response = post_json(client, '/add', {'key': 'value'})
    assert response.status_code == 200
    assert json_of_response(response) == {"answer": 'value' * 2}
```

## Related links:
* [Testing flask applications](http://flask.pocoo.org/docs/0.11/testing/)
* [pytest fixtures for flask](https://github.com/pytest-dev/pytest-flask) I haven't checked them. Maybe uyseful
* [Flaskr test application from examples of Flask](https://github.com/pallets/flask/tree/master/examples/flaskr)
