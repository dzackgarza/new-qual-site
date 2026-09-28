---
schema: qual/card@1
id: P-BKF77-3
kind: problem
title: Matrix powers converge to zero exactly below the spectral radius threshold
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Proved necessity on eigenvectors and sufficiency blockwise from the binomial formula for powers of Jordan blocks."
---

::: {.problem}
Let $T$ be an $n\times n$ complex matrix. Show that
\[
\lim_{k\to\infty}T^k=0
\]
if and only if every eigenvalue of $T$ has absolute value less than $1$.
:::

::: {.solution}
<1>1. If $T^k\to0$, then every eigenvalue has absolute value less than $1$.
::: {.proof}
Let $\lambda$ be an eigenvalue of $T$, and choose a nonzero eigenvector
$v$ with
$$
Tv=\lambda v.
$$
Then for every $k\ge0$,
$$
T^kv=\lambda^kv.
$$
Since $T^k\to0$, we have
$$
T^kv\to0.
$$
Hence
$$
\lambda^kv\to0.
$$
Because $v\ne0$, this forces
$$
|\lambda|^k\to0,
$$
which is possible only when
$$
\boxed{|\lambda|<1.}
$$
:::

<1>2. Reduce the converse to one Jordan block.
::: {.proof}
Assume every eigenvalue of $T$ has absolute value less than $1$. Over
$\mathbb C$, write
$$
T=SJS^{-1},
$$
where $J$ is the Jordan normal form of $T$. Then
$$
T^k=SJ^kS^{-1}.
$$
Thus it is enough to prove that every Jordan block occurring in $J$ has
powers tending to zero.
:::

<1>3. Powers of a Jordan block with $|\lambda|<1$ tend to zero.
::: {.proof}
Let
$$
J_\lambda=\lambda I+N
$$
be a Jordan block of size $r$, where
$$
N^r=0.
$$
Since $\lambda I$ and $N$ commute, the binomial theorem gives
$$
J_\lambda^k
=\sum_{j=0}^{r-1}\binom{k}{j}\lambda^{k-j}N^j.
$$

If $\lambda=0$, then
$$
J_0^k=N^k=0
$$
for all $k\ge r$.

Now suppose
$$
0<|\lambda|<1.
$$
For each fixed $j<r$,
$$
\binom{k}{j}|\lambda|^{k-j}
\le \frac{k^j}{j!}|\lambda|^{k-j}.
$$
An exponential with ratio strictly less than $1$ dominates every fixed
polynomial, so
$$
k^j|\lambda|^k\longrightarrow0.
$$
Hence
$$
\binom{k}{j}\lambda^{k-j}\longrightarrow0
$$
for every $j=0,\ldots,r-1$. Since the sum above has only finitely many
terms,
$$
J_\lambda^k\longrightarrow0.
$$
:::

<1>4. Conclude for $T$.
::: {.proof}
Every Jordan block of $J$ has powers tending to zero by step <1>3, so
$$
J^k\to0.
$$
Therefore
$$
T^k=SJ^kS^{-1}\to0.
$$
Combining this with step <1>1 proves
$$
\boxed{
T^k\to0
\iff
\text{every eigenvalue $\lambda$ of $T$ satisfies $|\lambda|<1$.}}
$$
:::
:::
