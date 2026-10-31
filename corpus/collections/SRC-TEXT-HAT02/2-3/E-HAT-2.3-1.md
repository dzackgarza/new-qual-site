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
---

::: {.problem}
If $T_n(X, A)$ denotes the torsion subgroup of $H_n(X, A; \ZZ)$, show that the functors $(X, A) \mapsto T_n(X, A)$, with the obvious induced homomorphisms $T_n(X, A) \to T_n(Y, B)$ and boundary maps $T_n(X, A) \to T_{n-1}(A)$, do not define a homology theory.
Do the same for the 'mod torsion' functor $MT_n(X, A) = H_n(X, A; \ZZ) / T_n(X, A)$.
:::

::: {.solution}
The exactness axiom fails for both constructions, already on the Moore-space pair $(X,A)$ in which $X$ is obtained from $A=S^1$ by attaching a $2$-cell by a degree-$m$ map, $m>1$.

::: pf

::: {.pf-step #s1}

For that pair the integral long exact sequence reads
$$
0=H_2(X)\longrightarrow H_2(X,A)\cong\ZZ\xrightarrow{\partial=m}\ZZ\cong H_1(A)
\longrightarrow H_1(X)\cong\ZZ_m\longrightarrow H_1(X,A)=0.
$$

::: pf-proof

The cellular chain complex of $X$ is $\ZZ\xrightarrow{m}\ZZ\to\ZZ$, so $H_2(X)=0$ and $H_1(X)\cong\ZZ_m$. Because $(X,A)$ is a good pair with $X/A\cong S^2$, the relative group is $H_2(X,A)\cong H_2(S^2)\cong\ZZ$, and the connecting map is multiplication by the attaching degree $m$. Finally $H_1(A)\to H_1(X)$ is onto, so $H_1(X,A)=0$.

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
