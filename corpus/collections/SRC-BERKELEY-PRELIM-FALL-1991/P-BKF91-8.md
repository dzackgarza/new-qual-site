---
schema: qual/card@1
id: P-BKF91-8
kind: problem
title: Convergence of $\sum\sqrt{a_na_{n+1}}$ from convergence of $\sum a_n$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Used the arithmetic-geometric mean inequality for the forward implication
    and an alternating 1/k^3, 1/k sequence for the counterexample.
---

::: {.problem}
Let $a_1,a_2,\ldots$ be positive real numbers.

1. Prove that
\[
\sum_{n=1}^{\infty}a_n<\infty
\quad\Longrightarrow\quad
\sum_{n=1}^{\infty}\sqrt{a_na_{n+1}}<\infty.
\]

2. Prove that the converse is false.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For every $n\ge1$,
$$
\sqrt{a_na_{n+1}}\le\frac{a_n+a_{n+1}}2.
$$

::: pf-proof

This is the arithmetic-geometric mean inequality for the positive numbers $a_n$ and $a_{n+1}$.

:::

:::

::: {.pf-step #s2}

If
$$
\sum_{n=1}^\infty a_n<\infty,
$$
then
$$
\sum_{n=1}^\infty\sqrt{a_na_{n+1}}<\infty.
$$

::: pf-proof

By step [](#s1){.pf-ref}, for every $N$,
$$
\begin{aligned}
\sum_{n=1}^N\sqrt{a_na_{n+1}}
&\le\frac12\sum_{n=1}^N(a_n+a_{n+1})\\
&\le\sum_{n=1}^{N+1}a_n.
\end{aligned}
$$
The right-hand side is bounded uniformly in $N$ by the convergent series $\sum a_n$. Since the partial sums on the left are increasing, they converge.

:::

:::

::: {.pf-step #s3}

Define a positive sequence by
$$
a_{2k-1}=\frac1{k^3},
\qquad
a_{2k}=\frac1k
\qquad(k\ge1).
$$
Then
$$
\sum_{n=1}^\infty a_n=\infty.
$$

::: pf-proof

The even-indexed subseries is
$$
\sum_{k=1}^\infty a_{2k}
=
\sum_{k=1}^\infty\frac1k,
$$
which diverges.

:::

:::

::: {.pf-step #s4}

For the sequence in step [](#s3){.pf-ref},
$$
\sum_{n=1}^\infty\sqrt{a_na_{n+1}}<\infty.
$$

::: pf-proof

For $k\ge1$,
$$
\sqrt{a_{2k-1}a_{2k}}
=
\frac1{k^2}.
$$
Also
$$
\sqrt{a_{2k}a_{2k+1}}
=
\frac{1}{\sqrt{k(k+1)^3}}
\le
\frac1{k^2},
$$
because $k(k+1)^3\ge k^4$. Hence
$$
\sum_{n=1}^\infty\sqrt{a_na_{n+1}}
\le
2\sum_{k=1}^\infty\frac1{k^2}
<\infty.
$$

:::

:::

::: {.pf-step #s5}

Thus the converse is false.

::: pf-proof

Steps [](#s3){.pf-ref} and [](#s4){.pf-ref} give a positive sequence for which the geometric-mean series converges while $\sum a_n$ diverges.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} proves part 1, and step [](#s5){.pf-ref} proves part 2.

:::

:::

:::
