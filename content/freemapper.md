+++
title = "freemapper"
template = "program.html"
description = "freemapper macht aus offenen Geodaten den Ausgangsstand einer OL-Karte für OpenOrienteering Mapper und OCAD."

[extra]
repo = "freemapper"
role = "Der Ausgangsstand der Karte"
lead = "freemapper macht aus den offenen Geodaten eines Bundeslandes und aus OpenStreetMap ein Startprojekt für eine OL-Karte. Was die Daten sicher zeigen, ist schon gezeichnet; alles andere liegt als Vorlage oder Kandidat bereit."
+++

## Was es macht

- Eine georeferenzierte Karte für OpenOrienteering Mapper (`.omap`), auf Wunsch auch für OCAD. Gebäude, befestigte
  Flächen, Wege, Treppen, Mauern, Gewässer und andere verlässliche Objekte sind schon gezeichnet.
- Vorlagen zum Kartieren: Luftbild, Schummerung, Hangneigung, lokales Relief und die Höhe der Vegetation.
- Was unsicher ist (Stadtmobiliar, viele Wege, Böschungen und Kuppen aus dem Gelände, Sperrgebiete), liegt als
  Kandidat in einer eigenen Karte zum Prüfen gegen das Luftbild und im Gelände. Der Prüfausdruck zeichnet alle
  Kandidaten lagetreu.
- Eine Trainingskarte zum Drucken und Laufen, wie sie ist: Karte und Kandidaten zusammen, so aufgeräumt, dass
  kein Symbol auf einem anderen liegt.
- Hinweise zu Genehmigungen: Kreis, Gemeinde, Schutzgebiete, Naturdenkmale, Denkmale, Wald und Forstverwaltung
  im Kartengebiet und wen man vor einer Veranstaltung meist fragt. Ein Hinweis, keine Rechtsauskunft.

## Kartenarten

| Karte | Norm | Maßstab |
|---|---|---|
| Schulhof | ISSprOM 2019-2 | 1:1000 |
| Sprint | ISSprOM 2019-2 | 1:4000 oder 1:5000 |
| Wald | ISOM 2017-2 | 1:15 000, 1:10 000 oder 1:7500 |

freemapper kennt fünfzehn Bundesländer, alle außer Thüringen. Auch Polen ist nutzbar (Höhenmodell, Luftbild, Gebäude und Landnutzung von GUGiK).
Wie gut die Karte wird, hängt von den Daten des Bundeslandes ab; das [Handbuch](@/handbuch/freemapper/_index.md) nennt sie für
jedes einzeln, die [Beispiele](@/beispiele.md) zeigen je
eine Sprint- und eine Waldkarte.

## Installieren

Unten das Archiv für Ihr System herunterladen und auspacken. Im Ordner liegt das Programm `freemapper`
(unter Windows `freemapper.exe`) mit Handbuch und Lizenz.

- macOS startet ein Programm aus dem Internet erst, wenn die Quarantäne-Markierung weg ist:
  `xattr -d com.apple.quarantine freemapper`
- Windows zeigt beim ersten Start „Der Computer wurde durch Windows geschützt“: *Weitere Informationen* →
  *Trotzdem ausführen*.
- Unter Linux läuft freemapper auf jeder Distribution.

`freemapper --version` zeigt, ob alles geklappt hat. Später holt `freemapper update` die neueste Version.

## Die erste Karte

```sh
freemapper init schulhof --place "Clara-Zetkin-Schule Strausberg" --kind schoolyard
freemapper run schulhof --pdf --training
```

Wer das Gebiet lieber auf einer Karte zeichnet, öffnet mit `freemapper select schulhof` die Gebietsseite im Browser.
Ein KI-Assistent wie Claude oder Codex kann freemapper auch selbst installieren und bedienen; die Anleitung für ihn
steht in [AGENTS.md](https://github.com/HenryJobst/freemapper/blob/main/AGENTS.md).
