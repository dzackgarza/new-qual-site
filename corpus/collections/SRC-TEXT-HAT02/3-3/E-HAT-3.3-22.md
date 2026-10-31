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
---

::: {.problem}
Show that $H_c^n(X \times \RR; G) \approx H_c^{n-1}(X; G)$ for all $n$.
:::

::: {.solution}
Let $K\subset X$ be compact and $I=[-a,a]\subset\RR$ with $a>0$. The sets $K\times I$ are cofinal among compact subsets of $X\times\RR$: the projections of any compact subset are compact and lie in such a product. By the relative suspension isomorphism,
$$
H^n(X\times\RR,(X\times\RR)\setminus(K\times I);G)
\cong H^{n-1}(X,X\setminus K;G).
$$
Indeed, the complement on the left is $(X\setminus K)\times\RR\,\cup\,X\times(\RR\setminus I)$. The relative cochain product with the generator of $H^1(\RR,\RR\setminus I;\ZZ)$ gives the displayed isomorphism, equivalently by excision and the suspension isomorphism for the pair $(X,X\setminus K)$. These maps commute with inclusions when $K$ and $I$ increase. Taking the filtered direct limit gives $H_c^n(X\times\RR;G)\cong H_c^{n-1}(X;G)$.
:::
