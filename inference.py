import threading
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

# Run your existing main() in background
def run_env():
    try:
        main()
    except Exception as e:
        print(f"Error running env: {e}")

threading.Thread(target=run_env).start()

# Simple server for Hugging Face
class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Cloud Optimizer Env is running")
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/reset":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            # minimal valid response
            response = b'{"status": "reset successful"}'
            self.wfile.write(response)

        else:
            self.send_response(404)
            self.end_headers()
server = HTTPServer(("0.0.0.0", 7860), Handler)
print("Server running on port 7860...")
server.serve_forever()