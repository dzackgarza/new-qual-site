---
schema: qual/card@1
id: P-H2AG2
kind: problem
title: The Kronecker sequences $u_k(j)=\delta_{kj}$ form an orthonormal system in
  $\ell^2(\ZZ)$
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - L²
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: problem
Show that the set \( \ts{ u_k(j) \da \delta_{kj} } \subseteq \ell^2(\ZZ) \) forms an orthonormal system.
:::
::: {.solution}
<1>1. Each $u_k = (\delta_{kj})_{j \in \ZZ}$ lies in $\ell^2(\ZZ)$.
::: {.proof}
$\|u_k\|_2^2 = \sum_j |\delta_{kj}|^2 = 1 < \infty$.
:::

<1>2. $\|u_k\|_2 = 1$ for every $k$.
::: {.proof}
<1>1 computation: exactly one entry (at $j = k$) is $1$, all others $0$.
:::

<1>3. $u_k \perp u_m$ for $k \neq m$: $\inner{u_k}{u_m} = \sum_j \delta_{kj}\delta_{mj} = 0$.
::: {.proof}
for each $j$, $\delta_{kj}\delta_{mj} = 0$ since $k \neq m$ (no single $j$ can equal both).
:::

<1>4. Q.E.D.: $\ts{u_k}_{k \in \ZZ}$ is an orthonormal system in $\ell^2(\ZZ)$.
::: {.proof}
<1>2 and <1>3 are exactly the two defining properties of orthonormality.
:::
(It is in fact an orthonormal basis: $\ell^2(\ZZ)$ is complete, and the $u_k$'s span a dense subspace — the finitely supported sequences.)
:::
