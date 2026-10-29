---
schema: qual/card@1
id: P-WESRA10-I3
kind: problem
title: 'State the spectral theorem for compact self-adjoint operators'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part I, item 3 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
State the spectral theorem for compact symmetric (self-adjoint) operators on a Hilbert space.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Let $H$ be a real or complex Hilbert space and let
$$
T:H\to H
$$
be compact and self-adjoint. Then every nonzero spectral value of $T$ is a
real eigenvalue, each nonzero eigenspace is finite-dimensional, distinct
eigenspaces are orthogonal, and $0$ is the only possible accumulation point
of the nonzero spectrum.


::: pf-proof

This is the spectral theorem for compact self-adjoint operators.

:::

:::

::: {.pf-step #s1-2}

There is an orthonormal family of eigenvectors $(e_j)$ for the nonzero
eigenvalues $(\lambda_j)$ such that
$$
\overline{\operatorname{span}}\{e_j\}
=(\ker T)^\perp,
$$
and, after adjoining any orthonormal basis of $\ker T$, one obtains an
orthonormal basis of $H$ consisting entirely of eigenvectors of $T$.


::: pf-proof

This is the orthogonal-eigenspace decomposition supplied by the same
spectral theorem. The kernel is precisely the eigenspace for eigenvalue $0$.

:::

:::

::: {.pf-step #s1-3}

For every $x\in H$,
$$
\boxed{
Tx=\sum_j \lambda_j\langle x,e_j\rangle e_j
}
$$
where the sum is finite or countable and converges in the Hilbert-space norm.
If there are infinitely many nonzero eigenvalues, then
$$
\lambda_j\to0.
$$


::: pf-proof

Expand the component of $x$ in $(\ker T)^\perp$ in the orthonormal
eigenbasis from step [](#s1-2){.pf-ref}. The component of $x$ in $\ker T$ is annihilated
by $T$, while $T e_j=\lambda_j e_j$ on each nonzero eigenspace. This yields
the displayed expansion. Compactness gives that an infinite sequence of
distinct nonzero eigenvalues can accumulate only at $0$.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} give the standard precise statement of the spectral
theorem requested in the problem.

:::

:::

:::
