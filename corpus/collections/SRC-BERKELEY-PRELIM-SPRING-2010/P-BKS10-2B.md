---
schema: qual/card@1
id: P-BKS10-2B
kind: problem
title: Simplicity of a full matrix ring
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
  note: Checked against the vendored UC Berkeley Spring 2010 preliminary-exam solution packet, which reproduces the problem statement before its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the matrix-unit isolation argument for an arbitrary nonzero two-sided ideal.
---

::: {.problem}
Show that the ring of all $n\times n$ matrices over a field has no two-sided ideals other than $0$ and the whole ring.
:::

::: {.solution}
Let $k$ be the field and write
$$
R\coloneqq M_n(k).
$$
For $1\leq r,s\leq n$, let $E_{rs}$ denote the standard matrix unit.

::: pf

::: {.pf-step #single-unit-in-ideal}
Let $I\subseteq R$ be a nonzero two-sided ideal. Then $I$ contains
at least one matrix unit $E_{rs}$.

::: pf-proof
Choose a nonzero matrix
$$
A=(a_{ij})\in I.
$$
There are indices $p,q$ with
$$
a_{pq}\neq0.
$$
For arbitrary indices $r,s$, two-sided ideal closure gives
$$
E_{rp}AE_{qs}\in I.
$$
A direct multiplication of matrix units gives
$$
E_{rp}AE_{qs}
=
a_{pq}E_{rs}.
$$
In particular, taking any fixed $r,s$ and multiplying by the scalar
$a_{pq}^{-1}\in k$ shows
$$
E_{rs}\in I.
$$
:::

:::

::: {.pf-step #all-units-in-ideal}
Every matrix unit $E_{rs}$ belongs to $I$.

::: pf-proof
The computation in step [](#single-unit-in-ideal){.pf-ref} holds for arbitrary $r$ and $s$, while the
same nonzero entry $a_{pq}$ of $A$ is used throughout. Therefore
$$
E_{rs}\in I
$$
for every pair of indices.
:::

:::

::: {.pf-step #nonzero-ideal-is-whole}
Every nonzero two-sided ideal $I$ equals $R$.

::: pf-proof
The matrix units
$$
\{E_{rs}:1\leq r,s\leq n\}
$$
form a $k$-basis of $M_n(k)$. By step [](#all-units-in-ideal){.pf-ref}, they all lie in $I$. Since an
ideal is in particular an additive subgroup closed under multiplication by
scalar matrices, it contains every $k$-linear combination of the matrix
units. Hence
$$
I=R.
$$
:::

:::

::: {.pf-step #ideal-classification}
The only two-sided ideals of $M_n(k)$ are
$$
\boxed{0\text{ and }M_n(k)}.
$$

::: pf-proof
The zero ideal is a two-sided ideal, and step [](#nonzero-ideal-is-whole){.pf-ref} shows that every nonzero
two-sided ideal is the whole ring.
:::

:::

::: pf-qed
Step [](#ideal-classification){.pf-ref} is the required classification.
:::

:::

:::
