---
schema: qual/card@1
id: P-WESRA07-II5
kind: problem
title: A dominated-convergence limit with powers of $1+x^2$
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, item 5 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Compute
$$
\lim_{n\to\infty}\int_0^1\frac{1+n x^2}{(1+x^2)^n}\,dx.
$$
:::

::: {.solution}

Let $f_n(x) \coloneqq \frac{1+n x^2}{(1+x^2)^n}$ on $[0,1]$.

::: pf

::: {.pf-step #bound}

$0\le f_n\le1$ on $[0,1]$ for every $n$.

::: pf-proof

Bernoulli's inequality gives $(1+x^2)^n\ge 1+n x^2$.

:::

:::

::: {.pf-step #limit}

$f_n(x)\to0$ for every $x\in(0,1]$.

::: pf-proof

With $q = 1+x^2 > 1$, the numerator $1+nx^2$ grows linearly in $n$ and the denominator $q^n$ grows exponentially, so the ratio tends to $0$.

:::

:::

::: pf-step

$\displaystyle\lim_{n\to\infty}\int_0^1 f_n(x)\,dx=\boxed{0}$.

::: pf-proof

By steps [](#bound){.pf-ref} and [](#limit){.pf-ref}, $f_n\to0$ almost everywhere on $[0,1]$ with the integrable bound $1$, so the dominated convergence theorem applies.

:::

:::

:::

:::
