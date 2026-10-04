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
Prove that $e ^ { A } = \left( e ^ { A / N } \right) ^ { N } , N \in \mathbb { R }$
:::

::: {.remark}
The source states $N\in\mathbb R$, but the ordinary matrix power
$(e^{A/N})^N$ is defined here only for integer $N$. The intended statement is
for $N\in\mathbb N$.
:::

::: {.solution}
Fix
$$
N\in\mathbb N.
$$

<1>1. The matrix $A/N$ commutes with itself.

::: {.proof}
Every matrix commutes with itself:
$$
\left[\frac AN,\frac AN\right]=0.
$$
:::

<1>2. For every positive integer $k$,
$$
\left(e^{A/N}\right)^k
=
e^{kA/N}.
$$

::: {.proof}
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

<1>3. Taking $k=N$ in step <1>2 gives
$$
\left(e^{A/N}\right)^N
=
e^A.
$$

::: {.proof}
Substitute $k=N$:
$$
e^{kA/N}
=
e^{NA/N}
=
e^A.
$$
:::

<1>4. Hence
$$
\boxed{e^A=\left(e^{A/N}\right)^N}.
$$

::: {.proof}
This is step <1>3 with the two sides reversed.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 proves the corrected intended statement for every
$N\in\mathbb N$.
:::
:::
