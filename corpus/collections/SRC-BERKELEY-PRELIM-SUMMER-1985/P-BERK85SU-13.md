---
schema: qual/card@1
id: P-BERK85SU-13
kind: problem
title: Averaging a polynomial over the $k$th roots of unity
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    For 1<=j<k, multiplication by a primitive kth root permutes the kth
    roots of unity while multiplying their jth-power sum by a nontrivial
    scalar, so that sum vanishes. Expanding P then leaves only its constant
    term in the average.
---

::: {.problem}
Let $P(z)$ be a polynomial of degree less than $k$ with complex coefficients, and let
\[
\omega_1,\ldots,\omega_k
\]
be the $k$th roots of unity in $\mathbb C$. Prove that
\[
\frac1k\sum_{i=1}^k P(\omega_i)=P(0).
\]
:::

::: {.solution}
Write
$$
P(z)=a_0+a_1z+\cdots+a_{k-1}z^{k-1},
$$
where some of the final coefficients may be zero.

<1>1. For every integer $j$ with $1\le j<k$,
$$
\sum_{i=1}^k\omega_i^j=0.
$$

::: {.proof}
Let $\zeta$ be a primitive $k$th root of unity. Multiplication by
$\zeta$ permutes the set of all $k$th roots of unity. Hence
$$
\sum_{i=1}^k\omega_i^j
=
\sum_{i=1}^k(\zeta\omega_i)^j
=
\zeta^j\sum_{i=1}^k\omega_i^j.
$$
Since $1\le j<k$ and $\zeta$ has order $k$, one has
$\zeta^j\neq1$. Therefore
$$
(1-\zeta^j)\sum_{i=1}^k\omega_i^j=0,
$$
which forces the displayed sum to vanish.
:::

<1>2. One has
$$
\sum_{i=1}^k P(\omega_i)=ka_0.
$$

::: {.proof}
Expanding the polynomial term by term gives
$$
\begin{aligned}
\sum_{i=1}^kP(\omega_i)
&=
\sum_{i=1}^k
\sum_{j=0}^{k-1}a_j\omega_i^j\\
&=
\sum_{j=0}^{k-1}
a_j\sum_{i=1}^k\omega_i^j.
\end{aligned}
$$
For $j=0$, the inner sum is $k$. For every $1\le j<k$, step <1>1
shows that the inner sum is $0$. Thus only the constant term remains:
$$
\sum_{i=1}^kP(\omega_i)=ka_0.
$$
:::

<1>3. Therefore
$$
\boxed{
\frac1k\sum_{i=1}^kP(\omega_i)=P(0)
}.
$$

::: {.proof}
By step <1>2,
$$
\frac1k\sum_{i=1}^kP(\omega_i)=a_0,
$$
and by definition $a_0=P(0)$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required identity.
:::
:::
