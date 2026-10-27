"""Unit tests for local read-only demo server."""
from __future__ import annotations
import json
from http.client import HTTPConnection
from threading import Thread
from http.server import ThreadingHTTPServer
import unittest
from smart_surfaces.server import Handler, FILES, CSP


class ServerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.httpd = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        cls.thread = Thread(target=cls.httpd.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()
        cls.httpd.server_close()
        cls.thread.join(timeout=3)

    def request(self, path, method="GET"):
        conn = HTTPConnection("127.0.0.1", self.httpd.server_address[1], timeout=3)
        conn.request(method, path)
        response = conn.getresponse()
        code = response.status
        headers = dict(response.getheaders())
        body = response.read()
        conn.close()
        return code, headers, body

    def test_html(self):
        code, headers, data = self.request("/?profile=round")
        self.assertEqual(code, 200)
        self.assertIn(b"Smart Surfaces", data)
        self.assertIn("text/html", headers["Content-Type"])
        self.assertEqual(headers["Cache-Control"], "no-store")
        self.assertEqual(headers["Content-Security-Policy"], CSP)

    def test_status_explicitly_demo(self):
        code, headers, data = self.request("/api/status")
        self.assertEqual(code, 200)
        obj = json.loads(data)
        self.assertEqual(obj["kind"], "demo")
        self.assertEqual(obj["schemaVersion"], 1)
        self.assertIn("roomTempC", obj)

    def test_known_assets(self):
        for route in FILES:
            with self.subTest(route=route):
                self.assertEqual(self.request(route)[0], 200)

    def test_unknown_path(self):
        for route in ["/other", "/../etc/passwd", "/.git/config", "/api/secret"]:
            with self.subTest(route=route):
                self.assertEqual(self.request(route)[0], 404)

    def test_post_disabled(self):
        self.assertEqual(self.request("/api/status", "POST")[0], 405)


if __name__ == "__main__":
    unittest.main()
