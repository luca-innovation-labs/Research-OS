# SMART SURFACES

**Modulare Smart Mirrors & transparente LCDs** · Forschungs- und DIY-Projekt von Innovation Labs  
**Stand: 2026-10-27 · Phase: Konzept + lauffähiger Software-Demonstrator, keine freigegebene Bauanleitung**

Ein hardwareunabhängiges System für vier Einbaukonzepte:

1. **Round Mirror:** runder Spiegel, halbdurchlässiges Spezialglas und verborgenes HDMI-Display.
2. **Mirror Cabinet:** Spiegelschrank mit getrennter, servicefähiger Displaykassette.
3. **Transparent PC:** modifiziertes LCD ohne Backlight als beleuchtetes PC-Seitenfenster.
4. **Repurposed Phone:** gebrauchte Samsung-Galaxy-Telefone mit DeX als Displaycomputer (oder experimentell alternative Linux-Umgebungen).

> **Wesentliche Unterscheidung:** Ein modifiziertes LCD funktioniert nur bei ausreichendem Gegenlicht; bei den Smart Mirrors bleibt das LCD unverändert und liegt hinter speziellem Spiegelglas. Samsung DeX ist nur mit unterstützten Galaxy-Modellen/One-UI-Kombinationen verfügbar. GrapheneOS hat derzeit keine offiziellen Samsung-Builds.

## Schnellstart: Dashboard als Demo

Python 3.10+ wird benötigt; keine zusätzlichen Bibliotheken.

```bash
cd software
python3 -m smart_surfaces.server
# im Browser http://127.0.0.1:8765/?profile=round öffnen
# weitere Profile: cabinet, tower, dex
```

Der Server hört standardmäßig **nur auf 127.0.0.1**. Die Daten im Dashboard sind klar als **Demodaten** gekennzeichnet, keine Live-Sensoren! Ein Netzwerk-Gateway mit Authentifizierung/HTTPS wird vor einem Einsatz auf anderen Geräten erforderlich.

```bash
cd software
python3 -m unittest discover -s tests -v
```

## Ordner

| Pfad | Inhalt |
|---|---|
| `software/` | Laufbarer Standardbibliotheks-Webserver, zugängliches Dashboard, Tests |
| `config/display-profiles.json` | Profildefinitionen für die vier Displaytypen |
| `docs/ARCHITECTURE.md` | Komponentenarchitektur, Datenflüsse, Datenschutz |
| `docs/HARDWARE.md` | Vergleich der Displaytechnologien und Controller |
| `docs/SAMSUNG-DEX.md` | Smartphone-Reuse, DeX, Linux, GrapheneOS, Stromversorgung |
| `docs/SAFETY.md` | Elektrische, thermische und mechanische Risiken/Abnahmekriterien |
| `docs/CAD.md`, `cad/` | Parametrisches Konstruktionserfordernis, Messschema |
| `docs/BOM.csv` | Modellhafte Beschaffungsliste ohne Preisgarantie |
| `docs/ROADMAP.md` | Meilensteine, Entscheidungsgates, Prioritäten |
| `docs/TEST-MATRIX.md` | Nachweisbare Testkriterien und Status |
| `docs/SOURCES.md` | Hersteller- und Softwarequellen, Abrufdatum |

## Entwicklungsstrategie

- **Phase 0 – Spezifikation:** Funktionsprinzipien, Risiken und Messprogramm festlegen. **Erledigt (Dokumentation).**
- **Phase 1 – Technischer PoC:** Demo-Dashboard, Basistests, Profilmuster. **Software-Demo erstellt; Hardware offen.**
- **Phase 2 – Optikversuche:** Spiegelglas-Muster, LCD-Lichtversuche und Lesbarkeit messen. **Offen.**
- **Phase 3 – Individuelle CAD-Modelle:** nach Aufmaß, mit Sicherheitsprüfung. **Offen.**
- **Phase 4 – Pilotmontage:** Trennung von Netzspannung, Wärme- und Kondensationsprüfung. **Offen.**
- **Phase 5 – Dauerbetrieb:** dokumentierte Ergebnisse und Revision. **Offen.**

**Nicht vorliegend:** Aufmaßdaten, bestätigte Kompatibilität konkreter Monitore/Smartphones, physische Versuche, Zertifikate, elektrische Freigabe, fertige STL-Modelle.

## Geltungsbereich

Ein unabhängiges Innovation-Labs-Projekt; keine Datei von anderen Wohnungs-, Küchen- oder Schulprojekten ist Voraussetzung. Keine Schlüssel oder privaten Netzwerkadressen einchecken. Kein automatischer Einsatz von Geräten ohne technische Prüfung.