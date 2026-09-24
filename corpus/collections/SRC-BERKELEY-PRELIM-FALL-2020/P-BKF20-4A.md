---
schema: qual/card@1
id: P-BKF20-4A
kind: problem
title: Convergence of $\prod_{k\ge1}(1-z^k)$
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
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
    Independently checked the retained Fall 2020 solution. Nonzero convergence
    of the partial products forces 1-z^n to tend to 1 and hence |z|<1; for
    |z|<1 the logarithms form an absolutely convergent series.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the necessary factor-limit condition, the equivalence z^n -> 0
    iff |z|<1, the logarithm estimate on the tail, and nonvanishing of the
    resulting product limit.
---

::: {.problem}
By definition, an infinite product converges if its sequence of finite partial products converges to a nonzero number. Find all $z\in\mathbb C$ for which
\[
\prod_{k=1}^{\infty}(1-z^k)
\]
converges.
:::

::: {.solution}
For $n\ge1$, write
$$
P_n(z)\coloneqq\prod_{k=1}^n(1-z^k).
$$

<1>1. If the infinite product converges in the stated sense, then
$$
z^n\longrightarrow0.
$$

::: {.proof}
Suppose
$$
P_n(z)\longrightarrow P
$$
with $P\ne0$. Then also
$$
P_{n-1}(z)\longrightarrow P.
$$
For all sufficiently large $n$, $P_{n-1}(z)\ne0$, and therefore
$$
1-z^n
=
\frac{P_n(z)}{P_{n-1}(z)}
\longrightarrow
\frac PP
=
1.
$$
Hence $z^n\to0$.
:::

<1>2. The conclusion of step <1>1 implies
$$
|z|<1.
$$

::: {.proof}
If $|z|\ge1$, then
$$
|z^n|=|z|^n\ge1
$$
for every $n$, so $z^n$ cannot tend to $0$. Thus convergence of the
product requires $|z|<1$.
:::

<1>3. Now suppose $|z|<1$. There is $N$ such that for every $k\ge N$,
$$
|z|^k\le\frac12
$$
and
$$
\left|\log(1-z^k)\right|
\le
2|z|^k,
$$
where $\log$ denotes the principal logarithm.

::: {.proof}
Since $|z|^k\to0$, choose $N$ so that $|z|^k\le1/2$ for $k\ge N$.
For $|w|<1$,
$$
\log(1-w)
=
-\sum_{m=1}^{\infty}\frac{w^m}{m}.
$$
Consequently, for $|w|\le1/2$,
$$
\begin{aligned}
|\log(1-w)|
&\le
\sum_{m=1}^{\infty}\frac{|w|^m}{m}\\
&\le
\sum_{m=1}^{\infty}|w|^m\\
&=
\frac{|w|}{1-|w|}\\
&\le
2|w|.
\end{aligned}
$$
Apply this with $w=z^k$.
:::

<1>4. If $|z|<1$, then
$$
\sum_{k=N}^{\infty}\log(1-z^k)
$$
converges absolutely.

::: {.proof}
By step <1>3,
$$
\sum_{k=N}^{\infty}
|\log(1-z^k)|
\le
2\sum_{k=N}^{\infty}|z|^k.
$$
The series on the right is geometric and converges because $|z|<1$.
:::

<1>5. If $|z|<1$, the partial products $P_n(z)$ converge to a nonzero
limit.

::: {.proof}
No factor $1-z^k$ vanishes, since $|z^k|<1$. Put
$$
L
\coloneqq
\sum_{k=N}^{\infty}\log(1-z^k),
$$
which exists by step <1>4. For $n\ge N$,
$$
\prod_{k=N}^n(1-z^k)
=
\exp\left(
\sum_{k=N}^n\log(1-z^k)
\right).
$$
Taking $n\to\infty$ gives
$$
\prod_{k=N}^{\infty}(1-z^k)
=
e^L
\ne
0.
$$
The finite initial product
$$
\prod_{k=1}^{N-1}(1-z^k)
$$
is also nonzero, so multiplying it by $e^L$ gives a nonzero limit for
$P_n(z)$.
:::

<1>6. Therefore the product converges exactly for
$$
\boxed{\{z\in\CC:|z|<1\}}.
$$

::: {.proof}
Steps <1>1--<1>2 prove necessity, and steps <1>3--<1>5 prove
sufficiency.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 gives the requested set.
:::
:::
