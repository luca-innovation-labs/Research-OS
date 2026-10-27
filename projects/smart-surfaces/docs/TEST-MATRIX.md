# Verifikation und Prüfmatrix

| ID | Test | Akzeptanzkriterium | Status |
|---|---|---|---|
| SW-01 | GET `/` und `/api/status` | HTTP 200, korrektes Format | automatisiert vorgesehen |
| SW-02 | Profile-Parameter | Nur `round`, `cabinet`, `tower`, `dex`; sonst round | manuell/automatisiert vorgesehen |
| SW-03 | Pfad-Traversal | Keine Dateien außerhalb der Allowlist erreichbar | automatisiert vorgesehen |
| SW-04 | CSP und Anti-Cache | CSP Header, keine Cloud-Anfragen | automatisiert vorgesehen |
| SW-05 | Mobil/DeX | 320 px bis 1920 px, gut lesbar | offen |
| SW-06 | Tastatur/Screenreader | Fokus, Rollen, kontrastreiche UI | offen |
| OPT-01 | MirroView-Muster | lesbar bei definierter Lux-Stufe | offen |
| OPT-02 | PC-LCD | ausreichende Transparenz und Homogenität | offen |
| HW-01 | 24h Temperaturtest | keine Überhitzung/ungeplanten Abschaltungen | offen |
| HW-02 | Neustart | definierter Zustand nach Spannungsverlust | offen |
| HW-03 | Galaxy-DeX | Android/One UI/Hub/HDMI kompatibel | offen |
| SAFE-01 | Glas-/Wandstatik | schriftliche Freigabe vor Hängen | offen |
| SAFE-02 | Elektro/Bad | Fachprüfung nach Standort | offen |

**Hinweis:** Entwicklungs-Unit-Tests ersetzen keine Hardware- oder Elektrosicherheitsabnahme.
