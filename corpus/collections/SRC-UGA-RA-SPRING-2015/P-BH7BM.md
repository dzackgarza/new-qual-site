---
schema: qual/card@1
id: P-BH7BM
kind: problem
title: Orthogonal projection onto a finite orthonormal set is the best approximation;
  finite-dimensional subspaces of a Hilbert space are closed
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Closure
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Spring 2015 Problem 5 in the preserved UGA real-analysis source extraction.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $\mathcal H$ be a Hilbert space.

1. Let $x\in \mathcal H$ and $\theset{u_n}_{n=1}^N$ be an orthonormal set.
  Prove that the best approximation to $x$ in $\mathcal H$ by an element in $\spanof_\CC\theset{u_n}$ is given by
  $$
  \hat x \definedas \sum_{n=1}^N \inner{x}{u_n}u_n.
  $$
2. Conclude that finite dimensional subspaces of $\mathcal H$ are always closed.
:::
::: {.solution}

::: pf

::: {.pf-step #s1}
$\hat x = \sum_{n=1}^N \inner{x}{u_n} u_n$ satisfies $x - \hat x \perp u_m$ for every $m$.

::: pf-proof
$\inner{x - \hat x}{u_m} = \inner{x}{u_m} - \sum_n \inner{x}{u_n}\inner{u_n}{u_m} = \inner{x}{u_m} - \inner{x}{u_m} = 0$, using orthonormality $\inner{u_n}{u_m} = \delta_{nm}$.
:::

:::

::: {.pf-step #s2}
$x - \hat x \perp \spanof_\CC\theset{u_n}$.

::: pf-proof
step [](#s1){.pf-ref} gives orthogonality to each basis vector, hence to every finite linear combination.
:::

:::

::: {.pf-step #s3}
For every $y = \sum_n c_n u_n \in \spanof_\CC\theset{u_n}$: $\|x - y\|^2 = \|x - \hat x\|^2 + \|\hat x - y\|^2$.

::: pf-proof
$x - y = (x - \hat x) + (\hat x - y)$ with $\hat x - y \in \spanof_\CC\theset{u_n}$ and $x - \hat x \perp \hat x - y$ (step [](#s2){.pf-ref}); the Pythagorean theorem applies.
:::

:::

::: {.pf-step #s4}
$\|x - y\| \ge \|x - \hat x\|$ for all $y \in \spanof_\CC\theset{u_n}$, with equality iff $y = \hat x$.

::: pf-proof
step [](#s3){.pf-ref} shows $\|x - y\|^2 = \|x - \hat x\|^2 + \|\hat x - y\|^2 \ge \|x - \hat x\|^2$; equality forces $\|\hat x - y\| = 0$.
:::

:::

::: pf-step
Q.E.D. (part 1).

::: pf-proof
step [](#s4){.pf-ref} says $\hat x$ is the unique best approximation to $x$ in $\spanof_\CC\theset{u_n}$.
:::

:::

::: pf-step
Part 2: a finite-dimensional subspace $V$ of $\mathcal H$ is closed.

::: pf-proof

::: pf-step
Let $\theset{u_1, \ldots, u_N}$ be an orthonormal basis of $V$ (Gram–Schmidt).

::: pf-proof
$V$ finite-dimensional admits an orthonormal basis.
:::

:::

::: pf-step
$V = \spanof_\CC\theset{u_1,\ldots,u_N}$.

::: pf-proof
an orthonormal set is linearly independent and spans by choice of basis.
:::

:::

::: {.pf-step #s6-3}
If $(y_k) \subseteq V$ converges to $y \in \mathcal H$, then $y \in V$.

::: pf-proof
write $y_k = \sum_n \inner{y_k}{u_n}u_n$ (Fourier expansion in the basis). Continuity of the inner product gives $\inner{y_k}{u_n} \to \inner{y}{u_n}$, so $y_k \to \sum_n \inner{y}{u_n} u_n$; the limit is unique, hence $y = \sum_n \inner{y}{u_n} u_n \in V$.
:::

:::

::: pf-qed
step [](#s6-3){.pf-ref} shows $V$ contains the limits of its convergent sequences, i.e. $V$ is closed.
:::

:::

:::

:::

:::
