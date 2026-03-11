---
name: keine-update-entries
description: Use this skill when creating a new knowledge entry or editing an existing one in the Keine knowledge base. Trigger when asked to add, ingest, document, or update any piece of knowledge — a URL, PDF, book, concept, note, or research finding. Use this skill even when the user doesn't say "entry" — if they want to capture or update knowledge, this is the skill.
compatibility: Require `keine-manage` skill
---

# Creating and Editing Knowledge Entries

## Creating a new entry

### 1. Search first

Before creating, check whether something close already exists:

```sh
grep -ri "keyword" docs/
ls docs/tags/
```

If a close match exists, consider updating it instead of creating a new file.

### 2. Choose a slug

Format: `YYYY-MM-DD-short-descriptive-slug.md`. Use today's date. Keep the slug lowercase and hyphen-separated. Prefer concrete nouns over vague ones (`2026-03-11-docker-networking.md` beats `2026-03-11-containers.md`).

### 3. Write the file

Fill all frontmatter fields:

```yaml
---
title: "Human-readable title"
description: "One sentence for use in tag indexes"
tags: ["tag1", "tag2"]
source: "URL, DOI, or other reference"   # required — link to the original
source_type: "url | pdf | book | note"   # required — omit only for original writing
---
```

Body:
- **H1** = title (exactly one)
- **## Summary** — 2-5 sentences capturing the core idea
- **## Content** — main knowledge; use H3+ for subsections
- **## Related** — relative links to other entries, tags, or maps

For ingested content (URL, PDF, book), summarize in your own words — do not copy verbatim.

### 4. Update tags

Run from the repo root after writing the file:

```sh
uv run scripts/maintain_tags.py
```

### 5. Commit

You *must* stage the new entry and any updated tag files:

```sh
git add docs/<new-entry>.md docs/tags/
git commit -m "docs: add <title>"
```

---

## Editing an existing entry

1. Find the entry — search by keyword or tag (see below)
2. Edit content or frontmatter as needed
3. If tags changed, re-run `uv run scripts/maintain_tags.py`
4. You *must* commit:
   ```sh
   git add docs/<entry>.md docs/tags/
   git commit -m "docs: update <title>"
   ```

---

## Finding entries

- By keyword: `grep -ri "term" docs/`
- By tag: read `docs/tags/<tag>.md`
- By topic: check `docs/maps/` for a topic map
