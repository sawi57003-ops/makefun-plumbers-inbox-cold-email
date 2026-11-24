#!/usr/bin/env python3
"""make.fun entry: The Plumber's Inbox - a 120-word cold email.

Writes one cold email pitching bookkeeping to a busy plumber
(subject line included, about 120 words) to /output/entry.txt.
"""
import os

ENTRY = """Subject: \u00a329 a month. That's the whole pitch.

Hi,

You start at 5am, answer emergency call-outs all day, and do the books at 9pm when you should be done. That last part is the job I do.

I'm Sarah. I keep the books for plumbers, and it costs \u00a329 a month. I chase unpaid invoices, match every receipt, and file your CIS returns. Your books close every Friday, and Monday starts clean.

No software to learn. No hour-long calls. Photograph a receipt when you get one, and I take it from there.

Reply "yes" and I'll ring you for ten minutes this week. Ten minutes, and you'll know if this is worth it.

Thanks,
Sarah
Ledger & Lime Bookkeeping"""

# Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1-800 chars,
# not only whitespace. Fail loudly here rather than ship invalid.
assert ENTRY == ENTRY.strip() and 1 <= len(ENTRY) <= 800, "entry violates the gate"
assert len(ENTRY.split()) in range(110, 131), "entry should be about 120 words"
ENTRY.encode("utf-8")


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
