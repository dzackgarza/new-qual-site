---
schema: qual/card@1
id: P-UCLAB03F-03
kind: problem
title: Convergence of the sequence $(1+1/n)^n$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 3 of the official UCLA Basic Exam Fall 2003 PDF.
---

::: {.problem}
Prove that the sequence $(a_n)$ defined by
$$
a_n=\left(1+\frac1n\right)^n
$$
converges as $n\to\infty$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every positive integer $n$,
$$
a_n
=
\sum_{k=0}^{n}
\frac1{k!}
\prod_{j=0}^{k-1}\left(1-\frac{j}{n}\right),
$$
where the empty product for $k=0$ is $1$.


::: pf-proof

By the binomial theorem,
$$
\left(1+\frac1n\right)^n
=
\sum_{k=0}^{n}\binom nk\frac1{n^k}.
$$
For $k\le n$,
$$
\binom nk\frac1{n^k}
=
\frac{n(n-1)\cdots(n-k+1)}{k!\,n^k}
=
\frac1{k!}
\prod_{j=0}^{k-1}\left(1-\frac{j}{n}\right).
$$
Substituting gives the formula.

:::

:::

::: {.pf-step #s1-2}

The sequence $(a_n)$ is increasing.


::: pf-proof

Fix $n$. For each $k\le n$ and each $j\in\{0,\ldots,k-1\}$,
$$
1-\frac{j}{n+1}
\ge
1-\frac{j}{n}.
$$
All these factors are nonnegative. Hence the $k$th summand in the expansion from step [](#s1-1){.pf-ref} for $a_{n+1}$ is at least the corresponding $k$th summand for $a_n$. In addition, $a_{n+1}$ contains the positive term with $k=n+1$. Therefore
$$
a_{n+1}\ge a_n.
$$

:::

:::

::: {.pf-step #s1-3}

For every $n$,
$$
a_n\le3.
$$


::: pf-proof

Every factor in the product from step [](#s1-1){.pf-ref} lies in $[0,1]$. Therefore
$$
a_n
\le
\sum_{k=0}^{n}\frac1{k!}.
$$
For $k\ge1$,
$$
k!=1\cdot2\cdot3\cdots k\ge2^{k-1},
$$
so
$$
\frac1{k!}\le\frac1{2^{k-1}}.
$$
Thus
$$
a_n
\le
1+\sum_{k=1}^{n}\frac1{2^{k-1}}
<
1+\sum_{m=0}^{\infty}\frac1{2^m}
=3.
$$

:::

:::

::: {.pf-step #s1-4}

The sequence $(a_n)$ converges.


::: pf-proof

By step [](#s1-2){.pf-ref}, $(a_n)$ is increasing, and by step [](#s1-3){.pf-ref} it is bounded above. The monotone convergence theorem for real sequences therefore implies that $(a_n)$ converges to its supremum.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves the required convergence.

:::

:::

:::
