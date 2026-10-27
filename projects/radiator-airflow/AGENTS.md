# AGENTS.md — AIRFLOW (verbindlich für alle Subagenten)

## GitHub scope: INNOVATION ONLY
- Ausschließlich **GitHub-Account `luca-innovation-labs`** und die GitHub-Verbindung **Innovation-labs** verwenden.
- Aktuelles einziges Schreibziel: **`luca-innovation-labs/Research-OS`**, Projektpfad `projects/radiator-airflow/`. Ein weiteres Innovation-Repo nur nach expliziter Freigabe.
- **`evidorworkspace-arch` (Evidor) ist tabu**: keine GitHub-Aufrufe für AIRFLOW dort, auch kein Lesen, Listen, Suchen, Schreiben, Löschen, Issues/PRs oder Migration dorthin. Das gilt selbst dann, wenn OAuth/PAT technisch Zugriff erlaubt.
- Andere Berechtigungen eines OAuth-Tokens sind **keine** Erlaubnis zur Verwendung für dieses Projekt.
- Bei unbekanntem GitHub-Login oder unklarem Ziel: **STOP**, nicht auf einen anderen Account ausweichen.
- Vor jeder GitHub-Aktion den authentifizierten Login und `owner/repo` gegen `fleet/connector-scope.json` prüfen. Bei Connector-Aufrufen immer explizit die Verbindung mit Login `luca-innovation-labs` wählen.
- Auf lokalen Maschinen vor Git-Writes: `python3 projects/radiator-airflow/fleet/scripts/git_scope_guard.py` aus Repo-Root. Fehlercode != 0 heißt STOP.
- Öffentliche Fremd-Repositories dürfen als öffentliches technisches Quellenmaterial gelesen werden; **keine** AIRFLOW-Artefakte dort ablegen.

## Credentials and true isolation
Eine Prompt- oder Skriptregel verhindert nicht alle denkbaren direkten GitHub-API-Aufrufe. Für einen externen autonom arbeitenden Agenten **separat auf Innovation/Research-OS begrenztes Fine-grained PAT oder GitHub-App-Installationstoken** benutzen. Kein accountübergreifendes persönliches PAT. Tokens niemals veröffentlichen oder loggen. Nicht ohne separaten Auftrag bestehende Evidor-Credentials ändern.

## Safety & review
Die normalen Projektgates gelten weiter. Research-OS ist öffentlich: keine Wohnungsfotos, Adressen, WLAN-Daten oder private Inventare committen. Vor PR/Commit Quellen und Tests angeben; keine unbeaufsichtigten Hardware- oder Bestellaktionen.
