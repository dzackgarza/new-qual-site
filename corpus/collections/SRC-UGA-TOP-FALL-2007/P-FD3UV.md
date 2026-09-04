---
schema: qual/card@1
id: P-FD3UV
kind: problem
title: Every continuous map $\mathbb{RP}^2\to S^1\times S^1$ is null-homotopic
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
---

::: problem
Show that any continuous map $f : \RP^2 \to S^1 \times S^1$ is necessarily null-homotopic.
:::

::: {.solution}
<1>1. The induced homomorphism
\[
f_*:\pi_1(\RP^2)\to\pi_1(T^2)
\]
is zero.
::: {.proof}
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

<1>2. The map $f$ lifts to the universal cover
\[
p:\RR^2\to T^2.
\]
::: {.proof}
Choose basepoints.
The covering-space lifting criterion requires
\[
f_*\pi_1(\RP^2)
\subseteq
p_*\pi_1(\RR^2).
\]
Both sides are zero: the left by <1>1 and the right because $\RR^2$ is simply connected.
Thus there is a continuous lift
\[
\widetilde f:\RP^2\to\RR^2
\]
such that
\[
p\circ\widetilde f=f.
\]
:::

<1>3. $f$ is null-homotopic.
::: {.proof}
The universal cover $\RR^2$ is contractible, so $\widetilde f$ is homotopic to a constant map.
Composing this homotopy with $p$ gives a homotopy from $f$ to a constant map in $T^2$.
:::
:::
