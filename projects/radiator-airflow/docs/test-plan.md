# Testkonzept V0–V1, preregistriert

## Fragestellungen
(1) Mehr Wärmeübertragung an Raumluft bei vergleichbarem Betriebszustand? (2) Kürzere Zeit bis Zieltemperatur? (3) Angemessene Geräusche, Verbrauch und Sicherheit? (4) Ist eine niedrigere Vorlauftemperatur bei gleichem Komfort realistisch?

## Aufbau/Instrumente
Log von Raumluft in 2+ Positionen (konstant gleiche Sensorpositionen), Radiator-Vorlauf/-Rücklauf per angeklemmten und isolierten Temperaturfühlern, Oberflächentemperatur, Lufttemperatur an Ein-/Austritt, Netzteilwirkleistung mit Leistungsmessgerät, Drehzahl/Tach, akustischer Pegel am definierten Messplatz. Wenn ein sauberer Wärmestromvergleich gewünscht wird: kalibrierter Wassermassenstrom plus Vor- und Rücklauftemperatur (Q = m_dot * c_p * ΔT) und definierter stationärer Zustand. Differenztemperaturen ohne Durchfluss sind **kein Wärmestromnachweis**.

## Versuchsdesign
- Sicherheit/Material: Vorab unter thermischer Höchstlast, ohne persönlichen Betrieb.
- A/B/A alternierend, gleiche Thermostat-/Heizkurveneinstellung, Fenster/ Türen/ Möbelposition, dokumentierte Außenbedingungen. Anfangstemperatur und Wärmespeicherung möglichst vergleichbar halten.
- Fan OFF, 25%, 40%, 60% PWM, maximale begründbare Leisestufe; drei gleiche Wiederholungen nach Möglichkeit.
- Akustik: Smartphone nur relativer Trend, besser geeignetes Schallpegelmessgerät, dB(A) bei festem Abstand; Tonalität subjektiv protokollieren.
- Steuerung: Kaltstart, Stromwiederkehr, Sensorsprung/Unterbrechung, blockierte Rotoren, WiFi-Ausfall (falls ESP), ein Lüfter abgezogen, Thermostat schließt, unbeabsichtigter Dauerlauf.
- Aufzeichnungsdaten roh bewahren, Zeitstempel einheitlich. Kein Vergleich von Maximal-Lüfterdatenblattwerten als tatsächliche Messung.

## Kriterien für G5 -> G6 (vorläufig)
1. Kein thermischer/mechanischer/elektrischer Sicherheitsmangel.
2. Geringe und akzeptierte Geräusche bei festgelegter Ziel-Drehzahl.
3. Dokumentierte positive Wirkung auf Aufheizrate oder nachgewiesene Wärmestromsteigerung über Messunsicherheit.
4. Stabiler Start/Stop inkl. Hysterese, keine ungewollten Anläufe durch Fehlmessungen.
5. Wartungszugang ohne Werkzeugzerstörung, keine blockierten Ventile.
6. Tatsächliche Stromkosten in Jahresbetrachtung berechnet; Energieeinsparung nur bei erhärteter Evidenz ausweisen.

## Energiekennzahl
Elektrische Mehrenergie E = P_avg [W] * Laufzeit [h] / 1000 [kWh]. Beispiel *keine Prognose*: 5 W * 8h * 150 Tage = 6 kWh/a. Reale CO2- und Eurosparzahl erst nach dokumentierter Heizsystembeschreibung/vergleichbarer Betriebsdaten.

## Datenmodell
trial_id, radiator_id, mode, fan_pwm_pct, fan_rpm, room_sensor_1_C, room_sensor_2_C, flow_C, return_C, inlet_air_C, outlet_air_C, outside_C, power_W, timestamp, notes.
