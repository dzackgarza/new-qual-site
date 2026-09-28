---
schema: qual/card@1
id: E-SS1.EX-26
kind: problem
title: Primitives of a continuous function differ by a constant
classification:
  areas:
  - complex-analysis
  topics: ['Complex Numbers', 'Power Series', 'Cauchy-Riemann']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}
26. Suppose f is continuous in a region Ω. Prove that any two primitives of f (if they exist) difer by a constant.
:::

::: {.solution}
Let $F$ and $G$ be primitives of $f$ on the region $\Omega$, and set $H=F-G$. Then
\[
H'(z)=F'(z)-G'(z)=f(z)-f(z)=0
\]
for every $z\in\Omega$.

Fix $z_0\in\Omega$. Since $\Omega$ is open, some disc $D(z_0,r)$ lies in $\Omega$. For any $z\in D(z_0,r)$, the segment
\[
\gamma(t)=z_0+t(z-z_0),\qquad 0\le t\le1,
\]
lies in the disc. The function $t\mapsto H(\gamma(t))$ has derivative
\[
H'(\gamma(t))(z-z_0)=0,
\]
so it is constant. Thus $H(z)=H(z_0)$ throughout $D(z_0,r)$. Hence $H$ is locally constant on $\Omega$.

A locally constant function on a connected set is constant: for any value $c$, the level set $H^{-1}(c)$ is both open and closed. Since a region is connected, the nonempty level set containing $z_0$ must be all of $\Omega$. Therefore $F-G$ is constant on $\Omega$.
:::
