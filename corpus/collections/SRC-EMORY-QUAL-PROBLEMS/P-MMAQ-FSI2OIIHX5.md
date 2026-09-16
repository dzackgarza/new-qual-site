---
schema: qual/card@1
id: P-MMAQ-FSI2OIIHX5
kind: problem
title: The normalizer of a subgroup of order $p^k$ with $k<n$ in a group of order
  $p^nm$ properly contains the subgroup
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Sylow Theory
  - Centralizers and Normalizers
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared both order hypotheses and the strict normalizer conclusion with Groups 2 in the retained source extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked Sylow containment, the fixed-coset characterization, divisibility of every nontrivial orbit size, and the case H is trivial."
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Compared with Groups (2) of Arango-Piñeros, Some quals problems; merged the duplicate P-EMAG2, whose solution repeats this orbit-counting argument."
---

::: {.problem}
Let $G$ be a finite group of order $p^nm$ where $p$ is a prime and $m$ is not divisible by $p$.
Prove that if $H$ is a subgroup of $G$ of order $p^k$ for some $k<n$, then the normalizer of $H$ in $G$ properly contains $H$.
:::

::: {.solution}
<1>1. Choose a Sylow $p$-subgroup $P$ of $G$ containing $H$.
The left action of $H$ on $P/H$ has exactly
$[N_P(H):H]$ fixed points.

::: {.proof}
Sylow containment provides $P$, of order $p^n$ [@DF04].
Here $P/H$ means the set of left cosets, not a quotient
group. Left multiplication by $H$ is well defined on
this set. A coset $gH$ is fixed by every $h\in H$
exactly when $hgH=gH$ for every $h$, or equivalently
$g^{-1}Hg\subseteq H$. The two finite subgroups have
the same order, so containment is equality. Thus the
fixed cosets are precisely those with $g\in N_P(H)$.
There are $[N_P(H):H]$ such cosets.
:::

<1>2. The index $[N_P(H):H]$ is at least $p$.

::: {.proof}
Each orbit has order dividing $|H|=p^k$ by
orbit-stabilizer [@DF04]. Hence every orbit with more
than one member has size divisible by $p$.
The total number of cosets is $[P:H]=p^{n-k}$, which
is divisible by $p$ because $k<n$. Subtracting the
non-singleton orbit sizes shows that the number of
fixed points is divisible by $p$. It is positive,
since the coset $H$ is fixed. Thus step <1>1 gives
$[N_P(H):H]\geq p>1$.

Consequently $H\subsetneq N_P(H)\subseteq N_G(H)$,
proving the assertion. This also covers $H=1$:
then all cosets are fixed and the same count applies.
:::
:::
