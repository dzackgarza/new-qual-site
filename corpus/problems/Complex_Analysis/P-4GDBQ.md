---
schema: qual/card@1
id: P-4GDBQ
kind: problem
title: The principal square root is discontinuous across the negative real axis
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Logarithm
  - Continuity
  - Counterexamples
relations: []
review: draft
audit:
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'The source leaves f_1 undefined and parametrizes gamma_2 by t in (pi, 0); the statement defines f_1 as the branch r^{1/2} e^{i theta/2}, -pi < theta < pi, takes t in (0, pi) on both arcs, and states the limits as z tends to z_0 along each arc.'
---

::: {.exercise}
Let $f_1(re^{i\theta})\coloneqq r^{1/2}e^{i\theta/2}$ for $r>0$ and $-\pi<\theta<\pi$, a branch of $z^{1\over 2}$ on $\CC\sm(-\infty,0]$.
Let $z_0 = r_0e^{i\pi} \in (-\infty, 0) \subseteq \RR$, and show that $z^{1\over 2}$ is not continuous along $(-\infty, 0)$ by computing
$$
\begin{aligned}
\lim_{z\to z_0,\ z\in \gamma_1} f_1(z) &= i\sqrt{r_0}, \\
\lim_{z\to z_0,\ z\in \gamma_2} f_1(z) &= -i\sqrt{r_0},
\end{aligned}
$$
where

- $\gamma_1 = \theset{r_0 e^{it} \st t\in (0, \pi) }$,
- $\gamma_2 = \theset{r_0 e^{-it} \st t\in (0, \pi) }$.

![The situation](../../assets/Complex_Analysis/010_Basics/figures/2021-12-19_03-19-37.png)

:::

::: {.solution}

::: pf

::: pf-step
$\lim_{z\to z_0,\ z\in \gamma_1} f_1(z) = \boxed{i\sqrt{r_0}}$ and $\lim_{z\to z_0,\ z\in \gamma_2} f_1(z) = \boxed{-i\sqrt{r_0}}$, so no branch of $z^{1/2}$ on $\CC\sm(-\infty,0]$ that agrees with $f_1$ extends continuously to $z_0$.

::: pf-proof
On $\gamma_1$, $z=r_0e^{it}$ with $t\to\pi^-$, so $f_1(z)=\sqrt{r_0}\,e^{it/2}\to\sqrt{r_0}\,e^{i\pi/2}=i\sqrt{r_0}$.
On $\gamma_2$, $z=r_0e^{-it}$ has argument $\theta=-t\to-\pi^+$, so $f_1(z)=\sqrt{r_0}\,e^{-it/2}\to\sqrt{r_0}\,e^{-i\pi/2}=-i\sqrt{r_0}$.
The two limits differ since $r_0>0$.
:::

:::

:::

:::
