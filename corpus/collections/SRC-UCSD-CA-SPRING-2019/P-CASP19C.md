---
schema: qual/card@1
id: P-CASP19C
kind: problem
title: "Analytic function on B(0,1+epsilon) with |f|<1 on |z|=1 has a unique fixed point in D"
classification:
  areas:
  - complex-analysis
  topics:
  - Fixed Points
  - Rouché
  - Holomorphic Functions
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
Let $f$ be an analytic function on the open disk $B(0, 1 + \varepsilon)$ for some $\varepsilon > 0$.
Assume that $|f(z)| < 1$ for all $|z| = 1$.
Prove that there exists a **unique fixed point** $z_0 \in \mathbb{D}$ (i.e. $|z_0| < 1$ and $f(z_0) = z_0$).
:::

::: solution
Let
\[
g(z)=z-f(z).
\]
On $|z|=1$,
\[
|g(z)-z|=|f(z)|<1=|z|.
\]
By Rouché's theorem, $g$ and $z$ have the same number of zeros in $\mathbb D$, counted with multiplicity. Since $z$ has exactly one zero there, so does $g$.

Therefore there is exactly one point $z_0\in\mathbb D$ satisfying
\[
g(z_0)=0,
\]
i.e.
\[
f(z_0)=z_0.
\]
:::
