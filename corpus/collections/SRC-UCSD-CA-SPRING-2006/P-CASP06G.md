---
schema: qual/card@1
id: P-CASP06G
kind: problem
title: "Solving the ∂-equation for compactly supported smooth functions"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
For each $\psi \in C_0^\infty(\mathbb{C})$ (the space of smooth functions with compact support) satisfying $$\iint_{\mathbb{C}} \psi(z) z^n \, dx\,dy = 0$$ for all $n \geq 0$, there exists a $u \in C_0^\infty(\mathbb{C})$ such that $\frac{\partial u}{\partial \bar{z}} = \psi$.
:::

::: {.solution}
<1>1. Define $u(z) = \frac{1}{2\pi i} \iint_{\mathbb{C}} \frac{\psi(w)}{w - z}\, dw \wedge d\bar w$ (the Cauchy transform of $\psi$).
Proof: this is the standard solution operator for the $\bar\partial$-equation.

<1>2. $\frac{\partial u}{\partial \bar z} = \psi$.
Proof: the Cauchy transform satisfies $\frac{\partial}{\partial \bar z}\left(\frac{1}{2\pi i}\iint \frac{\psi(w)}{w-z}\, dw \wedge d\bar w\right) = \psi(z)$ (the fundamental solution of $\bar\partial$ is $\frac{1}{\pi z}$).

<1>3. $u$ is smooth.
Proof: $\psi$ is smooth with compact support, and the Cauchy transform of a smooth compactly supported function is smooth.

<1>4. $u$ has compact support.
<2>1. For $|z|$ large, expand $\frac{1}{w-z} = -\frac{1}{z}\sum_{n=0}^{\infty} \left(\frac{w}{z}\right)^n$.
Proof: geometric series, valid for $|z| > |w|$.
<2>2. Then $u(z) = -\frac{1}{2\pi i}\sum_{n=0}^{\infty} z^{-(n+1)} \iint \psi(w) w^n\, dw \wedge d\bar w = 0$ for $|z|$ large.
Proof: the hypothesis $\iint \psi(w) w^n = 0$ for all $n \ge 0$ makes every coefficient vanish.
<2>3. Hence $u$ vanishes outside a large disk, so $u$ has compact support.
Proof: <2>2.

<1>5. Q.E.D.
Proof: <1>2, <1>3, and <1>4.
:::
