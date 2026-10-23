#!/usr/bin/env python3
"""Install the YouTube Agent pack for whichever AI you use.

The skills themselves are AI-agnostic — this script just puts the right
files in the right place for each agent:

    python3 install.py --target claude-code   # ~/.claude/skills/
    python3 install.py --target muse          # Muse custom-skills folder
    python3 install.py --target codex         # AGENTS.md router + skills/ into a project
    python3 install.py --target gemini        # GEMINI.md + AGENTS.md + skills/ into a project
    python3 install.py --target cursor        # .cursor/rules/ + skills/ into a project
    python3 install.py --target generic       # SYSTEM_PROMPT.md + skills/ into a folder

Add --dest PATH to override where files go.
Original pack by Jake Schincariol (MIT). Universal packaging: fouzkhan-dev.
"""
import argparse
import shutil
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent
HOME = Path.home()


def copy_skills(dest: Path):
    dest.mkdir(parents=True, exist_ok=True)
    skills = sorted((SRC / "skills").glob("yt-*"))
    for s in skills:
        target = dest / s.name
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(s, target)
    return len(skills)


def copy_file(name: str, dest: Path, sub: str = ""):
    d = dest / sub if sub else dest
    d.mkdir(parents=True, exist_ok=True)
    shutil.copy2(SRC / name, d / Path(name).name)


def copy_tree(name: str, dest: Path):
    target = dest / name
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(SRC / name, target)


def main():
    ap = argparse.ArgumentParser(description="Install YouTube Agent for any AI")
    ap.add_argument("--target", required=True,
                    choices=["claude-code", "muse", "codex", "gemini", "cursor", "generic"],
                    help="which AI you use")
    ap.add_argument("--dest", default=None, help="override install folder")
    a = ap.parse_args()
    dest = Path(a.dest).expanduser() if a.dest else None

    if a.target == "claude-code":
        d = dest or (HOME / ".claude" / "skills")
        n = copy_skills(d)
        voice_dir = HOME / ".claude" / "youtube"
        voice_dir.mkdir(parents=True, exist_ok=True)
        voice = voice_dir / "voice.md"
        if not voice.exists():
            shutil.copy2(SRC / "templates" / "voice.md", voice)
        print(f"Installed {n} skills -> {d}")
        print(f"Voice file -> {voice} (fill it in!)")
        print("Restart Claude Code, then try: /yt-script")

    elif a.target == "muse":
        d = dest or (HOME / "workspace" / "custom-skills")
        n = copy_skills(d)
        print(f"Installed {n} skills -> {d}")
        print("Muse picks them up as custom skills automatically.")

    elif a.target in ("codex", "gemini", "cursor", "generic"):
        d = dest or Path.cwd()
        d.mkdir(parents=True, exist_ok=True)
        copy_tree("skills", d)
        copy_tree("templates", d)
        copy_file("config.example.json", d)
        if a.target == "codex":
            copy_file("AGENTS.md", d)
            print(f"Installed AGENTS.md router + skills/ -> {d}")
            print("Open this project with your agent and ask for a script — it routes itself.")
        elif a.target == "gemini":
            copy_file("GEMINI.md", d)
            copy_file("AGENTS.md", d)
            print(f"Installed GEMINI.md + AGENTS.md + skills/ -> {d}")
        elif a.target == "cursor":
            copy_file("adapters/cursor/youtube-agent.mdc", d, sub=".cursor/rules")
            # the rule file must be named youtube-agent.mdc in .cursor/rules
            installed = d / ".cursor" / "rules" / "youtube-agent.mdc"
            src_rule = SRC / "adapters" / "cursor" / "youtube-agent.mdc"
            shutil.copy2(src_rule, installed)
            copy_file("AGENTS.md", d)
            print(f"Installed Cursor rule + AGENTS.md + skills/ -> {d}")
        else:
            copy_file("SYSTEM_PROMPT.md", d)
            print(f"Installed SYSTEM_PROMPT.md + skills/ -> {d}")
            print("Paste SYSTEM_PROMPT.md into your AI, then paste any skills/yt-*/SKILL.md you need.")

    else:  # argparse prevents this
        sys.exit(2)


if __name__ == "__main__":
    main()
