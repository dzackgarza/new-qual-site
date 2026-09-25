---
schema: qual/card@1
id: P-BKF84-3
kind: problem
title: Monotone functions as pointwise limits of continuous functions
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 3 of the deterministic MinerU Flash extraction of the Berkeley Fall 1984 preliminary exam.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Checked countability of the jump set and the piecewise-linear interpolation on meshes containing the first finitely many discontinuities.
---

::: {.problem}
Prove or give a counterexample: if $f:[0,1]\to\mathbb R$ is nondecreasing, then there is a sequence of continuous functions $f_n:[0,1]\to\mathbb R$ such that
\[
\lim_{n\to\infty}f_n(x)=f(x)
\]
for every $x\in[0,1]$.
:::

::: {.solution}
<1>1. The set of discontinuities of $f$ in $(0,1)$ is at most
countable.

::: {.proof}
For $x\in(0,1)$, monotonicity gives the one-sided limits
$$
f(x-)
=
\sup_{t<x}f(t),
\qquad
f(x+)
=
\inf_{t>x}f(t),
$$
and
$$
f(x-)\leq f(x)\leq f(x+).
$$
Thus, if $f$ is discontinuous at $x$, then
$$
f(x-)<f(x+).
$$

For every discontinuity $x$, choose a rational number
$$
q_x\in\bigl(f(x-),f(x+)\bigr).
$$
If $x<y$ are two discontinuities, then
$$
f(x+)\leq f(y-),
$$
so the two open intervals
$$
\bigl(f(x-),f(x+)\bigr),
\qquad
\bigl(f(y-),f(y+)\bigr)
$$
are disjoint. Hence $q_x\neq q_y$. The map $x\mapsto q_x$ injects the
set of discontinuities into $\QQ$, proving countability.
:::

<1>2. Enumerate the interior discontinuities as
$$
D=\{d_1,d_2,\ldots\},
$$
with the evident finite interpretation if there are only finitely many.
For each $n$, let $P_n$ be the finite partition obtained by adjoining
the first $n$ points of $D$ to the uniform mesh
$$
\left\{
0,\frac1n,\frac2n,\ldots,1
\right\}.
$$

::: {.proof}
Step <1>1 makes such an enumeration possible. The union defining $P_n$
is finite, contains $0$ and $1$, and can therefore be listed in strictly
increasing order.
:::

<1>3. Define $f_n$ to be the continuous piecewise-linear function that
agrees with $f$ at every point of $P_n$.

::: {.proof}
On every pair of consecutive points
$$
a<b
$$
of $P_n$, define $f_n$ to be the affine function satisfying
$$
f_n(a)=f(a),
\qquad
f_n(b)=f(b).
$$
The formulas on adjacent subintervals agree at their common endpoint,
so $f_n$ is continuous on $[0,1]$.

Since $f$ is nondecreasing, $f(a)\leq f(b)$ whenever $a<b$. Hence
$f_n$ is itself nondecreasing on every partition interval and therefore
on all of $[0,1]$.
:::

<1>4. If $x$ is a discontinuity of $f$, then
$$
f_n(x)\longrightarrow f(x).
$$

::: {.proof}
If $x\in(0,1)$, then $x=d_m$ for some $m$. For every $n\geq m$, the
point $x$ belongs to $P_n$, so
$$
f_n(x)=f(x).
$$
At the endpoints $0$ and $1$, the same equality holds for every $n$
because both endpoints belong to every uniform mesh.
:::

<1>5. If $f$ is continuous at $x$, then
$$
f_n(x)\longrightarrow f(x).
$$

::: {.proof}
For each $n$, let $a_n\leq x\leq b_n$ be consecutive points of $P_n$
whose interval contains $x$. Because $P_n$ contains the uniform mesh,
$$
0\leq x-a_n\leq\frac1n,
\qquad
0\leq b_n-x\leq\frac1n.
$$
Thus
$$
a_n\longrightarrow x,
\qquad
b_n\longrightarrow x.
$$

By step <1>3 and monotonicity,
$$
f(a_n)
\leq
f_n(x)
\leq
f(b_n).
$$
Continuity of $f$ at $x$ gives
$$
f(a_n)\longrightarrow f(x),
\qquad
f(b_n)\longrightarrow f(x).
$$
The squeeze theorem therefore yields $f_n(x)\to f(x)$.
:::

<1>6. Consequently, the statement is true:
$$
\boxed{
f_n(x)\longrightarrow f(x)
\quad\text{for every }x\in[0,1].
}
$$

::: {.proof}
Every point is either a discontinuity, covered by step <1>4, or a
continuity point, covered by step <1>5.
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>2--<1>6 construct the required sequence of continuous
functions.
:::
:::
