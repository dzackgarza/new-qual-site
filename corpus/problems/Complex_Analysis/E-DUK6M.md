---
schema: qual/card@1
id: E-DUK6M
kind: problem
title: $\int_\RR\frac{xe^{2ix}}{x^2-1}\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'The source states the identity $\int_\RR {xe^{2ix} \over x^2-1}\dx = i\pi \cos(2)$ with no request. The integrand has nonintegrable simple poles at $\pm1$, so the integral exists only as a principal value; the statement now asks to show the identity for the principal value.'
---

::: {.exercise}
Show that the principal value integral satisfies
$$
I \coloneqq \operatorname{p.v.}\int_\RR {xe^{2ix} \over x^2-1}\dx = i\pi \cos(2).
$$
:::

::: {.solution}
Let $f(z)=\frac{ze^{2iz}}{z^2-1}$, which has simple poles at $\pm1$ on $\RR$.
For $0<\varepsilon<1<R$, let $\Gamma=C_1+C_2+C_4+C_R$, where

- $C_1$ is $[-R,-1-\varepsilon]\cup[-1+\varepsilon,1-\varepsilon]\cup[1+\varepsilon,R]$ on the real axis;
- $C_2$ is $-1+\varepsilon e^{it}$ and $C_4$ is $1+\varepsilon e^{it}$, each for $t$ from $\pi$ to $0$ (clockwise, above the pole);
- $C_R$ is $Re^{it}$ for $t\in[0,\pi]$.

The figure shows the same indentations on a rectangular contour; here the outer arc is the semicircle $C_R$:

![](../../assets/Complex_Analysis/040_Residues/figures/2021-12-21_01-47-37.png)

::: pf

::: {.pf-step #zero}
$\int_\Gamma f=0$.

::: pf-proof
$\Gamma$ encloses no singularity of $f$.
:::

:::

::: {.pf-step #arc}
$\int_{C_R}f\to0$ as $R\to\infty$.

::: pf-proof
This is Jordan's lemma for $e^{2iz}$ on the upper half-plane, since $\abs{z/(z^2-1)}\le R/(R^2-1)\to0$ on $C_R$.
:::

:::

::: {.pf-step #indent}
As $\varepsilon\to0$, $\int_{C_2}f\to-\pi i\cdot\frac{e^{-2i}}2$ and $\int_{C_4}f\to-\pi i\cdot\frac{e^{2i}}2$.

::: pf-proof
A clockwise half-circle about a simple pole contributes $-\pi i$ times the residue in the limit, and
$$
\Res_{z=-1}f=\lim_{z\to-1}\frac{ze^{2iz}}{z-1}=\frac{e^{-2i}}2,\qquad
\Res_{z=1}f=\lim_{z\to1}\frac{ze^{2iz}}{z+1}=\frac{e^{2i}}2.
$$
:::

:::

::: pf-step
$I=i\pi\cos(2)$.

::: pf-proof
Letting $\varepsilon\to0$ and $R\to\infty$, $\int_{C_1}f\to I$, and steps [](#zero){.pf-ref}, [](#arc){.pf-ref} and [](#indent){.pf-ref} give $0=I-\pi i\qty(\frac{e^{-2i}}2+\frac{e^{2i}}2)=I-\pi i\cos(2)$.
:::

:::

:::

:::

