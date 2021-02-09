# Developing a Simple Webserver
## AIM:
To develop a simple webserver to serve html pages.

## DESIGN STEPS:
### Step 1: 
HTML content creation
### Step 2:
Design of webserver workflow
### Step 3:
Implementation using Python code
### Step 4:
Serving the HTML pages.
### Step 5:
Testing the webserver

## PROGRAM:
### MYWEBSERVER.PY
```
from http.server import HTTPServer,BaseHTTPRequestHandler

content="""
<!doctype html>
<html>
<head>
<title>my webserver</title>
</head> 
<body>
<h1>this is my first web server</h1>
</body>
</html>
"""

class Myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")

     # to create response reader
        self.send_response(200)
        self.send_header('content-type','text/html;charset=utf-8')
        self.end_headers()

        #to send responce
        self.wfile.write("Hello".encode())

#to send the responce
server_address=('',80)

#to createserver object
httpd=HTTPServer(server_address,Myhandler)

#listen at port 
print("My webserver is running...")
httpd.serve_forever()

```
## OUTPUT:
 
![OUTPUT]:(./static/img/o1.png)

## RESULT:
Thus a simple webserver is designed for to display multiplication table and is hosted in the URL http://kumaravel.student.saveetha.in.