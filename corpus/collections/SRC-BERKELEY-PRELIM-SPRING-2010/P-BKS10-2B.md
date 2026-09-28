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

<1>1. Let $I\subseteq R$ be a nonzero two-sided ideal. Then $I$ contains
at least one matrix unit $E_{rs}$.

::: {.proof}
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

<1>2. Every matrix unit $E_{rs}$ belongs to $I$.

::: {.proof}
The computation in step <1>1 holds for arbitrary $r$ and $s$, while the
same nonzero entry $a_{pq}$ of $A$ is used throughout. Therefore
$$
E_{rs}\in I
$$
for every pair of indices.
:::

<1>3. Every nonzero two-sided ideal $I$ equals $R$.

::: {.proof}
The matrix units
$$
\{E_{rs}:1\leq r,s\leq n\}
$$
form a $k$-basis of $M_n(k)$. By step <1>2, they all lie in $I$. Since an
ideal is in particular an additive subgroup closed under multiplication by
scalar matrices, it contains every $k$-linear combination of the matrix
units. Hence
$$
I=R.
$$
:::

<1>4. The only two-sided ideals of $M_n(k)$ are
$$
\boxed{0\text{ and }M_n(k)}.
$$

::: {.proof}
The zero ideal is a two-sided ideal, and step <1>3 shows that every nonzero
two-sided ideal is the whole ring.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required classification.
:::
:::
