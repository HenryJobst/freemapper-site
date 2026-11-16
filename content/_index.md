+++
title = "Orientierungslaufkarten aus offenen Daten"
template = "index.html"

[extra]
lead = "Die freemapper-Suite zeichnet aus amtlichen Geodaten der Bundesländer und aus OpenStreetMap den Ausgangsstand einer OL-Karte, legt die Bahnen und druckt die Kartenblätter. Freie Software für Windows, macOS und Linux."
cta_download = "freemapper herunterladen"
cta_examples = "Beispiele ansehen"
examples_url = "https://github.com/HenryJobst/freemapper/blob/main/examples/README.md"
image_alt = "Trainingskarte des Viktoriaparks in Berlin-Kreuzberg: Gebäude grau, Parkflächen gelb und weiß, Privatgelände olivgrün, Wege und Treppen, Höhenlinien braun"
image_caption = "Trainingskarte Viktoriapark, Berlin-Kreuzberg, Sprint 1:4000. freemapper hat sie aus offenen Daten erzeugt; ein Klick öffnet das PDF zum Drucken."
programs_title = "So arbeiten die Programme zusammen"
steps = [
  "freemapper erzeugt aus den Daten des Bundeslandes den Ausgangsstand der Karte.",
  "Kartiert wird weiter in OpenOrienteering Mapper oder OCAD und im Gelände.",
  "freemapper-courseplan legt die Bahnen auf der fertigen Karte.",
  "freemapper-print druckt ein Kartenblatt je Bahn.",
]
states_title = "Für welche Orte?"
states_text = "freemapper kennt die offenen Geodaten von fünfzehn Bundesländern: Gebäude und Nutzung aus dem Liegenschaftskataster, Geländemodell, Luftbild und Oberflächenmodell. Dazu kommt OpenStreetMap."
states = [
  "Baden-Württemberg", "Bayern", "Berlin", "Brandenburg", "Bremen", "Hamburg", "Hessen",
  "Mecklenburg-Vorpommern", "Niedersachsen", "Nordrhein-Westfalen", "Rheinland-Pfalz", "Saarland",
  "Sachsen", "Sachsen-Anhalt", "Schleswig-Holstein",
]
states_missing = "Für Thüringen gibt es noch keine Datenquellen."
ai_title = "Mit einem KI-Assistenten"
ai_text = "freemapper lässt sich auch von einem KI-Assistenten wie Claude oder Codex installieren und bedienen, über die Kommandozeile oder als MCP-Server. Man sagt, welche Karte man braucht und für welchen Ort; der Assistent legt das Projekt an und erzeugt die Karte. Die Anleitung für den Assistenten steht in [AGENTS.md](https://github.com/HenryJobst/freemapper/blob/main/AGENTS.md)."
free_title = "Freie Software"
free_text = "Alle Programme sind freie Software unter der AGPL-3.0-or-later, der Quelltext liegt auf [GitHub](https://github.com/HenryJobst). Die Karten tragen die Quellenangaben, die die Lizenzen der Daten verlangen. Behalten Sie sie bei, wenn Sie eine Karte weitergeben."

[[extra.programs]]
repo = "freemapper"
role = "Der Ausgangsstand der Karte"
text = "Zeichnet Gebäude, Wege, befestigte Flächen und alles andere, was die Daten sicher zeigen, und legt Luftbild, Schummerung, Hangneigung und Vegetationshöhen als Vorlagen dazu. Was unsicher ist, kommt als Kandidat zum Prüfen. Schulhof-, Sprint- und Waldkarten für OpenOrienteering Mapper und OCAD, auf Wunsch mit einer Trainingskarte zum Drucken und Hinweisen zu Genehmigungen."

[[extra.programs]]
repo = "freemapper-courseplan"
role = "Bahnen legen"
text = "Ein Editor im Browser für die Bahnen auf der fertigen Karte. Er prüft sie gegen die Wettkampfbestimmungen, gleicht mit Purple Pen ab und gibt IOF-XML 3.0 für die Auswertung aus."
state = "In Arbeit, vieles schon nutzbar"

[[extra.programs]]
repo = "freemapper-print"
role = "Kartenblätter drucken"
text = "Macht aus der fertigen Karte und den Bahnen die druckfertigen Blätter, eines je Bahn: ein Vektor-PDF im exakten Maßstab, mit Bahnaufdruck, Postenbeschreibung und Quellenangaben."
+++
