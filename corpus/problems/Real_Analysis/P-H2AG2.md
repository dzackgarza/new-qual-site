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

::: {.problem}
Show that the set $\theset{ u_k(j) \definedas \delta_{kj} } \subseteq \ell^2(\ZZ)$ forms an orthonormal system.
:::

::: {.solution}

::: pf

::: pf-step

$\theset{u_k}_{k \in \ZZ}$ is orthonormal: $\norm{u_k}_2 = 1$ for every $k$ and $\inner{u_k}{u_m} = 0$ for $k \neq m$.

::: pf-proof

::: pf-step

$u_k = (\delta_{kj})_{j \in \ZZ}$ lies in $\ell^2(\ZZ)$ and $\norm{u_k}_2 = 1$.

::: pf-proof

Exactly one entry of $u_k$, at $j = k$, is nonzero, and it equals $1$, so $\norm{u_k}_2^2 = \sum_j \abs{\delta_{kj}}^2 = 1$.

:::

:::

::: pf-step

$\inner{u_k}{u_m} = 0$ for $k \neq m$.

::: pf-proof

$\inner{u_k}{u_m} = \sum_j \delta_{kj}\delta_{mj}$, and each term vanishes because $j$ cannot equal both $k$ and $m$.

:::

:::

:::

:::

:::

:::

::: {.remark}
$\theset{u_k}$ is an orthonormal basis of $\ell^2(\ZZ)$: its span is the space of finitely supported sequences, which is dense, since the truncations of $a \in \ell^2(\ZZ)$ to $|j| \le N$ converge to $a$.
:::
