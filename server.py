import os
import secrets
from http.server import HTTPServer, SimpleHTTPRequestHandler
from base64 import b64decode

AUTH_USER = os.environ["AUTH_USER"]
AUTH_PASS = os.environ["AUTH_PASS"]
PORT = int(os.environ.get("PORT", 3000))
SITE_DIR = os.path.join(os.path.dirname(__file__), "site")


class AuthHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=SITE_DIR, **kwargs)

    def do_GET(self):
        auth = self.headers.get("Authorization")
        if not auth or not auth.startswith("Basic "):
            self._send_auth_required()
            return
        try:
            decoded = b64decode(auth.split(" ", 1)[1]).decode()
            user, password = decoded.split(":", 1)
        except Exception:
            self._send_auth_required()
            return
        if not (
            secrets.compare_digest(user, AUTH_USER)
            and secrets.compare_digest(password, AUTH_PASS)
        ):
            self._send_auth_required()
            return
        super().do_GET()

    def _send_auth_required(self):
        self.send_response(401)
        self.send_header("WWW-Authenticate", 'Basic realm="LLM Wiki"')
        self.end_headers()


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", PORT), AuthHandler)
    print(f"Server running on port {PORT}")
    server.serve_forever()
