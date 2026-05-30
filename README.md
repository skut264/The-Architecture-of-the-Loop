# Architecture of the Loop — Book Project

## Overview
A living, growing mystical book that evolves as Patrick shares findings.

## Structure
- `index.html` — The reader website (dark theme, gold accents, search, TOC)
- `chapters/` — Markdown chapter sources (auto-generated)
- `assets/` — Images, diagrams, audio

## Adding a Chapter
When Patrick shares a finding:
1. Store the finding in fact_store (holographic memory)
2. Update `index.html` chapter data array
3. Optionally save chapter as markdown in `chapters/`

## Access
Open `index.html` in any browser. For sharing, serve via any static server.
