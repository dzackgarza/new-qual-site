---
schema: qual/card@1
id: P-BKF07-4B
kind: problem
title: Prime ideals of a product of two fields
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Fall 2007 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked maximality of the projection kernels and the
    idempotent argument exhausting all prime ideals against the vendored
    solution.
---

::: {.problem}
Let \(K,L\) be fields, and give \(K\times L\) componentwise addition and multiplication.
Find all prime ideals of \(K\times L\).
:::

::: {.solution}
Let
$$
I\coloneqq K\times\{0\},
\qquad
J\coloneqq\{0\}\times L.
$$

<1>1. The ideals $I$ and $J$ are maximal, hence prime.

::: {.proof}
The second coordinate projection
$$
\pi_L:K\times L\longrightarrow L
$$
is surjective with kernel $I$, so
$$
(K\times L)/I\cong L.
$$
Since $L$ is a field, $I$ is maximal. Similarly, the first coordinate
projection has kernel $J$ and quotient isomorphic to $K$, so $J$ is
maximal.
:::

<1>2. Every prime ideal $P\subseteq K\times L$ is equal to $I$ or
$J$.

::: {.proof}
In $K\times L$,
$$
(1,0)(0,1)=(0,0)\in P.
$$
Since $P$ is prime, either $(1,0)\in P$ or $(0,1)\in P$.

If $(1,0)\in P$, then for every $a\in K$,
$$
(a,0)=(a,0)(1,0)\in P,
$$
so $I\subseteq P$. By maximality of $I$ from step <1>1 and properness
of the prime ideal $P$, this forces $P=I$.

If $(0,1)\in P$, the same argument gives $J\subseteq P$, hence
$P=J$.
:::

<1>3. The prime ideals of $K\times L$ are exactly
$$
\boxed{K\times\{0\},\ \{0\}\times L}.
$$

::: {.proof}
Step <1>1 shows that both displayed ideals are prime, and step <1>2
shows that there are no others.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested classification.
:::
:::
