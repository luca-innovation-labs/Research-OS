# AIRFLOW v1 / Anforderungen und Zielkonflikte

**Vorläufige Priorität:** Sicherheit > ausreichender Wärmezuwachs > akzeptable Lautstärke > Kosten > Smart-Home-Komfort. Die persönliche Wahl zwischen Lautstärke und Kosten ist offen.

| ID | Priorität | Anforderung | Abnahmemethode |
|---|---|---|---|
| R01 | MUSS | 12-V-Schutzkleinspannung, extern geprüftes Steckernetzteil | Sicherheitsreview + Herstellerdokumente |
| R02 | MUSS | Keine Berührung wasserführender Bestandteile mit Bohrer/Schraube | Montagezeichnungen & Sichtprüfung |
| R03 | MUSS | Material, Ventilator und Kabel innerhalb Temperaturgrenzen | Heiz-Hotspot-Messung und Thermiktest |
| R04 | MUSS | Schutz gegen abfallende/verkantete Lüftermodule, Eingriff in Rotor | Mechanik-/Serviceprobe |
| R05 | MUSS | Nach Heizkörpertemperatur automatisch ein/aus, 2–5 K Hysterese nur als Startannahme | Funktionstest |
| R06 | MUSS | Auch ohne WLAN/HA normal benutzbar | WLAN-Ausfalltest |
| R07 | MUSS | Anpassbarkeit an echte Maße, ohne frei erfundene Standardgeometrie | Parametersweep und Einbaucheck |
| R08 | MUSS | Messbare Heizwirkung oder Ergebnis inconclusive | Kontrollversuch |
| R09 | MUSS | Einheitliche BOM, mechanische Interface-Version, Nachvollziehbarkeit | Release-Audit |
| R10 | SOLL | Leise im Aufenthaltsbereich bei typischer Leistung | 1m-Test, Wohnpositionsbeurteilung |
| R11 | SOLL | Leichte Reinigung und Lüfteraustausch | Demontagetest |
| R12 | SOLL | Einkauf und Druck unabhängig von Einzelanbieter | Export STEP/STL/3MF, Standard-Fans |
| R13 | KANN | ESPHome und Home Assistant mit optionalem Nachtmodus | Integrationstest |
| R14 | KANN | Mehrere Fan-Reihen individuell regeln | Thermik/Akustik-Nachweis |
| R15 | KANN | Sensor-Logging und Energie-Benchmark | Datenqualitätstest |

## Bewertung der Varianten
Score erst nach tatsächlichem Aufmaß und Pilotmessung! Kriterien Vorschlag: Temperaturreserve 25%, akustische Qualität 25%, Wärmekomfort 20%, Fertigungskosten 15%, Wartbarkeit 10%, Optik 5%. Diese Gewichte sind **Vorschläge**, keine Nutzervorgaben. Varianten ohne R01–R04 werden unabhängig vom Score verworfen.

## Projektabgrenzung
Heizkörpertypen vor Foto nicht unterstellen; kein pauschaler Eco-Benefit ohne Energiebilanz. Heizkostenverteiler dürfen weder direkt angeblasen noch in ihrer Messung beeinflusst werden; Einfluss/Herstellerfreigabe gesondert klären.
