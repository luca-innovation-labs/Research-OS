# CHAT 05 — FreeCAD Parametrik

## Mission
Vor G1 nur Schnittstellen-/Parametermodell planen; dann Baugruppen A/B in FreeCAD, Volumenkörper/STEP/STL validieren.

## Pflichtkontext
Vor jeder Arbeit lesen: `projects/radiator-airflow/fleet/START-HERE.md`, `fleet/OPERATING-RULES.md`, `fleet/STATUS.md`, `docs/superpowers/specs/2026-10-27-airflow-system-design.md`, `docs/interface-contracts.md`.

## Owned outputs
`cad/airflow/geometry.py`, `cad/README.md` (relative Pfade gelten unter `projects/radiator-airflow/`). Nur diese Dateien ändern, weitere nach Abstimmung mit CHAT 00.

## Startgate
G2. Vor G1 sind keine individuell passenden STL und vor G5 keine physisch bestätigten Leistungsdaten möglich. Wenn Blockade: aussagekräftiges Issue-/PR-Handoff statt generischer Füllarbeit.

## Qualitätskriterien
- Konkretes, reproduzierbares Deliverable: FCStd, STEP, STL/3MF, Längen-/Kollisionscheck.
- Jede Behauptung durch Quelle oder Messung belegt, Datum und Unsicherheit genannt.
- Prüffälle vorhanden und dokumentiert oder ehrlich mit `NOT RUN` begründet.
- Übergabe an nächste Rolle mit exakt benannten Dateipfaden, Versions- und Sicherheitsblockern.
- Keine privaten Wohnungsdaten/Secrets ins öffentliche Repo, keine Nutzerkäufe, keine Änderungen an 230 V/Heizkörperhydraulik.

## Fertigmeldung
`STATUS | Deliverable | commit/PR | Tests + Beleg | Blocker | nächste abhängige Chatrolle`.
