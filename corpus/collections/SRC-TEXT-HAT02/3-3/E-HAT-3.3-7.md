---
schema: qual/card@1
id: E-HAT-3.3-7
kind: problem
title: Degree 1 maps to $S^n$
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 7; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 7; it matches the printed text. The card makes the implicit $n>0$ explicit.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the construction: collapse the complement of an orientation-compatible ball, giving a map
    to $B/\partial B=S^n$ of local degree 1 at an interior regular value.
- event: source-checked
  by: claude
  date: 2026-11-07
  note: >-
    Re-read against the printed exercise (p.258) and restored the printed sentence, which has no
    $n>0$; the card's earlier note called that hypothesis implicit, and it is now shown to be
    forced by the definition: for $n=0$ the target $S^0$ is disconnected, has no fundamental class,
    and $f_*([M])$ is one summand of $\ZZ^2$, so no degree is defined. The solution now says this
    instead of assuming it, and the construction for $n\ge1$ is unchanged.
---

::: {.problem}
For a map $f: M \to N$ between connected closed orientable $n$-manifolds with fundamental classes $[M]$ and $[N]$, the degree of $f$ is defined to be the integer $d$ such that $f_*([M]) = d[N]$, so the sign of the degree depends on the choice of fundamental classes.
Show that for any connected closed orientable $n$-manifold $M$ there is a degree 1 map $M \to S^n$.
:::

::: {.solution}
The case $n=0$ is excluded by the definition rather than by the mathematics: $S^0$ is disconnected, so it has no fundamental class, and for $M$ a point the image $f_*([M])\in H_0(S^0;\ZZ)=\ZZ^2$ is a single summand for every map $f$, so no integer $d$ satisfies $f_*([M])=d[S^0]$. So take $n\ge1$.

Choose an embedded closed $n$-ball $B\subset M$ whose interior is orientation-compatible with the chosen fundamental class $[M]$. Collapse the complement of the interior of $B$ to a point:
$$
q:M\longrightarrow M/(M-\operatorname{int}B).
$$
The quotient is naturally homeomorphic to
$$
B/\partial B\cong S^n.
$$
Choose the final homeomorphism $B/\partial B\to S^n$ to preserve orientation on the interior of $B$.

Let $f:M\to S^n$ be the resulting map. For a point $y$ in the image of $\operatorname{int}B$, the preimage $f^{-1}(y)$ consists of one point and $f$ is an orientation-preserving local homeomorphism there. By the local-degree formula, $\deg f=1$. Equivalently, the quotient map sends $[M]$ to the fundamental class of $B/\partial B$.

Thus every connected closed orientable $n$-manifold admits a degree-$1$ map to $S^n$.
:::
