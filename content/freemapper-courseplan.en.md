+++
title = "freemapper-courseplan"
template = "program.html"
description = "freemapper-courseplan sets orienteering courses on the finished map, checks them against the competition rules and syncs with Purple Pen."

[extra]
repo = "freemapper-courseplan"
role = "Setting courses"
lead = "freemapper-courseplan is the course-setting program of the suite: you set the courses in an editor in the browser on the finished map from OpenOrienteering Mapper. The program is in progress; much of it is usable."
+++

## What it does

- **Controls, courses and special objects** in the editor on the map: start, finish, controls with code and
  description, bends, marked routes and out-of-bounds areas.
- **Checks by the German competition rules of 2026**, such as control distances, sharp angles and enough different
  first controls, each with its source and with reasoned exceptions (`check`).
- **Purple Pen both ways**: import, export and sync, so both programs can be used side by side.
- **IOF XML 3.0** for the results software.
- **Score courses** with point values, time limit and suggested control sites.

The courses are printed with [freemapper-print](@/freemapper-print.en.md).

## Install

Download the archive for your system below and unpack it. As with freemapper, macOS needs
`xattr -d com.apple.quarantine freemapper-courseplan`, and Windows asks on the first start (*More info* → *Run
anyway*). `freemapper-courseplan --version` shows that it worked; `freemapper-courseplan update` fetches the newest
version later.

## The first course

```sh
freemapper-courseplan init hall.omap --title "Training"
freemapper-courseplan edit hall.courseplan.toml
```

`edit` opens the editor in the browser. The instructions for AI assistants are in
[AGENTS.md](https://github.com/HenryJobst/freemapper-courseplan/blob/main/AGENTS.md).
