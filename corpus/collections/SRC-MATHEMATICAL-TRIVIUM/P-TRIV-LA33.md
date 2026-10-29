---
schema: qual/card@1
id: P-TRIV-LA33
kind: problem
title: $e^A=(e^{A/N})^N$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 33, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Prove that $e ^ { A } = \left( e ^ { A / N } \right) ^ { N } , N \in \RR$
:::

::: {.remark}
The source states $N\in\RR$, but the ordinary matrix power
$(e^{A/N})^N$ is defined here only for integer $N$. The intended statement is
for $N\in\NN$.
:::

::: {.solution}

Fix
$$
N\in\NN.
$$

::: pf

::: pf-step

The matrix $A/N$ commutes with itself.


::: pf-proof

Every matrix commutes with itself:
$$
\left[\frac AN,\frac AN\right]=0.
$$

:::

:::

::: {.pf-step #s1-2}

For every positive integer $k$,
$$
\left(e^{A/N}\right)^k
=
e^{kA/N}.
$$


::: pf-proof

Proceed by induction on $k$. For $k=1$ the identity is immediate.

Assume
$$
\left(e^{A/N}\right)^k
=
e^{kA/N}.
$$
The matrices $kA/N$ and $A/N$ commute, so by the commuting-exponential
identity,
$$
e^{kA/N}e^{A/N}
=
e^{(k+1)A/N}.
$$
Therefore
$$
\left(e^{A/N}\right)^{k+1}
=
e^{(k+1)A/N}.
$$

:::

:::

::: {.pf-step #s1-3}

Taking $k=N$ in step [](#s1-2){.pf-ref} gives
$$
\left(e^{A/N}\right)^N
=
e^A.
$$


::: pf-proof

Substitute $k=N$:
$$
e^{kA/N}
=
e^{NA/N}
=
e^A.
$$

:::

:::

::: {.pf-step #s1-4}

Hence
$$
\boxed{e^A=\left(e^{A/N}\right)^N}.
$$


::: pf-proof

This is step [](#s1-3){.pf-ref} with the two sides reversed.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves the corrected intended statement for every
$N\in\NN$.

:::

:::

:::
