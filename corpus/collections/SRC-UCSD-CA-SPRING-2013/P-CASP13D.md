---
schema: qual/card@1
id: P-CASP13D
kind: problem
title: "Counting zeros of a degree-7 polynomial in the unit disk"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into a Lamport proof and checked it: the splitting
    f = 6z^3 + (z^7 - 2z^5 - z + 1), the triangle-inequality bound 5 < 6 on |z| = 1, and
    Rouche giving the three zeros of 6z^3. The correctness of the split and the
    nonvanishing of the dominant term on the circle are now stated as the hypotheses
    Rouche needs rather than left implicit. The collection's provenance is the examination
    paper only, so no retained solution set covers the exercise and the argument is the
    card's own.
---

::: {.problem}
How many zeroes (counted with multiplicity) does the polynomial $$f(z) = z^7 - 2z^5 + 6z^3 - z + 1$$ have in the unit disk $\DD$?
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #split}
On the circle $\abs{z}=1$ the polynomial splits as $f(z)=h(z)+g(z)$ with $h(z)\coloneqq6z^3$ and $g(z)\coloneqq z^7-2z^5-z+1$.

::: pf-proof
$f(z)=z^7-2z^5+6z^3-z+1$ by definition, so the two sides agree identically, not only on the circle.
:::

:::

::: {.pf-step #dominated}
$\abs{g(z)}<6=\abs{h(z)}$ for every $z$ with $\abs{z}=1$.

::: pf-proof
On that circle $\abs{z^7}=\abs{z^5}=\abs{z}=1$, so the triangle inequality gives $\abs{g(z)}\le1+2+1+1=5$, while $\abs{h(z)}=6\abs{z}^3=6$.
:::

:::

::: {.pf-step #rouche}
$f$ and $h=6z^3$ have the same number of zeros in the unit disc, counted with multiplicity.

::: pf-proof
$f$ and $h$ are polynomials, hence holomorphic on a neighbourhood of the closed disc, and step [](#dominated){.pf-ref} shows that on the boundary circle the summand $g=f-h$ is dominated in modulus by $h$, which does not vanish there. Both hypotheses of Rouché's theorem hold, so the zero counts agree.
:::

:::

::: {.pf-step}
$f$ has exactly $\boxed{3}$ zeros in $\DD$, counted with multiplicity.

::: pf-proof
$h(z)=6z^3$ vanishes only at $z=0$, with multiplicity $3$, so by step [](#rouche){.pf-ref} $f$ has three zeros in the disc, counted with multiplicity.
:::

:::

:::
:::
