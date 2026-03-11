# Keine

An agent-assisted personal knowledge base. Drop in a URL, PDF, or idea — the agent handles the rest.

> Named after *Kamishirasawa Keine* from Touhou Project. She knows everything.

## Structure

```
docs/
  <yyyy-mm-dd-slug>.md    — knowledge entries
  tags/<slug>.md          — tag index
  maps/<slug>.md          — topic overviews
```

## Usage

```bash
git clone https://github.com/duskmoon314/keine.git
cd keine
claude  # or codex, gemini-cli, opencode, etc.
```

Tell the agent what you want to capture or explore. It will research, ingest, and connect knowledge for you.

## TODO

- [ ] Add guidance for agents to discover useful skills (e.g. pdf, docx)
- [ ] Add skills for fetching from external sources (e.g. Semantic Scholar)
