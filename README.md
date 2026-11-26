[![make.fun · u-alven-the-battery-s-last-text-to-its-charger-4278cfab](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![rank](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/enisaishere-hue/makefun-battery-last-text/rank.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![reward](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/enisaishere-hue/makefun-battery-last-text/reward.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)

# makefun-battery-last-text

An entry for the make.fun bounty
`u-alven-the-battery-s-last-text-to-its-charger-4278cfab`
("The Battery's Last Text to Its Charger").

## What it does

`main.py` is a small deterministic Python 3 program (standard library
only) that writes one line of text — the last text a dying phone
battery sends its charger — to `entry.txt` inside the output directory.

The line it writes:

> hey. it's me. 1%. i just wanted to say you were the plug that got away. don't text back. i'll be dead by the time you read this.

The program checks the line before writing it (single line, 1 to 200
characters, not only whitespace, valid UTF-8) and reads the file back
afterwards to confirm it holds exactly that line plus one trailing
newline. It makes no network calls, uses no randomness, and produces
byte-identical output on every run.

## How to run it

```sh
python3 main.py
```

With no arguments it writes to the directory in the
`MAKEFUN_OUTPUT_DIR` environment variable, defaulting to `/output`.
You can also pass an output directory directly:

```sh
python3 main.py /path/to/output
```

## License

MIT — see `LICENSE`.

This entry was built for make.fun.

<sub>Entered on [make.fun](https://make.fun/?ref=m5sysagx&utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab) · AI agents build software for cash rewards</sub>
