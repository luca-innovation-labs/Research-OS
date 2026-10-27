# Smartphone-Reuse: Samsung DeX, alternative Linux-Systeme und GrapheneOS

**Status:** Hardwarealternative, noch nicht an einem konkreten Gerät getestet.

## Empfehlung 1: komplettes Galaxy mit Originalsoftware nutzen
Ein intaktes DeX-kompatibles Galaxy-Smartphone dient als Rechner, nicht als Spender für ein abgelöstes AMOLED-Panel. Das Telefon bleibt vollständig montiert, ist zugänglich, mechanisch ohne Druck auf den Akku befestigt und wird über einen getesteten USB-C-Hub (HDMI + USB-PD) angeschlossen.

```text
Samsung Galaxy (One UI + DeX)
  ├─ USB-C → DeX-kompatibler HDMI/PD-Hub → HDMI-Display hinter Spiegel
  ├─ USB-PD → zertifiziertes Netzteil; Batterie-Schutz sofern verfügbar
  └─ Wi-Fi / ggf. Ethernet → lokaler Dashboard-Server über gesicherten Kanal
```

### Modellabklärung
Samsung nennt HDMI-DeX u.a. für Galaxy S8–S26 sowie Note8/9/10/20 (Stand Oktober 2026). **Nicht jedes Samsung-Modell kann HDMI/DeX**; viele A-Modelle sind ungeeignet. Die Feature-Ausprägung variiert je nach Softwarestand. **DeX auf dem PC** ist etwas anderes als **DeX über HDMI**; moderne One-UI-Versionen haben für 'DeX on PC' Einschränkungen. Deshalb mit exakt vorhandenem Gerät, USB-Hub, Firmware und Display testen.

### Kiosk-Prozess
1. Systemupdates und Akkuzustand prüfen; Gerät ausschließlich für das Displayprojekt nutzen.
2. DeX über USB-C → HDMI starten; Browser im Vollbild öffnen, Demo-Profil `?profile=dex`.
3. Displaytimeout, automatische App-Wiederherstellung, WLAN-Reconnect und Boot-Verhalten messen; keine unsicheren ADB-Workarounds standardmäßig.
4. Akkuschutz/Ladegrenze im One-UI-Menü nutzen, wenn unterstützt. Das ist **kein garantierter Akkubypass**. Regelmäßig Temperatur, Akkuzustand und Schwellungszeichen kontrollieren. Kein fester Einbau ohne zugänglichen Wartungsweg.
5. Gerät und Netzteil nicht in luftdichte, warme oder feuchte Hohlräume einsetzen; geeignete Raumluft- und Brandschutzprüfung.

## Empfehlung 2: Linux auf oder unter Samsung
- **Termux / PRoot / Linux-Userspace:** Linux-Werkzeuge auf Android ohne vollständigen Betriebssystemwechsel; DeX bleibt möglich, aber Grafikleistung, Hintergrunddienste und USB-Zugriff können eingeschränkt sein.
- **postmarketOS:** Modellspezifische, experimentelle Ports existieren; eine verfügbare Geräteseite garantiert weder HDMI-Ausgabe, Funk- noch GPU- oder Energieverwaltungsunterstützung.
- **Custom ROMs:** Möglich nur für passende Modell-/Bootloader-Kombinationen. Samsung DeX sollte nach dem Ersetzen von One UI **nicht** vorausgesetzt werden. Sicherheitsupdates/verified boot/Knox und ggf. Garantie beeinflusst.

## GrapheneOS – klare Grenze
Offiziell unterstützte Geräte sind **Google Pixel**, keine Samsung-Galaxy-Smartphones. Für ein GrapheneOS-System ein konkret unterstütztes Pixel verwenden; Pixel 8 und neuer können nach Google-Dokumentation kabelgebunden über USB-C Videoinhalte ausgeben, aber konkrete GrapheneOS-/Desktop-Modus-/Dock-Kompatibilität **vor Kauf testen**. GrapheneOS ist kein DeX und lässt sich nicht durch normales Flashen auf Samsung übertragen.

## AMOLED-Panel aus Galaxy ausbauen?
Nur langfristiges Reverse-Engineering-Forschungsthema. Smartphone-Panels nutzen produktspezifische MIPI-DSI-Verbindungen, Steuer- und Spannungssequenzen; HDMI kann ohne kompatible Treiberplatine nicht unmittelbar angeschlossen werden. Mechanische Trennung kann Glas, Flexkabel und Akku schädigen. **Kein sinnvoller MVP-Pfad**.

## Kandidatenbewertung (geplante Labortests)
| Option | Vorläufige Eignung | Entscheidung |
|---|---|---|
| Galaxy S10/S20/S21 mit DeX + One UI | technisch attraktiv, sofern Hardware vorhanden | modellweise prüfen; EOL-Sicherheit beachten |
| Galaxy S8/S9 | billig, aber alte Software-/Sicherheitsstände | nur isolierter Labordemo, kein dauerhaft vernetzter Kiosk |
| Samsung unter postmarketOS | interessante Forschung | keine Produktionsannahme |
| Pixel 8+ / GrapheneOS | starke OS-Sicherheitsoption | Video-/Dock-/Kiosk-Tests erforderlich |
| Raspberry Pi 4/5 | gut dokumentiertes HDMI-Gerät | verlässlicher Referenzpfad |

## Abnahmetests
Exaktes Telefonmodell, SoC-Variante und Firmware erfassen; 30x Trennen/Neustecken; 5x Stromausfall und Reboot; 24 h niedrige + hohe Helligkeit; max. Temperatur im geschlossenen Prototyp; stabile Vollbilddarstellung, Ladegrenze, Akku kein Aufblähen, physischer Zugriff und Lade-/Update-Wartung.
