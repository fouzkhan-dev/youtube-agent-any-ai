# YouTube Agent — for ANY AI

Eleven skills that run a YouTube channel — scripts off 21 hook formulas
with a scored hook, title and thumbnail linted as one pairing, an edit
decision list from your transcript, a retention reader that finds the
exact moments people leave, a Shorts cutter, chapters, search, comments,
the weekly plan, a channel audit, and a virality engine that ranks your
niche by outlier multiple rather than channel size.

The original pack was built **for Claude only**. This repo is the same
pack, packaged so it can be **configured with any AI** — Claude, Codex,
Gemini, Cursor, ChatGPT, Muse, or a local LLM. The skills and tools are
unchanged (MIT, by Jake Schincariol — see `NOTICE.md`).

**Nothing gets published until you do it.** These skills write. You upload.

## Quick start

```bash
git clone https://github.com/fouzkhan-dev/youtube-agent-any-ai.git
cd youtube-agent-any-ai
python3 install.py --target <your-ai>
```

| `--target` | For | What it installs |
| --- | --- | --- |
| `claude-code` | Claude Code | skills → `~/.claude/skills/`, voice template → `~/.claude/youtube/voice.md` |
| `muse` | Muse personal agent | skills → Muse's custom-skills folder |
| `codex` | Codex & other AGENTS.md agents | `AGENTS.md` router + `skills/` into your project |
| `gemini` | Gemini CLI | `GEMINI.md` + `AGENTS.md` + `skills/` into your project |
| `cursor` | Cursor | `.cursor/rules/youtube-agent.mdc` + `skills/` |
| `generic` | ChatGPT / any chat AI | `SYSTEM_PROMPT.md` to paste, + `skills/` to attach |

No installer fan? The manual route also works everywhere: give your AI
the `AGENTS.md` file (the router) and access to the `skills/` folder.
Chat-only AIs: paste `SYSTEM_PROMPT.md`, then paste the single
`SKILL.md` you need at the top of the chat — it runs as a mode.

## Configure it yours

```bash
cp config.example.json config.json
```
Set your channel name, niche and language, then spend ten minutes on the
voice file: copy `templates/voice.md`, fill it in (or give your AI three
of your videos and say "write my voice.md from these"), and point
`voice_file` in `config.json` at it. Every skill reads that file. It
matters more here than anywhere else, because you have to say the words
out loud.

## The eleven

| command | what it does |
| --- | --- |
| `/yt-script` | One idea into a script. Five hooks off 21 formulas, scored, then the spoken script with retention beats marked. |
| `/yt-package` | Title and thumbnail as one pairing, linted for truncation, duplication and vagueness. |
| `/yt-edit` | A transcript into an edit decision list: dead air, filler cues, retakes, with timecodes. |
| `/yt-comment` | The comment section triaged into four piles, then replies in your voice. Says which one to pin. |
| `/yt-plan` | A week that fits the hours you actually have. One anchor, one cheap one, three Shorts. |
| `/yt-viral` | What is working in your niche, ranked by multiple over each channel's own median. |
| `/yt-retention` | Your retention export read properly: hook leak, the cliffs, the slide, and what to change. |
| `/yt-shorts` | The Shorts already inside a long video, with a new first line written for each. |
| `/yt-seo` | The description, the tags that are worth having, and the three queries this should win. |
| `/yt-chapters` | Chapters from a transcript, validated against YouTube's own rules so they render. |
| `/yt-audit` | The whole channel, ending in ONE fix rather than twenty. |

## The six tools

Every one runs on a clean Python 3 with no dependencies.

```bash
python3 skills/yt-script/hookscore.py --hook "one line"
python3 skills/yt-package/title.py --title "..." --thumb "..."
python3 skills/yt-edit/deadair.py transcript.srt
python3 skills/yt-chapters/chapters.py transcript.srt
python3 skills/yt-retention/retention.py retention.csv
python3 skills/yt-viral/swipe.py collected.json --min 2.0
```

## The fine print

- **It does not publish.** Every skill ends in a block you copy and a
  question — ship it, or change it?
- **`hookscore.py` is a heuristic, not a predictor.** A low score is a
  reason to look again; a high score is not a promise.
- **Nothing invents a number.** If a skill wants a figure it doesn't
  have, it asks you for it or writes the line without it.

## Licence

MIT. Original work © 2026 Jake Schincariol — use it, change it, ship it.
