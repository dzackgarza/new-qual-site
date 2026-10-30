---
schema: qual/card@1
id: P-APAF20G
kind: problem
title: Eigenvalues of a compact-group representation have modulus one
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $R\colon G\to\mathrm{GL}(H)$ be a linear representation of a compact group $G$ on a finite-dimensional Hilbert space $H$.
Prove that, for all $g\in G$, the eigenvalues of $R(g)$ have modulus $1$.
:::

::: {.solution}

Assume, as usual for representations of compact topological groups, that $R$ is continuous.

::: pf

::: {.pf-step #uniform-operator-norm-bound}
There is a constant $M>0$ such that
$$
\norm{R(h)}_{\mathrm{op}}\le M
\qquad\text{for every }h\in G.
$$

::: pf-proof
Because $G$ is compact and $R:G\to\mathrm{GL}(H)$ is continuous, the image $R(G)$ is compact. The operator norm is continuous on the finite-dimensional space $\operatorname{End}(H)$, so it attains a finite maximum on $R(G)$.
:::

:::

::: {.pf-step #eigenvalue-modulus-at-most-one}
If $R(g)v=\lambda v$ with $v\ne0$, then $\abs{\lambda}\le1$.

::: pf-proof
For every positive integer $n$,
$$
R(g^n)v=R(g)^nv=\lambda^n v.
$$
Hence, by step [](#uniform-operator-norm-bound){.pf-ref},
$$
\abs{\lambda}^n\norm{v}
=\norm{R(g^n)v}
\le \norm{R(g^n)}_{\mathrm{op}}\norm{v}
\le M\norm{v}.
$$
Since $v\ne0$,
$$
\abs{\lambda}^n\le M
$$
for every $n$. If $\abs{\lambda}>1$, the left side tends to infinity, a contradiction. Thus $\abs{\lambda}\le1$.
:::

:::

::: {.pf-step #eigenvalue-modulus-at-least-one}
In fact $\abs{\lambda}\ge1$.

::: pf-proof
Since $R(g)$ is invertible,
$$
R(g^{-1})v=R(g)^{-1}v=\lambda^{-1}v.
$$
Applying step [](#eigenvalue-modulus-at-most-one){.pf-ref} to the group element $g^{-1}$ and its eigenvalue $\lambda^{-1}$ gives
$$
\abs{\lambda^{-1}}\le1,
$$
so $\abs{\lambda}\ge1$.
:::

:::

::: pf-step
Therefore every eigenvalue of every $R(g)$ has modulus $1$.

::: pf-proof
Combine steps [](#eigenvalue-modulus-at-most-one){.pf-ref} and [](#eigenvalue-modulus-at-least-one){.pf-ref}:
$$
1\le\abs{\lambda}\le1.
$$
Hence
$$
\boxed{\abs{\lambda}=1}.
$$
:::

:::

:::

:::
