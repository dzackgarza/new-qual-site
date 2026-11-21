---
schema: qual/card@1
id: P-JHUU45RA2
kind: problem
title: 'Unit ball of $L^2$ is not compact'
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against entry 2 of the undated JHU Real and Complex Analysis exam on pp. 4–5 of the preserved packet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Prove that the unit ball of $L^2([0,1])$, with its norm topology, is not compact.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own orthonormal-sequence argument follows, with orthonormality, the pairwise distance and the conclusion as separate steps.

::: pf

::: {.pf-step #orthonormal}
$e_{n}(x)=\sqrt2\sin(n\pi x)$ are orthonormal in $L^{2}([0,1])$, so $\norm{e_{n}}_{2}=1$ and each $e_{n}$ lies in the closed unit ball.

::: pf-proof
$\int_{0}^{1}2\sin^{2}(n\pi x)dx=\int_{0}^{1}\big(1-\cos(2n\pi x)\big)dx=1-\frac{\sin(2n\pi)}{2n\pi}=1$, and for $m\ne n$ the product formula $2\sin(m\pi x)\sin(n\pi x)=\cos((m-n)\pi x)-\cos((m+n)\pi x)$ integrates to $0$ over $[0,1]$ since both cosine terms have integer frequency.
:::

:::

::: {.pf-step #distance}
$\norm{e_{n}-e_{m}}_{2}=\sqrt2$ for $m\ne n$.

::: pf-proof
Expanding, $\norm{e_{n}-e_{m}}_{2}^{2}=\norm{e_{n}}_{2}^{2}+\norm{e_{m}}_{2}^{2}-2\operatorname{Re}\langle e_{n},e_{m}\rangle=1+1-0=2$ by step [](#orthonormal){.pf-ref}.
:::

:::

::: {.pf-step #no-subsequence}
$(e_{n})$ has no norm-convergent subsequence.

::: pf-proof
A convergent subsequence would be Cauchy, but by step [](#distance){.pf-ref} any two distinct terms are $\sqrt2$ apart, so no subsequence is Cauchy.
:::

:::

::: {.pf-qed}
$(e_{n})$ is a sequence in the closed unit ball with no convergent subsequence. A compact metric space is sequentially compact, so the ball — which is a metric space under the $L^{2}$ norm — is not compact.
:::

:::

:::
