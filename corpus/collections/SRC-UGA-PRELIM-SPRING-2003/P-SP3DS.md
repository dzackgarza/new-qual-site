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

::: problem
Does there exist a divergent series $\sum_{i=0}^\infty a_i$ of positive real numbers $a_i$ such that $\sum_{i=0}^\infty \sqrt{a_i}$ converges?
If so, give an example; if not, prove it.
:::

::: solution
<1>1. No such series exists.
:::

<1>2. Suppose that $\sum_{i=0}^\infty \sqrt{a_i}$ converges.
Then there is an index $N$ such that $0<a_i<1$ for every $i\ge N$.
::: {.proof}
Convergence of $\sum \sqrt{a_i}$ implies $\sqrt{a_i}\to0$, hence $a_i\to0$. Therefore $a_i<1$ eventually.
:::

<1>3. For every $i\ge N$,
\[
a_i\le \sqrt{a_i}.
\]
::: {.proof}
If $0<a_i<1$, then squaring decreases the number: $(\sqrt{a_i})^2=a_i\le\sqrt{a_i}$.
:::

<1>4. The series $\sum_{i=0}^\infty a_i$ converges.
::: {.proof}
By <1>3,
\[
0\le \sum_{i=N}^m a_i\le \sum_{i=N}^m \sqrt{a_i}
\]
for every $m\ge N$. The right-hand partial sums are bounded because $\sum \sqrt{a_i}$ converges. Hence the positive-term series $\sum_{i=N}^\infty a_i$ converges by comparison. Adding the finite initial sum $\sum_{i=0}^{N-1}a_i$ preserves convergence.
:::

<1>5. Therefore it is impossible for $\sum a_i$ to diverge while $\sum\sqrt{a_i}$ converges.
:::
:::
