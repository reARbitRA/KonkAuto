# KONKAUTO SDAD decks

Two complementary 16:9 vector PDFs are maintained in the repository root:

- `KONKAUTO_SDAD_Workflow.pdf` — the original 20-slide workflow deck.
- `KONKAUTO_SDAD_Manifesto_19slides.pdf` — the separate, exactly 19-slide technical doctrine / manifesto.

Both decks use selectable text and embedded Archivo Black / IBM Plex Sans / IBM Plex Mono fonts. The manifesto deck uses black, white, and the single steel-cyan accent `#7C9BFF`.

## Rebuild

Install ReportLab, then run either or both generators from the repository root:

```sh
python3 -m pip install reportlab
python3 tools/konkauto_deck/build_konkauto_deck.py
python3 tools/konkauto_deck/build_konkauto_manifesto.py
```

The generators write their respective PDFs to the repository root by default. Pass `--output /path/to/file.pdf` to either script to choose another destination.

The bundled fonts are distributed under the SIL Open Font License; the license notices are in `assets/fonts/`.
