---
schema: qual/card@1
id: P-FD3UV
kind: problem
title: Every continuous map $\RP^2\to S^1\times S^1$ is null-homotopic
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Fundamental Group
  - Covering Spaces
relations: []
review: draft
audit:
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Completed the missing null-homotopy step by lifting to the universal cover R^2 -> T^2.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 4 of the official UGA Fall 2007 topology exam; it is the same result also recorded for Spring 2013 problem 6.
---

::: {.problem}
Show that any continuous map $f : \RP^2 \to S^1 \times S^1$ is necessarily null-homotopic.
:::

::: {.solution}

::: pf

::: {.pf-step #f-star-zero}
The induced homomorphism
\[
f_*:\pi_1(\RP^2)\to\pi_1(T^2)
\]
is zero.

::: pf-proof
We have
\[
\pi_1(\RP^2)\cong\ZZ/2\ZZ,
\qquad
\pi_1(T^2)\cong\ZZ^2.
\]
If $u=f_*([1])$, then
\[
2u=f_*(2[1])=0.
\]
The group $\ZZ^2$ is torsion-free, so $u=0$.
:::

:::

::: {.pf-step #f-lifts}
The map $f$ lifts to the universal cover
\[
p:\RR^2\to T^2.
\]

::: pf-proof
Choose basepoints.
The covering-space lifting criterion requires
\[
f_*\pi_1(\RP^2)
\subseteq
p_*\pi_1(\RR^2).
\]
Both sides are zero: the left by step [](#f-star-zero){.pf-ref} and the right because $\RR^2$ is simply connected.
Thus there is a continuous lift
\[
\widetilde f:\RP^2\to\RR^2
\]
such that
\[
p\circ\widetilde f=f.
\]
:::

:::

::: pf-step
$f$ is null-homotopic.

::: pf-proof
The universal cover $\RR^2$ is contractible, so $\widetilde f$ is homotopic to a constant map.
Composing this homotopy with $p$ gives a homotopy from $f$ to a constant map in $T^2$.
:::

:::

:::

:::
