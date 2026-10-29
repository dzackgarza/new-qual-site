---
schema: qual/card@1
id: P-HPQ7U
kind: problem
title: When $A^n\to 0$
classification:
  areas:
  - algebra
  topics:
  - Eigenvalues and Eigenvectors
  - Matrices
  - Nilpotence
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09

---

::: {.problem}
When do the powers of a square complex matrix $A \in M_n(\CC)$ tend to zero ($\lim_{k \to \infty} A^k = 0$)?
:::

::: {.solution}
Write $\rho(A)$ for the spectral radius of $A$, the largest modulus of an eigenvalue.
Put $A=PJP^{-1}$ in Jordan normal form.

::: pf

::: {.pf-step #blocks}
$A^k\to0$ if and only if $J_\lambda^k\to0$ for every Jordan block $J_\lambda$ of $J$.

::: pf-proof
Since $A^k=PJ^kP^{-1}$ and conjugation by $P$ is a homeomorphism of $M_n(\CC)$, $A^k\to0$ if and only if $J^k\to0$, and $J^k$ is block diagonal with blocks $J_\lambda^k$.
:::

:::

::: {.pf-step #small}
If $\abs{\lambda}<1$, then $J_\lambda^k\to0$.

::: pf-proof
Write $J_\lambda=\lambda I+N$ with $N^d=0$. Since $\lambda I$ and $N$ commute,
$$
J_\lambda^k
=
\sum_{j=0}^{d-1}\binom{k}{j}\lambda^{k-j}N^j.
$$
For each fixed $j$, $\binom{k}{j}\abs{\lambda}^{k-j}\to0$ as $k\to\infty$, because $\binom{k}{j}$ grows polynomially in $k$ while $\abs{\lambda}^{k}$ decays exponentially.
:::

:::

::: {.pf-step #large}
If $\abs{\lambda}\ge1$, then $J_\lambda^k\not\to0$.

::: pf-proof
The diagonal entries of $J_\lambda^k$ are $\lambda^k$, and $\abs{\lambda^k}\ge1$.
:::

:::

::: pf-step
$A^k\to0$ if and only if $\boxed{\rho(A)<1}$, that is, every eigenvalue of $A$ lies in the open unit disk.

::: pf-proof
Combine steps [](#blocks){.pf-ref}, [](#small){.pf-ref} and [](#large){.pf-ref}.
:::

:::

:::

:::
