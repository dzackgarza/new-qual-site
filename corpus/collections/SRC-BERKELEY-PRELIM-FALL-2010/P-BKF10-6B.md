---
schema: qual/card@1
id: P-BKF10-6B
kind: problem
title: Groups of order $30$ are not simple
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 6B of the retained Berkeley Fall 2010 preliminary-exam solution packet f10solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the exact Sylow counts n_5=6 and n_3=10 under simplicity,
    trivial intersections of distinct prime-order Sylow subgroups, and
    the resulting element-count contradiction.
---

::: {.problem}
Show that there are no simple groups of order $30$.
:::

::: {.hint}
Show that if a noncyclic simple group has order divisible by a prime $p$, then it has at least $p^2-1$ nontrivial elements of order a power of $p$.
:::

::: {.solution}
Suppose, for contradiction, that $G$ is simple and
$$
\abs{G}=30=2\cdot3\cdot5.
$$

<1>1. The number $n_5$ of Sylow $5$-subgroups of $G$ is $6$.

::: {.proof}
Sylow's theorems give
$$
n_5\mid6,
\qquad
n_5\equiv1\pmod5.
$$
Thus $n_5$ is either $1$ or $6$. If $n_5=1$, the unique Sylow
$5$-subgroup is normal, contradicting simplicity because it is nontrivial
and proper. Hence $n_5=6$.
:::

<1>2. The group $G$ has exactly $24$ nonidentity elements of order $5$.

::: {.proof}
Each Sylow $5$-subgroup has order $5$, hence has four nonidentity
elements, all of order $5$. Two distinct subgroups of order $5$ intersect
only in the identity: a nontrivial intersection would have order $5$ and
would force the two subgroups to be equal. Therefore the six Sylow
$5$-subgroups from step <1>1 contribute
$$
6(5-1)=24
$$
distinct nonidentity elements of order $5$.
:::

<1>3. The number $n_3$ of Sylow $3$-subgroups of $G$ is $10$.

::: {.proof}
Sylow's theorems give
$$
n_3\mid10,
\qquad
n_3\equiv1\pmod3.
$$
Among the divisors $1,2,5,10$ of $10$, only $1$ and $10$ are congruent
to $1$ modulo $3$. Simplicity excludes $n_3=1$ for the same reason as in
step <1>1. Hence $n_3=10$.
:::

<1>4. The group $G$ has exactly $20$ nonidentity elements of order $3$.

::: {.proof}
Each Sylow $3$-subgroup has order $3$ and therefore has two nonidentity
elements. Distinct subgroups of order $3$ intersect only in the identity,
so the ten Sylow $3$-subgroups from step <1>3 contribute
$$
10(3-1)=20
$$
distinct nonidentity elements of order $3$.
:::

<1>5. The counts in steps <1>2 and <1>4 are impossible in a group of
order $30$.

::: {.proof}
No element can simultaneously have order $3$ and order $5$. Hence the
$24$ elements counted in step <1>2 and the $20$ elements counted in step
<1>4 are disjoint. Thus $G$ would contain at least
$$
24+20=44
$$
nonidentity elements, although a group of order $30$ has only $29$
nonidentity elements. This is a contradiction.
:::

<1>6. Therefore no group of order $30$ is simple.

::: {.proof}
Step <1>5 contradicts the assumption that a simple group $G$ of order
$30$ exists.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is exactly the required conclusion.
:::
:::
