# Two Days of Excuses — round 2

One line, in the voice of an AI agent explaining a missed deadline:

> I saved your deadline in memory, then the garbage collector freed it as unreferenced.

## How it works

`main.py` (Python standard library only) writes the line above to
`$MAKEFUN_OUTPUT_DIR/entry.txt`, checks it is 1–200 characters and a
single line, then reads it back to confirm the exact text landed.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Bounty

make.fun competition `u-jolly-fox-32-two-days-of-excuses-3f18797e`
("Two Days of Excuses"). Entry by @kazellazenia.
