---
schema: qual/card@1
id: P-YGU32
kind: problem
title: Entire functions satisfying $\abs{f(z)}\ge\abs{z}$
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Entire Functions
  - Removable Singularities
  - Zeros
relations: []
review: draft
---

::: {.problem}
Find all entire functions that satisfy
$$
\abs{f(z)} \geq \abs{z} \quad \forall z\in \CC.
$$
Prove this list is complete.
:::

::: {.solution}
Let $f$ be entire with $\abs{f(z)}\ge\abs{z}$ for all $z$.

::: pf

::: {.pf-step #zeros}
$f(z)=0$ only at $z=0$.

::: pf-proof
If $f(z)=0$, then $\abs{z}\le\abs{f(z)}=0$.
:::

:::

::: {.pf-step #g}
$g(z)\coloneqq z/f(z)$ extends to an entire function with $\abs{g}\le1$.

::: pf-proof
By step [](#zeros){.pf-ref}, $g$ is holomorphic on $\CC\setminus\theset{0}$, and there $\abs{g(z)}=\abs{z}/\abs{f(z)}\le1$.
A bounded isolated singularity is removable by Riemann's theorem, and the extension satisfies $\abs{g(0)}\le1$ by continuity.
:::

:::

::: pf-step
The entire functions with $\abs{f(z)}\ge\abs{z}$ are exactly $\boxed{f(z)=cz \text{ with } c\in\CC,\ \abs{c}\ge1}$.

::: pf-proof
By step [](#g){.pf-ref} and Liouville's theorem, $g$ is a constant $c_0$ with $\abs{c_0}\le1$, and $c_0\ne0$ since $g(z)=z/f(z)\ne0$ for $z\ne0$.
Hence $f(z)=cz$ with $c=1/c_0$ and $\abs{c}\ge1$ on $\CC\setminus\theset{0}$, and at $0$ by continuity.
Conversely, every such $f$ satisfies $\abs{f(z)}=\abs{c}\abs{z}\ge\abs{z}$.
:::

:::

:::

:::
