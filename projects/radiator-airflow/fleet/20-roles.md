# 20-Chat-Flotte — spätere Aktivierung, noch NICHT gestartet

Jeder Chat besitzt einen abgegrenzten Verantwortungsbereich. Gemeinsame Regel: Fakten/Annahmen/Entscheidungen trennen, Quellen dokumentieren, keine individuellen Wohnungsdaten in öffentliches Repo, keine ungeprüften Freigaben. Hand-off immer als Markdown-PR/Commit mit Scope, offenen Punkten, konkreten Akzeptanzkriterien und Querverweisen. Die Steuerzentrale (Chat 00, optional) integriert Ergebnisse, ersetzt keine Fachabnahme.

| Chat | Verantwortung | Prüfbares Deliverable | Voraussetzung |
|---|---|---|---|
| 01 | Projektsteuerung & Anforderungen | Lastenheft und Gatecheckliste | Start |
| 02 | Radiator-Typologie & Aufmaß | Schema plus korrekt erfasstes anonymes Inventar | Nutzerfotos/ Maße privat |
| 03 | Literatur & Wärmetransport | Quellenbasierte Thermikmodelle und Grenzen | G0 |
| 04 | Markt/Patente/Lizenzen | Wettbewerbsvergleich und Lizenzmatrix | G0 |
| 05 | Strömungs-/Druckanalyse | Fan-PQ × Kanalwiderstand, ggf. CFD-Konzept | G1/2 |
| 06 | Lüfterauswahl & Akustik | Shortlist mit Datenblatt, RPM/Schall-Grenzen | G1/2 |
| 07 | Systemarchitektur & Modulstandards | Interface-Spezifikation | G1/2 |
| 08 | CAD Basismodul (FreeCAD) | param. Modelle + STEP/STL + Tests | G2 |
| 09 | CAD Halterung/Anschlüsse | sichere Clips/Füße/Magnete, Belastungsfälle | G2 |
| 10 | Drucktechnik/Werkstoffe | orientierter Druckplan, Temperaturkriechtests | G2 |
| 11 | Elektrik & SELV-Sicherheit | geprüfter 12-V-Schalt-/Sicherungsplan | G2 |
| 12 | Sensorik/Messsystem | Temperatursensorik, Kalibrierung, Toleranzen | G2 |
| 13 | MCU & Firmware ESPHome | offlinefähige Regelung, Tests und Konfig | G3 Elektrik |
| 14 | Smart-Home & Security | HA optional, OTA/WLAN-Failover, Secrets | G3 Firmware |
| 15 | Ergonomie/Lautstärke-UX | Reinigungszugang, Lärm, Bedienelemente | G3 |
| 16 | Stückliste/Preis & Lieferanten | revisionsgenaue BOM, Beschaffung ohne Auftrag | G3 |
| 17 | Messdesign & Statistik | A/B/A-Plan, Datenmodell, Konfidenz | G3 |
| 18 | Prototypaufbau & Montage | Montageanleitung, Fotos (privat), Prüfergebnisse | G4 |
| 19 | Dauerhaltbarkeit & FMEA | thermische/mechanische Störfalltests, Risk Register | G4/5 |
| 20 | Unabhängige QA & Systemintegration | signierte Checklisten, Gatefreigabe/No-Go | alle |

## Kollisionsregel
01 koordiniert, 20 kontrolliert unabhängig, 08/09 teilen mechanische Schnittstelle, 11/13 teilen Elektrik/Firmware-Contract, 03/05/17 trennen Theorie/Soll/Test. Kein doppeltes Editieren derselben Datei ohne git-Branch-Zuordnung. Für jeden Chat eigene Issue/Branch oder Projektordner.

## Erstes Arbeitsprogramm
Wave A: Chats 01–07 + 16 + 17 recherchieren ohne Maße; Wave B: 02, 08–12 nach Aufmaß; Wave C: 13–15 + 18 nach Sicherheitsreview; Wave D: 19 + 20 für Prototypabnahme. Blockierte Rollen sollen offenen Input ausweisen, nicht erfinden.

## Fortschrittsmeldung
Nur nachweislich erledigte Artefakte zählen; 100% erst nach validiertem, dokumentiertem und einsatzbereitem System. Fortschritt je Gate und Funktionsumfang nennen statt frei geschätzter Scheingenauigkeit.
