---
schema: qual/card@1
id: E-U2A4C
kind: problem
title: Residues at $\infty$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Singularities
  - Laurent Series
relations: []
review: draft
---

::: {.exercise}
Compute
$$
\Res_{z=\infty}e^z,
\qquad
\Res_{z=\infty}{z-1\over z+1}.
$$
:::

::: {.solution}
Recall that $\Res_{z=\infty}f(z) = -\Res_{w=0}\frac{f(1/w)}{w^2}$.

::: pf

::: pf-step
$\Res_{z=\infty}e^z = \boxed{0}$.

::: pf-proof
The Laurent series $\frac{e^{1/w}}{w^2} = \sum_{k=0}^\infty \frac{w^{-k-2}}{k!}$ has no $w^{-1}$ term.
:::

:::

::: pf-step
$\Res_{z=\infty}{z-1\over z+1} = \boxed{2}$.

::: pf-proof
With $f(z) = \frac{z-1}{z+1}$, for $\abs{w}<1$
$$
\frac{f(1/w)}{w^2} = \frac{1}{w^2}\cdot\frac{1-w}{1+w} = \frac{1}{w^2}\left(1-2w+2w^2-2w^3+\cdots\right),
$$
so $\Res_{w=0}\frac{f(1/w)}{w^2} = -2$. As a check, the only finite pole of $f$ is $z=-1$, with residue $-2$, and the residues of a rational function on $\CP^1$ sum to zero.
:::

:::

:::

:::
