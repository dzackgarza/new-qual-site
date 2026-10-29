---
schema: qual/card@1
id: E-JK5PG
kind: problem
title: The integral of $1/(x^4+1)$ over $\RR$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Poles
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source prints only the identity, without an instruction or the differential dx; the statement asks to show it and supplies dx.
---

::: {.exercise}
Show that
$$
\int_\RR {dx \over x^4 + 1} = {\pi \sqrt{2} \over 2}
.$$
:::

::: {.solution}
Let $f(z)\coloneqq{1\over z^4+1}$, and for $R>1$ let $\Gamma_R$ be the segment $[-R,R]$ followed by the semicircle $C_R=\theset{Re^{it} \st t\in[0,\pi]}$.

![](../../assets/figures/2021-07-29_18-41-05.png)

::: pf

::: {.pf-step #residues}
$2\pi i\sum_{z_k\in\HH}\Res_{z=z_k}f={\pi\sqrt2\over2}$.

::: pf-proof
The poles of $f$ in $\HH$ are the simple zeros $z_1=e^{i\pi/4}$ and $z_2=e^{3i\pi/4}$ of $z^4+1$, with residues $1/(4z_k^3)$. Hence
$$
2\pi i\sum_k{1\over4z_k^3}={\pi i\over2}\qty{e^{-3i\pi/4}+e^{-i\pi/4}}={\pi i\over2}\,e^{-i\pi/2}\cdot2\cos\qty{\pi\over4}={\pi\sqrt2\over2}
.$$
:::

:::

::: {.pf-step #arc}
$\int_{C_R}f(z)\dz\to0$ as $R\to\infty$.

::: pf-proof
On $C_R$, $\abs{z^4+1}\ge R^4-1$, so the ML estimate bounds the integral by $\pi R/(R^4-1)$.
:::

:::

::: pf-qed
By the residue theorem and step [](#residues){.pf-ref}, $\int_{-R}^R f(x)\dx+\int_{C_R}f(z)\dz={\pi\sqrt2\over2}$ for $R>1$, and letting $R\to\infty$ with step [](#arc){.pf-ref} gives the result.
:::

:::

:::
