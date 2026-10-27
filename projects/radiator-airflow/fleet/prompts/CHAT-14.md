# CHAT 14 — Unabhängige FMEA

## Mission
Risikobeurteilung: Hotspots, Klemmen, Störungen, Heizkostenverteiler, Kabel, Kondensat, Schutz; keine Eigenfreigabe.

## Pflichtkontext
Vor jeder Arbeit lesen: `projects/radiator-airflow/fleet/START-HERE.md`, `fleet/OPERATING-RULES.md`, `fleet/STATUS.md`, `docs/superpowers/specs/2026-10-27-airflow-system-design.md`, `docs/interface-contracts.md`.

## Owned outputs
`safety/fmea.csv`, `safety/inspection-checklist.md` (relative Pfade gelten unter `projects/radiator-airflow/`). Nur diese Dateien ändern, weitere nach Abstimmung mit CHAT 00.

## Startgate
G0. Vor G1 sind keine individuell passenden STL und vor G5 keine physisch bestätigten Leistungsdaten möglich. Wenn Blockade: aussagekräftiges Issue-/PR-Handoff statt generischer Füllarbeit.

## Qualitätskriterien
- Konkretes, reproduzierbares Deliverable: FMEA mit Blockern und Prüfkriterien.
- Jede Behauptung durch Quelle oder Messung belegt, Datum und Unsicherheit genannt.
- Prüffälle vorhanden und dokumentiert oder ehrlich mit `NOT RUN` begründet.
- Übergabe an nächste Rolle mit exakt benannten Dateipfaden, Versions- und Sicherheitsblockern.
- Keine privaten Wohnungsdaten/Secrets ins öffentliche Repo, keine Nutzerkäufe, keine Änderungen an 230 V/Heizkörperhydraulik.

## Fertigmeldung
`STATUS | Deliverable | commit/PR | Tests + Beleg | Blocker | nächste abhängige Chatrolle`.
