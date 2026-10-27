# Technische Schnittstellen zwischen Chats (v0.1)

## Mechanical API
`radiator_profile`: Einheiten mm/°C; anonymisierte ID; Typ; Breite/Höhe/Tiefe; Bodenfreiheit; Wandfreiheit; Unterseitenöffnung; freier Ausströmquerschnitt; Hindernisse; maximale Oberflächentemperatur.
`FanSpec`: SKU, Außenrahmen L×B×H, Schraublochkreis/Abstand, Kabelausgang, min.PWM Drehzahl, maximale Umgebungstemperatur, Kennfeld/Q-p, elektrische Daten.
`AirModule`: `variant` A/B/C, `fan_spec_id`, `adapter_interface_revision`, `mounting_safety_revision`, `print_material_sku`.
Durchmesser, Clips und Magnettaschen sind parametrisch; keine festen Defaultwerte als universeller Fertigungsentwurf. Nach Anpassung Verifikation von passendem Einbauraum, Sockel/Sensor/Heizkostenverteiler und Servicefreiraum.

## Electrical API
Externes geprüftes Netzteil mit 12V, Polarität eindeutig. 4-pin DC-Fan: GND, +12V, Tach, PWM laut konkretem Modell. PWM-Kandidat 25 kHz Open-Drain mit geeigneter Schaltstufe; TACH getrennt, nur 3.3V-kompatibler Pullup am MCU. Ein freier Fan-PWM-Pin der MCU ist kein freigegebener direkt verdrahteter Ausgang. Netzteilströme inkl. Fan-Start/Controller/derating nach Test. Mechanische Schutzabdeckung und Kabelzugentlastung.

## Firmware API (technische Zustandsverträge)
`FanControlInput` = `{radiator_C, ambient_C?, fan_rpm?, power_ok, config}`. 
`FanControlOutput` = `{state, command_pct, error_reason?}`.
Konfigurierbar: `on_C`, `off_C`, `start_pulse_pct`, `start_pulse_seconds`, `min_run_pct`, `cooldown_seconds`, `max_board_C`, `enable`.
Invariante: `on_C > off_C`; `max_board_C` darf nicht als Ersatz für echte Übertemperatursicherung missverstanden werden. Bei Sensorverlust keine ungeprüfte starke Dauerstufe. RPM-Timeout nur wenn tach unterstützt. Kopplung Home Assistant optional.

## GitHub API der Flotte
Task -> eigenes GitHub Issue (Titelprefix `[AIRFLOW]`), Branch `airflow/<domain>/<slug>`, eigenes Owner-File. Ergebnisse nur mit Version, Quellen, Tests und Abhängigkeiten. Keine Änderung am root-Research-OS-Index ohne PR. Controller 00 macht Integrationschecks; QA 14/15 darf nicht eigene Sicherheitsbehauptungen absegnen.
