---
schema: qual/card@1
id: E-IZKCV
kind: problem
title: $\int_\RR\frac{dx}{x^4+1}$ by a semicircle
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
\int_\RR {dx \over x^4 + 1} = {\pi \sqrt{2} \over 2} = {\pi \over \sqrt 2}
.$$
:::

::: {.solution}
Let $f(z)\coloneqq{1\over z^4+1}$, and for $R>1$ let $\Gamma_R$ be the segment $[-R,R]$ followed by the semicircle $C_R=\theset{Re^{it} \st t\in[0,\pi]}$.

![](../../assets/figures/2021-07-29_18-41-05.png)

::: pf

::: {.pf-step #poles}
The poles of $f$ in $\HH$ are $z_1=e^{i\pi/4}$ and $z_2=e^{3i\pi/4}$, both simple, with $\Res_{z=z_k}f={1\over4z_k^3}$.

::: pf-proof
The roots of $z^4=-1$ are $e^{i\pi/4},e^{3i\pi/4},e^{5i\pi/4},e^{7i\pi/4}$, of which the first two lie in $\HH$.
They are simple since $\dd{}{z}(z^4+1)=4z^3\neq0$ there, and the residue of $1/q$ at a simple zero $z_k$ of $q$ is $1/q'(z_k)$.
:::

:::

::: {.pf-step #sum}
$2\pi i\qty{\Res_{z=z_1}f+\Res_{z=z_2}f}={\pi\sqrt2\over2}$.

::: pf-proof
By step [](#poles){.pf-ref},
$$
\begin{aligned}
2\pi i \sum_k \Res_{z=z_k}f
&= {\pi i \over 2}\qty{e^{-3 i \pi/4} + e^{-9 i \pi/4}}
= {\pi i \over 2}\qty{e^{-3 i \pi/4} + e^{-i \pi/4}} \\
&= {\pi i \over 2}\, e^{-i\pi/2}\qty{e^{- i \pi/4} + e^{i \pi/4}}
= \pi \cos\qty{\pi \over 4}
= {\pi \sqrt 2 \over 2}
.\end{aligned}
$$
:::

:::

::: {.pf-step #arc}
$\int_{C_R}f(z)\dz\to0$ as $R\to\infty$.

::: pf-proof
On $C_R$, $\abs{z^4+1}\ge R^4-1$, so the ML estimate bounds the integral by $\pi R/(R^4-1)$.
:::

:::

::: pf-qed
By the residue theorem, $\int_{-R}^R f(x)\dx+\int_{C_R}f(z)\dz={\pi\sqrt2\over2}$ for $R>1$ by step [](#sum){.pf-ref}, and letting $R\to\infty$ with step [](#arc){.pf-ref} gives the result.
:::

:::

:::
