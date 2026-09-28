---
schema: qual/card@1
id: P-BKF06-6B
kind: problem
title: Global fixed points of actions of the nonabelian group of order $21$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 6B of the retained Berkeley Fall 2006 preliminary-exam solution packet f06solution.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained orbit-decomposition argument, including
    realizability of every sum of proper-subgroup indices and the final
    numerical semigroup calculation.
---

::: {.problem}
Let $G$ be a nonabelian group of order $21$.
Find the largest positive integer $n$ such that whenever $G$ acts on a set $S$ of size $n$, some element of $S$ is fixed by every element of $G$.
:::

::: {.solution}
<1>1. A finite transitive $G$-set has the form $G/H$ and has size
$$
[G:H]
$$
for the stabilizer $H$ of any point.

::: {.proof}
For a point $s$ in a transitive $G$-set, the orbit-stabilizer map
$$
G/G_s\longrightarrow Gs,
\qquad
gG_s\longmapsto gs,
$$
is a bijection. Since the action is transitive, $Gs$ is the whole
set.
:::

<1>2. A transitive orbit contains a point fixed by every element of
$G$ if and only if its size is $1$.

::: {.proof}
In the description $G/H$ from step <1>1, a point is globally fixed
exactly when its stabilizer is all of $G$, that is, when $H=G$.
This is equivalent to
$$
[G:H]=1.
$$
:::

<1>3. The possible sizes of a nontrivial orbit with no global fixed
point are
$$
3,\qquad 7,\qquad 21.
$$

::: {.proof}
By Lagrange's theorem, a proper subgroup $H<G$ has order
$$
1,\quad3,\quad\text{or}\quad7,
$$
so its index is respectively
$$
21,\quad7,\quad\text{or}\quad3.
$$
All three occur: the trivial subgroup has index $21$, while Sylow's
theorems give subgroups of orders $3$ and $7$.
:::

<1>4. A positive integer $N$ admits a $G$-set of size $N$ with no
global fixed point if and only if
$$
N=3r+7s+21t
$$
for some nonnegative integers $r,s,t$.

::: {.proof}
Every finite $G$-set is the disjoint union of its orbits. If it has no
global fixed point, step <1>2 excludes one-point orbits, so step
<1>3 shows that its size is a sum of $3$'s, $7$'s, and $21$'s.

Conversely, for subgroups of indices $3$, $7$, and $21$, the
corresponding transitive sets $G/H$ have no global fixed point by
step <1>2. Taking the indicated numbers of disjoint copies realizes
every such sum.
:::

<1>5. The largest positive integer not expressible as
$3r+7s+21t$ is
$$
11.
$$

::: {.proof}
Since $21=7\cdot3$, the $21t$ term is redundant, so it suffices to
consider sums $3r+7s$.

The integer $11$ is not such a sum: if $s=0$, it is not divisible by
$3$, while $s=1$ leaves $4$, and $s\ge2$ is already too large.

Every integer $N\ge12$ is representable. According to its residue
modulo $3$,
$$
\begin{array}{ll}
N\equiv0\pmod3 &: N=3(N/3),\\
N\equiv1\pmod3 &: N=7+3((N-7)/3),\\
N\equiv2\pmod3 &: N=14+3((N-14)/3).
\end{array}
$$
For the last two cases, the relevant smallest integers at least
$12$ are $13$ and $14$, so the displayed coefficients are
nonnegative.
:::

<1>6. The largest integer with the required fixed-point property is
$$
\boxed{11}.
$$

::: {.proof}
By step <1>4, the property holds exactly for positive integers that
are not sums of the allowed nontrivial orbit sizes. Step <1>5 shows
that the largest such integer is $11$.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required answer.
:::
:::
