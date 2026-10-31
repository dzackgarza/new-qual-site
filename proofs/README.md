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
| `cards/NormExtension.lean` | `P-TAMURAS15-10`, partial | For a closed subspace $Y$ of a real normed space and $x\notin Y$: a functional of norm at most one vanishing on $Y$ with $\varphi x\ne0$, built from the normed quotient, `exists_dual_vector` and `Submodule.Quotient.norm_mk_le`. |

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
`cards/NormExtension.lean` now covers the case $x\notin Y$. The remaining half is
$x\in Y$, and it needs no second norm structure on $Y$: the analytic Hahn--Banach
theorem `exists_extension_of_le_sublinear` extends a linear functional from
$\operatorname{span}\{x\}$ to $Y$ against the sublinear function $\|\cdot\|_1$,
giving $|f y|\le\|y\|_1$ with $f x=\|x\|_1$. The precise remaining step is to
build the partial linear map on $\operatorname{span}\{x\}$ with value $\|x\|_1$
(in Mathlib terms a `LinearPMap` with that domain), apply that theorem, and then
extend the resulting bounded functional to $E$ by `exists_extension_norm_eq`,
whose bound is $\le K\|\cdot\|$ because $\|y\|_1\le K\|y\|$.
