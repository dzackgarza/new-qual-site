---
schema: qual/card@1
id: P-UG5YN
kind: problem
title: Every continuous map $\RP^n\to S^1$ is null-homotopic for $n\geq 2$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homotopy
  - Covering Spaces
relations: []
review: draft
audit:
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Completed the missing implication f_*=0 => f null-homotopic using the universal cover R -> S^1.
---

::: {.problem}
Prove that, for $n \geq 2$, every continuous map $f: \RP^n \to S^1$ is null-homotopic.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The induced homomorphism
\[
f_*:\pi_1(\RP^n)\to\pi_1(S^1)
\]
is zero.

::: pf-proof

For $n\ge2$,
\[
\pi_1(\RP^n)\cong\ZZ/2\ZZ,
\qquad
\pi_1(S^1)\cong\ZZ.
\]
Let $u=f_*([1])\in\ZZ$.
Since $2[1]=0$ in $\ZZ/2\ZZ$,
\[
2u=f_*(2[1])=f_*(0)=0.
\]
The group $\ZZ$ has no nonzero element of order $2$, so $u=0$.

:::

:::

::: pf-step

The map $f$ lifts through the universal covering map
\[
p:\RR\to S^1,
\qquad
p(t)=e^{2\pi i t}.
\]

::: pf-proof

Choose basepoints and regard $f$ as a based map.
The covering-space lifting criterion requires
\[
f_*\pi_1(\RP^n)
\subseteq
p_*\pi_1(\RR).
\]
By step [](#s1){.pf-ref} the left side is zero, and the right side is zero because $\RR$ is simply connected.
Thus there is a continuous lift
\[
\widetilde f:\RP^n\to\RR
\]
with
\[
p\circ\widetilde f=f.
\]

:::

:::

::: pf-step

$f$ is null-homotopic.

::: pf-proof

The space $\RR$ is contractible, so $\widetilde f$ is homotopic to a constant map.
Composing this homotopy with $p$ gives a homotopy from
\[
f=p\circ\widetilde f
\]
to a constant map in $S^1$.

:::

:::

:::

:::
