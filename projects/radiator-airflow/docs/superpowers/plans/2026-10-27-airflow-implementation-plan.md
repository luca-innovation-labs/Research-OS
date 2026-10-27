# AIRFLOW Modular Booster Implementation Plan (Entwurf)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Entwurf, Simulation/Validierung, Prototyp und bedarfsgerechte Kleinserie modularer 12-V-Heizkörperlüfter, angepasst an anonymisierte reale Aufmaßdaten.

**Architecture:** FreeCAD-parametrisierte S/M-Lüfter-/Kanal-/Halter-Baugruppen mit markiertem Fan-/Duct-Interface; elektrische 12V-Module mit PWM- und tachometrischer Steuerung; messdatenbasierte Freigabegates. Fallback: fertig gekaufter 12-V-Temperaturregler, Smart Home optional.

**Tech Stack:** FreeCAD Python, STEP + 3MF/STL, FDM ASA/PETG erst nach Temperaturprüfung, ESP32/ESPHome optional, CSV + Python-Pytest für Datencheck, GitHub Issues/PRs.

**Spec:** `docs/superpowers/specs/2026-10-27-airflow-system-design.md`

## Global Constraints
- Eigentümer luca-innovation-labs; niemals Evidor. Research-OS ist öffentlich, keine Adresse/Wohnungsfotos/Sicherheitsdaten.
- Keine netzspannungsführende Eigenkonstruktion; einzig geprüftes externes 12-V-Steckernetzteil.
- Elektroheizkörper ausgeschlossen bis Herstellerfreigabe. Keine Bohrungen/Beschädigungen an Heizkörper oder Leitungen.
- Nie ECO-40°C-Modelle blind an heißen Heizkörpern einsetzen.
- Keine CAD-Fertigungsfreigabe ohne echte Maße und Kontakttemperatur.
- Keine externen Bestellungen/Veröffentlichungen im Namen des Nutzers ohne explizites Okay.
- Quelle, Datum, Bauteilrevision und reproduzierbarer Test gehören zu jedem technischen Claim.
- Nicht alle Agenten arbeiten parallel an derselben Datei. Eigene Issue/Branch und QA vor Merge.

## Review Focus (technische Fehlerbilder -> konkrete Tests)
1. Zu geringe Bodenfreiheit: CAD-Validierung verweigert Einbaukonfiguration, zeigt minimale Freihöhe inkl. Servicebedarf (Task 2/3).
2. 12-V-PSU unterdimensioniert/Anlaufstrom: Power-Budget-Test prüft Hersteller-Maxima plus Derating und Anlaufmessung (Task 5).
3. Temperaturfühler lose/fehlerhaft: State-Machine sperrt unplausible Eingänge und startet nicht unbemerkt (Task 6).
4. Heizkostenverteiler/elektrischer Heizkörper erkannt: Montagefreigabe verweigert, Unklarheit an Betreiber adressieren (Task 1/3).
5. Luftstrom-Bonus unter Messrauschen: Messauswertung gibt `inconclusive`, keinen Erfolg (Task 8).

---

### Task 1: Aufmaßmodell & Auschlussregeln (CHAT-02)
**Files:** Create `engineering/radiator_profile.schema.json`, `engineering/validate_profile.py`, `tests/test_profiles.py`.
**Interfaces:** `RadiatorProfile` Felder: radiator_id, heater_kind, model_type, radiator_dimensions_mm, free_clearances_mm, bottom_opening_mm, obstacles, surface_hot_C, measurement_confidence.
- [ ] Negativtests für missing dims, Nullwerte, Elektroheizkörper, Heizkostenverteiler nahe Strömungspfad definieren.
- [ ] Validierungs-API implementieren: `validate_profile(profile)-> (ok, blockers, warnings)`.
- [ ] Schema gegen gemessene anonymisierte Profile und Test-Fakes prüfen.
- [ ] Status im Issue, commit und eigener Review dokumentieren.

### Task 2: Lüfterdatenbank + Auswahlheuristik (CHAT-04)
**Files:** Create `engineering/fans.csv`, `engineering/fan_selection.py`, `tests/test_fan_selection.py`.
**Interfaces:** `FanSpec`: sku, size_mm, depth_mm, rpm_curve, pq_curve, rated_max_ambient_C, max_A, acoustic_reference, source_url, verified_at; `select_candidates(profile, fan_db)`.
- [ ] Ablehnung zu heißer oder geometrisch nicht passender Fans testen.
- [ ] Datiertes Herstellerdatenblatt und exakte Variante erfassen.
- [ ] Kandidaten mit QA-Hinweis auf fehlende PQ/Startmessung liefern.
- [ ] Datenqualität prüfen, nicht Freiluftvolumenstrom als Einbauwert setzen.

### Task 3: Parametrische FreeCAD-Baugruppen (CHAT-05/06)
**Files:** Create `cad/airflow/geometry.py`, `cad/airflow/interfaces.json`, `cad/README.md`, `tests/test_cad_constraints.py`.
**Interfaces:** `build_module(profile, fan, variant)-> BuildResult` erzeugt natives FCStd, STEP, STL (tesselliert, 3MF optional).
- [ ] Geometrie-Tests für negative Wandstärken, Schraubenrandabstand, Kollision, Parameterrandfälle erstellen.
- [ ] Direct-Clip A, Plenum B und POD C als unabhängige Bausätze modellieren; noch kein druckreifes STL bei ungemessenem Gerät.
- [ ] Fanlochbild als Datenblattmaß parametrieren, Service- & Werkzeugzugang erhalten.
- [ ] CAD-Dokument auf Baugruppenzusammenbau, Volumenkörpervalidität und Export prüfen.

### Task 4: Druck / FMEA der Werkstoffe (CHAT-07/14)
**Files:** Create `manufacturing/material-matrix.csv`, `manufacturing/print-orientation.md`, `tests/test_printability.py`.
- [ ] Kandidatenmaterialspezifikationen (HDT/UL94 nur belegbar) sowie Verformungsrisiken erfassen.
- [ ] Prüfkörper mit realistischer Schrauben-/Cliplast konstruieren und dokumentieren.
- [ ] Nach thermischen Daten und Kriechversuch Fertigungsmaterial, Layerorientierung, Toleranzen freigeben.
- [ ] Drei Dienstleister auf demselben 3MF/STL-Muster und gleicher ASA/PETG-Spezifikation vergleichen.

### Task 5: Niedervolt-Elektrik/Schutz (CHAT-08)
**Files:** Create `electronics/diagram.pdf`, `electronics/power-budget.csv`, `electronics/connector-pinout.md`, `tests/test_power_budget.py`.
- [ ] Negativfälle Überschreiten von Dauerstrom, Einschaltstrom, Leitungstemperatur und Verpolung definieren.
- [ ] Zertifiziertes externes 12-V-Netzteil, geeignete Sicherung, separate Niedervolt-Teile spezifizieren.
- [ ] 25-kHz-open-drain-PWM, getrennter Tacho-Pullup, 12-V/3,3-V-Pegel und USB-Backfeed prüfen.
- [ ] unabhängige elektrische Sicherheitsprüfung vor Zusammenbau.

### Task 6: Temperaturregelung/optionales ESPHome (CHAT-09/10)
**Files:** Create `firmware/airflow.yaml`, `firmware/control_contract.md`, `tests/test_control_states.py`.
**Interfaces:** OFF/WAIT_WARM/PRESPIN/RUN/COOLDOWN/SENSOR_FAULT/OVER_TEMP; Start- und Aus-Schwellen konfigurierbar, Hysterese obligatorisch.
- [ ] Tests für fehlerhafte Sensorwerte, Startimpuls, Rotorstopp, WiFi-Ausfall, Spannungswiederkehr definieren.
- [ ] Erst offlinefähiges autonomes Steuermodul, danach Home-Assistant-Integration.
- [ ] Firmware dry-run/Konfig-Validierung und reale 12-V-Tischtests; ESPHome-Version pinnen.
- [ ] Kein ungefragtes öffentliches WLAN/OTA-Open-AP mit Defaultpasswort.

### Task 7: Lieferanten, BOM und RFQ (CHAT-11/12)
**Files:** Create `manufacturing/bom-v1.csv`, `manufacturing/quote-comparison.csv`, `manufacturing/rfq.md`.
- [ ] Mindestens 3 Druck-Dienstleister mit gleicher Revision, gleicher Menge, gleichem Material vergleichen.
- [ ] Komponenten nur mit Datenblatt, aktueller verfügbarer SKU und Preis inkl. Versand aufnehmen.
- [ ] Fehlende Preisdaten als unknown, nicht 0 EUR behandeln.
- [ ] Bestellentscheidung als separaten Nutzer-Gate protokollieren.

### Task 8: Pilot-Messung und Statistik (CHAT-13/15)
**Files:** Create `tests/protocols/ab-a-test.md`, `tests/data/experiment-template.csv`, `tests/analysis/compare_trials.py`.
**Interfaces:** `compare_trials(control, booster)-> {effect, uncertainty, verdict}` mit verdict = `better|unchanged|inconclusive`.
- [ ] Versuchsauswertung bei nicht vergleichbaren Außentemperaturen/Heizkurven = inconclusive testen.
- [ ] Messsensoren kalibrieren bzw. Messunsicherheiten erfassen.
- [ ] A/B/A, gleiche Heizleistungseinstellungen, gleiche Sensorpositionen und Testreplikate soweit praktisch möglich.
- [ ] physische Sicherheitsprüfung und protokollierte Abnahme vor unbeaufsichtigtem Betrieb.

### Task 9: Montage- und Serienfreigabe (CHAT-00/15)
**Files:** Create `release/INSTALL.md`, `release/QA.md`, `release/MAINTENANCE.md`, `release/traceability.csv`.
- [ ] Nur geprüfte Konfigurationen mit radiator_id und exakter Stückliste freigeben.
- [ ] Schritt-für-Schritt-Montage mit Kabelzugentlastung, Sicherungen, Reinigungszugang und Abschaltoption.
- [ ] Nutzerprotokoll für echten Aufbau/Tests und Rückmeldeschleife dokumentieren.
- [ ] Digital DONE, Physisch DONE und BLOCKED getrennt ausweisen.

## Handoff
Gates vor Fortschrittsmeldungen nach `fleet/STATUS.md`; alle zugehörigen Prompts unter `fleet/prompts/`; neue Issues `[AIRFLOW]` und branches `airflow/<domain>/<slug>`. Geometrie- und Elektronik-Freigabe niemals ohne fachliche Review und Nutzermessung.
