---
schema: qual/card@1
id: E-SS6.PR-2
kind: problem
title: $\zeta(s)=\frac{s}{s-1}-s\int_1^\infty\{x\}x^{-s-1}\,dx$ for $\Re(s)>0$
classification:
  areas:
  - complex-analysis
  topics:
  - Zeta Function
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.exercise}
2. Prove that for $\operatorname{Re}(s) > 0$,
$$
\zeta(s) = \frac{s}{s-1} - s \int_1^\infty \frac{\{x\}}{x^{s+1}}\,dx,
$$
where $\{x\} = x - \lfloor x \rfloor$ is the fractional part of $x$.
:::

::: {.solution}
<1>1. The representation holds on $\Re(s)>0$.
    ::: {.proof}
    <2>1. For $\Re(s) > 1$ and $M \in \mathbb{N}$, apply Abel summation (integration by parts):
    $$\sum_{n=1}^M n^{-s} = \int_{1^-}^M x^{-s}\,d\lfloor x \rfloor = \frac{\lfloor M \rfloor}{M^s} + s \int_1^M \frac{\lfloor x \rfloor}{x^{s+1}}\,dx = M^{1-s} + s \int_1^M \frac{x - \{x\}}{x^{s+1}}\,dx.$$
    <2>2. Split the integral:
    $$s \int_1^M \frac{x}{x^{s+1}}\,dx = s \int_1^M x^{-s}\,dx = s \left[ \frac{x^{1-s}}{1-s} \right]_1^M = \frac{s}{s-1} (1 - M^{1-s}).$$
    <2>3. Thus
    $$\sum_{n=1}^M n^{-s} = \frac{s}{s-1} + M^{1-s} \left(1 - \frac{s}{s-1}\right) - s \int_1^M \frac{\{x\}}{x^{s+1}}\,dx = \frac{s}{s-1} - \frac{M^{1-s}}{s-1} - s \int_1^M \frac{\{x\}}{x^{s+1}}\,dx.$$
    <2>4. For $\Re(s) > 1$, as $M \to \infty$, $|M^{1-s}| = M^{1-\Re(s)} \to 0$.
    <2>5. Because $0 \le \{x\} < 1$, the integral $\int_1^\infty \frac{\{x\}}{x^{s+1}}\,dx$ converges absolutely and uniformly on compact subsets of $\Re(s) > 0$.
    <2>6. Taking $M \to \infty$ gives $\zeta(s) = \frac{s}{s-1} - s \int_1^\infty \frac{\{x\}}{x^{s+1}}\,dx$ for $\Re(s) > 1$, and by analytic continuation this holds for all $\Re(s) > 0$ with $s \neq 1$.

:::

<1>2. Q.E.D.

::: {.proof}
Step <1>1 is the claim.
:::
:::
