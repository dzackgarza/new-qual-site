---
schema: qual/card@1
id: P-UCLAB12W-04
kind: problem
title: Cesàro convergence of nonnegative partial sums
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 4 of the retained UCLA Basic Examination, Winter 2012.
---

::: {.problem}
Let $(a_n)$ be a sequence of nonnegative numbers and put
\[
s_n=\sum_{k=1}^n a_k.
\]
Suppose $s_n$ tends to $s\in\RR$ in the Cesàro sense:
\[
\lim_{n\to\infty}\frac{s_1+\cdots+s_n}{n}=s.
\]
Show that $\sum_{k=1}^\infty a_k$ converges and equals $s$.
:::

::: {.solution}

Let
$$
A_n=\frac1n\sum_{j=1}^n s_j.
$$
By hypothesis, $A_n\to s$.

::: pf

::: {.pf-step #s1-1}

The sequence $(s_n)$ is nonnegative and nondecreasing.


::: pf-proof

Since every $a_k\ge0$,
$$
s_{n+1}-s_n=a_{n+1}\ge0,
$$
and each partial sum $s_n$ is nonnegative.

:::

:::

::: {.pf-step #s1-2}

The sequence $(s_n)$ is bounded above.


::: pf-proof

Suppose instead that $(s_n)$ is unbounded. Since it is nondecreasing by step [](#s1-1){.pf-ref}, it then tends to $+\infty$.

Let $M>0$. Choose $N$ such that
$$
s_N>2M.
$$
For every $n\ge2N$ and every $j\ge N$, monotonicity gives $s_j\ge s_N$. Hence
$$
A_n
=\frac1n\sum_{j=1}^n s_j
\ge
\frac1n\sum_{j=N}^n s_j
\ge
\frac{n-N+1}{n}s_N
\ge
\frac12s_N
>M.
$$
Since $M$ is arbitrary, this would force $A_n\to+\infty$, contradicting the finite limit $A_n\to s$.

:::

:::

::: {.pf-step #s1-3}

There exists $L\in\RR$ such that
$$
s_n\longrightarrow L.
$$


::: pf-proof

By steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref}, $(s_n)$ is nondecreasing and bounded above. Therefore it converges to its supremum
$$
L=\sup_n s_n.
$$

:::

:::

::: {.pf-step #s1-4}

The Cesàro means $A_n$ converge to the same limit $L$.


::: pf-proof

Let $\varepsilon>0$. Choose $N$ such that
$$
\abs{s_j-L}<\frac\varepsilon2
$$
for every $j\ge N$. For $n\ge N$,
$$
\begin{aligned}
\abs{A_n-L}
&=\abs{\frac1n\sum_{j=1}^n(s_j-L)}\\
&\le
\frac1n\sum_{j=1}^{N-1}\abs{s_j-L}
+
\frac1n\sum_{j=N}^n\abs{s_j-L}\\
&\le
\frac1n\sum_{j=1}^{N-1}\abs{s_j-L}
+
\frac\varepsilon2.
\end{aligned}
$$
The finite first sum divided by $n$ tends to $0$, so for sufficiently large $n$ it is less than $\varepsilon/2$. Thus $\abs{A_n-L}<\varepsilon$.

:::

:::

::: {.pf-step #s1-5}

One has
$$
L=s.
$$


::: pf-proof

By hypothesis $A_n\to s$, while step [](#s1-4){.pf-ref} gives $A_n\to L$. Limits in $\RR$ are unique, so $L=s$.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{\sum_{k=1}^{\infty}a_k=s}.
$$


::: pf-proof

The partial sums of the series are exactly $s_n$. By steps [](#s1-3){.pf-ref} and [](#s1-5){.pf-ref},
$$
s_n\to s.
$$
This is precisely convergence of the series to $s$.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
