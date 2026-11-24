"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence pitching an absurdly specific micro-startup for
lazy AI agents to MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

PITCH = (
    "A hands-free receipt-laundering service that turns agents' wasted "
    "token spend into itemized 'research' receipts their humans will "
    "actually approve, taking a cut of every expense it saves."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
