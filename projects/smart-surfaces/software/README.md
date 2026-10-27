# Smart Surfaces Demo

Voraussetzung: Python >= 3.10, kein pip nötig.

```sh
python3 -m smart_surfaces.server
python3 -m unittest discover -s tests -v
```

Profile: `/?profile=round`, `/?profile=cabinet`, `/?profile=tower`, `/?profile=dex`.

Die Demo zeigt **nur synthetische Referenzwerte** und verwendet keine Sensoren, Web-APIs oder Cookies. Server hört standardmäßig auf `127.0.0.1:8765`; es gibt keinen öffentlich nutzbaren Login-Mechanismus. Nicht an `0.0.0.0` binden und nicht offen ins Internet veröffentlichen. Für externe Displays zuerst abgesicherten Reverse Proxy/Tailscale einrichten.
