import socket
import requests
n = 0

def foo():
    global n
    n += 1

with open("/tmp/test", "+w") as test:
    test.write("ok")

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
s.connect(("www.python.org", 80))

with open("/tmp/boom", '+w') as boom:
    boom.write("ok")

r = requests.get("https://google.com")
