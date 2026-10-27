# CHAT 07 — 3D-Druck/Werkstoffe

## Mission
Datenblatt mit HDT, Temperaturkriechen, Einbaulast, Prüfkörper & Musterauftrag; weder PLA noch ASA blind annehmen.

## Pflichtkontext
Vor jeder Arbeit lesen: `projects/radiator-airflow/fleet/START-HERE.md`, `fleet/OPERATING-RULES.md`, `fleet/STATUS.md`, `docs/superpowers/specs/2026-10-27-airflow-system-design.md`, `docs/interface-contracts.md`.

## Owned outputs
`manufacturing/material-matrix.csv`, `manufacturing/print-orientation.md` (relative Pfade gelten unter `projects/radiator-airflow/`). Nur diese Dateien ändern, weitere nach Abstimmung mit CHAT 00.

## Startgate
G2. Vor G1 sind keine individuell passenden STL und vor G5 keine physisch bestätigten Leistungsdaten möglich. Wenn Blockade: aussagekräftiges Issue-/PR-Handoff statt generischer Füllarbeit.

## Qualitätskriterien
- Konkretes, reproduzierbares Deliverable: Druckfreigabe und Versuchsanleitung.
- Jede Behauptung durch Quelle oder Messung belegt, Datum und Unsicherheit genannt.
- Prüffälle vorhanden und dokumentiert oder ehrlich mit `NOT RUN` begründet.
- Übergabe an nächste Rolle mit exakt benannten Dateipfaden, Versions- und Sicherheitsblockern.
- Keine privaten Wohnungsdaten/Secrets ins öffentliche Repo, keine Nutzerkäufe, keine Änderungen an 230 V/Heizkörperhydraulik.

## Fertigmeldung
`STATUS | Deliverable | commit/PR | Tests + Beleg | Blocker | nächste abhängige Chatrolle`.
