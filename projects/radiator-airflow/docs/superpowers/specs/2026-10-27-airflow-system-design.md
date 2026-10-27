# AIRFLOW: Technischer Systementwurf v0.2 (27.10.2026)
**Status: vorgeschlagener Entwurf, noch nicht zur Fertigung freigegeben.** Account: luca-innovation-labs. Öffentliches Research-OS: keine persönlichen Fotos/Adressen/Geodaten.

## Nutzerauftrag / Ziele
Individuell unter vorhandenen Heizkörpern montierbare, möglichst leise, günstige 12-V-Booster. Eigenständige, parametrisch anpassbare 3D-Druck-Gehäuse, online verfügbare Standardkomponenten, daheim einfach zusammenbauen, Steckernetzteil verwenden. Optional ESPHome/Home Assistant. Mehrere Heizkörper erhalten gemeinsame Ersatzteile/Baugruppen. 16 spezialisierte Chats im wellengesteuerten Verfahren, max. 20 wenn rechtfertigbar. Nach Eingang der echten Maße am 29.10.2026 geometrisch konkretisieren.

## Erfolgskriterien (konkret, vorläufig)
- Unter normaler und höchster zu erwartender Heizlast: innerhalb spezifizierter Grenztemperaturen aller Bauteile, kein Kriechen/Ablösen, berührungsgeschützt und elektrische Niedervolt-Sicherheit.
- Bei kontrolliertem A/B/A-Versuch messbar kürzere Aufheizung oder höhere Wärmeabgabe; nur Verbesserungen > Unsicherheit als solche kennzeichnen.
- Akustisch beim normalen Aufenthaltsort akzeptiert; durch 1m-L_Aeq, Umgebungsrauschen und Tonalität im Versuchsblatt dokumentieren. Numerische Grenzwerte mit Nutzer finalisieren.
- Nachrüstbar ohne Änderung von wasserführenden Elementen; staub-/servicefreundlich; modular austauschbare Lüfter.
- Ohne Internet oder Home Assistant selbstständig temperaturgeführt arbeiten; offline-konfigurierbar; Stromausfall und Sensorfehler sicher.
- Für jede Heizkörpervariante: CAD-Quelle, STEP/STL/3MF, Schaltplan, BOM mit konkreten SKUs, Endmontage, Mess-/Prüfakte.

## Explizite Nichtziele
Keine Eigenentwicklung oder Modifikation der 230-V-Seite, keine Gebäudeeingriffe, keine Heizungsmanipulation, keine Abdeckung von Heizkostenverteilern/Temperaturreglern, keine erfundenen Heizkosten- oder CO₂-Ersparnisse, keine ungenehmigten Bestellungen. Elektroheizkörper nicht Zielgruppe ohne Herstellerfreigabe.

## Drei Ansätze / Trade-offs
A. Freie Direktmontage (klassischer Booster): preiswert, einfache Lüfterwechsel, evtl. Bypass und Resonanzen.
B. **Plenum-/Schienenmodul** (vorläufig präferiert): verbesserte Anströmung der Konvektionskanäle möglich, mehr Material/Strömungswiderstand, erst durch Tests bestätigen.
C. Bodenpod mit Luftumlenkung: für geringe Einbauhöhe und schwierigem Befestigungsbereich, mehr Sichtbarkeit, Fußraum/Ansaugverschmutzung.
A und B für denselben Heizkörper als A/B-Mechanikkonzept testen. C nur als geometrischer Fallback.

## Modularität / Systemarchitektur
Schnittstelle 1: Heizkörper-Montageadapter (typabhängig) mit mechanischer Sicherheitsverriegelung; berührt kein unter Druck stehendes Bauteil. Schnittstelle 2: Luftmodul (typunabhängige Koppelgeometrie, auswechselbarer Fan-Träger, Schwingungsentkopplung). Schnittstelle 3: Niedervolt-Elektrik (12V DC zu 4-Pin-PWM-Lüftern; austauschbar, markierte Steckrichtung, Zugentlastung). Schnittstelle 4: Sensor- und Steuerungsmodul außerhalb heißer Bereiche. Elektronik v0 mit fertigem Temperaturregler, v1 optional ESP32 plus ESPHome.
Alle Schnittstellen als datierte CAD-/Schaltplan-Versionen, nicht durch stillschweigende Parameteränderungen.

## Konkretes Vorab-Risikomodell
- Heizkörper-Unterseite kann deutlich heißer als Raumluft sein: 40°C-limitierte Lüfter nur nach Temperaturen zulassen; nicht unbeaufsichtigt evaluieren.
- Eine 120-mm-Lüfterfläche passt häufig nicht ohne Überhang zu schmalen Radiatoren; Plenum und Querströmung können Lautstärke/Verlust erhöhen. Daher 80/92/120-mm-Kandidaten und echte lichte Maße.
- Bei Heizkostenverteilern ist einflussfreie Anordnung gesondert zu prüfen. Niemals gezielt Gerät anblasen/abschirmen, gegebenenfalls Vermieter/Messdienst kontaktieren.
- Magnete allein als Primärsicherung nicht annehmen. Print-Temperatur, Kriechen, Magnetwerkstoff/Temperatur, Kabelwege und Berührschutz nachweisen.
- Lüfterhersteller-Daten für Freiluft-Volumenstrom sind **keine** Kennlinie der installierten Einheit.

## Prüf-Gates
G0 Studien/Anforderungen -> G1 anonymes Aufmaß + reale Temperaturen -> G2 Varianten-/Lüfterkonzept -> G3 prüfbarer FreeCAD/STEP/STL + Niedervoltschaltplan/Steuerung -> G4 Prototyp -> G5 Thermik/Akustik/Elektrik/Befestigung im Versuch -> G6 bewachter Pilotbetrieb -> G7 weitere Radiatoren und Wartungsakte.
**Digital DONE** = alle Dateien technisch geprüft und ausführbar. **Physisch DONE** = nach realen Messungen und Montageprotokoll. Physisches DONE kann kein Chat allein erklären.

## Noch vom Nutzer einzuholen
Reale Geometrie und Heizungstyp, Fotos nur privat, Heizkreis/Heizkostenverteiler vorhanden?, akustische Priorität, Budgetobergrenze, Erlaubnis für eventuelle Montage. Bis dahin hypothetische Geometrie nur als Testszenario, nie als freigegebene Stückzahl oder Zuschnitt.
