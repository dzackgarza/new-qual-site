---
schema: qual/card@1
id: FT-T7OAO
kind: theorem
title: Fubini
prompts:
- State Fubini's theorem.
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
Let $f(x, y) \in L^1(\RR^n\cross \RR^k)$.
Then for almost every $y\in \RR^k$,

1. The slice function $f^y(x)\definedas f(x ,y)$ is *integrable*, so $f^y \in L^1(\RR^n)$.

2. The function $F(y) \definedas \int_{\RR^n} f^y(x) \, dx$ is *integrable*, so $F\in L^1(\RR^{k})$.

3. $$\int_{\RR^{n+k}} f(\vector u) \, d\vector u = \int_{\RR^n} \qty{ \int_{\RR^k} f^y(x) \, dx} \, dy$$ in any order.

> Note: requires **integrability**, not just measurability, but doesn't require non-negativity.
:::
