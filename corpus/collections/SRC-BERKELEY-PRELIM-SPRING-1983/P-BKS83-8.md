---
schema: qual/card@1
id: P-BKS83-8
kind: problem
title: The harmonic sum $1+1/2+\cdots+1/n$ is never an integer for $n>1$
classification:
  areas: [prelim]
  topics: []
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
  note: Checked the lcm denominator and the unique odd summand determined by the largest power of two not exceeding n.
---

::: {.problem}
Let $n>1$ be an integer. Prove that
\[
1+\frac12+\cdots+\frac1n
\]
is not an integer.
:::

::: {.solution}
Let $2^k$ be the largest power of $2$ not exceeding $n$. Since $n>1$,
one has $k\ge1$ and
$$
2^k\le n<2^{k+1}.
$$

<1>1. If
$$
L\coloneqq\operatorname{lcm}(1,2,\ldots,n),
$$
then the exact power of $2$ dividing $L$ is $2^k$.

::: {.proof}
The integer $2^k$ occurs among $1,\ldots,n$, so $2^k$ divides $L$.
No integer at most $n$ is divisible by $2^{k+1}$, by the choice of $k$.
Hence
$$
v_2(L)=k.
$$
:::

<1>2. In
$$
L\left(1+\frac12+\cdots+\frac1n\right)
=
\sum_{j=1}^n\frac Lj,
$$
exactly one summand is odd.

::: {.proof}
For each $j\le n$,
$$
v_2\!\left(\frac Lj\right)=k-v_2(j).
$$
Thus $L/j$ is odd exactly when $v_2(j)=k$. Since
$n<2^{k+1}$, the only $j\in\{1,\ldots,n\}$ divisible by $2^k$ is
$$
j=2^k.
$$
Therefore $L/2^k$ is odd and every other $L/j$ is even.
:::

<1>3. The harmonic sum is not an integer.

::: {.proof}
By step <1>2, the integer
$$
N\coloneqq\sum_{j=1}^n\frac Lj
$$
is odd. By step <1>1, $L$ is even. If the harmonic sum were an integer,
then
$$
\frac NL
$$
would be an integer, so $L$ would divide $N$. That is impossible because
an even integer cannot divide an odd integer.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required conclusion.
:::
:::
