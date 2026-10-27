# 29.10.2026 — Heizkörper-Aufmaß in 5 Minuten pro Gerät

**Minimalanforderung, damit die Konstruktion starten kann**:
1. Foto **vorne** (kompletter Heizkörper mit Thermostat).
2. Foto **von unten** (Konvektionsbleche, freie Öffnung).
3. Foto **seitlich** mit Zollstock.
4. Werte: **Breite, Höhe, Tiefe, Abstand von Boden zur Unterkante** (alle mm).
5. Angeben: Elektroheizung oder wassergeführter Heizkörper? Heizkostenverteiler am Gerät vorhanden? Hindernisse auf Unterseite/Steckdose?

Mehr NICHT vorab messen. Aus Fotos präzise Nachmesspunkte nur bei Bedarf.
Zusätzlich für die technische Freigabe später: maximale Heizkörper-Oberflächentemperatur im Heizbetrieb und Umgebungsluft unter der Heizfläche. Kein unsicheres Berühren heißer Flächen, ggf. kontaktlosen Sensor oder aufgeklebten Sensor nach Anleitung verwenden.

## Datenhaltung
Fotos bleiben in privatem Chat/privaten Dateien bzw. künftig PRIVATEM Innovation-Projektrepository; NICHT in öffentlichem Research-OS. Im öffentlichen GitHub nur anonymisierte IDs und generische Schemata.

## Daten für Agent 02
`radiator_id` RAD-01 etc.; `heater_kind` WATER/ELECTRIC/UNKNOWN; Maße mm; `floor_gap_mm`; `obstruction_photo_present`; `has_heat_cost_allocator` YES/NO/UNKNOWN; `max_hot_surface_C` unbekannt bis Messung. UNKNOWN blockiert ggf. G2.
