---
schema: qual/card@1
id: FT-4JRQX
kind: theorem
title: Tonelli
prompts:
- State Tonelli's theorem.
classification:
  areas:
  - real-analysis
  topics:
  - Fubini-Tonelli
  - Integrals
relations: []
review: draft
---

::: {.theorem}
Let $f(x, y)$ be non-negative and measurable on $\RR^{n}\cross \RR^k$.
Then for almost every $y\in \RR^k$,

1. The slice function $f^y(x) \definedas f(x, y)$ is measurable on $\RR^n$.

2. The function $F(y) \definedas \int_{\RR^n} f^y(x) \, dx$ is measurable on $\RR^k$.

3. $$\int_{\RR^{n+k}} f(\vector u) \, d\vector u = \int_{\RR^n} \qty{\int_{\RR^k} f^y(x) \,dx}\, dy$$ in any order (where the integral may be infinite.)

> Note: requires **non-negativity** and **measurability**, but not integrability.
:::
