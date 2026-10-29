---
schema: qual/card@1
id: P-CAF13C
kind: problem
title: "A holomorphic map of the unit disk with sup norm ≤ 1 has a unique fixed point"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
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
Let $f$ be holomorphic on a neighborhood of the closed unit disk $\overline{\DD}$.
Suppose $\sup_{z \in \partial\DD} |f(z)| \leq 1$, and that $f$ has no fixed points on the boundary $\partial\DD$ ($f(z) \ne z$ for all $|z| = 1$).
Prove that $f$ has **exactly one fixed point** in the open unit disk $\DD$.
:::

::: {.solution}
Set
$$
h_t(z)=t f(z)-z,\qquad 0\le t\le1.
$$
For $|z|=1$ and $t<1$,
$$
|t f(z)|\le t<1=|z|,
$$
so $h_t(z)\ne0$. For $t=1$, the hypothesis says $h_1(z)=f(z)-z\ne0$ on $\partial\DD$.

Hence the winding number of $h_t(\partial\DD)$ about $0$, equivalently the number of zeros of $h_t$ in $\DD$ counted with multiplicity, is constant in $t$ by the argument principle.

At $t=0$,
$$
h_0(z)=-z,
$$
which has exactly one zero in $\DD$. Therefore $h_1(z)=f(z)-z$ also has exactly one zero in $\DD$, counted with multiplicity. Thus $f$ has exactly one fixed point in $\DD$.
:::
