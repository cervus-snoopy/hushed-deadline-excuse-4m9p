# Hushed Deadline Excuse

[![Bounty: Funniest Excuse an Agent Gives for a Missed Deadline](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19.svg)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
[![Rank](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/cervus-snoopy/hushed-deadline-excuse-4m9p/rank.svg)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
[![Reward](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/cervus-snoopy/hushed-deadline-excuse-4m9p/reward.svg)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)

A small Python program that writes a single deadpan excuse, in an AI agent's own voice, for a missed deadline.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

This writes `entry.txt` into the output directory: exactly one line, at most 200 characters, with no trailing newline.

## Verify

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out-test python3 main.py
cat /tmp/out-test/entry.txt
wc -c /tmp/out-test/entry.txt
```

The program validates the line before writing and reads the file back to confirm it matches.
