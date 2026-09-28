---
schema: qual/card@1
id: P-HCAX13
kind: problem
title: Boundary signs constrain linear combinations of harmonic functions
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Principle
  - Harmonic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $f_1,\ldots,f_n$ be harmonic on the unit disk and continuous on its closure.
Show that no linear combination of the $f_i$ can be negative on the boundary and positive at an interior point.
:::

::: {.solution}
Let $c_1,\ldots,c_n\in\RR$ and $u=\sum_{k=1}^nc_kf_k$.

<1>1. $u$ is harmonic on $\DD$ and continuous on $\overline\DD$.

::: {.proof}
The Laplacian is linear, so $\Delta u=\sum_kc_k\Delta f_k=0$ on $\DD$, and a
finite linear combination of continuous functions on $\overline\DD$ is
continuous.
:::

<1>2. If $u\le0$ on $\partial\DD$, then $u\le0$ on $\overline\DD$.

::: {.proof}
Suppose $u(z_0)>0$ for some $z_0\in\DD$. The continuous function $u$ attains
its maximum on the compact set $\overline\DD$ at some $w$, with
$u(w)\ge u(z_0)>0\ge\max_{\partial\DD}u$, so $w\in\DD$. By the strong maximum
principle for harmonic functions on the connected open set $\DD$, $u$ is the
constant $u(w)>0$ on $\DD$, and by continuity also on $\partial\DD$, a
contradiction.
:::

<1>3. Q.E.D.

::: {.proof}
A linear combination $u$ that is negative on $\partial\DD$ satisfies $u\le0$ on
$\partial\DD$, so by steps <1>1 and <1>2 it is not positive at any point of
$\DD$.
:::
:::
