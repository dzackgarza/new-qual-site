---
schema: qual/card@1
id: P-BKF83-4
kind: problem
title: Every real sequence has a monotone subsequence
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked the exhaustive tail-maximum dichotomy and the recursive construction in the finite-tail-maximum case.
---

::: {.problem}
Prove or disprove: every infinite sequence of real numbers has either a nondecreasing subsequence or a nonincreasing subsequence.
:::

::: {.solution}
The assertion is true.

<1>1. Call an index $n$ a tail maximum if
$$
x_n\ge x_m
\qquad
\text{for every }m>n.
$$
If there are infinitely many tail maxima, the sequence has a nonincreasing
subsequence.

::: {.proof}
List infinitely many tail-maximum indices in increasing order:
$$
n_1<n_2<n_3<\cdots.
$$
Since $n_{j+1}>n_j$ and $n_j$ is a tail maximum,
$$
x_{n_j}\ge x_{n_{j+1}}
$$
for every $j$. Hence
$$
x_{n_1},x_{n_2},x_{n_3},\ldots
$$
is nonincreasing.
:::

<1>2. If there are only finitely many tail maxima, the sequence has a
strictly increasing subsequence.

::: {.proof}
Choose $N$ larger than every tail-maximum index, taking $N=1$ if there
are none. Then no $n\ge N$ is a tail maximum. Therefore, for every
$n\ge N$, there exists $m>n$ such that
$$
x_m>x_n.
$$

Set $n_1=N$. Once $n_j$ has been chosen, choose
$$
n_{j+1}>n_j
$$
with
$$
x_{n_{j+1}}>x_{n_j}.
$$
This recursion continues indefinitely and produces a strictly increasing,
hence nondecreasing, subsequence.
:::

<1>3. Every infinite real sequence therefore has a monotone subsequence.

::: {.proof}
Either there are infinitely many tail maxima or there are only finitely
many. Step <1>1 handles the first case and step <1>2 handles the second.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 proves the stated assertion.
:::
:::
