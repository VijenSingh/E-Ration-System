from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import os,subprocess
import sys,time,thread,threading
import startup
class S(BaseHTTPRequestHandler):


    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()



    def do_GET(self):
        if(self.path=='/'):
            #demo()
            self._set_headers()
            self.wfile.write(open("html/head.html",'r').read())
            self.wfile.write(open("html/body.html",'r').read())
            self.wfile.write(open("html/body2.html",'r').read())
            self.wfile.write(open("html/footer.html",'r').read())

        if(self.path.find('/file')>=0):
            self._set_headers()
            self.wfile.write(open("file/" + self.path[6:],'rb').read())

        elif(self.path.find('/StartTask')>=0):
            self._set_headers()
            self.wfile.write(startup.StartTask())

        elif(self.path.find('/readFile')>=0):
            self._set_headers()
            self.wfile.write(startup.readFile(startup.get('file')))


    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        self._set_headers()

        self.wfile.write("<html><body><h1>Success...!</h1></body></html>")

def run(server_class=HTTPServer, handler_class=S, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    startup.ld()
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

demo()
