---
schema: qual/card@1
id: P-BKS07-9A
kind: problem
title: The integral inequality $f(x)\ge L\int_0^x f(t)\,dt$ forces $f\ge0$
classification:
  areas: [prelim]
  topics:
  - Real Analysis
relations: []
review: draft
---

::: {.problem}
Suppose $b$ and $L$ are positive constants and $f \colon [0, b] \to \RR$ is continuous and satisfies
$$
f(x) \geq L \int_{0}^{x} f(t)\, dt, \qquad (0 \leq x \leq b).
$$
Show that $f(x) \geq 0$ for $0 \leq x \leq b$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Let $F(x)=\int_0^xf(t)\,dt$. Then $\frac{d}{dx}\bigl(F(x)e^{-Lx}\bigr)\ge0$ on $[0,b]$.

::: pf-proof

$F$ is differentiable with $F'=f$, because $f$ is continuous. So $\frac{d}{dx}\bigl(F(x)e^{-Lx}\bigr)=(f(x)-LF(x))e^{-Lx}\ge0$ by the hypothesis.

:::

:::

::: {.pf-step #s2}

$F\ge0$ on $[0,b]$.

::: pf-proof

By step [](#s1){.pf-ref} and the mean value theorem, $F(x)e^{-Lx}\ge F(0)=0$.

:::

:::

::: pf-qed

By the hypothesis and step [](#s2){.pf-ref}, $f(x)\ge LF(x)\ge0$.

:::

:::

:::
