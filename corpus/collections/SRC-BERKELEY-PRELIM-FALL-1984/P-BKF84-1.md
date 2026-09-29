---
schema: qual/card@1
id: P-BKF84-1
kind: problem
title: Powers entering a finite-index subgroup
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 1 of the deterministic MinerU Flash extraction of the Berkeley Fall 1984 preliminary exam.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Checked the index-three counterexample to Part (1) and the left-coset pigeonhole argument for Part (2).
---

::: {.problem}
Let $G$ be a group and let $H\le G$ have finite index $n$.
Prove or disprove:

1. If $a\in G$, then $a^n\in H$.

2. If $a\in G$, then for some $k$ with $1\le k\le n$ one has $a^k\in H$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Statement (1) is false in general.

::: pf-proof

Take
$$
G=S_3
$$
and
$$
H=\langle(12)\rangle
=
\{e,(12)\}.
$$
Then
$$
[G:H]=3,
$$
so $n=3$. Let
$$
a=(13).
$$
Since $a$ has order $2$,
$$
a^3=a=(13)\notin H.
$$
Thus an index-$n$ subgroup need not contain the $n$-th power of every
element when the subgroup is not normal.

:::

:::

::: {.pf-step #s2}

Statement (2) is true.

::: pf-proof

Consider the $n+1$ left cosets
$$
H,
\quad
aH,
\quad
a^2H,
\quad
\ldots,
\quad
a^nH.
$$
There are only $n$ distinct left cosets of $H$ in $G$, so two of these
must agree. Thus for some integers
$$
0\leq i<j\leq n
$$
one has
$$
a^iH=a^jH.
$$
Left multiplication by $a^{-i}$ gives
$$
H=a^{j-i}H.
$$
Hence
$$
a^{j-i}\in H.
$$
Setting
$$
k=j-i
$$
gives
$$
1\leq k\leq n,
$$
as required.

:::

:::

::: {.pf-step #s3}

Therefore the answers are
$$
\boxed{
\text{(1) false,}
\qquad
\text{(2) true.}
}
$$

::: pf-proof

Step [](#s1){.pf-ref} gives the counterexample to Part (1), and step [](#s2){.pf-ref} proves
Part (2).

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} settles both statements.

:::

:::

:::
