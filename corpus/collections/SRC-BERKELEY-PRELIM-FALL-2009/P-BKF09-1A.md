---
schema: qual/card@1
id: P-BKF09-1A
kind: problem
title: Generating function $\sum p(k)z^k$ of a polynomial sequence is rational
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $p(k)$ be a degree $n$ polynomial with complex coefficients defined by
$$
p(k)=p_0+\binom{k}{1}p_1+\binom{k}{2}p_2+\cdots+\binom{k}{n}p_n.
$$
Define
$$
f(z)=\sum_{k=0}^{\infty}p(k)z^k.
$$
Find the radius of convergence of the power series, prove that $f(z)$ is a rational function restricted to the disk of convergence, and give a formula for $f(z)$.
:::

::: {.solution}
We have
$$
\left(\frac{d}{dz}\right)^n\frac{1}{1-z}=\frac{n!}{(1-z)^{n+1}}.
$$
Since $\frac{1}{1-z}=\sum_{k=0}^{\infty}z^k$ for $\abs{z}<1$, we also have for $\abs{z}<1$
$$
\frac{n!}{(1-z)^{n+1}}=\left(\frac{d}{dz}\right)^n\sum_{k=0}^{\infty}z^k=\sum_{k=0}^{\infty}k(k-1)\cdots(k-n+1)z^{k-n}.
$$
Dividing by $n!$ and multiplying by $z^n$, and applying the same identity with $j$ in place of $n$, gives for $0\le j\le n$
$$
\frac{z^j}{(1-z)^{j+1}}=\sum_{k=0}^{\infty}\binom{k}{j}z^k.
$$
Thus,
$$
f(z)=\sum_{k=0}^{\infty}\sum_{j=0}^{n}p_j\binom{k}{j}z^k=\sum_{j=0}^{n}p_j\sum_{k=0}^{\infty}\binom{k}{j}z^k=\sum_{j=0}^{n}p_j\frac{z^j}{(1-z)^{j+1}},
$$
which is a sum of rational functions, and is therefore rational.
The series converges to this rational function in the disk $\abs{z}<1$, and the rational function has a pole on its boundary at $z=1$ (unless all $p_j=0$).
Thus the convergence radius $R=1$ if not all $p_j=0$ (and $R=\infty$ otherwise).
:::
