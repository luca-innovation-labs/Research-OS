# Sicherheitskonzept – Vorprüfung, KEINE elektrische Freigabe

## Kritische Ausschlüsse
- **Keine eigenen Arbeiten an offenen Netzspannungsnetzteilen** oder CRT-Hochspannungsanlagen. Auch ausgeschaltete Monitor-Netzteile enthalten u.U. gefährlich geladene Kondensatoren. Kein unsicherer Universal-Demontageleitfaden.
- **Kein Ausbau oder Bypass von Lithium-Akkus** im Rahmen des MVP. Alte, beschädigte oder aufgeblähte Geräte dürfen nicht in einem Gehäuse weiterbetrieben werden.
- **Keine DIY-Netzspannungsinstallation im Badezimmer.** Elektriker:in muss Schutzbereiche, RCD, IP-Einstufung, Verlegung und Anschlüsse am konkreten Standort nach den anzuwendenden VDE-Regeln beurteilen; 12/24V ist keine pauschale Freigabe.
- **Kein belastbares Spiegelglas auf bloßen 3D-Druck-Rastnasen.** Montage, Wandeignung, Schrauben, Ausbruchkanten, thermische Dehnung durch Fachbetrieb qualifizieren.
- **Keine innenliegenden lose befestigten Stromkabel** am PC-Netzteil; PC-Lüftung frei halten.

## Risiken & Gegenmaßnahmen
| Risiko | Gegenmaßnahme | Nachweis |
|---|---|---|
| Stromschlag beim Monitorumbau | Fachkundige Sichtung/Arbeiten im sicheren Zustand; gekapselte, zertifizierte Niederspannungslösung | Baugruppenliste + Elektroprüfung |
| Wärme / Brand | ausreichende Luftkanäle, Übertemperaturabschaltung, Netzteilreserve | Thermometerprotokoll 24 h im worst case |
| Kondensat / Spritzwasser | Montageort prüfen, IP-Schutz planen, Schutzbereiche einhalten | Abnahme Elektrik/Feuchte |
| Glasausfall | zulässige Glasbearbeitung, tragfähige Halter, Sicherheitsglasfrage | Mechanikreview |
| Akkuüberhitzung bei DeX | intaktes Telefon, Batterie-Schutz, Lade-/Entlade-Test, Wartungsöffnung | Thermolog + Sichtprüfung |
| OLED-Einbrennen | dynamische Anzeige, automatische Abdunklung und Schlafmodus | Wochen-/Monatsvergleich |
| Privatsphäre | keine Kamera/Voice im Standard, auth-gesteuertes Gateway | Threat-model-review |
| Nicht ausreichende Lesbarkeit | Probestück, Lux-/Kontrasttests über Tag/Nacht | Optikprotokoll |

## Projekt-Gates
**G0** (vor Bestellung): Maße/BoM/Controller bestätigt. **G1** (vor Ausbau): Sicherheitsfreigabe der Spenderhardware. **G2** (vor Integration): Glas und Halterung geprüft. **G3** (vor Dauereinsatz): Wärme, Elektrik, Datenschutz und Wiederanlauf dokumentiert.
