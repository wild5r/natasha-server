import json

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
from natasha import NamesExtractor

class RequestHandler(BaseHTTPRequestHandler):
    def extract_names(self, text):
        extractor = NamesExtractor()
        matches = extractor(text)
        return [_.fact.as_json for _ in matches]

    def do_POST(self):
        content_len = int(self.headers['Content-Length'])
        post_body = self.rfile.read(content_len)
        try:
            json_data = json.loads(post_body.decode('utf-8'))
            parsed_path = urlparse(self.path)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps({
                'original_data': json_data,
                'names': self.extract_names(json_data['data'])
            }).encode('utf-8'))
        except json.decoder.JSONDecodeError as e:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(json.dumps({
                'error': "%s" % e
            }).encode('utf-8'))
        return

if __name__ == '__main__':
    server = HTTPServer(('', 8080), RequestHandler)
    print('Starting server at http://localhost:8080')
    server.serve_forever()
