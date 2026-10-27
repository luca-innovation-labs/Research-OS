# AIRFLOW: Innovation-only GitHub-Policy

**Einziger Projekt-Account:** `luca-innovation-labs` (Connector-Anzeigename `Innovation-labs`).
**Einzig freigegebenes Repository für dieses Projekt:** `luca-innovation-labs/Research-OS`.
**Gesperrter Account:** `evidorworkspace-arch` — Evidor.

Vor **jeder** GitHub-Interaktion Repo-Owner/Login kontrollieren. Niemals einen Zugriff auf Evidor für AIRFLOW verwenden, selbst wenn OAuth oder PAT Zugang erlauben. Die Gate-Regeln aus `AGENTS.md` gelten für Chat 00–15, alle Subagenten, den Orchestrator und zukünftige Fortsetzungen. Nur öffentliche fremde GitHub-Repositories als *reine Technikreferenz* lesen.

### Werkzeugwahl
- **GitHub Connector/MCP:** verbindlich Kontoverbindung **Innovation-labs** wählen, deren authentifizierter Nutzer `luca-innovation-labs` lautet. Alle Schreibaufrufe mit `repository_full_name="luca-innovation-labs/Research-OS"`. Bei falscher verknüpfter Identität aufhören.
- **GitHub CLI / Remote Devices:** `git remote get-url origin` und `gh api user --jq .login` müssen zusammen erfolgreich geprüft werden, siehe `fleet/scripts/git_scope_guard.py`. Ist `gh` nicht verfügbar oder das Login falsch, nicht schreiben. Die echte Git-Credential-Quelle zusätzlich technisch auf Innovation einschränken.
- **Externer Agent Runner:** eigenes kurzlebiges GitHub-App-Installationstoken, Repoauswahl nur Innovation/Research-OS, minimaler Berechtigungsumfang. Kein gemeinsames PAT mit Evidor. Keine Änderung bestehender Kontoverbindungen ohne ausdrückliche Freigabe.

### Grenzen
Die Datei `connector-scope.json`, `AGENTS.md`, CLI-Preflight und CI-Test sind **Defense in Depth**, kein globaler Entzug existierender GitHub-Berechtigungen. Vollständig harte Isolation gibt es erst mit serverseitig auf Innovation beschränktem Credential. Andere Accountzugriffe dürfen unangetastet bleiben, sollen aber von AIRFLOW nicht benutzt werden.
