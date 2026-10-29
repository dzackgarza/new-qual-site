---
schema: qual/card@1
id: E-FCYUM
kind: problem
title: $\Res_{z=0}\frac{1}{z^2\sin z}$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Laurent Series
  - Poles
  - Trigonometry
relations: []
review: draft
---

::: {.exercise}
Compute
$$
\Res_{z=0} {1\over z^2 \sin(z)}.
$$

:::

::: {.solution}

::: pf

::: {.pf-step #reciprocal}
$\frac1{\sin z}=z^{-1}\qty(1+\frac16z^2+O(z^4))$ near $0$.

::: pf-proof
$\sin z=z\qty(1-x)$ with $x=\frac1{3!}z^2-\frac1{5!}z^4+\cdots=O(z^2)$, and $\frac1{1-x}=1+x+O(x^2)=1+\frac16z^2+O(z^4)$.
:::

:::

::: pf-step
$\Res_{z=0}\frac1{z^2\sin z}=\boxed{\frac16}$.

::: pf-proof
By step [](#reciprocal){.pf-ref}, $\frac1{z^2\sin z}=z^{-3}+\frac16z^{-1}+O(z)$, and the residue is the coefficient of $z^{-1}$.
:::

:::

:::

:::
