---
schema: qual/card@1
id: E-NSN6G
kind: problem
title: Locally uniform limit theorem for holomorphic functions
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Cauchy Estimates
  - Sequences of Functions
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source does not name the domain; the statement adds that the $f_n$ are holomorphic on an open set $\Omega$.
---

::: {.exercise}
Let $\Omega\subseteq\CC$ be open.
Prove that if $f_n\to f$ locally uniformly on $\Omega$ with $f_n$ holomorphic on $\Omega$, then $f_n'\to f'$ locally uniformly on $\Omega$ and $f'$ is holomorphic.
:::

::: {.solution}

::: pf

::: {.pf-step #f-holo}
$f$ is holomorphic on $\Omega$, so $f'$ is holomorphic on $\Omega$.

::: pf-proof
$f$ is continuous as a locally uniform limit of continuous functions.
For a closed triangle $T$ in a disc $D\subseteq\Omega$, $\int_{\partial T} f = \lim_n \int_{\partial T} f_n = 0$ by uniform convergence on $\partial T$ and Goursat's theorem, so $f$ is holomorphic on $D$ by Morera's theorem.
The derivative of a holomorphic function is holomorphic.
:::

:::

::: {.pf-step #estimate}
If $F$ is holomorphic on $\Omega$, $z\in\Omega$, and $\overline{D_{2r}(z)}\subseteq\Omega$, then
$$
\sup_{w\in \overline{D_r(z)}}\abs{F'(w)} \leq \frac1r \sup_{\zeta\in \overline{D_{2r}(z)}}\abs{F(\zeta)}.
$$

::: pf-proof
For $w\in\overline{D_r(z)}$ we have $\overline{D_r(w)}\subseteq\overline{D_{2r}(z)}\subseteq\Omega$, so the Cauchy integral formula gives
$$
\abs{F'(w)} = \abs{\frac1{2\pi i}\int_{\partial D_r(w)}\frac{F(\zeta)}{(\zeta-w)^2}\,d\zeta} \leq \frac1{2\pi}\cdot 2\pi r\cdot\frac{1}{r^2}\sup_{\zeta\in\overline{D_{2r}(z)}}\abs{F(\zeta)}.
$$
:::

:::

::: pf-step
$f_n'\to f'$ locally uniformly on $\Omega$.

::: pf-proof
Let $K\subseteq\Omega$ be compact.
Each $z\in K$ has an $r_z>0$ with $\overline{D_{2r_z}(z)}\subseteq\Omega$, and finitely many discs $D_{r_{z_1}}(z_1),\ldots,D_{r_{z_m}}(z_m)$ cover $K$.
By step [](#f-holo){.pf-ref}, step [](#estimate){.pf-ref} applies to $F=f_n-f$ and gives
$$
\sup_K\abs{f_n'-f'} \leq \max_{1\leq j\leq m}\frac1{r_{z_j}}\sup_{\overline{D_{2r_{z_j}}(z_j)}}\abs{f_n-f},
$$
which tends to $0$ because $f_n\to f$ uniformly on the compact set $\bigcup_j\overline{D_{2r_{z_j}}(z_j)}$.
:::

:::

:::

:::
