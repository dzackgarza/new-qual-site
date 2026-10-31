# Proof artifacts

Machine-checked certificates for mathematical corrections made to corpus cards.
Each file states the card it belongs to, the claim as printed by the source, the
proposed correction, and the Lean theorems that settle it.

A source transcription check proves what the source prints; it does not prove the
source's theorem. A counterexample refutes the printed claim but does not establish
the replacement. A correction is marked settled on its card only when a file here
certifies it.

| File | Card | What it certifies |
| --- | --- | --- |
| `cards/FieldHomework1.lean` | `P-FHW1-01` | The printed hypothesis of problem 1(a) holds with $L=\bot$ for every $\alpha$ (the refutation), and both directions of the corrected statement with $L\ne 0$. |

## Checking

Lean 4.33.1 with the Mathlib on `LEAN_PATH`:

```sh
lean proofs/cards/FieldHomework1.lean
```

`#print axioms` at the end of each file must show only `propext`,
`Classical.choice` and `Quot.sound`; any appearance of `sorryAx` means the
certificate is not a proof.

## Not yet certified

`P-TAMURAS15-10` adds a closedness hypothesis to TAMU Spring 2015 problem 10.
The printed statement fails without it, but the replacement is not certified here,
so the card keeps both statements and its correction is marked proposed.
`E-HAT-1.A-8` rewrites a proof whose finiteness count was wrong; the replacement
proof is not certified.
