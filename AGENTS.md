# AGENTS.md — YouTube Agent router (works with any AI agent)

You have a YouTube channel toolkit in the `skills/` folder of this repo.
Each skill is a self-contained instruction file. Your job is to route the
user's request to the right skill, **read that `SKILL.md` in full, and
follow it exactly** — including its gates and output format.

## Before writing anything spoken or published
1. If `config.json` exists, read it (channel name, niche, language).
2. Read the creator's voice file — `config.json` → `voice_file`
   (default `templates/voice.md`). Match that voice. The creator has to
   say these words out loud; if it doesn't sound like them, it's wrong.

## Routing table
| User wants | Read and follow |
| --- | --- |
| A script from an idea, hooks | `skills/yt-script/SKILL.md` |
| A title + thumbnail that work as one pairing | `skills/yt-package/SKILL.md` |
| An edit decision list from a transcript | `skills/yt-edit/SKILL.md` |
| Comment triage + replies in their voice | `skills/yt-comment/SKILL.md` |
| A weekly content plan that fits their hours | `skills/yt-plan/SKILL.md` |
| What's working in their niche (outliers) | `skills/yt-viral/SKILL.md` |
| Why viewers leave (retention export) | `skills/yt-retention/SKILL.md` |
| Shorts cut from a long video | `skills/yt-shorts/SKILL.md` |
| Description, tags, search queries | `skills/yt-seo/SKILL.md` |
| Chapters from a transcript | `skills/yt-chapters/SKILL.md` |
| A whole-channel audit with ONE fix | `skills/yt-audit/SKILL.md` |

## The six tools (Python 3, zero dependencies)
```bash
python3 skills/yt-script/hookscore.py --hook "one line"        # score a hook 0-100
python3 skills/yt-package/title.py --title "..." --thumb "..." # lint title + thumbnail
python3 skills/yt-edit/deadair.py transcript.srt               # dead air / filler / retakes
python3 skills/yt-chapters/chapters.py transcript.srt          # YouTube-valid chapters
python3 skills/yt-retention/retention.py retention.csv         # where viewers left, and why
python3 skills/yt-viral/swipe.py collected.json --min 2.0      # niche outliers by own-channel multiple
```
Run the matching tool whenever a skill calls for it. If your environment
cannot run code, do the steps manually and say so.

## Hard rules (from the original pack — do not break them)
- **Nothing publishes.** Every skill writes; the human uploads. Every
  output ends in a copyable block and the question: **ship it, or change it?**
- **Never invent a number.** If a figure is missing, ask for it or write
  the line without it.
- **Hooks are scored before scripts are written** (`hookscore.py`).
- `/yt-viral` reads public listings only — never log in as the user,
  never touch credentials.
