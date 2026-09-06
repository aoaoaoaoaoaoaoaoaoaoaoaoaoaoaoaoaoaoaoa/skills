---
name: font-design
description: Design and extend typefaces or coherent symbol alphabets with FontForge, editable vector sources, and rendered visual iteration. Use for original glyph design, font-family integration, glyph coverage gates, and replacing visually mismatched fallback fonts. Do not use for merely choosing an existing font.
---

# Font Design

Design glyphs, not a bag of Unicode coverage. Establish the face's cap height,
x-height, advance, sidebearings, stroke contrast and stress, terminals, serifs,
overshoot, and counter shapes from its actual outlines. Inspect `H O n o x 0 + /`
before extending it. A symbol must belong beside those forms and remain legible
at its destination size. Mathematical equality of dimensions is not optical
equality; adjust spacing, weight, centering, and overshoot by sight.

## Tools And Sources

Use FontForge for editable outlines, components, contour operations, and font
inspection. Its Python API supports cubic pens, SVG import/export, stroke
expansion, affine transforms, and SFD editing. Use FontTools for inspecting and
assembling OpenType tables when it preserves unaffected glyphs more faithfully.
Choose one canonical editable source: SFD, UFO, or a declared SVG glyph map.
Generated fonts and interchange exports are projections, not competing masters.

Install missing system tooling through `$ask-for-sudo`. FontForge's embedded
Python is a specialized runtime; do not wrap it in a Python environment that
hides its system extension. Use `$x11-gui-testing` for any graphical inspection.
Plain Python helpers follow the house Astral and PEP 723 rules.

Read the relevant [FontForge Python API](https://fontforge.org/docs/scripting/python/fontforge.html)
before relying on an operation. In particular, finish a glyph pen before asking
FontForge to stroke, validate, transform, or export its layer. Keep a pen's
quadratic/cubic model consistent with its destination font.
Index a font by Unicode with `font[ord(character)]`; string indices are glyph
names, so `font["0"]` does not mean the character zero.
Mirror centerline geometry before stroke expansion when a reflected expanded
contour develops intersections. Validate after rounding as well as before it.

Do not transplant another family's outlines to satisfy a request for visual
coherence. Reusing components from the chosen face is useful; importing the
rejected fallback under another filename is not redesign. Preserve license
notices and reserved-name obligations when deriving a face. Record provenance
for new outlines and exclude retired fonts from shipped assets and examples.

## Visual Loop

1. Draw a small related group on the face's metric grid. Use few intentional
   Bézier points and explicit extrema; retain useful components rather than
   flattening them prematurely.
2. Validate contours, winding, intersections, references, bearings, advance,
   and Unicode mapping. Validate the intended face without fallback.
3. Generate a font and render a proof at actual product sizes beside reference
   letters and neighboring symbols. Inspect both native-size output and a
   nearest-neighbor enlargement of that raster. Outline previews alone cannot
   judge small-size counters, hinting, or apparent weight.
4. Inspect the actual consuming renderer and control: a print specimen cannot
   prove an engraved button or a curved tape. Judge readability, family
   resemblance, optical placement, and pairwise consistency; then redraw.

Keep visual evidence for accepted groups. Do not accept a glyph solely because
it validates, covers a scalar, resembles its Unicode name, or looks attractive
when enlarged. Do not regenerate untouched outlines, metrics, hinting, or
shaping tables without a reason and an appropriate preservation check.

## Coverage And Delivery

Treat the declared glyph map as a build contract. Enumerate authored UI scalars,
including escaped literals, and fail the gate when a scalar lacks an admitted
glyph. The remedy is a deliberate symbol substitution or a designed addition
to the map, never silent font fallback. Keep authored UI coverage distinct from
arbitrary user text; preserve user data rather than making an unsupported name
an application crash.

Verify the exported font's actual cmap, contour validity, metrics, shaping, and
production rendering. Check distribution contents as well as source imports.
Removing a face from the active stack does not remove its compiled font assets.
Audit dependency features as well: egui's default font bundle can be reintroduced
by an instrumentation dependency even when the application disables it.
Use deterministic generation or a declared semantic-font comparison when
editor timestamps prevent byte equality. Deliver the editable source, the
generated font, its mapping and provenance, and the useful visual evidence.
