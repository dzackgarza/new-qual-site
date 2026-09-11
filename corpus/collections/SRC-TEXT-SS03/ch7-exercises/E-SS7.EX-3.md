---
schema: qual/card@1
id: E-SS7.EX-3
kind: problem
title: "SS 7.3: The Dirichlet series of the Moebius function and 1/zeta"
classification:
  areas:
  - complex-analysis
  topics: ['Zeta Function', 'Prime Number Theorem', 'Dirichlet Series']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
3. In line with the previous exercise, we consider the Dirichlet series for $1 / \zeta$

(a) Prove that for $\operatorname { R e } ( s ) > 1$

$$
\frac {1}{\zeta (s)} = \sum_ {n = 1} ^ {\infty} \frac {\mu (n)}{n ^ {s}},
$$

where $\mu ( n )$ is the M¨obius function defined by

$$
\mu (n) = \left\{ \begin{array}{l l} 1 & \text{if } n = 1, \\ (- 1) ^ {k} & \text{if } n = p_{1} \cdots p_{k} \text{, and the } p_{j} \text{ are distinct primes,} \\ 0 & \text{otherwise.} \end{array} \right.
$$

Note that $\mu ( n m ) = \mu ( n ) \mu ( m )$ whenever n and m are relatively prime.
[Hint: Use the Euler product formula for $\zeta ( s ) . ]$

(b) Show that

$$
\sum_ {k \mid n} \mu (k) = \left\{ \begin{array}{l l} 1 & \text { if } n = 1, \\ 0 & \text { otherwise }. \end{array} \right.
$$
:::

::: solution
For $\Re s>1$, the Euler product converges absolutely:
\[
\zeta(s)=\prod_p(1-p^{-s})^{-1}.
\]
Therefore
\[
\frac1{\zeta(s)}=\prod_p(1-p^{-s}).
\]
Expanding this absolutely convergent product, each squarefree integer $n=p_1\cdots p_k$ contributes $(-1)^k n^{-s}$, while integers divisible by a square do not occur. Hence
\[
\frac1{\zeta(s)}=\sum_{n=1}^\infty\frac{\mu(n)}{n^s}.
\]

For part (b), define
\[
S(n)=\sum_{d\mid n}\mu(d).
\]
If $n=1$, then $S(1)=\mu(1)=1$. If
\[
n=p_1^{e_1}\cdots p_r^{e_r}>1,
\]
only squarefree divisors contribute, so
\[
S(n)=\prod_{j=1}^r(1+\mu(p_j))
=\prod_{j=1}^r(1-1)=0.
\]
Thus
\[
\sum_{d\mid n}\mu(d)=
\begin{cases}
1,&n=1,\\
0,&n>1.
\end{cases}
\]
:::
