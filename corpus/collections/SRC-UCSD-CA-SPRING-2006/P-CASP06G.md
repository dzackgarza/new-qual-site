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

::: {.problem}
For each $\psi \in C_0^\infty(\mathbb{C})$ (the space of smooth functions with compact support) satisfying $$\iint_{\mathbb{C}} \psi(z) z^n \, dx\,dy = 0$$ for all $n \geq 0$, there exists a $u \in C_0^\infty(\mathbb{C})$ such that $\frac{\partial u}{\partial \bar{z}} = \psi$.
:::

::: {.solution}

::: pf

::: pf-step

Define $u(z) = \frac{1}{2\pi i} \iint_{\mathbb{C}} \frac{\psi(w)}{w - z}\, dw \wedge d\bar w$ (the Cauchy transform of $\psi$).

::: pf-proof

this is the standard solution operator for the $\bar\partial$-equation.

:::

:::

::: {.pf-step #s2}

$\frac{\partial u}{\partial \bar z} = \psi$.

::: pf-proof

the Cauchy transform satisfies $\frac{\partial}{\partial \bar z}\left(\frac{1}{2\pi i}\iint \frac{\psi(w)}{w-z}\, dw \wedge d\bar w\right) = \psi(z)$ (the fundamental solution of $\bar\partial$ is $\frac{1}{\pi z}$).

:::

:::

::: {.pf-step #s3}

$u$ is smooth.

::: pf-proof

$\psi$ is smooth with compact support, and the Cauchy transform of a smooth compactly supported function is smooth.

:::

:::

::: {.pf-step #s4}

$u$ has compact support.

::: pf-proof

::: pf-step

For $|z|$ large, expand $\frac{1}{w-z} = -\frac{1}{z}\sum_{n=0}^{\infty} \left(\frac{w}{z}\right)^n$.

::: pf-proof

geometric series, valid for $|z| > |w|$.

:::

:::

::: {.pf-step #s4-2}

Then $u(z) = -\frac{1}{2\pi i}\sum_{n=0}^{\infty} z^{-(n+1)} \iint \psi(w) w^n\, dw \wedge d\bar w = 0$ for $|z|$ large.

::: pf-proof

the hypothesis $\iint \psi(w) w^n = 0$ for all $n \ge 0$ makes every coefficient vanish.

:::

:::

::: pf-step

Hence $u$ vanishes outside a large disk, so $u$ has compact support.

::: pf-proof

Step [](#s4-2){.pf-ref}.

:::

:::

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

:::
