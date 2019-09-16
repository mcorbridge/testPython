import requests # https://2.python-requests.org/en/master/#
import time
# https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request

class TestRequestResponse:

    def __init__(self):
        print("TestRequestResponse init")

    def doRequest(self):
        payload = {'key1': 'value1'}
        r = requests.post('http://127.0.0.1:8080/testPost', data=payload)
        print(r.status_code)
        if r.status_code == 200:
            time.sleep(5)
            self.doResponse()

    def doResponse(self):
        r = requests.get('http://127.0.0.1:8080/')
        print(r.text)



testRequestResponse = TestRequestResponse()
isTrue = True
if isTrue:
    testRequestResponse.doRequest()
else:
    testRequestResponse.doResponse()

