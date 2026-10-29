---
schema: qual/card@1
id: E-FVXIT
kind: problem
title: Sharp bound on $\abs{f'(0)}$ for $f:\DD\to\theset{\Re w>0}$ with $f(0)=2$
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

::: {.problem}
Let $\HH_R\coloneqq\{w\in\CC:\Re w>0\}$.
Suppose $f:\DD\to\HH_R$ is analytic and satisfies $f(0)=2$.
Find a sharp upper bound for $\abs{f'(0)}$, and prove sharpness by example.
:::

::: {.solution}
Let $r(w)\coloneqq\frac i2w$, a biholomorphism $\HH_R\to\HH$ with $r(2)=i$, and $C(w)\coloneqq\frac{w-i}{w+i}$, a biholomorphism $\HH\to\DD$ with $C(i)=0$.

::: pf

::: {.pf-step #bound}
$\abs{f'(0)}\le4$.

::: pf-proof
$F\coloneqq C\circ r\circ f:\DD\to\DD$ is holomorphic with $F(0)=0$, so $\abs{F'(0)}\le1$ by the Schwarz lemma.
By the chain rule $F'(0)=C'(i)\cdot\frac i2\cdot f'(0)$, and $C'(w)=\frac{2i}{(w+i)^2}$ gives $\abs{C'(i)}=\frac12$.
Hence $1\ge\abs{F'(0)}=\frac14\abs{f'(0)}$.
:::

:::

::: pf-step
The sharp bound is $\abs{f'(0)}\le\boxed4$.

::: pf-proof
By step [](#bound){.pf-ref} it remains to attain it.
For $\abs\lambda=1$, the map $f(z)=r^{-1}\qty(C^{-1}(\lambda z))=2\frac{1+\lambda z}{1-\lambda z}$ is a biholomorphism $\DD\to\HH_R$ with $f(0)=2$ and $f'(0)=4\lambda$.
:::

:::

:::

:::
