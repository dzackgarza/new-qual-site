# Traps

Mechanical traps met while editing cards, each with the symptom and the repair. They are not
policy: the policies are in [AGENTS.md](AGENTS.md) and [CONTRIBUTING.md](CONTRIBUTING.md).

## `\restrict` and `\restriction` are different tokens

`vocabularies/macros.json` defines `\restrict` as `\vert`, so a card that writes
`F\restrict_{\partial D^2}` renders $F$ with a bar subscript. The semantic macro for a
restriction to a subset is `\restrictionof{X}{A}`.

**Symptom.** A `fs_edit` whose `old` text says `\restriction` on a card that wrote
`\restrict` fails with "old was not found in the file", even though the sentence is visibly
present.

**Repair.** Read the card's actual bytes before matching — `sed -n 'N,Mp' file | cat -A`, or a
one-line Python `repr` of the line — and match what is there. Do not rewrite `\restrict` to
`\restrictionof` as part of an unrelated edit: `\restrict` is a defined macro and its use is a
notation choice, not a defect (`STYLE-04` governs raw bars, which this is not).

## A `pf-proof` goes after the whole claim, displays included

In the Lamport markup a step is its claim, then exactly one `::: pf-proof`, then the step's
closing `:::`. Anything that belongs to the claim — prose and every `$$ … $$` display — must come
before the proof div.

**Symptom.** Inserting a proof body between a step's prose and a trailing display gives
`lamport proof: unknown div inside a proof step` from the filter, even though the fences balance
and `report_check.py` may report nothing else. Inserting a proof body in place of a step's closing
`:::` instead gives `unclosed fenced div` from `report_check.py`, or silently nests the next step
inside this one.

**Repair.** Move the claim's remaining lines above the proof div, then close the step. Recount the
closers afterwards: a step that gains a proof body needs its own `:::` **in addition to** the one
that closes the div, and a container step's `pf-proof` needs its own closer too. The cheap
instrument is a depth listing:

```
python3 -c "
lines=open('PATH',encoding='utf-8').read().split('\n')
d=0
for i,l in enumerate(lines,1):
    s=l.strip()
    if s==':::': d-=1; print(i,'CLOSE ->',d)
    elif l.startswith(':::'): d+=1; print(i,'OPEN',d,l[:60])
print('final depth',d)"
```

Depth must return to $0$, each `pf-step` opens exactly one level under its `pf` or `pf-proof`,
and a `pf-qed` is the last step of its own level — so it is a sibling of the `pf-step`s, never
inside one.
