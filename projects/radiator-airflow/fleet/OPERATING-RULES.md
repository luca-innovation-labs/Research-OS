# Mehragenten-Betriebsregeln

## Account-Isolation: bindend für Chat 00–15
`AGENTS.md` und `fleet/INNOVATION-ONLY.md` gelten für jeden Agenten, Unteragenten und Wiederholungslauf. Erlaubt: ausschließlich GitHub `luca-innovation-labs` über **Innovation-labs**, Repo `luca-innovation-labs/Research-OS`. Jegliche AIRFLOW-Aktion in Evidor ist untersagt, unabhängig von OAuth/PAT-Zugriff. Bei CLI-Writes zuvor `python3 projects/radiator-airflow/fleet/scripts/git_scope_guard.py` prüfen. Andere Berechtigungen sind keine Erlaubnis.

## Dateieigentum
00 Governance/Status/Release; 01 Research/literature; 02 measurement/profile; 03 Thermal & CFD; 04 fan selection; 05 CAD modules; 06 mechanical adapters; 07 FDM fabrication; 08 electrical and protection; 09 firmware; 10 smart home; 11 BOM; 12 print suppliers; 13 statistics/testing; 14 FMEA safety; 15 QA/release.
Kopplungen: 03+04 liefern Daten an 05, 05+06 an 07 und 12, 08 an 09, 09 an 10, 13/14/15 für Freigabe. Kein stilles Editieren fremder Owners. Querverweise als Issue-Kommentare oder datierte Dateien.

## Pull Request Contract
[ ] eindeutiges Issue mit reproduzierbarem Scope; [ ] nur eigene Dateien; [ ] Source-URLs/Datenblattdatum; [ ] Tests oder explizit fehlende Testumgebung; [ ] Sicherheitsauswirkung; [ ] verbleibende Blocker und nächste Chatrolle; [ ] QA/Review (nicht vom Ersteller).
Minimaler PR-Body: Why, Changes, Evidence, Tests, Risks, Remaining, Follow-up.

## Automatisierung
Chat-Workflows nur nach ausdrücklichem Nutzerstart. Ein gelegentlicher Controllerlauf darf GitHub prüfen, aber startet andere Sessions nicht automatisch. Auf VPS/Mac mögliche Agent-Jobs: nur mit Laufzeitbudget, API-Credentials außerhalb Repo, Stop-Befehl, Logs und Kostenlimits. Keine unbegrenzten Loop-Prozesse/heimliches Billing. Vollständig harte Repo-Isolation erfordert zusätzlich ein auf Innovation beschränktes Credential.

## Start-/Stop-Protokoll
Start: GitHub-Owner/Login prüfen, git origin und Issue/Gates lesen, isolierten Branch. Ende: Tests, PR, Commit-SHA, aktueller Blocker, nächste Rolle. Controller markiert DONE erst nachdem Acceptance Criteria mit tatsächlichen Artefakten belegt sind.
