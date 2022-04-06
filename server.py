#!/usr/bin/env python
# Listen on http 3000 and return HTML listing of current directory
# Fodder for the app event handler

import http.server
import socketserver

PORT = 3000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
