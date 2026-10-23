#!/usr/bin/env python3
"""Tiny static server for local testing.

Normal `python3 -m http.server` lets the browser cache game.js/style.css, so
edits can look like they "did nothing". This server disables caching.
"""
import http.server
import socketserver
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8731


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()


if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), NoCacheHandler) as httpd:
        print(f"Serving http://127.0.0.1:{PORT}/index.html (no cache)")
        httpd.serve_forever()
