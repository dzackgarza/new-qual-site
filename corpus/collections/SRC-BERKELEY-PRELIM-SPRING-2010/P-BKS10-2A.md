---
schema: qual/card@1
id: P-BKS10-2A
kind: problem
title: Sylow subgroups of order sixty-seven in a group of order 2010
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
  note: Independently checked the Sylow congruence and divisor conditions and the cyclic example.
---

::: {.problem}
Let \(G\) be a group of order
\[
2010=2\cdot3\cdot5\cdot67.
\]
Determine how many subgroups of order \(67\) the group \(G\) can have, and give examples for each possible number.
:::

::: {.solution}
Let $n_{67}$ denote the number of subgroups of $G$ of order $67$.

<1>1. Every subgroup of $G$ of order $67$ is a Sylow $67$-subgroup.

::: {.proof}
Since
$$
\abs G
=
2\cdot3\cdot5\cdot67,
$$
the largest power of $67$ dividing $\abs G$ is $67^1$. Therefore the
Sylow $67$-subgroups are exactly the subgroups of order $67$.
:::

<1>2. One has
$$
\boxed{n_{67}=1}.
$$

::: {.proof}
By the Sylow theorems,
$$
n_{67}\equiv1\pmod{67}
$$
and
$$
n_{67}\mid\frac{2010}{67}=30.
$$
Every positive divisor of $30$ is at most $30$, while the next positive
integer after $1$ that is congruent to $1$ modulo $67$ is $68$. Hence the
only possibility is
$$
n_{67}=1.
$$
:::

<1>3. The cyclic group of order $2010$ is an example realizing the unique
possible value.

::: {.proof}
The cyclic group
$$
C_{2010}
$$
has order $2010$. A cyclic group has a unique subgroup of order $d$ for
each divisor $d$ of its order, so it has exactly one subgroup of order
$67$, in agreement with step <1>2.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>2 determines the only possible number of order-$67$ subgroups, and
step <1>3 supplies the requested example.
:::
:::
