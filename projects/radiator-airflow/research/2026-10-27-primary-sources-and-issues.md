# Quellen-Audit und Designrisiken (27.10.2026)

| Frage | Quelle (Hersteller/Original) | Verifiziert / Konsequenz |
|---|---|---|
| Heizleistungszunahme | Bayram & Koç (2023), https://doi.org/10.1016/j.csite.2023.103432 | Erhöhte Wärmeabgabe experimentell, stärkster Effekt bei niedrigerem Vorlauf; keine allgemeine Einspar-Prozentzahl |
| Noctua Slim | https://www.noctua.at/en/products/nf-a12x15-pwm/specifications | 120x120x15mm, bis 70°C Umgebung, max 0.13A, 94.2m³/h frei, 1.53mm H2O |
| ARCTIC günstig | https://www.arctic.de/en/P12-PWM-PST/ACFAN00120A | 120x120x25mm, bis 40°C Umgebung, 0.1A, 95.7m³/h frei, 2.20mm H2O |
| Fan PWM | https://www.manualshelf.com/manual/intel/d510mo-1/4-wire-pulse-width-modulation-pwm-controlled-fans-specification/page-9.html | 25 kHz, 21–28 kHz zulässig, pull-up im Fan, 5.25V max. Open-drain/collector Treiber besser als MCU-push-pull |
| Existierende Steuerung | https://github.com/andrekuehne/openradfan | ESPHome 12V-Controller/2×4 Fans, global power cutoff. Hardware-Warnung: USB nicht bei gestecktem Controller wegen möglicher Rückspeisung; kein Blindkopieren von Default-WiFi |
| Fernwärme/Gas/Heizkostenverteiler | https://www.vattenfall.de/infowelt-energie/nachhaltig-heizen/was-ist-ein-heizkostenverteiler | Mess-/Abrechnungsgerät darf nicht manipuliert/thermisch direkt beeinflusst werden; ggf. Messdienst fragen |
| FDM-Druck Franken | https://3ddruckfranken.de/index.html | Online-STL/3MF-Rechner, ASA/PETG, 320mm Bauraum; Noch kein Angebot |
| PrintYourParts Nürnberg | https://printyourparts.de/3d-druck-nuernberg | technische Materialien inkl. ASA/PETG, Abholung/Versand; noch kein Angebot |
| 3Dimension Allersberg | https://www.3dimension-allersberg.de/ | FDM, ASA/PETG und Kleinserien; noch kein Angebot |
| VF-TEK | https://www.vf-tek.de/ | Online-Kalkulator, ASA/PETG, noch kein Angebot |

## Offene Recherche
(1) CAD-Lizenzen bestehender Projekte, (2) Fan-Qp-Daten und RPM bei kleinen PWM-Werten, (3) thermische Daten des ausgewählten Filaments bei realer Last, (4) Energieverteilung in zentraler Heizung und Einfluss auf Heizkostenverteiler, (5) unabhängige Vergleichsmessung unter stationären Bedingungen.

## Korrektur früherer Schlussfolgerungen
- Noctua-Temperaturrating gilt **Umgebungsluft am Lüfter**, nicht eine beliebig heiße Gehäusekontaktfläche.
- ARCTIC P12 ist ohne Temperaturtest kein freigegebener Direktanbau an heißen Heizkörpern.
- 120-mm-Lüfter passen nicht automatisch unter einen 100-mm-tiefen Heizkörper.
- OpenRadFan ist eine wertvolle Vorlage, nicht fertig übernommene/sicherheitsgeprüfte Systemlösung.
- Preis-/Lieferzeitseiten sind Anbieteraussagen, keine bindenden Angebote.
