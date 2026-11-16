+++
title = "freemapper-print"
template = "program.html"
description = "freemapper-print prints the finished orienteering map with the courses: one vector PDF per course at exact scale."

[extra]
repo = "freemapper-print"
role = "Printing map sheets"
lead = "freemapper-print turns a finished orienteering map and the courses from a course-setting program into print-ready map sheets, one per course."
+++

## What it makes

- The map at exact print scale as a vector PDF, on A4, A3 or a page size of your own, also at another scale with
  the symbol sizes the norm asks for, such as 1:3000 for the youngest classes.
- One sheet per course with the course overprint in purple and the control descriptions, from Purple Pen
  (`.ppen`) or from any program that writes IOF XML 3.0 (Condes, OCAD).
- Control numbers that keep clear of legs, circles and the map's symbols; `check` suggests a better place.
- The sheet around it: frame, title block, club and sponsor logos, north lines, a check distance to measure, and
  the map's credit lines.

## Install

Download the archive for your system below and unpack it. As with freemapper, macOS needs
`xattr -d com.apple.quarantine freemapper-print`, and Windows asks on the first start (*More info* → *Run anyway*).
`freemapper-print --version` shows that it worked; `freemapper-print update` fetches the newest version later.

## The first sheets

```sh
freemapper-print init training --map map.omap --courses courses.ppen --title "Training"
freemapper-print check training
freemapper-print export training --out-dir pdfs
```

The instructions for AI assistants are in
[AGENTS.md](https://github.com/HenryJobst/freemapper-print/blob/main/AGENTS.md).
