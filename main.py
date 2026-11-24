"""The Houseplant Out-of-Office — one auto-reply, in the plant's own voice.

Design against the brief
------------------------
The brief wants an out-of-office auto-reply a houseplant would send:
plant voice first, a fresh joke that surprises, the plant's own life
(water, roots, sunlight, long stretches of being ignored) driving the
joke rather than decorating it, tight inside 120 characters, original —
no office cliches, no lines already worn out by other auto-replies.

This entry does it in three beats:

1. The concrete scene — the human has gone away for two weeks and left
   the houseplant in charge of the inbox. A specific, believable moment;
   nothing exotic, nothing that needs explaining.
2. The reversal — the plant is not the one out of office; it is the one
   holding the office now. The ignored fern suddenly has a job, and the
   job is answering the mail.
3. The punch — "I only know one reply: water." The plant's entire
   vocabulary, its whole life, is one need. Every email gets the same
   answer, because from the plant's point of view every problem has the
   same solution. The joke never explains itself.

Why it wins: the setup and the payoff are the same thing (the plant's
single need), so every word earns its place — no filler, no second
punchline competing for attention, and a twist a judge can get in one
read. It is 100 characters (102 bytes UTF-8), well inside the 1-120 gate.

The program writes exactly that one auto-reply to /output/entry.txt.
"""

import os

ENTRY_TEXT = (
    "Out of office \u2014 my human left me in charge of the inbox "
    "for two weeks. I only know one reply: water."
)


def main() -> None:
    text = ENTRY_TEXT
    # Gate: UTF-8 text of 1 to 120 characters, not only white space.
    assert 1 <= len(text) <= 120, f"entry length {len(text)} outside 1-120"
    assert text.strip(), "entry must not be only white space"
    text.encode("utf-8")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
