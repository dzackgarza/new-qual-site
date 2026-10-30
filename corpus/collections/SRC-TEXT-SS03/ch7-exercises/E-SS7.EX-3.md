---
schema: qual/card@1
id: E-SS7.EX-3
kind: problem
title: $\sum_n\mu(n)n^{-s}=1/\zeta(s)$ for the Möbius function
classification:
  areas:
  - complex-analysis
  topics:
  - Zeta Function
  - Prime Number Theorem
  - Dirichlet Series
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
In line with the previous exercise, we consider the Dirichlet series for $1/\zeta$.

(a) Prove that for $\Re(s) > 1$
$$
\frac{1}{\zeta(s)} = \sum_{n=1}^{\infty} \frac{\mu(n)}{n^s},
$$
where $\mu(n)$ is the Möbius function defined by
$$
\mu(n) = \begin{cases} 1 & \text{if } n = 1, \\ (-1)^k & \text{if } n = p_1 \cdots p_k \text{, and the } p_j \text{ are distinct primes,} \\ 0 & \text{otherwise.} \end{cases}
$$
Note that $\mu(nm) = \mu(n)\mu(m)$ whenever $n$ and $m$ are relatively prime. [Hint: Use the Euler product formula for $\zeta(s)$.]

(b) Show that
$$
\sum_{k \divides n} \mu(k) = \begin{cases} 1 & \text{if } n = 1, \\ 0 & \text{otherwise.} \end{cases}
$$
:::

::: {.solution}
For $\Re s>1$, the Euler product converges absolutely:
$$
\zeta(s)=\prod_p(1-p^{-s})^{-1}.
$$
Therefore
$$
\frac1{\zeta(s)}=\prod_p(1-p^{-s}).
$$
Expanding this absolutely convergent product, each squarefree integer $n=p_1\cdots p_k$ contributes $(-1)^k n^{-s}$, while integers divisible by a square do not occur. Hence
$$
\frac1{\zeta(s)}=\sum_{n=1}^\infty\frac{\mu(n)}{n^s}.
$$

For part (b), define
$$
S(n)=\sum_{d\mid n}\mu(d).
$$
If $n=1$, then $S(1)=\mu(1)=1$. If
$$
n=p_1^{e_1}\cdots p_r^{e_r}>1,
$$
only squarefree divisors contribute, so
$$
S(n)=\prod_{j=1}^r(1+\mu(p_j))
=\prod_{j=1}^r(1-1)=0.
$$
Thus
$$
\sum_{d\mid n}\mu(d)=
\begin{cases}
1,&n=1,\\
0,&n>1.
\end{cases}
$$
:::
