# Thermik / Akustik – Ingenieursnotizen v0.1

## Strömungsphysik
Heizkörper: Strahlung + natürliche/erzwungene Konvektion. Mehr Gebläseluft erhöht den konvektiven Wärmeübergangskoeffizienten, kann aber zugleich die mittlere Heizkörpertemperatur senken. Relative Effekte hängen von Wasser-Massenstrom, Vorlauf, Rücklauf, Thermostatstellung und Wärmeanforderung ab. Keine direkte Energieeinsparung ableiten. Referenz: https://doi.org/10.1016/j.csite.2023.103432

## Lüfterauswahl ist ein Netzpunktproblem
Auswahl aus Ventilatorkennlinie Δp(Q) und Druckverlustkurve Kanal + Konvektionsbleche. Einbauvolumenstrom ist der Schnittpunkt; maximale Herstellerluftmenge bei 0-Pa Gegendruck ist keine realistische Betriebsprognose. 1.53 mmH2O Noctua und 2.20 mmH2O ARCTIC sind getrennte Maxima bei anderer Drehzahl/Betriebsbedingung, nicht direkte Praxiswerte.
Varianten A/B/C mit identischem Fan, gleicher Versorgung und PWM-Stufe vergleichen. Turbulenz, Leckpfade, Querschnittsverengung, Rückströmung und Gitterwiderstand dokumentieren.

## Akustik
Messbar: Hintergrund `L_Aeq`, Booster bei 25/40/60% PWM `L_Aeq`, 1m definierter Abstand, ein zweiter Wert beim Schlaf-/Sitzplatz, Drehzahl. Bei niedrigen Grundpegeln verändert die Lautstärke nicht linear; Tonalität, Brummen, Resonanz und Anlauf sind subjektiv relevant. Handy-Mikrofon nur für relative Trends, Schallpegelmessgerät für absolute Werte.

## Kosten-/Wirtschaftsmodell
Mehrbedarf: `fan_energy_kWh = measured_total_input_W * on_hours / 1000` (Netzteilverluste einschließen). Gas-/Wärme-/Strompreise und gemessene Energieeinsparung getrennt. Zeit bis Solltemperatur reicht allein nicht als Nachweis von Heizkosteneinsparung.

## Besonderheit Heizkostenverteiler
Eine mechanische oder thermische Beeinflussung des Ablesegeräts ist zu vermeiden; Lage dokumentieren und gegebenenfalls Messdienst/Vermieter konsultieren. Thermostatkopf nicht direkt anblasen. Referenz Hintergrund (kein Rechtsgutachten): https://www.vattenfall.de/infowelt-energie/nachhaltig-heizen/was-ist-ein-heizkostenverteiler

## Relevante Datenblätter
Noctua NF-A12x15 PWM https://www.noctua.at/en/products/nf-a12x15-pwm/specifications — 120x120x15mm; 70°C Umgebung; 0.13A max; 94.2m³/h frei; 1.53mm H2O max.
ARCTIC P12 PWM PST https://www.arctic.de/en/P12-PWM-PST/ACFAN00120A — 120x120x25mm; 40°C Umgebung; 95.7m³/h frei; 2.20mm H2O max.
Materialfreigabe und Lüfterauswahl nur nach realem Heizkörper-Hotspot.
