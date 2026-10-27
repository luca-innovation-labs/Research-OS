# Beschaffung und Bauteilshortlist (keine Bestellfreigabe)

## Kandidaten
| Kandidat | Herstellerangabe | Temperatur-/Eignungsgrenze |
|---|---|---|
| Noctua NF-A12x15 PWM | 120x120x15 mm; bis 94,2 m³/h; 1,53 mm H2O; 1,56 W max. | bis 70 °C Umgebung; Ideal bei flacher Montage; Preis nach Angebotsprüfung |
| ARCTIC P12 PWM PST | 120x120x25 mm; bis 95,7 m³/h; 2,20 mm H2O | bis 40 °C Umgebung; nicht ohne Heizkörper-Hotspottest direkt montieren |
| 80-/92-mm 4-pin PWM | noch keine modellgenaue Datenblattprüfung | Erst dann kaufen, wenn 120-mm-Geometrie ausscheidet |
| DS18B20 Temperaturfühler | Kontakt-Temperatur mit isolierter Befestigung | Sensor-/Kalibrierabweichungen prüfen |
| ESP32/ESPHome | nur V1+ | Versorgung/DC-DC/PWM-Treiber, gute Gehäuseplatzierung |
| Zertifiziertes 12V-DC-Netzteil | modellabhängig, mit ausreichendem Anlauf-Headroom | Abseits der heißen Zone |
| Befestigung | Schrauben, Silikonpuffer, optional Magnete/Klemmen | thermischer Test plus Fallback-Halter |

## Design-for-Cost
Zwei Referenzkonfigurationen kalkulieren:
- ECO: günstige 80/120-mm-PWM-Fans + einfacher fertiger Temperaturregler + PETG/ASA nach Freigabe.
- QUIET/SMART: tempgeeignete Slim-Lüfter + druckoptimierter Kanal + ESPHome + servicefreundliche Elektronik.

**BOM noch nicht validiert.** Preise und Verfügbarkeit können sich ändern; Beschaffung nach CAD-Freeze und Temperaturmessung. Maximaler Luftstrom **nicht** mit tatsächlichem Luftdurchsatz verwechseln.

## Einkaufs-Mindestangaben
Hersteller/SKU, Maße, Betriebsspannung, Dauer- und Anlaufstrom, Betriebstemperatur, statischer Druck/Fan-PQ-Kurve, Lager, dB(A)-Methode, Garantiedauer, Rückgabebedingungen, Stückpreis inkl. Versand; Netzteil EU-Sicherheitskennzeichnung, Schutzklasse, thermische Spezifikation.

## Langfristig
Wartungs-/Ausfallkosten, fehlende Ersatzteile, 3D-Druckfilament-Mengen, Kabelsatz-Verschnitt und 12-V-Stromkosten sind explizit in der BOM zu erfassen.
