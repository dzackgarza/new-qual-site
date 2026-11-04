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
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 1.3, Exercise 9.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the lifting proof: $f_*$ is trivial because $\pi_1(X)$ is finite and $\ZZ$ is torsion free, the lifting criterion applies to $\RR\to S^1$, and the straight-line homotopy in $\RR$ descends to a null-homotopy of $f$. The hint block agrees with the book's bracketed hint.
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Read line by line against Hatcher, Algebraic Topology, §1.3 Exercise 9. Verified: $f_*$ has finite
    image in $\pi_1(S^1)\cong\ZZ$, and the only finite subgroup of $\ZZ$ is trivial; the lifting
    criterion for the covering $\RR\to S^1$ applies with the chosen basepoint $t_0$ because
    $p_*(\pi_1(\RR,t_0))$ is trivial and $X$ is path connected and locally path connected; and
    $H(x,u)=p((1-u)\widetilde f(x)+ut_0)$ is a continuous homotopy, the straight line staying in $\RR$,
    from $f$ to the constant map at $s_0$. The local path-connectedness hypothesis is used exactly at
    the lifting criterion. No gap found; nothing deferred.
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
