---
schema: qual/card@1
id: P-PRACT20-W3-02
kind: problem
title: Convergence of $\sum n!\,x^{2n}/(n^n(1+x^{2n}))$
classification:
  areas:
  - prelim
  topics:
  - Series
  - Convergence
relations: []
review: draft
---

::: {.problem}
For which values of $x$ does $\displaystyle \sum_{n=1}^{\infty} \frac{n!\, x^{2n}}{n^{n} (1 + x^{2n})}$ converge?
:::

::: {.solution}
Using $0\le\frac{x^{2n}}{1+x^{2n}}\le1$, we see that for any $x$,

$$
\sum_{n=1}^{\infty}\frac{n!\,x^{2n}}{n^n(1+x^{2n})}\le\sum_{n=1}^{\infty}\frac{n!}{n^n}.
$$

The latter sum converges; thus the former converges for all $x\in\RR$ by comparison. To prove the latter converges, use the ratio test with $a_n=n!/n^n$:

$$
\lim_{n\to\infty}\frac{a_{n+1}}{a_n}=\lim_{n\to\infty}\frac{(n+1)!\,n^n}{n!\,(n+1)^{n+1}}=\lim_{n\to\infty}\frac{1}{\left(1+\frac1n\right)^n}=\frac1e<1.
$$
:::
