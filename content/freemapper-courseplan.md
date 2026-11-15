+++
title = "freemapper-courseplan"
template = "program.html"
description = "freemapper-courseplan legt OL-Bahnen auf der fertigen Karte, prüft sie gegen die Wettkampfbestimmungen und gleicht mit Purple Pen ab."

[extra]
repo = "freemapper-courseplan"
role = "Bahnen legen"
lead = "freemapper-courseplan ist das Bahnlegungsprogramm der Suite: Man legt die Bahnen in einem Editor im Browser auf der fertigen Karte aus OpenOrienteering Mapper. Das Programm ist in Arbeit, vieles ist schon nutzbar."
+++

## Was es macht

- **Posten, Bahnen und Sonderobjekte** im Editor auf der Karte: Start, Ziel, Posten mit Code und Beschreibung,
  Knickpunkte, Pflichtstrecken und Sperrgebiete.
- **Prüfungen nach den Wettkampfbestimmungen 2026**, etwa Postenabstände, spitze Winkel und genug verschiedene erste
  Posten, jeweils mit Quelle und mit begründeten Ausnahmen (`check`).
- **Purple Pen in beide Richtungen**: importieren, exportieren und abgleichen, damit beide Programme nebeneinander
  nutzbar sind.
- **IOF-XML 3.0** für die Auswertung.
- **Score-Bahnen** mit Punktwerten, Zeitlimit und Vorschlägen für Postenstellen.

Gedruckt werden die Bahnen mit [freemapper-print](@/freemapper-print.md).

## Installieren

Unten das Archiv für Ihr System herunterladen und auspacken. Wie bei freemapper braucht macOS
`xattr -d com.apple.quarantine freemapper-courseplan`, und Windows fragt beim ersten Start nach (*Weitere
Informationen* → *Trotzdem ausführen*). `freemapper-courseplan --version` zeigt, ob alles geklappt hat;
`freemapper-courseplan update` holt später die neueste Version.

## Die erste Bahn

```sh
freemapper-courseplan init halle.omap --title "Training"
freemapper-courseplan edit halle.courseplan.toml
```

`edit` öffnet den Editor im Browser. Die Anleitung für KI-Assistenten steht in
[AGENTS.md](https://github.com/HenryJobst/freemapper-courseplan/blob/main/AGENTS.md).
