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

::: pf

::: {.pf-step #s1}

Call an index $n$ a tail maximum if
$$
x_n\ge x_m
\qquad
\text{for every }m>n.
$$
If there are infinitely many tail maxima, the sequence has a nonincreasing
subsequence.

::: pf-proof

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

:::

::: {.pf-step #s2}

If there are only finitely many tail maxima, the sequence has a
strictly increasing subsequence.

::: pf-proof

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

:::

::: {.pf-step #s3}

Every infinite real sequence therefore has a monotone subsequence.

::: pf-proof

Either there are infinitely many tail maxima or there are only finitely
many. Step [](#s1){.pf-ref} handles the first case and step [](#s2){.pf-ref} handles the second.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} proves the stated assertion.

:::

:::

:::
