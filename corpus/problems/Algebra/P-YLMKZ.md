---
schema: qual/card@1
id: P-YLMKZ
kind: problem
title: Root bounds for polynomials over division rings
classification:
  areas:
  - algebra
  topics:
  - Polynomials
  - Rings
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09

---

::: {.problem}
Can a polynomial over a division ring (skew-field) have more roots than its degree?
:::

::: {.solution}
Let $\HH$ be the Hamilton quaternions, and let $S=\{bi+cj+dk:b,c,d\in\RR,\ b^2+c^2+d^2=1\}$.

::: pf

::: pf-step
Every $q\in S$ satisfies $q^2+1=0$.

::: pf-proof
Expanding with $i^2=j^2=k^2=-1$ and $ij=-ji$, $ik=-ki$, $jk=-kj$, the cross terms cancel and $q^2=-(b^2+c^2+d^2)=-1$.
:::

:::

::: pf-qed
$\boxed{\text{Yes}}$: the degree-$2$ polynomial $x^2+1$ over the division ring $\HH$ has the infinitely many roots in $S$.
:::

:::

:::
