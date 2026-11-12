---
schema: qual/card@1
id: E-HAT-2.3-1
kind: problem
title: Torsion subgroup and mod-torsion functor do not define homology theories
classification:
  areas:
  - topology
  topics:
  - Homology
  - Axiomatic Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.3, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: >-
    Statement compared with Hatcher, Algebraic Topology, Section 2.3, Exercise 1, and it matches the
    printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the argument and rewrote it. The earlier version computed the torsion of the pair
    $(D^2,S^1)$ and then said that this example does not detect the failure; that false start is
    removed and the proof now runs on the single Moore-space pair. On that pair $H_1(X,A)=0$ and
    $T_1(X)=\ZZ_m$ with $T_1(A)=T_2(X,A)=0$, so the torsion sequence cannot be exact at $T_1(X)$, and
    the mod-torsion sequence fails at $MT_1(A)$ because $m\ZZ\ne\ZZ$.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Certificates for the rewritten proof, which the earlier note left as an obligation.
    <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/MooreSpaceExactness.lean> certifies the group theory: $\ZZ/m$ is nontrivial for
    $m\ge2$ (`nontrivial_zmod`) and torsion (`nsmul_eq_zero_zmod`), a sequence with trivial ends
    cannot be exact at $\ZZ/m$ (`subsingleton_of_kernel_eq_range`, applied in `torsion_not_exact`),
    and multiplication by $m\ge2$ on $\ZZ$ is injective (`mul_eq_zero_int`) but not surjective
    (`not_surjective_mul`, `mod_torsion_not_exact`). proofs/cards/DeltaComplexHomology.sage
    certifies the cellular data: the complex with $d_1=0$, $d_2=m$ has homology $\ZZ$, $\ZZ/m$, $0$
    for $m=2,3,4,5,6,12$, and the Smith form of $(m)$ is $(m)$. The identification of these groups
    with the homology of the Moore pair is Hatcher's cellular computation and is not formalized.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    The identification of the chain complexes with the homology of the space is not formalized and
    is not claimed to be: it is Hatcher's Theorem 2.35 for the finite CW structure with one cell in
    dimensions $0,1,2$, the Cellular Boundary Formula of §2.2 giving $d_1=0$ and $d_2=m$, and
    Proposition 2.22 for the good pair $(X,A)$ with $A=S^1$ a subcomplex and $X/A=S^2$.
    proofs/README.md records these three citations with their hypotheses checked, separately from
    the Lean group lemmas and from the Sage sample, which covers only $m\in\{2,3,4,5,6,12\}$ and
    does not settle the uniform statement.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Statement matches Exercise 1 of §2.3 as printed on p. 165, both functors included. The
    Moore-space counterexample was recomputed: with X = S^1 with a 2-cell attached by a degree m
    map, H_2(X)=0, H_1(X)=Z_m, H_2(X,A)=Z and the connecting map is m, so T_1(X)=Z_m sits between
    two vanishing torsion groups, and for MT the segment Z -m-> Z -> 0 is not exact at the middle
    term. Results now cited: the axioms of p. 160, Theorem 2.35 p. 139 with the Cellular Boundary
    Formula p. 141, Proposition 2.22 p. 124 and Corollary 2.14 p. 114. What is not covered: no
    certificate.
---

::: {.problem}
If $T_n(X, A)$ denotes the torsion subgroup of $H_n(X, A; \ZZ)$, show that the functors $(X, A) \mapsto T_n(X, A)$, with the obvious induced homomorphisms $T_n(X, A) \to T_n(Y, B)$ and boundary maps $T_n(X, A) \to T_{n-1}(A)$, do not define a homology theory.
Do the same for the 'mod torsion' functor $MT_n(X, A) = H_n(X, A; \ZZ) / T_n(X, A)$.
:::

::: {.solution}
The exactness axiom fails for both constructions, already on the Moore-space pair $(X,A)$ in which $X$ is obtained from $A=S^1$ by attaching a $2$-cell by a degree-$m$ map, $m>1$. The axioms are those of p. 160, and the exactness axiom is the one requiring a long exact sequence for a CW pair.

::: pf

::: {.pf-step #s1}

For that pair the integral long exact sequence reads
$$
0=H_2(X)\longrightarrow H_2(X,A)\cong\ZZ\xrightarrow{\partial=m}\ZZ\cong H_1(A)
\longrightarrow H_1(X)\cong\ZZ_m\longrightarrow H_1(X,A)=0.
$$

::: pf-proof

The cellular chain complex of $X$ is $\ZZ\xrightarrow{m}\ZZ\to\ZZ$, so $H_2(X)=0$ and $H_1(X)\cong\ZZ_m$; the chain complex of a cell complex and the Cellular Boundary Formula are those of Theorem 2.35 (p. 139) and p. 141. Because $(X,A)$ is a good pair with $X/A\cong S^2$, the relative group is $H_2(X,A)\cong H_2(S^2)\cong\ZZ$ by Proposition 2.22 (p. 124) with Corollary 2.14 (p. 114), and the connecting map is multiplication by the attaching degree $m$, which is the cellular boundary $d_2$ of p. 141 read through that identification. Finally $H_1(A)\to H_1(X)$ is onto, so $H_1(X,A)=0$.

:::

:::

::: pf-step

$T_*$ is not exact on this pair.

::: pf-proof

Every group in the displayed sequence except $H_1(X)$ is torsion-free, so $T_2(X)$, $T_2(X,A)$, $T_1(A)$ and $T_1(X,A)$ all vanish, while $T_1(X)=\ZZ_m$. The sequence of torsion groups therefore contains
$$
T_1(A)=0\longrightarrow T_1(X)=\ZZ_m\longrightarrow T_1(X,A)=0,
$$
which is exact at $T_1(X)$ only if $\ZZ_m=0$.

:::

:::

::: pf-step

$MT_*$ is not exact on this pair.

::: pf-proof

Quotienting the integral sequence by its torsion subgroups gives
$$
MT_2(X,A)\cong\ZZ\xrightarrow{m}MT_1(A)\cong\ZZ\longrightarrow MT_1(X)=0,
$$
and exactness at $MT_1(A)$ would require $m\ZZ=\ZZ$, which fails for $m>1$.

:::

:::

:::

Thus neither $T_*$ nor $MT_*$ satisfies the exactness axiom, so neither defines a homology theory.
:::
