# Roadmap / Entscheidungsprotokoll

## Entscheidungsstand am 2026-10-27
- D-001: Research-first; noch kein einsatzbereites Gerät, kein CAD validiert.
- D-002: 12-V-SELV-Versorgung und geprüfter Netzadapter; keine AC-Eigenkonstruktion.
- D-003: Plattenradiatoren als erster Zieltyp; Elektroheizkörper bis Herstellerfreigabe ausgeschlossen.
- D-004: Konzeptvergleich zwischen Direct-Clip und Shrouded-Rail; Floor-Pod als Fallback.
- D-005: ESPHome nur optional, autarker temperaturabhängiger Betrieb ist Pflicht.
- D-006: Erste Pilotinstallation mit Ausgangsmessung; keine Heizkostenversprechen.
- D-007: GitHub Research-OS/Innovation ist nur temporärer *öffentlicher* Forschungsstand ohne persönliche Wohnungsinformationen; endgültiges privates eigenes Repo/Account noch festzulegen. Evidor ausdrücklich nicht als Ziel.

## Work packages
G0 Research: Primärstudien, Prior-Art/Lizenz, technische Datenblätter, Risiken -> Quellenregister.
G1 Geometrie: echte Maße, Fotos (privat), höchste Heizkörpertemperatur -> ausgefülltes, freigegebenes Aufmaß.
G2 Konzept: Platzierung, Basisquerschnitt, zwei übertragbare CAD-Kandidaten -> Variantenentscheid mit Begründung.
G3 Engineering: parametrisches CAD, Druck-/Montageplan, Elektronikschema & Firmwareplan -> Review.
G4 Prototype: eine Einheit, Montageanleitung, Messbereitschaft -> Bauakte.
G5 Verify: Sicherheit, Temperatur, Geräusche, Leistung und Störfälle -> Validierungsbericht.
G6 Pilot: reales Gerät in Nutzung mit regelmäßiger Kontrolle -> Freigabe.
G7 Scale: Geometrievarianten, BOM, 20-Chat QA-Abnahme, fortlaufender Wartungsprozess.

## Kritische Unbekannte
Heizkörpertypen und -maße, Temperaturprofil, Nutzerspezifische Priorität (Preis/Lärm), Werkstoff-/Druckereignung, Heizsystem, Steckdosenlage. Bis dahin keine millimetergenaue Teilefreigabe.

## Übergabe
Die Datei fleet/20-roles.md definiert Rollen, Abhängigkeiten und Übergabekriterien. Aufruf der 20 Chats muss aktiv von Nutzer/Orchestrator initiiert werden; alleinige Ablage hier startet keine Agenten.
