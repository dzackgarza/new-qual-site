---
schema: qual/card@1
id: P-ROMKF
kind: problem
title: If $\lim_{n\to\infty}|a_{n+1}|/|a_n|=L$ then $\lim_{n\to\infty}|a_n|^{1/n}=L$
classification:
  areas:
  - complex-analysis
  topics:
  - Convergence Tests
  - Power Series
  - Sequences of Numbers
relations: []
review: draft
---

::: {.problem}
Let $a_n \neq 0$ and assume that $\displaystyle
\lim_{n \rightarrow \infty} \frac{|a_{n+1}|}{|a_n|} = L$. Show that
$\displaystyle
\lim_{n \rightarrow \infty}
\sqrt[n]{|a_n|} = L.
%p_n^{\frac{1}{n}} = L.$ In particular, this shows that when
applicable, the ratio test can be used to calculate the radius of
convergence of a power series.
:::

::: {.solution}
First suppose $0<L<\infty$. Set
\[
r_k=\frac{|a_{k+1}|}{|a_k|}.
\]
Then $r_k\to L$, and
\[
|a_n|=|a_0|\prod_{k=0}^{n-1}r_k.
\]
Taking logarithms,
\[
\frac1n\log|a_n|
=\frac{\log|a_0|}{n}
+\frac1n\sum_{k=0}^{n-1}\log r_k.
\]
Since $\log r_k\to\log L$, Cesàro convergence gives
\[
\frac1n\log|a_n|\to\log L.
\]
Exponentiating yields
\[
|a_n|^{1/n}\to L.
\]

If $L=0$, then for every $\varepsilon>0$ we eventually have $r_k<\varepsilon$,
so $|a_n|^{1/n}\le C^{1/n}\varepsilon^{1-o(1)}$ and hence the limit is $0$.
If $L=\infty$, apply the same argument to $1/|a_n|$, whose successive ratio
tends to $0$. Thus in all cases
\[
\boxed{\lim_{n\to\infty}|a_n|^{1/n}=L.}
\]
:::
