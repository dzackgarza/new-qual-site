---
schema: qual/card@1
id: E-HAT-3.3-22
kind: problem
title: Compactly supported cohomology and $\times \RR$
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 22; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 22; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the argument: products $K\times I$ are cofinal among compact sets in $X\times\RR$, and the
    relative suspension isomorphism, from the cross product with the generator of $H^1(\RR,\RR-I)$,
    shifts degree by one compatibly with inclusions.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    The step was named a "relative suspension isomorphism" without saying which map it is or why it
    is an isomorphism. It is now written as the relative cross product with the generator of
    $H^1(\RR,\RR\setminus I;\ZZ)$, identified as the relative Künneth formula of Theorem 3.18 p.219
    applied to the two pairs — one term in the sum, no Tor term because the real factor's group is
    $\ZZ$ — with coefficients $G$ reached afterwards by the universal coefficient theorem. The
    cofinality of the products $K\times I$ and compatibility with inclusions are unchanged.
---

::: {.problem}
Show that $H_c^n(X \times \RR; G) \approx H_c^{n-1}(X; G)$ for all $n$.
:::

::: {.solution}
Let $K\subset X$ be compact and $I=[-a,a]\subset\RR$ with $a>0$. The sets $K\times I$ are cofinal among compact subsets of $X\times\RR$: the projections of any compact subset are compact and lie in such a product. The reduction is the relative cross product with the generator $1_I\in H^1(\RR,\RR\setminus I;\ZZ)$,
$$
H^{n-1}(X,X\setminus K;\ZZ)\longrightarrow H^n(X\times\RR,(X\times\RR)\setminus(K\times I);\ZZ),
\qquad \alpha\longmapsto\alpha\times1_I,
$$
and this is an isomorphism because the second pair has cohomology only in degree $1$: the relative Künneth formula (Theorem 3.18 p.219) for the pairs $(X,X\setminus K)$ and $(\RR,\RR\setminus I)$, whose product pair is exactly $(X\times\RR,(X\setminus K)\times\RR\cup X\times(\RR\setminus I))$, has just the single term $\alpha\otimes1_I$ in total degree $n$ and no Tor term, since $H^1(\RR,\RR\setminus I;\ZZ)\cong\ZZ$ is free. For coefficients $G$ the same conclusion follows from the universal coefficient theorem, which introduces the matching $\operatorname{Tor}(H^n(X,X\setminus K;\ZZ),G)$ on both sides. These maps commute with inclusions when $K$ and $I$ increase. Taking the filtered direct limit gives $H_c^n(X\times\RR;G)\cong H_c^{n-1}(X;G)$.
:::
