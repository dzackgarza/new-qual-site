---
schema: qual/card@1
id: P-AW6IK
kind: problem
title: A function holomorphic on $0<|z|<1$ with $\int_{|z|=r}f=0$ for all $r<1$, but
  not holomorphic at $0$
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Singularities
  - Counterexamples
  - Residues
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
Show by example that there exists a function $f(z)$ that is holomorphic on the punctured disk $D^*(0, 1) = \{z \in \mathbb{C} \mid 0 < |z| < 1\}$ such that for all $0 < r < 1$:
$$\oint_{|z| = r} f(z) \, dz = 0,$$
but $f$ is not holomorphic at $z = 0$.
:::

::: solution
Take
\[
f(z)=\frac1{z^2}.
\]
This is holomorphic on $0<|z|<1$ and has a pole of order $2$ at $0$, so it does not extend holomorphically across $0$.

For $0<r<1$, parameterize $|z|=r$ by $z=re^{it}$, $0\le t\le2\pi$. Then
\[
\oint_{|z|=r}\frac{dz}{z^2}
=\int_0^{2\pi}\frac{i r e^{it}}{r^2e^{2it}}\,dt
=\frac{i}{r}\int_0^{2\pi}e^{-it}\,dt
=0.
\]
Equivalently, the Laurent expansion is just $z^{-2}$, whose residue at $0$ is $0$.

Hence $f$ satisfies the required integral condition for every $r$, despite having a nonremovable singularity at $0$.
:::
