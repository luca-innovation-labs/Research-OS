# Hardware und Displayprinzipien

## A – Rundspiegel (erste Wahl)
- **Vorderseite:** reflektierendes, **halbdurchlässiges** Glas (z.B. Pilkington MirroView / MirroView 50/50); Schnitt, Kanten, Gewicht, Befestigung vom Glasfachbetrieb beurteilen lassen.
- **Dahinter:** übliches, unverändertes rechteckiges HDMI-Display (7–10 Zoll) für Informationsfenster. Rückseite um das Display lichtdicht auskleiden; möglichst schwarzer Bildschirmhintergrund; Glasprobestück vor Serienbestellung testen.
- **Alternative:** rundes 5-Zoll-IPS-HDMI-LCD (Waveshare 1080×1080), zusätzliche Touchfunktion hinter Glas nicht garantiert.
- **Compute:** Pi 4/5, vorhandener kleiner Rechner oder qualifiziertes DeX-Smartphone.
- **Licht:** dimmbares, indirektes LED-Ringlicht mechanisch getrennt vom Display. Feuchtraum nur nach Standort-/IP-/Elektrofachprüfung.
- **Parametrische Konstruktion:** äußerer Spiegeldurchmesser, Tiefe, Displayposition/Größe, thermische Wege, tragfähige Glaslagerung.

## B – Spiegelschrank
- Displaykassette hinter geeigneter Spiegelpartie; nicht hinter einer herkömmlich rückseitig versilberten, undurchlässigen Spiegelfläche.
- Vermeide Kabel über bewegte Türscharniere, falls kein professionell geeigneter Kabelübergang vorgesehen ist; bevorzugt festes Gehäusesegment.
- Prüfen: Türgewicht/Scharniere, Wandbefestigung, Belüftung, Feuchtigkeit, Kondensat, Temperatur, Wartung, Blendung.
- Der mögliche Innenausbau muss zu vorhandener Bautiefe passen.

## C – PC-Tower transparentes LCD
- Gebrauchte LCD-Module können durch **Entfernung von Backlight, Lichtleiter und Reflektor** teilweise durchsichtig werden. Notwendige Polarisationsfilter und Glaszelle bleiben erhalten. Das Verfahren ist modellabhängig; nicht jedes Panel ist geeignet.
- Panel **nicht zuschneiden, bohren oder biegen**. Flachbandleitungen und Treiber dürfen keine Zugkräfte aufnehmen.
- **Displaycontroller/EDID:** Wenn ursprüngliche Elektronik passend und sicher weiterverwendbar ist, HDMI/DP-Ausgabe des PCs nutzen; andernfalls exakte LCD-Panel-ID erfassen und einen kompatiblen Treiber prüfen. Keine Universal-Kompatibilität annehmen.
- **Lesbarkeit:** Helle, homogene Innenbeleuchtung ist erforderlich. Polarisatoren und Farbe reduzieren Durchlass; Schwarz/Weiß-Effekt hängt von Paneltyp und Polarisatorausrichtung ab. RGB-PC-Beleuchtung ersetzt nicht unbedingt gerichtetes, ausreichend diffuses Gegenlicht.
- Tower darf Luftführung, GPU-Freiraum, Temperaturen und Seitenteilhalt nicht verschlechtern. Elektrische Abschirmung und Erdung von Metallgehäuseteilen nicht beeinträchtigen.
- Netzteil/Backlight-Elektronik und Hochspannungspunkte des Spendermonitors ausschließlich durch qualifizierte Personen beurteilen/demontieren; sicherheitsgefährdende Eigenarbeiten sind kein Teil dieser Anleitung.

## Alternative Technologien
| Technik | Transparenz | Typisches Einsatzfeld | Risiko/Limit |
|---|---|---|---|
| unverändertes LCD + MirroView | Spiegelbild mit gelegentlichen Overlays | Rundspiegel, Schrank | Glaspreis, Helligkeit |
| LCD ohne Beleuchtung | teiltransparente Farbgrafik | PC-Tower | empfindliche Demontage, Beleuchtungsbedarf |
| Transparent-OLED | selbstleuchtende Inhalte auf durchlässiger Fläche | Premium | hoher Preis, Kontrast in hellen Räumen |
| projektiver Spiegel | Bild auf spezieller Fläche | Experiment | Kalibrierung, Licht, Bauvolumen |

## Nachgewiesene Herstellerangaben (2026-10-27)
- Waveshare 5inch 1080x1080 LCD: 5 Zoll, HDMI, aktive Fläche 127,6 mm, Gesamtmaß 150×150×7 mm, 300 cd/m², Leistungsaufnahme 2 W (Herstellerdaten); geeignet als runde Bildfläche, **nicht** als transparentes Panel.
- Raspberry Pi 5: 2× micro-HDMI, empfohlen 5 V/5 A-Netzteil; Pi 4 normalerweise 5 V/3 A.
- Pilkington MirroView und MirroView 50/50: für Displayintegration; die Variante 50/50 ist für helle Umgebungen optimiert. Optische Daten nur nach exakter Glasdicke/Variante und aktueller Datenblattversion auslegen.

## Beschaffungskriterien vor Kauf
Displaymodell / Panel-ID, aktive Pixel, Außenabmessungen, Pinout, Videoeingang, Lichtstärke, Controller, Stromaufnahme, Betriebsspannung, Wärmeabgabe, Einsatzort/IP, Gewicht, Lieferbarkeit, Rückgaberecht, Glasabmessung/Bearbeitung, Servicezugang.
