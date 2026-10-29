---
schema: qual/card@1
id: P-ODNWF
kind: problem
title: An ideal of a PID containing an irreducible $a$ equals $Ra$
classification:
  areas:
  - algebra
  topics:
  - Principal Ideal Domains
  - Ideals
  - Factorization
relations: []
review: draft
---

::: {.problem}
Let $R$ be a PID, let $I\subsetneq R$ be a proper ideal, and suppose $a\in I$ is irreducible. Prove that
$$
I=(a).
$$
:::

::: {.solution}
Since $R$ is a PID, write $I=(d)$.

::: pf

::: {.pf-step #factor}

$a=dr$ for some $r\in R$, and $d$ is not a unit.

::: pf-proof

Since $a\in(d)$, such an $r$ exists. If $d$ were a unit, then $I=(d)=R$, contradicting that $I$ is proper.

:::

:::

::: pf-step

$I=(a)$.

::: pf-proof

Since $a$ is irreducible and $d$ is not a unit, the factorization $a=dr$ of step [](#factor){.pf-ref} forces $r$ to be a unit. Hence $d$ and $a$ are associates, and $I=(d)=(a)$.

:::

:::

:::

:::
