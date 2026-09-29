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

::: pf

::: {.pf-step #I-J-maximal-prime}
The ideals $I$ and $J$ are maximal, hence prime.

::: pf-proof
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

:::

::: {.pf-step #every-prime-is-I-or-J}
Every prime ideal $P\subseteq K\times L$ is equal to $I$ or
$J$.

::: pf-proof
In $K\times L$,
$$
(1,0)(0,1)=(0,0)\in P.
$$
Since $P$ is prime, either $(1,0)\in P$ or $(0,1)\in P$.

If $(1,0)\in P$, then for every $a\in K$,
$$
(a,0)=(a,0)(1,0)\in P,
$$
so $I\subseteq P$. By maximality of $I$ from step [](#I-J-maximal-prime){.pf-ref} and properness
of the prime ideal $P$, this forces $P=I$.

If $(0,1)\in P$, the same argument gives $J\subseteq P$, hence
$P=J$.
:::

:::

::: {.pf-step #prime-ideals-list}
The prime ideals of $K\times L$ are exactly
$$
\boxed{K\times\{0\},\ \{0\}\times L}.
$$

::: pf-proof
Step [](#I-J-maximal-prime){.pf-ref} shows that both displayed ideals are prime, and step [](#every-prime-is-I-or-J){.pf-ref}
shows that there are no others.
:::

:::

::: pf-qed
Step [](#prime-ideals-list){.pf-ref} gives the requested classification.
:::

:::

:::
