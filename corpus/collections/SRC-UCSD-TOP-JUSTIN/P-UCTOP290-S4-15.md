---
schema: qual/card@1
id: P-UCTOP290-S4-15
kind: problem
title: Count based, unbased and three-sheeted covers for $S_3$
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Groups
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Read sheet 4, Problem 15 against its extraction and PDF page image.
---

::: {.problem}
Let $X$ be path-connected, locally path-connected and
semilocally simply connected, with $\pi_1(X)\cong S_3$.
Up to the appropriate equivalence, how many coverings does
$X$ have of each kind?

(a) Based path-connected coverings.

(b) Unbased path-connected coverings.

(c) Three-sheeted coverings that need not be path-connected.
:::

::: {.solution}

(a) Based connected coverings correspond to subgroups of $S_3$
without identifying conjugate subgroups. There are the trivial
subgroup, the three subgroups of order $2$, the unique subgroup
$A_3$ of order $3$, and the whole group. Thus the answer is
$\boxed{6}$.

(b) Unbased connected coverings correspond to conjugacy classes
of subgroups. The three order-$2$ subgroups are conjugate; the
other three types each form one class. Thus the answer is
$\boxed{4}$.

(c) An unbased three-sheeted covering corresponds to an
isomorphism class of $S_3$-sets of size $3$. A transitive orbit
of size at most $3$ can have size $1$, $2$, or $3$. There is
one orbit type of each size: a fixed point, $S_3/A_3$, and
$S_3/C_2$, respectively. The partitions of $3$ using these
orbit sizes are
$$
3,\qquad 2+1,\qquad 1+1+1.
$$
Each yields one covering. Thus the answer is $\boxed{3}$.

:::
