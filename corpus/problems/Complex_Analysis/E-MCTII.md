---
schema: qual/card@1
id: E-MCTII
kind: problem
title: Schwarz lemma bound for a bounded function on the right half-plane
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.exercise}
Suppose $f$ is holomorphic and $\abs{f(z)}\leq 1$ for $\Re(z) > 0$ with $f(1) = 0$.
Find an upper bound for $\abs{f(2)}$.
:::

::: {.solution}
Let $\phi(z)\coloneqq\frac{z-1}{z+1}$.

::: pf

::: {.pf-step #cayley}
$\phi$ maps $\theset{\Re z>0}$ biholomorphically onto $\DD$, with $\phi(1)=0$ and $\phi(2)=\frac13$.

::: pf-proof
$\abs{z-1}<\abs{z+1}$ if and only if $\Re z>0$, and $\phi$ is a Möbius transformation with inverse $w\mapsto\frac{1+w}{1-w}$, which maps $\DD$ into $\theset{\Re z>0}$.
:::

:::

::: pf-step
$\abs{f(2)}\le\boxed{\frac13}$.

::: pf-proof
By step [](#cayley){.pf-ref}, $F\coloneqq f\circ\phi^{-1}$ is holomorphic on $\DD$ with $\abs F\le1$ and $F(0)=f(1)=0$, so the Schwarz lemma gives $\abs{F(w)}\le\abs w$. Hence $\abs{f(2)}=\abs{F(\frac13)}\le\frac13$.
:::

:::

:::

:::

::: {.remark}
The bound is attained by $f=\phi$.
:::
