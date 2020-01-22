# Chepurna
# ID:6152714
# CNT4713-U01 - assignment 2
# 1/19/2020

import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
