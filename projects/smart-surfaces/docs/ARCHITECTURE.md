# Architektur / ADR-001

## Ziel
Eine einzige datensparsame Oberfläche auf unterschiedlichen Endgeräten: Browser auf Raspberry Pi, Windows/Linux-PC, Samsung DeX oder Android/Pixel. **Anzeige und Datenquellen entkoppeln**: HTML/CSS/JS-Client zieht Daten von optionalen lokalen Diensten, direktes Hardwarezugriffsrecht nur an einem dedizierten Connector.

```text
Optional: lokaler Hub (Linux / Mac mini / Home Assistant)
 ├─ Sensordatenadapter → validierte Messwerte
 ├─ Gerätestatusadapter → erlaubte, anonymisierte PC-Metriken
 ├─ Kalender-/Wetteradapter → nur mit ausdrücklicher Freigabe
 └─ Authentifizierter HTTPS-Endpunkt (zukünftig)
                     │
          LAN nur über gesichertes Gateway
        ┌────────────┼──────────────┐
  Rundspiegel     Spiegelschrank   PC-Tower  (+ DeX-Endgerät)
  Pi/DeX/Pixel    Pi/DeX          PC/kleiner Pi
  HDMI-Panel      HDMI-Panel      transparentes LCD
  MirroView       MirroView       beleuchteter Innenraum
```

## Laufzeitentwurf
- **MVP:** Keine Abhängigkeiten; Python-Server mit ausschließlich erlaubten statischen Dateien und schreibgeschütztem `/api/status`; `127.0.0.1:8765`.
- **Client:** Vanilla JS; Profile `round`, `cabinet`, `tower`, `dex` per festem Allowlist-Parameter; system fonts; unterstützt `prefers-reduced-motion`.
- **Datenmodell:** `schemaVersion`, `kind: demo`, Zeitstempel, `roomTempC`, `humidityPercent`, `cpuTempC`, `cpuLoadPercent`; Demodaten niemals als echte Sensormessung ausgeben.
- **Folgeversion:** Austauschbare Adapter mit expliziten Berechtigungen, MQTT nur mit Authentifizierung, Werte plausibilisieren, Fehler-/Offline-Status anzeigen.
- **State management:** Browserlocalstate vermeiden, keine Anwenderprofile in URL, keine Analytics/Tracker/Remote Fonts.

## Privatsphäre / Bedrohungsmodell
1. Der Dashboard-Server darf **nicht** ungeschützt im Internet oder im gesamten LAN lauschen.
2. Browser-Kiosk darf keine Cloud-Secrets, Kalender-Tokens oder Smart-Home-Credentials erhalten.
3. Externe Daten nur in Gateway abrufen; an Displays nur die minimal benötigten, bereinigten Felder weitergeben.
4. Für Netzwerkzugriff später: TLS, Zugriffskontrolle (z.B. Tailscale oder authentifizierter Reverse Proxy), URL-Allowlist, Rate-Limits, Update- und Widerrufsweg.
5. Keine Kameras/Mikrofone im MVP; für Präsenzsensoren ohne Bildaufnahme bevorzugt PIR/mmWave.
6. Monitor-/PC-Telemetrie nur über lokalen autorisierten Adapter, kein Fernsteuerungsinterface im Kiosk.

## Entscheidungen
- ADR-001: Thin client im Browser statt Electron überall → weniger RAM und plattformoffen.
- ADR-002: Samsung mit Original-One-UI für DeX; alternative OS nur prototypisch und getrennt.
- ADR-003: Keine DIY-Akkumodifikation in Gehäusen; Endgeräte vollständig belassen.
- ADR-004: Bauen erst nach optischem Muster und elektrischem Designreview.
