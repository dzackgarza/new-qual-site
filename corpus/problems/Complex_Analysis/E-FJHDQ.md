---
schema: qual/card@1
id: E-FJHDQ
kind: problem
title: $\abs{f(z)}\le\abs{\frac{z-i}{z+i}}$ for holomorphic $f:\HH\to\DD$ with $f(i)=0$
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
Show that if $f:\HH\to \DD$ is holomorphic and $f(i) = 0$ then $\abs{f(z)} \leq \abs{z-i\over z+i}$.

:::

::: {.solution}
Let $g(z)\coloneqq\frac{z-i}{z+i}$ be the Cayley map, a biholomorphism $\HH\to\DD$ with inverse $g^{-1}(w)=i\frac{1+w}{1-w}$.

::: pf

::: {.pf-step #schwarz}
$F\coloneqq f\circ g^{-1}:\DD\to\DD$ satisfies $\abs{F(w)}\le\abs w$ for $w\in\DD$.

::: pf-proof
$F$ is holomorphic and $F(0)=f(g^{-1}(0))=f(i)=0$, so this is the Schwarz lemma.
:::

:::

::: pf-step
$\abs{f(z)}\le\abs{\frac{z-i}{z+i}}$ for $z\in\HH$.

::: pf-proof
Take $w=g(z)$ in step [](#schwarz){.pf-ref}: $\abs{f(z)}=\abs{F(g(z))}\le\abs{g(z)}$.
:::

:::

:::

:::
