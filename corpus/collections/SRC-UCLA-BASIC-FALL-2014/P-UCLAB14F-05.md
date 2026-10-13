---
schema: qual/card@1
id: P-UCLAB14F-05
kind: problem
title: Convergence of the nested-radical recurrence
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
  note: Checked against Problem 5 of the retained UCLA Basic Examination, Fall 2014.
---

::: {.problem}
Problem 5. Consider the sequence
\[
a_1=\sqrt2,
\qquad
a_{n+1}=\sqrt{2+a_n}\quad(n\geq1).
\]
Prove that this sequence converges and find its limit.
:::

::: {.solution}
<1>1. One has
\[
0<a_n<2
\]
for every $n$.

::: {.proof}
The initial term satisfies
\[
0<a_1=\sqrt2<2.
\]
Assume
\[
0<a_n<2.
\]
Then
\[
2<a_n+2<4,
\]
so
\[
0<a_{n+1}=\sqrt{2+a_n}<2.
\]
The claim follows by induction.
:::

<1>2. The sequence $(a_n)$ is increasing.

::: {.proof}
It is enough to prove
\[
a_{n+1}>a_n.
\]
Since both sides are positive, this is equivalent to
\[
2+a_n>a_n^2.
\]
Rearranging,
\[
2+a_n-a_n^2
=(2-a_n)(a_n+1).
\]
By step <1>1,
\[
2-a_n>0
\qquad\text{and}\qquad
a_n+1>0.
\]
Hence
\[
2+a_n-a_n^2>0,
\]
which proves
\[
a_{n+1}>a_n.
\]
:::

<1>3. The sequence $(a_n)$ converges.

::: {.proof}
By step <1>2, $(a_n)$ is increasing.
By step <1>1, it is bounded above by $2$.
The monotone convergence theorem for real sequences therefore gives convergence to some limit
\[
L\le2.
\]
:::

<1>4. The limit satisfies
\[
L=\sqrt{2+L}.
\]

::: {.proof}
From the recurrence,
\[
a_{n+1}=\sqrt{2+a_n}.
\]
Both $a_n$ and $a_{n+1}$ converge to $L$.
The square-root function is continuous on $[0,\infty)$, so passing to the limit gives
\[
L=\sqrt{2+L}.
\]
:::

<1>5. The only possible positive solution of the equation in step <1>4 is
\[
\boxed{L=2}.
\]

::: {.proof}
Squaring
\[
L=\sqrt{2+L}
\]
gives
\[
L^2-L-2=0,
\]
so
\[
(L-2)(L+1)=0.
\]
Thus
\[
L=2
\quad\text{or}\quad
L=-1.
\]
Step <1>1 gives $L\ge0$, so only $L=2$ is possible.
:::

<1>6. Therefore
\[
\boxed{a_n\to2}.
\]

::: {.proof}
Step <1>3 gives existence of the limit, and step <1>5 identifies it.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required conclusion.
:::
:::
