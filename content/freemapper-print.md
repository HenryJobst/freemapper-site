+++
title = "freemapper-print"
template = "program.html"
description = "freemapper-print druckt die fertige OL-Karte mit den Bahnen: ein Vektor-PDF je Bahn im exakten Maßstab."

[extra]
repo = "freemapper-print"
role = "Kartenblätter drucken"
lead = "freemapper-print macht aus einer fertigen OL-Karte und den Bahnen aus einem Bahnlegungsprogramm die druckfertigen Kartenblätter, ein Blatt je Bahn."
+++

## Was es macht

- **Die Karte im exakten Druckmaßstab** als Vektor-PDF, auf A4, A3 oder einer eigenen Seitengröße, auch in einem
  anderen Maßstab mit den Symbolgrößen der Norm, etwa 1:3000 für die jüngsten Klassen.
- **Ein Blatt je Bahn** mit dem Bahnaufdruck in Violett und der Postenbeschreibung, aus Purple Pen (`.ppen`) oder
  aus jedem Programm, das IOF-XML 3.0 schreibt (Condes, OCAD).
- **Postennummern**, die Strecken, Kreise und die Symbole der Karte frei lassen; `check` schlägt einen besseren Platz
  vor.
- **Das Blatt drumherum**: Rahmen, Titelblock, Vereins- und Sponsorenlogos, Nordlinien, eine Kontrollstrecke zum
  Nachmessen und die Quellenangaben der Karte.

## Installieren

Unten das Archiv für Ihr System herunterladen und auspacken. Wie bei freemapper braucht macOS
`xattr -d com.apple.quarantine freemapper-print`, und Windows fragt beim ersten Start nach (*Weitere Informationen*
→ *Trotzdem ausführen*). `freemapper-print --version` zeigt, ob alles geklappt hat; `freemapper-print update` holt
später die neueste Version.

## Die ersten Blätter

```sh
freemapper-print init training --map karte.omap --courses bahnen.ppen --title "Training"
freemapper-print check training
freemapper-print export training --out-dir pdfs
```

Die Anleitung für KI-Assistenten steht in
[AGENTS.md](https://github.com/HenryJobst/freemapper-print/blob/main/AGENTS.md).
