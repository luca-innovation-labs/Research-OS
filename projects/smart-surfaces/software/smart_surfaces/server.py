"""Local-only, read-only demo server. No third-party dependencies."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
from urllib.parse import urlsplit

FILES = {
    "/": ("index.html", "text/html; charset=utf-8"),
    "/index.html": ("index.html", "text/html; charset=utf-8"),
    "/style.css": ("style.css", "text/css; charset=utf-8"),
    "/app.js": ("app.js", "text/javascript; charset=utf-8"),
}
WEB = Path(__file__).resolve().parent / "web"
CSP = "default-src 'none'; script-src 'self'; style-src 'self'; connect-src 'self'; img-src 'self' data:; font-src 'self'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        route = urlsplit(self.path).path
        if route == "/api/status":
            payload = {
                "schemaVersion": 1,
                "kind": "demo",
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "roomTempC": 22.4,
                "humidityPercent": 48,
                "cpuTempC": 43.1,
                "cpuLoadPercent": 17,
            }
            self.send_response(200)
            self.common_headers("application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(payload, separators=(",", ":")).encode("utf-8"))
            return
        if route not in FILES:
            self.send_response(404)
            self.common_headers("text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Not Found")
            return
        filename, mime = FILES[route]
        content = (WEB / filename).read_bytes()
        self.send_response(200)
        self.common_headers(mime)
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def common_headers(self, mime: str) -> None:
        self.send_header("Content-Type", mime)
        self.send_header("Content-Security-Policy", CSP)
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("Cache-Control", "no-store")

    def do_POST(self):
        self.send_response(405)
        self.common_headers("text/plain; charset=utf-8")
        self.end_headers()

    def log_message(self, fmt, *args):
        # No URL path logs (query strings can contain unintended personal data).
        return


def main(argv=None):
    parser = argparse.ArgumentParser(description="Local Smart Surfaces dashboard demo")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args(argv)
    if not (1024 <= args.port <= 65535):
        parser.error("port must be 1024-65535")
    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    print(f"Smart Surfaces Demo: http://127.0.0.1:{args.port}/?profile=round", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
