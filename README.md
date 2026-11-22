# freemapper-site

[English below](#english)

Die Website der freemapper-Suite: [freemapper](https://github.com/HenryJobst/freemapper),
[freemapper-courseplan](https://github.com/HenryJobst/freemapper-courseplan) und
[freemapper-print](https://github.com/HenryJobst/freemapper-print), unter <https://freemapper.de>.

Gebaut mit [Zola](https://www.getzola.org/) 0.23.6 und veröffentlicht mit GitHub Pages. Der Plan steht in
freemapper unter `docs/superpowers/specs/2026-11-15-website-design.md`.

Lokal ansehen:

```sh
zola serve
```

Bei der täglichen Aktualisierung (04:17 Uhr) holt `scripts/fetch-status.sh` den Dienststatus von freemapper (Branch `status`, geschrieben vom
nächtlichen Lauf); sind Geodienste eines Landes zwei Nächte in Folge ausgefallen, zeigt die Seite einen Hinweis. Ohne Status bleibt er weg.

Die Seite lädt nichts von anderen Servern. Die Schrift Inter liegt unter `static/fonts/` (SIL Open Font License,
siehe `static/fonts/README.md`), die Farben sind die der Suite aus freemapper-core.

## English

The website of the freemapper suite, built with Zola 0.23.6 and published with GitHub Pages at
<https://freemapper.de>. Run `zola serve` to look at it locally. The daily build fetches the service status of freemapper (`scripts/fetch-status.sh`) and shows a notice when a state's geodata services failed two nights in a row. It
loads nothing from other servers: the typeface Inter is in `static/fonts/` (SIL Open Font License), the colours are the
suite's from freemapper-core.

Code and texts: AGPL-3.0-or-later (`LICENSE`).
