# Proof artifacts

Machine-checked certificates for mathematical corrections made to corpus cards, kept in
three separate categories. They are not interchangeable.

1. **Group lemmas proved in Lean** — statements about groups, linear maps and tensor
   products, proved here with no `sorryAx`.
2. **Chain-level checks in Sage** — exact computations with Sage's `ChainComplex` on the
   chain complexes a card displays, for the listed values of the parameters. These are
   finite samples of a chain-level statement.
3. **The topological identification** — the step from a chain complex to the homology of
   a space. It is *not* formalized. It is a cited theorem, and the citation and the
   verification of its hypotheses are recorded below.

A finite sample in category 2 does not settle a uniform statement about spaces: the Sage
checks below cover $m\in\{2,3,4,5,6,12\}$ and $n\le8$, and every uniform claim about these
complexes rests on the theorems in category 3, not on the sample.

A source transcription check proves what the source prints; it does not prove the
source's theorem. A counterexample refutes the printed claim but does not establish the
replacement. A correction is marked settled on its card only when a file here certifies it.

## 1. Group lemmas proved in Lean

| File | Card | What it proves |
| --- | --- | --- |
| `cards/FieldHomework1.lean` | `P-FHW1-01` | The printed hypothesis of problem 1(a) holds with $L=\bot$ for every $\alpha$ (the refutation), and both directions of the corrected statement with $L\ne 0$. |
| `cards/SubgroupFiniteness.lean` | `E-HAT-1.A-8` | A group with a finite generating family has finitely many subgroups of a given nonzero index: `finite_hom` and `subgroup_eq_stabilizer_comap`. |
| `cards/NormExtension.lean` | `P-TAMURAS15-10` | For a closed subspace $Y$ of a real normed space and $x\notin Y$: a functional of norm at most one vanishing on $Y$ with $\varphi x\ne0$. |
| `cards/Tamuras15_10.lean` | `P-TAMURAS15-10` | The corrected statement in full, including the `x ∈ Y` case `exists_mem_S` by Hahn--Banach. |
| `cards/MooreSpaceExactness.lean` | `E-HAT-2.3-1` | The group data behind the two exactness failures: $\ZZ/m$ is nontrivial for $m\ge2$ and torsion; a sequence with trivial ends cannot be exact at $\ZZ/m$; multiplication by $m\ge2$ on $\ZZ$ is injective but not surjective. |
| `cards/TorTorsion.lean` | `E-HAT-3.A-6` | The coordinate step of the converse and the refutation of the inference it replaces: `ratchet_le`, `exact_order_smul`, `exists_coord`, `zmod_two_no_exact_order_eight`, `zmod_eight_order_four`. |
| `cards/TorReductions.lean` | `E-HAT-3.A-6` | The presentation-level `Tor` and the parts of Hatcher's Proposition 3A.5 that Mathlib supplies: the free case of (3) (`torKernel_eq_bot_of_subsingleton`), the group in (5) (`torsionBy_eq_ker`), the torsion-free-is-flat hypothesis of (3) (`flat_of_torsionFree`, Mathlib's Dedekind-domain instance), and the flatness form of (6) (`rTensor_injective_of_flat`, Mathlib's `Module.Flat.rTensor_preserves_injective_linearMap`). |

## 2. Chain-level checks in Sage

`cards/DeltaComplexHomology.sage`, run on the Sage development image (11.0.beta5, Python
3.14.10, source HEAD `b0cd7d86e2`; reproduced with `proot -R $HOME/sage-image/rootfs ...`):

| Card | Chain complex checked | Parameter range |
| --- | --- | --- |
| `E-HAT-2.1-4`, `-5`, `-6`, `-9` | the displayed $\Delta$-complex complexes: parachute, Klein bottle, the collapsed complex with $H_1=\ZZ/2^n$, the collapsed $\Delta^n$ | $n\le6$, $n\le8$ |
| `E-HAT-2.2-11` | the cube complex | one case |
| `E-HAT-2.2-19` | $\RP^n/\RP^m$ | $m\le4$, $n\le8$ |
| `E-HAT-2.3-1` | the Moore complex $d_1=0$, $d_2=m$, and the Smith form of $(m)$ on $\ZZ$ | $m\in\{2,3,4,5,6,12\}$ |

Every entry is a finite check of the chain-level statement for the listed parameters. None
of them is a statement about a space, and none settles the corresponding uniform claim.

## 3. The topological identification (cited, hypotheses verified)

For `E-HAT-2.3-1` the passage from the cellular chain complex to the homology of the Moore
space $X=S^1\cup_m e^2$ and of the pair $(X,A)$ with $A=S^1$ is made by three theorems of
Hatcher, whose hypotheses are checked here rather than assumed:

| Theorem | Statement used | Hypotheses, checked |
| --- | --- | --- |
| Theorem 2.35 | $H_n^{CW}(X)\cong H_n(X)$ | $X$ is a CW complex. $X=S^1\cup_m e^2$ has the finite CW structure with one cell in dimensions $0,1,2$. |
| Cellular Boundary Formula (pp. 140--141) | $d_n(e^n_\alpha)=\sum_\beta d_{\alpha\beta}e^{n-1}_\beta$ with $d_{\alpha\beta}$ the degree of the composite attaching map | $X$ is a CW complex with a set cell structure. With one $0$-cell and one $1$-cell, $d_1=0$; the $2$-cell is attached by a degree $m$ map, so $d_2=m$. |
| Proposition 2.22 | for good pairs, $q_*:H_n(X,A)\cong \widetilde H_n(X/A)$ | $(X,A)$ is a good pair: $A$ is a closed subspace that is a deformation retract of a neighbourhood. $A=S^1$ is a subcomplex of the CW complex $X$, so the pair is a good pair, and $X/A\cong S^2$. |

Nothing in category 1 or 2 establishes these; they are the uniform statement, cited from
the source being audited (`pi.math.cornell.edu/~hatcher/AT/AT.pdf`, the same file the
card's source checks use).

## 4. Cited, not formalized

For `E-HAT-3.A-6` the card now cites Hatcher's own Proposition 3A.5 by item number instead
of adverting to standard theory: (2) additivity, (3) vanishing for free or torsion-free
groups, (4) the reduction to the torsion subgroup, (5) $\operatorname{Tor}(\ZZ_n,B)\cong
B[n]$, and (6) the long exact sequence; together with Exercise 4 of §3.A for commutation
with direct limits. `cards/TorReductions.lean` formalizes the parts of (3), (5) and (6) that
are statements about torsion, flatness and tensor products; the comparison theorem (Lemma
3A.2), additivity (2), the torsion reduction (4) and the direct-limit statement (Exercise
4) are cited, and the file records why: Mathlib's `CategoryTheory.Tor` has no long exact
sequence or comparison API to reuse.

## 5. Outstanding obligations

Repairs made to a stored proof whose mathematical content no file here certifies. Each is a
claim of the form "this argument proves the stored statement", and none may be reported as
settled until a file here covers it:

- `E-HAT-2.2-16`, third step: the degree-zero case compares cycles and boundaries in the
  augmented complex, where the quotient is the reduced homology; the ordinary
  $Z_0/B_0$ is $H_0$ and the statement needs $\tilde H_0$. The rank induction runs on
  Pascal's identity.
- `E-HAT-2.3-2`, dimension step: the candidate's dimension axiom is checked at a point,
  with $S^0$ as the same computation.
- `E-HAT-3.A-2`: the restored direction "torsion-free implies $\operatorname{Tor}(A,B)=0$
  for all $B$" is a citation of exercise 5 of the same section.
- The step-level repairs of earlier audits — `E-HAT-1.1-17`, the closing steps of
  `E-HAT-1.2-12`, `-14`, `-16`, the restructuring of `E-HAT-1.2-22`, the rewrites of
  `E-HAT-1.A-8` and the closing steps of `E-HAT-1.A-9`, `-12` — are prose repairs of stored
  proofs and carry no machine certificate.

A `solution-reviewed` note on a card records that the proof was read and what was checked;
it is a review record, not a certificate.

## Checking

Lean 4.33.1 with the Mathlib on `LEAN_PATH`, and Sage for the integer linear algebra:

```sh
lean proofs/cards/MooreSpaceExactness.lean
lean proofs/cards/TorTorsion.lean
lean proofs/cards/TorReductions.lean
lean proofs/cards/FieldHomework1.lean
sage proofs/cards/DeltaComplexHomology.sage
```

`#print axioms` at the end of each file must show only `propext`, `Classical.choice` and
`Quot.sound`; any appearance of `sorryAx` means the certificate is not a proof.
