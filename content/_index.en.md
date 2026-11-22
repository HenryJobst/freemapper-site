+++
title = "Orienteering maps from open data"
template = "index.html"

[extra]
lead = "The freemapper suite draws the starting point of an orienteering map from the official geodata of the German states and from OpenStreetMap, sets the courses and prints the map sheets. Free software for Windows, macOS and Linux."
cta_download = "Download freemapper"
cta_examples = "See the examples"
examples_url = "https://github.com/HenryJobst/freemapper/blob/main/examples/README.en.md"
image_alt = "Training map of Viktoriapark in Berlin-Kreuzberg: buildings grey, park areas yellow and white, private ground olive green, paths and stairs, contours brown"
image_caption = "Training map of Viktoriapark, Berlin-Kreuzberg, sprint 1:4000. freemapper made it from open data; click for the PDF to print."
programs_title = "How the programs work together"
steps = [
  { repo = "freemapper", text = "makes the starting point of the map from the data of the state." },
  { text = "Mapping goes on in OpenOrienteering Mapper or OCAD and in the terrain." },
  { repo = "freemapper-courseplan", text = "sets the courses on the finished map." },
  { repo = "freemapper-print", text = "prints one map sheet per course." },
]
states_title = "For which places?"
states_text = "freemapper knows the open geodata of fifteen German states: buildings and land use from the cadastre, terrain model, aerial photos and surface model. OpenStreetMap comes on top. Outside Germany, Poland is usable: terrain model, aerial photos, buildings and land use from GUGiK, the EGiB cadastre."
states = [
  "Baden-Württemberg", "Bavaria", "Berlin", "Brandenburg", "Bremen", "Hamburg", "Hesse",
  "Lower Saxony", "Mecklenburg-Vorpommern", "North Rhine-Westphalia", "Rhineland-Palatinate", "Saarland",
  "Saxony", "Saxony-Anhalt", "Schleswig-Holstein",
]
states_missing = "Thuringia has no data sources yet."
ai_title = "With an AI assistant"
ai_text = "An AI assistant such as Claude or Codex can install and run freemapper, from the command line or as an MCP server. You say which map you need and for which place; the assistant sets up the project and makes the map. Its instructions are in [AGENTS.md](https://github.com/HenryJobst/freemapper/blob/main/AGENTS.md)."
free_title = "Free software"
free_text = "All programs are free software under the AGPL-3.0-or-later; the source is on [GitHub](https://github.com/HenryJobst). The maps carry the credit lines the data licences require. Keep them when you pass a map on."

[[extra.programs]]
repo = "freemapper"
role = "The starting point of the map"
text = "Draws buildings, paths, paved areas and everything else the data show reliably, and adds aerial photo, hillshade, slope and vegetation height as templates. What is uncertain comes as a candidate to check. Schoolyard, sprint and forest maps for OpenOrienteering Mapper and OCAD, on request with a training map to print and permit notes."

[[extra.programs]]
repo = "freemapper-courseplan"
role = "Setting courses"
text = "An editor in the browser for the courses on the finished map. It checks them against the competition rules, syncs with Purple Pen and writes IOF XML 3.0 for the results software."
state = "In progress, much of it usable"

[[extra.programs]]
repo = "freemapper-print"
role = "Printing map sheets"
text = "Turns the finished map and the courses into print-ready sheets, one per course: a vector PDF at exact scale, with course overprint, control descriptions and credit lines."
+++
