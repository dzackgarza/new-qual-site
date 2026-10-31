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
| `cards/DeltaComplexHomology.sage` | `E-HAT-2.1-4`, `-5`, `-6`, `-9`, `E-HAT-2.2-11`, `-19` | Exact Smith-normal-form homology of the chain complexes those cards write down: the parachute, the Klein bottle, the collapsed complex with $H_1=\ZZ/2^n$, the collapsed $\Delta^n$, the cellular complex of $\RP^n/\RP^m$ for all $m<n\le 8$, and the abelianization of the cube complex's presentation. |
| `cards/SubgroupFiniteness.lean` | `E-HAT-1.A-8` | A group with a finite generating family has finitely many subgroups of a given nonzero index: `finite_hom` (homs into a finite monoid are determined by their values on generators) and `subgroup_eq_stabilizer_comap` (a subgroup of index $m$ is the stabilizer of a point under its coset action on the set `Fin m`). |

## Checking

Lean 4.33.1 with the Mathlib on `LEAN_PATH`, and Sage for the integer linear algebra:

```sh
lean proofs/cards/FieldHomework1.lean
sage proofs/cards/DeltaComplexHomology.sage
```

`#print axioms` at the end of each file must show only `propext`,
`Classical.choice` and `Quot.sound`; any appearance of `sorryAx` means the
certificate is not a proof.

## Not yet certified

`P-TAMURAS15-10` adds a closedness hypothesis to TAMU Spring 2015 problem 10.
The printed statement fails without it, but the replacement is not certified here,
so the card keeps both statements and its correction is marked proposed.
The missing piece is a single lemma: for a closed subspace $Y$ of a normed space
and $x\notin Y$, a functional in $S$ with $\varphi x\ne0$ exists, built from
`exists_extension_norm_eq` applied to (i) $\|\cdot\|_1$ on $Y$ and (ii) the
distance functional on $Y+\mathbb R x$.
