# AIRFLOW — Modulare Heizkörper-Booster (Research & Fleet Handoff)

Stand: 2026-10-27 · Phase: Recherche/Konzept · **Noch kein Prototyp, keine Bestellungen, keine validierten CAD- oder Firmware-Artefakte.**

## Mission
Modulare, leise, kostensensible, wartbare und an reale Heizkörper anpassbare 12-V-Lüftermodule zur Verbesserung der erzwungenen Konvektion. Geplant sind parametrische 3D-Druckteile, optional autarke Thermostatsteuerung oder ESP32/ESPHome, klare Sicherheitsschranken und quantitative A/B-Tests.

## Wichtig: Eigentümer/Repo-Routing
**Projektinhaber und kanonischer Arbeitsort: GitHub `luca-innovation-labs` (Innovation), derzeit im Repository `Research-OS` unter `projects/radiator-airflow/`.** Evidor ist explizit kein Projektziel. Ein eigenständiges Repository unter demselben Innovation-Account kann bei Bedarf später angelegt werden. **Das derzeitige Research-OS-Repository ist öffentlich: keine privaten Adressen, Wohnungsfotos, personenbezogenen Aufmaßdaten, API-Secrets oder WLAN-Zugangsdaten einchecken.**

## Sofortige Links
- [Wissenschaft und externe Referenzen](research/2026-10-27-sources.md)
- [Designentscheidungen und Varianten](docs/architecture.md)
- [Sicherheit und Grenzen](docs/safety-and-failure-modes.md)
- [Messdatenbedarf](docs/measurement-intake.md)
- [Experiment und Akzeptanz](docs/test-plan.md)
- [Komponenten/BOM](docs/bom-and-sourcing.md)
- [Technik-/Steuerungsentwurf](docs/control-and-electronics.md)
- [20-Chat-Flotte: Rollen und Handoffs](fleet/20-roles.md)
- [Roadmap und Entscheidungslog](docs/roadmap-and-decisions.md)
- [Vorlage Aufmaß, anonymisiert](data/radiator-template.csv)
- [Vorlage Stückliste](data/bom-template.csv)

## Statusgates
G0 Recherche (begonnen) -> G1 Heizkörperinventar & Temperaturmessungen -> G2 Auswahl zwei geometrischer Konzepte -> G3 fertigungsgerechtes CAD & 12-V-Controller-Review -> G4 Prototypdruck -> G5 Sicherungs-/Akustik-/Thermiktests -> G6 Pilotinstallation -> G7 skalierter Rollout. **Nichts überspringen.**

## Evidenzgrade
FACT = externe Primärquelle, VERIFIED = reproduzierter eigener Test, HYPOTHESIS = plausibel aber ungetestet, DECISION = vorläufige Designentscheidung. Preise, Wirkungsgrad, Druckfestigkeit und Geräusch werden ausdrücklich nicht erfunden.

## Arbeitsauftrag
20 Chat-Rollen starten erst auf ausdrücklichen Nutzerwunsch. Bis dahin ist dies ein vorbereiteter, versionierter Arbeitsstand; kein Hintergrundprozess oder Agent läuft hierdurch automatisch.
