---
schema: qual/card@1
id: P-BKS21-3B
kind: problem
title: Existence of the Euler--Mascheroni limit
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
---

::: {.problem}
Prove that the limit
$$
\lim_{n\to\infty}\left(1+\frac12+\cdots+\frac1n-\log n\right)
$$
exists.
:::

Define
$$
a_n\coloneqq
\sum_{k=1}^n\frac1k-\log n.
$$

::: pf

::: {.pf-step #s1-1}

The sequence $(a_n)$ is decreasing.


::: pf-proof

For $n\geq1$,
$$
\begin{aligned}
a_{n+1}-a_n
&=
\frac1{n+1}-\log\frac{n+1}{n}\\
&=
\frac1{n+1}-\log\left(1+\frac1n\right).
\end{aligned}
$$
Now
$$
\log\left(1+\frac1n\right)
=
\int_n^{n+1}\frac{dx}{x}.
$$
For $x\in[n,n+1)$ one has $1/x>1/(n+1)$, hence
$$
\log\left(1+\frac1n\right)
>
\frac1{n+1}.
$$
Therefore $a_{n+1}-a_n<0$.

:::

:::

::: {.pf-step #s1-2}

The sequence $(a_n)$ is bounded below by $0$.


::: pf-proof

For each $k=1,\ldots,n$ and $x\in[k,k+1]$,
$$
\frac1x\leq\frac1k.
$$
Hence
$$
\log(n+1)
=
\int_1^{n+1}\frac{dx}{x}
\leq
\sum_{k=1}^n\frac1k.
$$
Thus
$$
a_n
\geq
\log(n+1)-\log n
=
\log\left(1+\frac1n\right)
>0.
$$

:::

:::

::: {.pf-step #s1-3}

The sequence $(a_n)$ converges to a finite real number.


::: pf-proof

By step [](#s1-1){.pf-ref}, $(a_n)$ is monotone decreasing, and by step [](#s1-2){.pf-ref} it is bounded below. The monotone convergence theorem for real sequences therefore implies that $(a_n)$ converges.

:::

:::

::: {.pf-step #s1-4}

Hence
$$
\boxed{
\lim_{n\to\infty}
\left(
1+\frac12+\cdots+\frac1n-\log n
\right)
\ \text{exists}
}.
$$


::: pf-proof

The expression inside the limit is exactly $a_n$, whose convergence is step [](#s1-3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required conclusion.

:::

:::
