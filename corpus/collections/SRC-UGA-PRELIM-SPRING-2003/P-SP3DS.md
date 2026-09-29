---
schema: qual/card@1
id: P-SP3DS
kind: problem
title: No divergent series of positive terms has convergent series of square roots
classification:
  areas:
  - prelim
  topics:
  - Series
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Does there exist a divergent series $\sum_{i=0}^\infty a_i$ of positive real numbers $a_i$ such that $\sum_{i=0}^\infty \sqrt{a_i}$ converges?
If so, give an example; if not, prove it.
:::

::: {.solution}

::: pf

::: pf-step
No such series exists.
:::

::: pf-step
Suppose that $\sum_{i=0}^\infty \sqrt{a_i}$ converges.
Then there is an index $N$ such that $0<a_i<1$ for every $i\ge N$.

::: pf-proof
Convergence of $\sum \sqrt{a_i}$ implies $\sqrt{a_i}\to0$, hence $a_i\to0$. Therefore $a_i<1$ eventually.
:::

:::

::: {.pf-step #s3}
For every $i\ge N$,
\[
a_i\le \sqrt{a_i}.
\]

::: pf-proof
If $0<a_i<1$, then squaring decreases the number: $(\sqrt{a_i})^2=a_i\le\sqrt{a_i}$.
:::

:::

::: pf-step
The series $\sum_{i=0}^\infty a_i$ converges.

::: pf-proof
By step [](#s3){.pf-ref},
\[
0\le \sum_{i=N}^m a_i\le \sum_{i=N}^m \sqrt{a_i}
\]
for every $m\ge N$. The right-hand partial sums are bounded because $\sum \sqrt{a_i}$ converges. Hence the positive-term series $\sum_{i=N}^\infty a_i$ converges by comparison. Adding the finite initial sum $\sum_{i=0}^{N-1}a_i$ preserves convergence.
:::

:::

::: pf-step
Therefore it is impossible for $\sum a_i$ to diverge while $\sum\sqrt{a_i}$ converges.
:::

:::
:::
