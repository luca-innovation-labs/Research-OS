# Elektronik/Regelung — Entwurfsgrundlage

## Referenzblock
230 V Steckdose -> **gekauftes und sicherheitsgeprüftes, passendes 12-V-Netzteil** außerhalb heißer/geschlossener Baugruppen -> 12-V-Abzweig mit Sicherung/Schutz und Zugentlastung -> handelsübliche 12-V-4-Pin-Lüfter. Parallel: 12 V -> geprüfter DC-DC 3,3/5 V Regler -> ESP32 (OPTIONAL); Sensoren (Vor- und Rücklauf, Raumluft, optional Gehäusetemperatur). AC-Anschlüsse nicht selber bauen.

## PWM-Fallstricke
Standardisierte 4-Pin-PC-Lüfter typischerweise 25 kHz open-drain/open-collector auf Pin 4; **nicht einfach ESP32-GPIO direkt an 5-V-PWM-Bus treiben**, sondern geeigneten transistorisierten Open-Drain-Treiber mit Pegelprüfung einsetzen. Pin 1=GND, Pin 2=12 V, Pin 3=TACH, Pin 4=PWM, aber tatsächliche Pinouts je Modell prüfen. Lüfter können bei 0 % PWM weiterlaufen: echte Versorgungstrennung und sichere Startlogik je Modell validieren. Nur EIN Tachosignal pro zusammengelegter Auswertung, falls nicht getrennt gepuffert. Elektroplan vor Umsetzung durch sachkundigen Reviewer freigeben.

## Firmwareziele
- Local-only, keine Internetpflicht; eigenständige Temperaturkurve unabhängig von Home Assistant.
- Zustände: OFF, WAIT_WARM, PRESPIN, RUN, COOLDOWN, SENSOR_FAULT, OVER_TEMP.
- Schaltschwellen als **vorgeschlagene** Testparameter: warm ab 34 °C, wieder aus unter 29 °C; mindestens 120s Haltezeit (hysteretisch), fein abgestufte Fan-PWM. Kein Start bei unbekanntem Sensortyp.
- Sicheres Verhalten: Fehler/Disconnection -> **Aus** und Fehlerindikator (bzw. unter Safety-Review festzulegender Modus); thermischer Hardwarenschutz unabhängig von Firmware; Netzteil bleibt elektrisch geschützt.
- Minimum/PWM testweise ermitteln: Motoranlauf ist bei kleinen PWM-Werten nicht sicher. Startimpuls und RPM-Prüfung mit Timeouts.
- OTA nur mit Authentifizierung und manueller Freigabe; keine Secrets im Repo, keine ungeschützten AP-Fallbacks. Geräteidentitäten und lokale Netzsegmentierung.
- WLAN-Störung darf Wärme-/Sicherheitslogik nicht beeinträchtigen.

## Konzeptvarianten
V0: fertiger Niedervolt-Thermostat + 12-V-Fan-Schaltung = minimaler Debug-Aufwand.
V1: ESP32 + DS18B20, Hardware-PWM + Tach, Standalone-WebUI = flexible Regelelektronik.
V2: ESPHome/Home Assistant/MQTT (nur falls gewünscht) = Komfortfeatures, zusätzliche Komplexität.

## Stromrechnung (Beispiel, noch nicht BOM)
4× Noctua NF-A12x15 mit max. 0,13 A pro Lüfter: statische Datenblatt-Summe 0,52 A bzw. 6,24 W bei 12 V. **Anlaufspitzen, Controller, Leitungsverluste und Temperatur-Derating separat auslegen; kein Netzteil ohne Headroom auswählen.** Herstellerwerte des tatsächlich gewählten Modells haben Vorrang.
