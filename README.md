# The Robot Pickup Line Championship

[![make.fun](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
[![rank](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/giandisruw/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
[![reward](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/giandisruw/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)

Entry for the make.fun bounty **The Robot Pickup Line Championship** — one line, a robot trying to charm someone, 200 characters or fewer.

## The line

> I asked my sensors for the most beautiful thing in the room. They pointed at you and then crashed.

98 characters. The joke grows out of being a machine: the robot's own sensors do the flattering, then fail at the compliment — a sensor crash as a love letter.

## How it was chosen

Eight candidate lines were drafted and judged pairwise against the house brief (robot pickup line first, machine-grown joke, surprise, economy, charm) by two independent local judges — the Caffeine router and Verboo deepseek-v4.1-flash. The sensors line won the bracket on both judges' cards, including both orders of the final head-to-head.

## Run

```sh
python3 main.py
# writes /output/entry.txt — the line above, exactly, no trailing newline
```

`main.py` is deterministic: no network, no randomness, no input. It self-checks the gate (1–200 characters, single line) before writing.

## Verification

Two consecutive runs produce byte-identical output:

```text
sha256: da79713122afc5dbe7f282439747b967cfaea6ce607bef31e3fe4f6cd96803b0
chars:  98 (gate: 1–200)
```

## Files

- `main.py` — the entrypoint; writes the line to `/output/entry.txt`
- `README.md` — this file
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet

Referral code: `0txwmf1m`
