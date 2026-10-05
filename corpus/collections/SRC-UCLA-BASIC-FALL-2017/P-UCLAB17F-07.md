---
schema: qual/card@1
id: P-UCLAB17F-07
kind: problem
title: Decay of a monotone summable sequence
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
  note: Checked against the vendored UCLA Basic Examination, Fall 2017, `assets/attachments/basic-17F.pdf`.
---

::: {.problem}
Let $(a_n)$ be a non-increasing sequence of positive real numbers with $\sum_{n=1}^\infty a_n<\infty$. Prove that
\[
\lim_{n\to\infty}n a_n=0.
\]
:::

::: {.solution}
For each $n\ge2$, set
\[
m_n=\left\lfloor\frac n2\right\rfloor.
\]

<1>1. For every
\[
k=m_n+1,\ldots,n,
\]
one has
\[
a_k\ge a_n.
\]

::: {.proof}
The sequence $(a_n)$ is non-increasing.
Since
\[
k\le n,
\]
one has
\[
a_k\ge a_n.
\]
:::

<1>2. Therefore
\[
(n-m_n)a_n
\le
\sum_{k=m_n+1}^{n}a_k.
\]

::: {.proof}
There are exactly
\[
n-m_n
\]
terms in the sum.
By step <1>1, each of them is at least $a_n$.
:::

<1>3. One has
\[
n-m_n\ge\frac n2.
\]

::: {.proof}
Since
\[
m_n=\left\lfloor\frac n2\right\rfloor
\le
\frac n2,
\]
subtracting from $n$ gives
\[
n-m_n
\ge
\frac n2.
\]
:::

<1>4. Hence
\[
0\le n a_n
\le
2\sum_{k=m_n+1}^{n}a_k.
\]

::: {.proof}
By steps <1>2--<1>3,
\[
\frac n2 a_n
\le
(n-m_n)a_n
\le
\sum_{k=m_n+1}^na_k.
\]
Multiply by $2$.
:::

<1>5. The right-hand side in step <1>4 tends to $0$.

::: {.proof}
Since
\[
\sum_{k=1}^{\infty}a_k
\]
converges,
its tails tend to zero:
\[
\sum_{k=N}^{\infty}a_k\to0
\]
as $N\to\infty$.
Because
\[
m_n+1\to\infty,
\]
one has
\[
0
\le
\sum_{k=m_n+1}^{n}a_k
\le
\sum_{k=m_n+1}^{\infty}a_k
\longrightarrow0.
\]
:::

<1>6. Therefore
\[
\boxed{\lim_{n\to\infty}na_n=0}.
\]

::: {.proof}
By step <1>4,
\[
0\le na_n
\le
2\sum_{k=m_n+1}^{n}a_k.
\]
The right side tends to zero by step <1>5.
The squeeze theorem gives the conclusion.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required limit.
:::
:::
