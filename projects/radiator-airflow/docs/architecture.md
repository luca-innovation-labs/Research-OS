# Konzeptionelle Architektur / Baukasten

Status: **Designhypothese, nicht freigegeben zur Fertigung.** Vorläufige Zielgruppe: wassergeführte Plattenheizkörper mit freien unteren Konvektionsöffnungen. Für elektrische Heizkörper, Heizregister oder unklare Bauarten gilt **No-Go bis Herstellerfreigabe**.

## Lösungsräume
A) **Direct Clip**: Lüfter unmittelbar in/unter Kanälen. + wenig Material; – punktuelle Verteilung, mögliche Hotspots/Vibration.
B) **Shrouded Rail** (Referenzwahl): Mehrere 80/92/120-mm-Lüfter an einem modularen Luftleitkanal. + skalierbar, bessere Dichtigkeit/Strömungsführung; – Einbauhöhe & Druckverlust prüfen.
C) **Floor Pod**: Bodenständige Gebläsekassette und Umlenkung. + für schwer befestigbare Radiatoren; – sichtbarer, Reinigungs- und Trittrisiko.

## Voraussichtliche Familie
- S (shallow): 60/80/92-mm als Kandidaten, Bauhöhe erst nach Messung festlegen.
- M: 120x15-mm Slim-Lüfter als Kandidat bei genügender Breite; keine Verengung der freien Ansaugfläche.
- L: 120x25/140-mm bzw. externes Pod nur nach Temperatur- und Hindernisfreigabe.

## CAD-Parameter (alle Millimeter, wenn nicht erwähnt)
rad_width, rad_height, rad_depth, floor_clearance, wall_gap, fin_channel_span, bottom_opening_depth, pipe_obstacle_map, fan_size, fan_thickness, fan_count, duct_clearance, wall_thickness, screw_diameter, magnet_diameter, service_clearance, cable_exit_side, shroud_lip. Geometrie darf nie auf angenommene DIN-Standardmaße beruhen.

## Modulschnittstellen
- Einheitlicher Rail/Adapter-Übergang; mechanische Verriegelung plus Schraube/Clip für Wartbarkeit.
- Fans austauschbar ohne Ausbau des gesamten Heizkörpers.
- Befestigung ohne Bohrungen in Druckbehälter/Heizkörper oder Beschädigung der Konvektionslamellen; verpolungs- und zugentlasteter Niedervoltkabelbaum.
- Magnetwirkung an konkretem Stahl prüfen, Haltekraft mit Temperatur/Sicherheitsfaktor und Schwingung validieren; keine N52-Magnete direkt an heißen Stellen ohne Materialdaten.
- Leicht erreichbare Staubreinigung, geschützte Rotorebene, Kind-/Haustierkontakt bedenken.
- Luft möglichst von unten nach oben durch heiße Kanäle; Bypass zwischen Lüfter und Heizkörper minimieren, ohne natürliches Konvektionsprofil unzulässig abzudecken.

## Mess- & Auswahlstrategie
Zunächst ein repräsentatives, gut zugängliches K2/K3-Gerät. Je zwei Geometrien (Direktmontage vs Luftkanal), identischer Lüfter und PWM-Stufe. Vergleiche Geräusch, Energieaufnahme, Wärmeaufstieg und Servicezugang. CFD erst nach Basistest für strittige Geometrie nutzen.

## Nichtziele v1
Keine selbst entwickelte Netzspannungstechnik. Kein Bauen an den Rohrleitungen. Keine ungeprüften Wirkungsgrad-/Sparversprechen. Keine Cloud-Abhängigkeit. Kein dekoratives Display, solange dessen Erwärmung, Stromverbrauch und Montage nicht freigegeben sind.
