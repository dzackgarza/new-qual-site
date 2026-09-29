---
schema: qual/card@1
id: P-BERK90S-18
kind: problem
title: A subset of complex numbers whose sum has modulus at least $\frac{1}{4\sqrt2}\sum\abs{z_j}$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: source-checked
  by: chatgpt
  date: 2026-09-22
  note: Compared the arbitrary complex numbers, the subset of indices, and the lower bound with constant 1/(4 sqrt(2)) with Problem 18 in the retained MinerU Flash extraction of Spring90.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-22
  note: Partitioned the indices into four half-open angular quadrants, selected one carrying at least one quarter of the total modulus, and projected its sum onto the quadrant bisector.
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: Checked disjoint quadrant boundaries, the argument convention at zero, the cosine bound on each quadrant, empty index sets, and the all-zero case.
---

::: {.problem}
Let $z_1,\ldots,z_n\in\CC$. Prove that there is a subset
$$
J\subset\{1,\ldots,n\}
$$
such that
$$
\abs{\sum_{j\in J}z_j}
\ge
\frac{1}{4\sqrt2}\sum_{j=1}^n\abs{z_j}.
$$
:::

::: {.hint}
Group the complex numbers by quadrant. Some quadrant contains
at least one quarter of the total modulus. Projection onto its
bisector retains at least $1/\sqrt2$ of each modulus.
:::

::: {.solution}
Put $M\coloneqq\sum_{j=1}^n\abs{z_j}$. For each $j$, choose
$\theta_j\in[0,2\pi)$ such that
$z_j=\abs{z_j}e^{i\theta_j}$, taking $\theta_j=0$ when $z_j=0$.
For $k\in\{0,1,2,3\}$, define
$$
J_k\coloneqq\left\{j\in\{1,\ldots,n\}:
\frac{k\pi}{2}\leq\theta_j<\frac{(k+1)\pi}{2}\right\},
\qquad
\beta_k\coloneqq\frac{k\pi}{2}+\frac\pi4.
$$

::: pf

::: {.pf-step #s1}

There is $k\in\{0,1,2,3\}$ such that
$$
\sum_{j\in J_k}\abs{z_j}\geq\frac M4.
$$

::: pf-proof

The half-open intervals defining $J_0,J_1,J_2,J_3$ partition
$[0,2\pi)$, so these index sets partition $\{1,\ldots,n\}$.
Consequently,
$$
\sum_{k=0}^3\sum_{j\in J_k}\abs{z_j}=M.
$$
At least one of these four nonnegative sums is at least their
average $M/4$.

:::

:::

::: {.pf-step #s2}

For every $k\in\{0,1,2,3\}$,
$$
\abs{\sum_{j\in J_k}z_j}
\geq\frac1{\sqrt2}\sum_{j\in J_k}\abs{z_j}.
$$

::: pf-proof

For $j\in J_k$, the defining inequalities give
$-\pi/4\leq\theta_j-\beta_k<\pi/4$. Hence
$$
\Re\bigl(e^{-i\beta_k}z_j\bigr)
=\abs{z_j}\cos(\theta_j-\beta_k)
\geq\frac{\abs{z_j}}{\sqrt2}.
$$
Multiplication by $e^{-i\beta_k}$ preserves modulus, and the
modulus of a complex number is at least its real part.
Summing the displayed inequalities gives
$$
\begin{aligned}
\abs{\sum_{j\in J_k}z_j}
&=\abs{e^{-i\beta_k}\sum_{j\in J_k}z_j}\\
&\geq\Re\left(e^{-i\beta_k}\sum_{j\in J_k}z_j\right)\\
&=\sum_{j\in J_k}\Re\bigl(e^{-i\beta_k}z_j\bigr)\\
&\geq\frac1{\sqrt2}\sum_{j\in J_k}\abs{z_j}.
\end{aligned}
$$

:::

:::

::: pf-qed

Choose $k$ as in step [](#s1){.pf-ref} and take $J=J_k$. Step [](#s2){.pf-ref} gives
$$
\abs{\sum_{j\in J}z_j}
\geq\frac1{\sqrt2}\sum_{j\in J}\abs{z_j}
\geq\frac{M}{4\sqrt2}
=\frac1{4\sqrt2}\sum_{j=1}^n\abs{z_j}.
$$
This also covers $M=0$, since all the sums then vanish.

:::

:::

:::
