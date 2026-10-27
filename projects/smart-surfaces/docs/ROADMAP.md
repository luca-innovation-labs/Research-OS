# Priorisierte Roadmap

## P0 · Grundlagen (erstes Inkrement)
- [x] Vier Hardwarepfade differenzieren; Smartphone-Reuse ergänzen
- [x] Referenzquellen und Risiken schriftlich erfassen
- [x] Einfacher lokaler Browser-Demonstrator mit Anzeigeprofilen und klaren Demowerten
- [x] Unit-/HTTP-Tests sowie minimale CI-Definition
- [ ] Vorhandene Hardware inventarisieren und konkretes Pilotgerät wählen
- [ ] Aufmaßdaten eintragen, Fotos anfordern (keine Standortdaten in öffentlichen Repos)

## P1 · Hardware-Machbarkeit
- [ ] MirroView / 50/50 als Muster mit gleichem LCD im Tages-/Dunkeltest vergleichen
- [ ] Ein LCD-Testspender vollständig identifizieren (Typenetikett, Anschluss, Panelcontroller)
- [ ] Transparent-LCD-Versuch unter fachlicher Aufsicht, vorher Sicherheitsprüfung
- [ ] Galaxy-DeX-USB-C-Hub/HDMI bei konkret vorhandenem Smartphone testen
- [ ] 5-Zoll-Waveshare optional als Vergleichsgerät testen

## P2 · Konstruktion
- [ ] CAD-Parameter vervollständigen
- [ ] Rundspiegel-Befestigung fachlich prüfen; Druckteile nur nach mechanischer Lastbewertung
- [ ] Spiegelschrank-Bauraum, Türmoment und Feuchtepfade prüfen
- [ ] PC-Panel-Kabel, Klemmschutz und Luftströmung prüfen

## P3 · Softwareprodukt
- [ ] Geräte-Registry mit Ablaufdatum/Versionen
- [ ] Authentifiziertes Gateway, Telemetrieadapter und HTTPS/Tailscale
- [ ] Konfigurierbare Anzeige-Layouts, local-first Speicherung und OTA-Updatekonzept
- [ ] Kiosk/Wiederanlauf nach Netzunterbrechungen in Testmatrix
- [ ] Bedienkonzept (Touch optional, Sprachassistent nur opt-in)

## P4 · Abnahme
- [ ] 24-Stunden-Wärmestabilität und Sichtprüfung
- [ ] Datenschutz- und Elektrosicherheitsreview
- [ ] Druckteil- und Glasmechanikreview
- [ ] Dokumentierte Wiederholbarkeit (BOM, Zeichnungen, Fotos, Versionsnummern)

## Entscheidungsregeln
**Spiegel:** 50/50 nur bevorzugen, wenn ein reales Muster bei Zielbeleuchtung besser lesbar ist; Reflexionswirkung ebenfalls bewerten. **Tower:** vorhandenes, tatsächlich passendes LCD vor Neukauf. **DeX:** nur mit Sicherheitsupdates/akzeptiertem Isolationskonzept und nach Dauerbetriebstest.
