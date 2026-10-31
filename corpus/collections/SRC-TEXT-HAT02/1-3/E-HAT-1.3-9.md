---
schema: qual/card@1
id: E-HAT-1.3-9
kind: problem
title: Maps to $S^1$ from spaces with finite fundamental group
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.exercise}
Show that if a path-connected, locally path-connected space $X$ has $\pi_1(X)$ finite, then every map $f: X \to S^1$ is nullhomotopic.
:::

::: {.hint}
Use the covering map $\RR\to S^1$.
:::

::: {.solution}
Fix $x_0\in X$, let $s_0=f(x_0)$, and choose $t_0\in\RR$ with $e^{2\pi i t_0}=s_0$.

::: pf

::: pf-step
The induced homomorphism $f_*:\pi_1(X,x_0)\to\pi_1(S^1,s_0)\cong\ZZ$ is trivial.

::: pf-proof
The image of a finite group under a homomorphism is finite. The only finite subgroup of $\ZZ$ is the trivial subgroup.
:::

:::

::: pf-step
The map $f$ has a lift $\widetilde f:X\to\RR$ through $p(t)=e^{2\pi i t}$ with $\widetilde f(x_0)=t_0$.

::: pf-proof
Both $f_*(\pi_1(X,x_0))$ and $p_*(\pi_1(\RR,t_0))$ are trivial. Since $X$ is path connected and locally path connected, the covering-space lifting criterion applies.
:::

:::

::: pf-step
The map $f$ is nullhomotopic.

::: pf-proof
The homotopy
$$
H(x,u)=p\bigl((1-u)\widetilde f(x)+u t_0\bigr)
$$
is continuous, equals $f(x)$ at $u=0$, and is the constant map with value $s_0$ at $u=1$.
:::

:::

:::

:::
