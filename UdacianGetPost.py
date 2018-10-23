from http.server import HTTPServer,BaseHTTPRequestHandler
from urllib.parse import parse_qs
from Udacian import Udacian

memory = []


form = '''<!DOCTYPE html>
  <title>Udacian</title>
  <form method="POST" action="http://localhost:9999/">
    <textarea name="name">name</textarea>
    <br>
    <textarea name="city">city</textarea>
    <br>
    <textarea name="enrollment">enrollment</textarea>
    <br>
    <textarea name="nanodegree">nanodegree</textarea>
    <br>
    <textarea name="status">status</textarea>
    <br>
    <button type="submit">Post it!</button>
  </form>
  <pre>
{}
  </pre>
'''

class MessageHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('Content-length',0))
        data = self.rfile.read(length).decode()
        name = parse_qs(data)["name"][0]
        city = parse_qs(data)["city"][0]
        enrollment = parse_qs(data)["enrollment"][0]
        nanodegree = parse_qs(data)["nanodegree"][0]
        status = parse_qs(data)["status"][0]
       


        udacian1 = Udacian(name,city,enrollment,nanodegree,status)
        
        memory.append(udacian1)
        #print(memory)

        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

        output = "My name is "+ name +" currently in "+city+" enrolled in "+enrollment+" - "+nanodegree+" - Status: "+status+""
        self.wfile.write(output.encode())

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html;charset=utf-8')
        self.end_headers()
        
        
        self.wfile.write(form.encode()) 

if __name__ == '__main__':
    server_address = ('',9999)
    httpd = HTTPServer(server_address,MessageHandler)
    httpd.serve_forever()



