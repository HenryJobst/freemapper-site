+++
title = "freemapper"
template = "program.html"
description = "freemapper makes the starting point of an orienteering map for OpenOrienteering Mapper and OCAD from open geodata."

[extra]
repo = "freemapper"
role = "The starting point of the map"
lead = "freemapper turns the open geodata of a German state and OpenStreetMap into a starter project for an orienteering map. What the data show reliably is drawn already; everything else is ready as a template or a candidate."
+++

## What it makes

- A georeferenced map for OpenOrienteering Mapper (`.omap`), on request also for OCAD. Buildings, paved areas,
  paths, stairs, walls, water and other reliable objects are drawn already.
- Templates for mapping: aerial photo, hillshade, slope, local relief and the height of the vegetation.
- What is uncertain (street furniture, many paths, banks and knolls from the terrain, out-of-bounds areas) comes
  as candidates in a map of its own, to check against the aerial photo and in the terrain. The check print draws every
  candidate true to position.
- A training map to print and run on as it is: map and candidates together, cleaned up so that no symbol lies on
  another.
- Permit notes: Kreis, municipality, protected areas, natural monuments, monuments, forest and forest office in
  the map area, and whom one usually asks before an event. A hint, not legal advice.

## Map kinds

| Map | Norm | Scale |
|---|---|---|
| Schoolyard | ISSprOM 2019-2 | 1:1000 |
| Sprint | ISSprOM 2019-2 | 1:4000 or 1:5000 |
| Forest | ISOM 2017-2 | 1:15 000, 1:10 000 or 1:7500 |

freemapper knows fifteen German states, all except Thuringia. Poland is usable too (terrain model, aerial photos, buildings and land use from GUGiK).
How good the map gets depends on the data of the state;
the [manual](@/handbuch/freemapper/_index.en.md) names them for each, the
[examples](@/beispiele.en.md) show a sprint and a forest map
for each.

## Install

Download the archive for your system below and unpack it. The folder holds the program `freemapper` (on Windows
`freemapper.exe`) with the manual and the licence.

- macOS starts a program from the internet only once the quarantine flag is gone:
  `xattr -d com.apple.quarantine freemapper`
- Windows shows "Windows protected your PC" on the first start: *More info* → *Run anyway*.
- On Linux, freemapper runs on any distribution.

`freemapper --version` shows that it worked. Later, `freemapper update` fetches the newest version.

## The first map

```sh
freemapper init schoolyard --place "Clara-Zetkin-Schule Strausberg" --kind schoolyard
freemapper run schoolyard --pdf --training
```

To draw the area on a map instead, `freemapper select schoolyard` opens the area page in the browser. An AI
assistant such as Claude or Codex can install and run freemapper itself; its instructions are in
[AGENTS.md](https://github.com/HenryJobst/freemapper/blob/main/AGENTS.md).
