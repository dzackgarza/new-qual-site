---
schema: qual/card@1
id: P-K3QJY
kind: problem
title: For an $S^3$-bundle over $S^5$, $H_3(E)\cong\ZZ$
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Homology
relations: []
review: draft
audit:
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Replaced the erroneous pi_0 calculation and scratchpad TODO with the homotopy-LES/Hurewicz argument.
---

Let $S^3 \to E \to S^5$ be a fiber bundle and compute $H_3(E)$.

::: {.solution}
<1>1. The total space $E$ is path connected and satisfies
\[
\pi_1(E)=\pi_2(E)=0.
\]
::: {.proof}
The fiber and base, $S^3$ and $S^5$, are path connected, so the total space of the fiber bundle is path connected.

The homotopy long exact sequence contains
\[
\pi_2(S^3)\longrightarrow\pi_2(E)\longrightarrow\pi_2(S^5)
\]
and
\[
\pi_1(S^3)\longrightarrow\pi_1(E)\longrightarrow\pi_1(S^5).
\]
All four sphere groups displayed on the outside vanish, so exactness gives
\[
\pi_2(E)=\pi_1(E)=0.
\]
:::

<1>2. $\pi_3(E)\cong\ZZ$.
::: {.proof}
The same long exact sequence contains
\[
\pi_4(S^5)\longrightarrow\pi_3(S^3)
\longrightarrow\pi_3(E)\longrightarrow\pi_3(S^5).
\]
Since
\[
\pi_4(S^5)=0,
\qquad
\pi_3(S^3)\cong\ZZ,
\qquad
\pi_3(S^5)=0,
\]
exactness makes the middle map an isomorphism.
:::

<1>3. $H_3(E)\cong\ZZ$.
::: {.proof}
By <1>1, $E$ is $2$-connected. The Hurewicz theorem therefore gives an isomorphism
\[
\pi_3(E)\xrightarrow{\sim}H_3(E).
\]
Apply <1>2.
:::
:::
