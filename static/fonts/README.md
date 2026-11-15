# Inter

Inter 4.1 by Rasmus Andersson and the Inter Project Authors (<https://rsms.me/inter/>), under the SIL Open Font
License 1.1 (`OFL.txt`; the licence names no reserved font name). Taken from `Inter-4.1.zip` of the release
<https://github.com/rsms/inter/releases/tag/v4.1> (SHA-256 `9883fdd4a49d4fb66bd8177ba6625ef9a64aa45899767dde3d36aa425756b11e`),
files `web/InterVariable.woff2` and `web/InterVariable-Italic.woff2`, reduced to Latin with

```sh
pyftsubset InterVariable.woff2 --output-file=InterVariable.woff2 --flavor=woff2 \
  --layout-features='kern,liga,calt,ccmp,locl,mark,mkmk,tnum,case,frac,sups,subs' \
  --unicodes='U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0300-0301,U+0308,U+2000-206F,U+20AC,U+2122,U+2190-2199,U+2212,U+2215,U+FEFF,U+FFFD'
```

The site serves the fonts itself; nothing is loaded from rsms.me or any other host.
