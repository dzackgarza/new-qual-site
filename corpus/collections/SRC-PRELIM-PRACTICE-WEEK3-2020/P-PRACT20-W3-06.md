---
schema: qual/card@1
id: P-PRACT20-W3-06
kind: problem
title: Convergence of $\sum n!\,x^n$ and $\sum n!\,x^{n^2}$
classification:
  areas:
  - prelim
  topics:
  - Power Series
  - Convergence
relations: []
review: draft
---

::: {.problem}
(a) For which $x$ does $\sum_{n=1}^{\infty} n!\, x^{n}$ converge?

(b) For which $x$ does $\sum_{n=1}^{\infty} n!\, x^{n^{2}}$ converge?
:::

::: {.solution}
(a) The series converges only at $x=0$. For $x\ne0$ the ratio test gives

$$
\lim_{n\to\infty}\abs{\frac{(n+1)!\,x^{n+1}}{n!\,x^n}}=\lim_{n\to\infty}(n+1)\abs{x}=\infty.
$$

(b) The series converges exactly for $\abs{x}<1$. It converges at $x=0$. For $x\ne0$ the ratio test gives

$$
\lim_{n\to\infty}\abs{\frac{(n+1)!\,x^{(n+1)^2}}{n!\,x^{n^2}}}=\lim_{n\to\infty}(n+1)\abs{x}^{2n+1}=\begin{cases}0,&0<\abs{x}<1,\\+\infty,&\abs{x}\ge1,\end{cases}
$$

since $(n+1)\abs{x}^{2n+1}=(n+1)e^{(2n+1)\log\abs{x}}$ and exponential decay beats linear growth when $\log\abs{x}<0$.
:::
