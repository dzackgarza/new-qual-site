---
schema: qual/card@1
id: P-CASP08A
kind: problem
title: "Statement and proof of Schwarz's Lemma"
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

::: problem
State and prove **Schwarz's Lemma** for holomorphic functions on the unit disk.
:::

::: solution
Let $f:\mathbb D\to\mathbb D$ be holomorphic with $f(0)=0$. Schwarz's lemma states
$$
|f(z)|\le |z|,\qquad |f'(0)|\le1.
$$
Moreover, equality at one nonzero point, or $|f'(0)|=1$, holds if and only if $f(z)=e^{i\theta}z$ for some $\theta\in\mathbb R$.

<1>1. Since $f(0)=0$,
$$
g(z)=\begin{cases}f(z)/z,&z\ne0,\\ f'(0),&z=0\end{cases}
$$
is holomorphic on $\mathbb D$.

<1>2. Fix $0<r<1$. On $|z|=r$, $|g(z)|\le1/r$. By the maximum-modulus principle, $|g(z)|\le1/r$ for $|z|\le r$. For fixed $z$, let $r\uparrow1$ through values larger than $|z|$; then $|g(z)|\le1$. Hence $|f(z)|\le|z|$ and $|f'(0)|\le1$.

<1>3. If $|f(z_0)|=|z_0|$ for some $z_0\ne0$, then $|g(z_0)|=1$. If $|f'(0)|=1$, then $|g(0)|=1$. In either case $g$ attains its maximum modulus at an interior point, so $g$ is constant. Its constant value has modulus $1$, hence $g=e^{i\theta}$ and $f(z)=e^{i\theta}z$. Conversely every rotation has equality.
:::
