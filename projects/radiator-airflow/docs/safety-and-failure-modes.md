# Sicherheitskonzept — vor der Fertigung verbindlich prüfen

## Absolute Grenzen
- Keine Netzspannung in offenen Eigenbau-Lüfterkästen oder gedruckten 3D-Gehäusen. 12-V-SELV und geeignetes geprüftes Steckernetzteil, trocken und nicht am warmen Heizkörper.
- Keine Modifikation an wasserführendem Heizkörper, Ventilen, Heizungsverdrahtung, Druckbehälter, Leitung, Hydraulik oder Typenschild.
- Keine Booster an Elektro-/Speicher-/Infrarotheizkörpern ohne ausdrücklich einschlägige Herstellerfreigabe; niemals eine vorhandene Lüftungsöffnung oder Sicherheitstemperaturregelung abdecken.
- Kein generischer PLA-Einsatz in thermisch belasteten Bereichen. PETG/ASA nicht blind aufgrund von Filament-Marketing wählen: tatsächliche Oberflächentemperatur, Wärmeformbeständigkeit unter Langzeitlast, Brandverhalten, Druckparameter und Kriechverformung evaluieren.
- Lufteintritt/-austritt muss offen bleiben; kein Überhitzen von Rohren, Sensoren, Kunststoffen, Klebstoffen, Netzteilen oder Möbeln.

## FMEA vorab
| Failure | Auswirkung | Mitigation/Nachweis |
|---|---|---|
| Lüfter blockiert | Überstrom, erhöhter Lärm, Stillstand | Fan-Schutzfunktion prüfen, passender Schutz an Stromzweig, rpm-Fehler |
| Controller/GPIO hängt | 100%-Lauf, Nichtlauf, ungewollte Reboots | Hardwarebegrenzung/Reset, lokaler Failsafe, Dauerlauftest |
| Temperatursonde fällt ab | Falsche PWM/Schaltschwelle | Halterung, Plausibilitätscheck, Sensor-Fehlerzustand |
| Magnet/Clip löst sich | Fall-/Schlaggefahr, Rotorkontakt | Temperaturtest, Zugtest, mechanische Redundanz |
| Kunststoff kriecht/erweicht | Absturz/Verformung/Brandrisiko | Temperaturmapping, Materialdaten, Alterungstest |
| Stecker kurzgeschlossen | Erwärmung/Brand | zertifiziertes Netzteil, Absicherung, Leitungsdimension |
| Staub/Haare sammeln sich | Luftwiderstand & Hygiene | Lüftergitter, abnehmbare Abdeckung, Wartungsplan |
| PWM-Signal falsch | Beschädigung von MCU/Lüfter | 25-kHz-Open-Drain-Stufe, Bench-Test/Oszilloskop |
| Thermostatventil verschattet | Sensor misst falsch / Regelung instabil | Abstandsfreiheit, kontrollierter Reglertest |
| Flüssigkeitsleck | Feuchte an Elektrik | Elektronik nie unter potenzieller Leckstelle ohne Schutz, Abschalt-/Abstandskonzept |

## Abnahmekriterien vor Montage
Gemessene reale Hotspots mit Radiator bei höchster normaler Vorlauftemperatur; Lüftertemperatur innerhalb der produktspezifischen **Umgebungstemperatur**; eigene Lastproben am gedruckten Teil; Tritt-/Finger-/Tier-Schutz; sichere Kabelwege und Isolation; Netzteil außerhalb warmer Zone; thermisch und elektrisch getrennte Wartbarkeit; 24-h beaufsichtigter Test ohne Geruch, Materialfluss oder ungewöhnliche Geräusche. **Keine unbeaufsichtigten Dauerversuche vor Freigabe.**

## Cybersecurity
Kein offener Default-WLAN-AP, keine öffentlich erreichbare UI, sichere OTA, lokale Authentifizierung und Secret-Handling. Home Assistant nur optional; Cloud-Zwang ist ausgeschlossen.
