---
schema: qual/card@1
id: E-HAT-4.D-5
kind: problem
title: Gysin sequence and Hopf invariant of sphere bundles
classification:
  areas:
  - topology
  topics:
  - Fiber Bundles
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Use the Gysin sequence to show that for a fiber bundle $S^k \to S^m \xrightarrow{p} S^n$ we must have $k = n-1$ and $m = 2n-1$.
Then use the Thom isomorphism to show that the Hopf invariant of $p$ must be $\pm 1$.
:::

::: {.solution}

::: pf

::: pf-step

The Gysin sequence for the sphere bundle $S^k \to S^m \xrightarrow{p} S^n$ is
$$\cdots \to H^{i-k-1}(S^n) \to H^i(S^n) \xrightarrow{p^*} H^i(S^m) \to H^{i-k}(S^n) \to \cdots.$$

::: pf-proof

the Gysin sequence of a sphere bundle.

:::

:::

::: pf-step

$H^i(S^m)$ is nonzero only for $i = 0, m$, and $H^i(S^n)$ is nonzero only for $i = 0, n$.

::: pf-proof

cohomology of spheres.

:::

:::

::: {.pf-step #s3}

The Gysin sequence forces $m = n + k + 1$ (so that the total space $S^m$ has the right dimension).

::: pf-proof

the Euler class lives in $H^{k+1}(S^n)$, which is nonzero only if $k + 1 = n$, i.e. $k = n - 1$; then $m = n + k = 2n - 1$.

:::

:::

::: {.pf-step #s4}

Hence $k = n - 1$ and $m = 2n - 1$.

::: pf-proof

Step [](#s3){.pf-ref}.

:::

:::

::: pf-step

The Euler class $e \in H^n(S^n) = \ZZ$ is a generator (up to sign), since the Gysin sequence is exact and the bundle is nontrivial.

::: pf-proof

the Euler class of the bundle $S^{n-1} \to S^{2n-1} \to S^n$ is $\pm 1$ times the generator of $H^n(S^n)$.

:::

:::

::: {.pf-step #s6}

The Hopf invariant of $p$ equals the Euler class (up to sign), so $H(p) = \pm 1$.

::: pf-proof

by the Thom isomorphism, the Hopf invariant of the bundle map $p$ is the Euler class, which is $\pm 1$.

:::

:::

::: pf-qed

Steps [](#s4){.pf-ref} and [](#s6){.pf-ref}.

:::

:::

:::
