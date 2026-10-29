---
schema: qual/card@1
id: P-MV7O6
kind: problem
title: Maximum modulus principle on the interior of a simple closed contour
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
review: draft
---

::: {.problem}
Let $\Omega$ be a simply connected open set and let $\gamma$ be a simple closed contour in $\Omega$ and enclosing a bounded region $U$ anticlockwise.
Let $f: \ \Omega \to \CC$ be a holomorphic function and $\abs{f(z)}\leq M$ for all $z\in \gamma$.
Prove that $\abs{f(z)}\leq M$ for all $z\in U$.
:::

::: {.solution}
::: pf

::: {.pf-step #closure-in-omega}
$\overline U=U\cup\gamma$ is a compact subset of $\Omega$, and $U$ is connected.

::: pf-proof
By the Jordan curve theorem $U$ is the bounded component of $\CC\setminus\gamma$, connected with boundary $\gamma$. If some $p\in U$ were not in $\Omega$, then $\gamma$ would have winding number $\pm1$ about $p\notin\Omega$, contradicting the simple connectivity of $\Omega$, in which every closed curve has winding number $0$ about every point outside $\Omega$.
:::

:::

::: pf-step
$\abs{f(z)}\le M$ for all $z\in U$.

::: pf-proof
By step [](#closure-in-omega){.pf-ref}, the continuous function $\abs{f}$ attains its maximum on $\overline U$ at some point $z_1$. If $z_1\in\gamma$, then $\abs{f}\le\abs{f(z_1)}\le M$ on $U$. If $z_1\in U$, then $\abs{f}$ has a local maximum at an interior point of the connected open set $U$, so by the maximum modulus principle $f$ is constant on $U$, hence by continuity on $\overline U$, and its constant modulus equals its modulus on $\gamma$, which is at most $M$.
:::

:::

:::
:::
