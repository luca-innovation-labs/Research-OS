# AIRFLOW Fleet Quickstart (für 16 spätere Chats)

1. Lies `projects/radiator-airflow/README.md`, `docs/superpowers/specs/2026-10-27-airflow-system-design.md`, `docs/interface-contracts.md`, `docs/requirements-v1.md`.
2. Lies `fleet/STATUS.md`. Starte nur deine explizit zugewiesene Rolle aus `fleet/prompts/CHAT-XX.md`.
3. Ermittle den tatsächlichen Repo-Stand. Berücksichtige konkurrierende Commits und offene PRs; nie in den gleichen Owner-Dateien arbeiten wie andere Chats.
4. Ausgelieferte Texte, CAD und Firmware erhalten Revision, Evidenzgrad, Testausgabe und verbleibende Blocker. Wenn Messungen fehlen: `BLOCKED`, keine Annahmen als Fakten ausgeben.
5. Erstelle Branch `airflow/<chatnum>-<topic>`, PR mit Testreport. Keine Bestellung, keine Umbauten, keine neuen Secrets, keine privaten Wohnungsfotos in das öffentliche Research-OS.
6. Chat 00 koordiniert und testet Integration. Chat 14 Sicherheitsabnahme, Chat 15 unabhängig QA. Ein Chat nimmt niemals eigene Arbeit endgültig ab.
7. Stoppe bei Sicherheitsblockern; technische Alternativen zeigen. Physischer Abschluss erst nach realen Tests durch Nutzer.

## Parallelität/Wellen
Wave A (sofort, ohne Maße): 00,01,03,04,08 (Sicherheits- und Datenblatt-Recherche),11,12,13.
Wave B (nach Aufmaß): 02,05,06,07,08 (Schaltplan),09 (Control Design).
Wave C (nach G3 Review): 10,13 (Tests),14,15.
Maximal etwa 4–6 aktive Worker bei getrennten Dateien; Zahl ist operativer Vorschlag, keine garantierte ChatGPT-Hintergrundkapazität.

## Done Definition
`RESEARCHED` recherchiert; `SPECIFIED` Konstruktion spezifiziert; `CAD_READY` modelliert/validiert; `BENCH_PASS` Labor-/Tischtest bestanden; `PILOT_PASS` reale Wohnungspilotmessung bestanden; `ROLLOUT_DONE` alle Heizkörper und Dokumentation abgeschlossen. Niemals eine Gesamt-100%-Angabe ohne Zustand `ROLLOUT_DONE`.
