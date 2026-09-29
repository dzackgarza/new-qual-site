---
schema: qual/card@1
id: P-BKF20-2B
kind: problem
title: Convergence of sums and termwise products of two series
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2020 solution. Partial sums prove
    convergence of the termwise sum, while a_n=b_n=(-1)^n/sqrt(n) gives two
    convergent alternating series whose termwise product is the harmonic series.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the partial-sum limit in part (a), convergence of both alternating
    counterexample series, and divergence of their product series.
---

::: {.problem}
Prove or give a counterexample.

(a) If $\sum a_n$ and $\sum b_n$ converge, then $\sum(a_n+b_n)$ converges.

(b) If $\sum a_n$ and $\sum b_n$ converge, then $\sum a_nb_n$ converges.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Statement (a) is true.

::: pf-proof

Let
$$
A_N\coloneqq\sum_{n=1}^N a_n,
\qquad
B_N\coloneqq\sum_{n=1}^N b_n.
$$
By hypothesis there are real numbers $A,B$ such that
$$
A_N\to A,
\qquad
B_N\to B.
$$
The $N$th partial sum of $\sum(a_n+b_n)$ is
$$
\sum_{n=1}^N(a_n+b_n)
=
A_N+B_N.
$$
Therefore
$$
A_N+B_N\longrightarrow A+B,
$$
so $\sum(a_n+b_n)$ converges.

:::

:::

::: {.pf-step #s2}

For
$$
a_n=b_n=\frac{(-1)^n}{\sqrt n}
\qquad(n\ge1),
$$
both series
$$
\sum_{n=1}^{\infty}a_n
\qquad\text{and}\qquad
\sum_{n=1}^{\infty}b_n
$$
converge.

::: pf-proof

The positive sequence
$$
\frac1{\sqrt n}
$$
is decreasing and tends to $0$. Hence
$$
\sum_{n=1}^{\infty}\frac{(-1)^n}{\sqrt n}
$$
converges by the alternating-series test. Since $a_n=b_n$, both stated
series converge.

:::

:::

::: {.pf-step #s3}

For the sequences in step [](#s2){.pf-ref}, the termwise-product series
$\sum_n a_nb_n$ diverges.

::: pf-proof

For every $n$,
$$
a_nb_n
=
\frac{(-1)^{2n}}{n}
=
\frac1n.
$$
Thus
$$
\sum_{n=1}^{\infty}a_nb_n
=
\sum_{n=1}^{\infty}\frac1n,
$$
which is the divergent harmonic series. Therefore statement (b) is
false.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves (a), while steps [](#s2){.pf-ref} and [](#s3){.pf-ref} give a counterexample to
(b).

:::

:::

:::
