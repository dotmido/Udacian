import requests,random,socket

def test_connection():
    print("Testing connection to server!")
    try:
        with socket.socket() as _socket:
            _socket.connect(("localhost",9999))
        print("Connection succeeded.")
        return None
    except socket.error:
        return "Server not responding at localhost port 9999"

def test_POST_303():
    '''The server should accept a POST and return a 303 to /.'''
    print("Testing POST request, looking for redirect.")
    mesg = random.choice(["Mohammed","Mustafa","dot","Mido"])
    uri = "http://localhost:9999/"
    try:
        _request = requests.post(uri, data = {'name': mesg}, allow_redirects=False)
    except requests.RequestException as _ex:
        return ("Couldn't communicate with the server. ({})\n"
                "If it's running, take a look at its output.").format(_ex)
    if _request.status_code == 501:
        return("501 Not implemented, doesnt know how to handle the GET request")
    elif _request.status_code != 303:
        return ("The server returned status code {} instead of a 303 redirect."
                ).format(_request.status_code)
    elif _request.headers['location'] != '/':
        return ("The server sent a 303 redirect to the wrong location."
                "I expected '/' but it sent '{}'.").format(
                    _request.headers['location'])
    else:
        print("POST request succeeded.")
        return None

def test_GET():
    print("Testing GET")
    uri ="http://localhost:9999"
    try:
        _request = requests.get(uri)
    except requests.RequestException as _ex:
        return("Cannot reach the server. ({})\n"
                "If its not running take a look at the output").format(_ex)
    if _request.status_code == 501:
        return("501 Not implemented, doesnt know how to handle the GET request")
    elif _request.status_code != 200:
        return("Server returned {}").format(_request.status_code)
    elif not _request.headers['content-type'].startswith('text/html'):
        return ("The server didn't return Content-type: text/html.")
    else:
        print("GET request succeeded!")
        return None

def test_memory():
    print("Testing if memory is working")
    _uri = "http://localhost:9999"
    _message = random.choice(["Mohammed","Mustafa","dot","Mido"])
    _reqest = requests.post(_uri,data={'name': _message})
    if _reqest.status_code !=200:
        return ("Returned status {}").format(_reqest.status_code)
    elif _message not in _reqest.text:
        return ("Sent message didnt show up, expected: {} returned: {}").format(_message,_reqest.text)
    else:
        print("Post-Get Succeeded!")

if __name__ == '__main__':
    tests = [test_connection, test_GET, test_memory,test_POST_303]
    for test in tests:
        _problem = test()
        if _problem is not None:
            print(_problem)
            break
    if not _problem:
        print("All tests succeeeded!")