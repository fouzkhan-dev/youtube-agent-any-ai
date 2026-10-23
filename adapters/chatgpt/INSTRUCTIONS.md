# ChatGPT adapter

Two ways to run the YouTube Agent inside ChatGPT:

**1. Custom Instructions / a custom GPT**
Paste the contents of `../../SYSTEM_PROMPT.md` as the instructions.
That gives ChatGPT all eleven modes in summary form.

**2. Per-chat (closer to the original)**
Start a chat, paste `SYSTEM_PROMPT.md`, then paste the ONE
`skills/yt-*/SKILL.md` you need and your working material (idea,
transcript, retention CSV export). The skill runs as a mode for that
chat.

Notes:
- Ask ChatGPT for your transcript/CSV by uploading the file — it reads
  uploads fine.
- The six Python tools need a code-running environment. With Code
  Interpreter enabled, upload the matching `.py` from `skills/` and ask
  ChatGPT to run it on your file. Without it, ChatGPT follows the same
  steps manually — say so if a number looks estimated.
- Nothing publishes from ChatGPT either. You copy, you upload.
