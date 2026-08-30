---
schema: qual/card@1
id: P-OZXEA
kind: problem
title: An entire function with $f(z)/z\to 0$ as $z\to\infty$ is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Entire Functions
  - Cauchy Estimates
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Suppose $f(z)$ is entire and 
\[
\lim_{z\to\infty} {f(z) \over z} = 0
.\]

Show that $f(z)$ is a constant.
:::

::: {.solution}
<1>1. $f(z)/z\to0$ as $z\to\infty$ implies $f$ bounded: for $|z|>R$, $|f(z)|\le|z|$.
Proof: limit.

<1>2. Cauchy estimate for $f'$: $|f'(0)|\le \max_{|z|=R}|f(z)|/R$.
Proof: Cauchy.

<1>3. For large $R$, $\max_{|z|=R}|f(z)|\le2R$, so $|f'(0)|\le2$.
Proof: <1>1.

<1>4. More generally $f(z)-f(0)$ satisfies same condition, and $g(z)=(f(z)-f(0))/z$ entire? Actually consider $g(z)=(f(z)-f(0))/z$ entire (removable at $0$).
Proof: $g$ entire.

<1>5. $g(z)\to0$ as $z\to\infty$ (since $f(z)/z\to0$), so $g$ bounded entire, hence constant $0$ by Liouville.
Proof: $g$ bounded.

<1>6. Hence $f(z)=f(0)$ constant.
Proof: <1>5.

<1>7. Q.E.D.
Proof: <1>6.
:::
