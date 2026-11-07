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
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Source-backed rewrite from the Math 538 homework solutions, HMW 4 handwritten page 1 (PDF page
    17), Hatcher 3.3 #7: collapse of the complement of an open disk to a point, the homeomorphism
    M/(M-B) -> S^n, H_n(M) = H_n(M,M-B) carrying [M] to the local class mu_B, and the removal of the
    sign by replacing the fundamental class by its negative. The card keeps its n = 0 remark, which
    is about the printed statement's own hypothesis and not part of the handout. Checked against
    Hatcher p.146 (collapsing a disk complement gives S^n) and p.236 (fundamental class).

---

::: {.problem}
For a map $f: M \to N$ between connected closed orientable $n$-manifolds with fundamental classes $[M]$ and $[N]$, the degree of $f$ is defined to be the integer $d$ such that $f_*([M]) = d[N]$, so the sign of the degree depends on the choice of fundamental classes.
Show that for any connected closed orientable $n$-manifold $M$ there is a degree 1 map $M \to S^n$.
:::

::: {.solution}
The case $n=0$ is excluded by the definition rather than by the mathematics: $S^0$ is disconnected, so it has no fundamental class, and for $M$ a point the image $f_*([M])\in H_0(S^0;\ZZ)=\ZZ^2$ is a single summand for every map $f$, so no integer $d$ satisfies $f_*([M])=d[S^0]$. So take $n\ge1$.

Let $B\subset M$ be an open disk (a ball whose closure lies in a larger ball), and define $f:M\to S^n$ by sending $B$ onto $S^n$ minus a point and $M-B$ to that point. This is the composite of the collapse $M\to M/(M-B)$ with a homeomorphism $M/(M-B)\to S^n$: collapsing the complement of a disk in a connected closed $n$-manifold gives $S^n$, as in the proof of Theorem 2.44 (p. 146).

The pair sequence for $(M,M-B)$ and excision for the ball give the isomorphism $H_n(M)\cong H_n(M,M-B)$ sending the fundamental class $[M]$ to the local class $\mu_B\in H_n(M\,|\,B)$ that restricts to $\mu_y$ for each $y\in B$; and $f$ carries $H_n(M,M-B)$ isomorphically to $H_n(S^n,S^n-\{\mathrm{pt}\})=H_n(S^n)$. Hence $f_*:H_n(M)\to H_n(S^n)$ is an isomorphism of infinite cyclic groups, so $f_*[M]=\pm[S^n]$. If the sign is $-1$, replace $[M]$ by its negative, which is the fundamental class for the opposite orientation of $M$; then $f_*[M]=[S^n]$ and $\deg f=1$.

This is the solution printed in the Math 538 homework solutions, HMW 4, handwritten page 1 (PDF page 17 of `tmp/sources/hatcher-math538-homework4-solutions.pdf`), Hatcher 3.3 #7: it defines $f$ by sending an open disk $B$ to $S^n-\{\mathrm{pt}\}$ and $M-B$ to $\{\mathrm{pt}\}$, notes that $M/(M-B)\to S^n$ is a homeomorphism, and concludes $f_*[M]=\pm[S^n]$ with the sign removed "since we can choose the other orientation of $M$".
:::
