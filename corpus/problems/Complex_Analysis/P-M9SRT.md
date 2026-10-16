---
schema: qual/card@1
id: P-M9SRT
kind: problem
title: The series $\sum_{n=1}^\infty f(z/n)$ for $f$ vanishing to order $2$ at $0$
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
Let $f$ be analytic on $\DD$, with $f(0)=f'(0)=0$. Show that
\[
g(z)=\sum_{n=1}^\infty f(z/n)
\]
defines an analytic function on $\DD$. Moreover, prove that
\[
g(z)=f(z)\sum_{n=1}^\infty\frac1{n^2}
\]
for all $z\in\DD$ if and only if $f(z)=cz^2$ for some constant $c$.
:::

::: {.solution}
Since $f(0)=f'(0)=0$, the function $F(z)=f(z)/z^2$ extends holomorphically across $0$. On every compact disk
$|z|\le r<1$, let $M_r=\max_{|w|\le r}|F(w)|$. Then
\[
|f(z/n)|\le M_r\frac{|z|^2}{n^2},
\]
so the series defining $g$ converges uniformly on compact subsets by the $M$-test and hence defines a holomorphic function.

Write
\[
f(z)=\sum_{m=2}^\infty a_mz^m.
\]
Normal convergence permits summing coefficientwise:
\[
g(z)=\sum_{m=2}^\infty a_m\zeta(m)z^m,
\qquad
\zeta(m)=\sum_{n=1}^\infty n^{-m}.
\]
Thus $g=\zeta(2)f$ exactly when
\[
a_m(\zeta(m)-\zeta(2))=0
\qquad(m\ge2).
\]
For every $m>2$, $\zeta(m)<\zeta(2)$, so $a_m=0$. Hence
$f(z)=a_2z^2$. Conversely, for $f(z)=cz^2$ one has
$g(z)=cz^2\sum n^{-2}=\zeta(2)f(z)$.
:::