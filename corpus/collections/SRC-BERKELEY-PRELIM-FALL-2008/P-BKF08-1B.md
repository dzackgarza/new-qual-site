---
schema: qual/card@1
id: P-BKF08-1B
kind: problem
title: A vector space over an infinite field is not a finite union of proper affine subspaces
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 1B of the retained Berkeley Fall 2008 preliminary-exam solution packet f08solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the minimal-cover reduction and the at-most-one intersection
    of the chosen affine line with each covering coset.
---

::: {.problem}
Let $V$ be a nonzero vector space over an infinite field.
Show that $V$ is not the union of finitely many cosets
$$
a_1+V_1,\ldots,a_n+V_n
$$
of proper subspaces $V_1,\ldots,V_n$.
:::

::: {.solution}
Let $K$ denote the infinite ground field.

<1>1. Suppose, for contradiction, that
$$
V=\bigcup_{i=1}^n(a_i+V_i),
$$
and choose such a cover with $n$ minimal.

::: {.proof}
This is the negation of the desired conclusion. Since the cover is
finite, among all finite covers by cosets of proper subspaces there is one
having the least possible number of cosets.
:::

<1>2. There exists
$$
v\in a_1+V_1
$$
such that
$$
v\notin a_i+V_i
\qquad(2\le i\le n).
$$

::: {.proof}
If every point of $a_1+V_1$ belonged to the union of the other cosets,
then deleting $a_1+V_1$ would still leave a cover of $V$, contradicting
the minimality in step <1>1.
:::

<1>3. Choose $w\in V\setminus V_1$ and consider the affine line
$$
L\coloneqq\{v+tw:t\in K\}.
$$
Each coset $a_i+V_i$ meets $L$ in at most one point.

::: {.proof}
For $i=1$, if $v+tw\in a_1+V_1$, then subtracting
$v\in a_1+V_1$ gives $tw\in V_1$. Since $w\notin V_1$, this forces
$t=0$. Thus $a_1+V_1$ meets $L$ only at $v$.

Now let $i\ge2$ and suppose two distinct parameters $s,t\in K$ satisfy
$$
v+sw\in a_i+V_i,
\qquad
v+tw\in a_i+V_i.
$$
Subtracting gives
$$
(s-t)w\in V_i.
$$
Because $s-t\ne0$, it follows that $w\in V_i$. Subtracting $sw\in V_i$
from $v+sw\in a_i+V_i$ then gives $v\in a_i+V_i$, contradicting step
<1>2. Hence there cannot be two such parameters.
:::

<1>4. There exists $t\in K$ such that
$$
v+tw\notin\bigcup_{i=1}^n(a_i+V_i).
$$

::: {.proof}
By step <1>3, each of the finitely many cosets excludes at most one
parameter $t\in K$. Hence only finitely many parameters place $v+tw$ in
the union. Since $K$ is infinite, choose $t$ outside that finite set.
:::

<1>5. The assumed finite cover cannot exist.

::: {.proof}
Step <1>4 produces a vector $v+tw\in V$ lying in none of the cosets,
contradicting the covering equality in step <1>1.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 proves the required nonexistence of a finite cover by cosets of
proper subspaces.
:::
:::
