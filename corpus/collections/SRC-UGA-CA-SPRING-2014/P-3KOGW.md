---
schema: qual/card@1
id: P-3KOGW
kind: problem
title: Mean-square identity for power series, and Liouville's theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Power Series
  - Entire Functions
relations: []
review: draft
---

::: {.problem}
\envlist

- Assume $f(z)=\sum_{n=0}^{\infty} c_{n} z^{n}$ converges in $\abs{z}<R$. Show that for $r<R$,

$$
\frac{1}{2 \pi} \int_{0}^{2 \pi}\abs{f\left(r e^{i \theta}\right)}^{2} d \theta=\sum_{n=0}^{\infty}\abs{c_{n}}^{2} r^{2 n}
$$

- Deduce Liouville's theorem from (a).

:::

::: {.solution}

::: pf

::: {.pf-step #parseval}
For $0\le r<R$,
$$
\frac{1}{2\pi}\int_0^{2\pi}\abs{f(re^{i\theta})}^2\,d\theta=\sum_{n=0}^\infty\abs{c_n}^2r^{2n}.
$$

::: pf-proof
A power series converges absolutely and uniformly on each closed disk $\abs{z}\le r$ with $r<R$. So on the circle $\abs{z}=r$ the double series
$$
\abs{f(re^{i\theta})}^2=f(re^{i\theta})\overline{f(re^{i\theta})}=\sum_{k,j\ge0}c_k\overline{c_j}\,r^{k+j}e^{i(k-j)\theta}
$$
converges absolutely and uniformly in $\theta$, since $\sum_{k,j}\abs{c_k}\abs{c_j}r^{k+j}=\bigl(\sum_k\abs{c_k}r^k\bigr)^2<\infty$. Hence it can be integrated term by term. Because
$$
\int_0^{2\pi}e^{i(k-j)\theta}\,d\theta=\begin{cases}2\pi,&k=j,\\0,&k\neq j,\end{cases}
$$
only the terms with $k=j$ remain, and they give $2\pi\sum_k\abs{c_k}^2r^{2k}$.
:::

:::

::: pf-step
If $f$ is entire and $\abs{f}\le M$ on $\CC$, then $f$ is constant.

::: pf-proof
The Taylor series of an entire function converges on all of $\CC$, so step [](#parseval){.pf-ref} holds for every $r\ge0$ and gives
$$
\abs{c_0}^2+\sum_{n\ge1}\abs{c_n}^2r^{2n}\le\frac1{2\pi}\int_0^{2\pi}M^2\,d\theta=M^2.
$$
For each $n\ge1$ this gives $\abs{c_n}^2\le M^2r^{-2n}$, which tends to $0$ as $r\to\infty$. So $c_n=0$ for all $n\ge1$, and $f=c_0$.
:::

:::

:::

:::
