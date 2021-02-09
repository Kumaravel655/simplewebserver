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