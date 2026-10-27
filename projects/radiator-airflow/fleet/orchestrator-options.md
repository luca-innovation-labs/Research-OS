# AIRFLOW Orchestrator: betreute Chat-Flotte und optionale Agent-Runtime

## Ziel / klare technische Grenze
16 unabhängige Aufgabenbereiche, kontrollierte Übergabe, Wiederaufnahme statt Wiederholung. **Das Anlegen von GitHub-Issues startet keine ChatGPT-Chats und erzeugt keinen automatischen Hintergrundlebenszyklus.** Autonomes Wiederanstoßen benötigt explizit eingerichtete und freigegebene externe Agent-Laufzeit oder manuelle Chat-Fortsetzung.

## Modus A – ChatGPT-Flotte manuell gestartet (sofort realisierbar)
- Nutzer eröffnet Chat 00 und 4–6 Fachchats per `fleet/prompts/CHAT-XX.md`, weist jeweils eine Issue-URL zu.
- Fachchat prüft Gate und liest GitHub-Issue, bearbeitet ein abgeschlossenes, überprüfbares Teilpaket, schiebt Commit/PR.
- Steuerzentrale wertet Reviews/Gates aus und erklärt die nächste Wave.
- Fortsetzung durch Nutzeraufruf (z. B. „weiter“) oder einen tatsächlich eingerichteten zulässigen Automationslauf, sofern dieser die erforderlichen Connectorrechte besitzt. Keine Behauptung eines automatischen Relaunchs.

## Modus B – externe Agent-Orchestrierung auf autorisierter Maschine (noch NICHT installiert/gestartet)
Vorbedingung: Nutzer wählt Laufzeit, Model/API-Verbindung, Budget, Code-Ausführungsrechte und Abbruchkontrollen. Erst dann auf Testbranch entwickeln.
```text
read GitHub issue/status -> validate gate / ACL / budget / time
 -> reserve exactly one issue and branch
 -> spawn bounded worker through an actual authenticated agent runtime
 -> collect commit, test results, exit status, cost
 -> independent reviewer -> open PR -> human gate when required
 -> update issue/status -> next eligible bounded worker
```
Maximal 4–6 gleichzeitige Worker als Startannahme, hohe CPU-Parallelität ist nicht mit zusätzlicher Modellkapazität gleichzusetzen. Eigene API-Kosten können entstehen. Nie automatisch ohne Budgetdeckel.

## Schutzmaßnahmen
- `max_concurrent_workers` default 4, `max_attempts_per_issue` 3, `max_model_spend_eur` vor Ausführung vom Nutzer einzutragen (unbekannt = kein API-Job).
- Stop/kill-Griff, Job-ID, Audit-Log, Timeout, pausierbar. Keine Dauerschleife ohne beobachtbare Grenzen.
- Agenten keine Live-Bestellungen, kein Verschieben privater Daten, kein 230-V-Eingriff, kein verdeckter Passwortzugriff.
- Incomplete/error -> BLOCKED, begründeter nächster Schritt, nicht automatisch „DONE“.
- Nur ein Write-Owner pro Issue/Datei. Main-Merges erst nach Review; physische Freigaben nur nach Nutzer-Messung.

## Exakte Priorisierung
Wave A (ohne Heizkörpermaße): 01,03,04,08,11,12,13,14; CHAT 00 koordiniert.
Wave B (nach gültigem Aufmaß): 02,05,06,07; 08/09 fortführen.
Wave C (nach geprüfter Elektrik und CAD): 09,10,13,14,15.
Wave D (Prototyp real gebaut): 13,14,15 Abnahme, dann Haus-Rollout.
Fortschritt ist nach Abnahmekriterien zu melden, nicht nach Anzahl Agentenantworten.

## Übergabebericht Format
```
ISSUE: #__
STATUS: TODO/IN_PROGRESS/BLOCKED_USER/BLOCKED_DEPENDENCY/REVIEW/DONE
BRANCH: airflow/xx-scope
COMMIT/PR: URL + vollständiger SHA
DELIVERABLES: Pfade
TESTS: Befehl, Ergebnis oder NOT_RUN + Grund
SOURCES: technische Primärlinks und Datum
RISKS: bestehende Sicherheits-/Datenblocker
NEXT: Agent + Eingabe + erforderliches Gate
```

## Migration eines späteren Projektordners
Falls der Nutzer einen eigenen Innovation-Projektordner bereitstellt, Dateien/Branches erst nach Besitz- und Privacy-Prüfung übernehmen. Keine Verdoppelung in Evidor. Öffentliche Research-OS-Dokumente bleiben frei von Adressen/Fotos/privaten Messinformationen.
