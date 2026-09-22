---
schema: qual/card@1
id: P-BERK90S-05
kind: problem
title: A nonnegative sequence with summably bounded upward increments converges
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: source-checked
  by: chatgpt
  date: 2026-09-22
  note: Compared Problem 5 with the retained MinerU Flash extraction of Spring90.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-22
---

::: {.problem}
Let $(x_n)$ be a sequence of nonnegative real numbers satisfying
$$
x_{n+1}\le x_n+\frac1{n^2}
$$
for every $n\ge1$. Prove that
$$
\lim_{n\to\infty}x_n
$$
exists.
:::

::: {.solution}
For each integer $n\geq1$, put
$$
s_n\coloneqq\sum_{k=1}^{n-1}\frac1{k^2},
\qquad y_n\coloneqq x_n-s_n,
$$
with $s_1=0$.

<1>1. The sequence $(s_n)$ converges to a finite real number $S\leq2$.

::: {.proof}
The sequence is nondecreasing because $s_{n+1}-s_n=1/n^2>0$. For $k\geq2$,
$$
\frac1{k^2}\leq\frac1{k(k-1)}=\frac1{k-1}-\frac1k.
$$
Thus, for $n\geq2$,
$$
0\leq s_n
\leq1+\sum_{k=2}^{n-1}\left(\frac1{k-1}-\frac1k\right)
=2-\frac1{n-1}<2.
$$
The bound also holds for $s_1=0$. By the monotone convergence theorem for
real sequences, $(s_n)$ has a finite limit $S\leq2$.
:::

<1>2. The sequence $(y_n)$ converges to a finite real number $L$.

::: {.proof}
The hypothesis on $(x_n)$ gives
$$
y_{n+1}-y_n
=x_{n+1}-x_n-\frac1{n^2}\leq0.
$$
Also, $x_n\geq0$ and step <1>1 give $y_n=x_n-s_n\geq-2$.
Let $L\coloneqq\inf_{n\geq1}y_n$. For every $\varepsilon>0$, the defining
property of the infimum gives an index $N$ with $y_N<L+\varepsilon$.
For all $n\geq N$, monotonicity gives
$$
L\leq y_n\leq y_N<L+\varepsilon.
$$
Hence $y_n\to L$.
:::

<1>3. Q.E.D.

::: {.proof}
The identity $x_n=y_n+s_n$ and steps <1>1--<1>2 imply
$$
\lim_{n\to\infty}x_n=L+S.
$$
Both terms on the right are finite, so the required limit exists.
:::
:::
