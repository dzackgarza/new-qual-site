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

::: problem
When do the powers of a square complex matrix $A \in M_n(\mathbb{C})$ tend to zero ($\lim_{k \to \infty} A^k = 0$)?
:::

::: solution
One has
\[
A^k\longrightarrow0
\quad\Longleftrightarrow\quad
\rho(A)<1,
\]
where $\rho(A)$ is the spectral radius.

Put $A=PJP^{-1}$ in Jordan normal form. Then
\[
A^k=PJ^kP^{-1},
\]
so $A^k\to0$ if and only if every Jordan block tends to zero.

For a Jordan block
\[
J_\lambda=\lambda I+N,
\qquad N^d=0,
\]
one has
\[
J_\lambda^k
=
\sum_{j=0}^{d-1}\binom{k}{j}\lambda^{k-j}N^j.
\]
If $|\lambda|<1$, then for each fixed $j$,
\[
\binom{k}{j}|\lambda|^{k-j}\to0,
\]
because exponential decay dominates polynomial growth. Hence $J_\lambda^k\to0$.

If $|\lambda|\ge1$, the diagonal entries of $J_\lambda^k$ are $\lambda^k$, which do not tend to zero. Thus a Jordan block tends to zero exactly when its eigenvalue has modulus $<1$.

Therefore $A^k\to0$ exactly when every eigenvalue of $A$ lies in the open unit disk, equivalently when $\rho(A)<1$.
:::
