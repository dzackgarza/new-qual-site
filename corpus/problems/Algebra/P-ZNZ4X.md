---
schema: qual/card@1
id: P-ZNZ4X
kind: problem
title: The radical of an ideal is an ideal, and $I(Z(I))=\sqrt{I}$
classification:
  areas:
  - algebra
  topics:
  - Ideals
  - Nilpotence
  - Geometry
relations: []
review: draft
---

::: {.problem}
Let $k$ be an algebraically closed field and $R=k[x_1,\ldots,x_n]$.
Define the "radical" of an ideal $I\trianglelefteq R$ and prove it is an ideal.
Prove that the ideal of all polynomials vanishing on the zero set of $I$ is $\sqrt{I}$.
:::


::: {.solution}
The radical is
\[
\sqrt I=\{f\in R:f^m\in I\text{ for some }m\ge1\}.
\]

It is an ideal. If $f^m\in I$ and $g^n\in I$, then every term in the binomial expansion of $(f+g)^{m+n}$ contains either $f^m$ or $g^n$, so
\[
(f+g)^{m+n}\in I.
\]
Also, for $r\in R$,
\[
(rf)^m=r^mf^m\in I.
\]
Thus $f+g,rf\in\sqrt I$.

Let
\[
Z(I)=\{a\in k^n:h(a)=0\text{ for every }h\in I\},
\]
and let $I(Z(I))$ be the ideal of polynomials vanishing on $Z(I)$.

First, $\sqrt I\subseteq I(Z(I))$: if $f^m\in I$, then for every $a\in Z(I)$,
\[
f(a)^m=0,
\]
so $f(a)=0$.

For the reverse inclusion, let $f\in I(Z(I))$. In
\[
k[x_1,\ldots,x_n,y]
\]
consider
\[
J=I+(1-yf).
\]
There is no common zero of $J$: a common zero would have its first $n$ coordinates in $Z(I)$, hence $f=0$, while simultaneously $1-yf=0$, impossible. By the weak Nullstellensatz, $J=(1)$. Hence
\[
1=\sum_i a_i h_i+b(1-yf),\qquad h_i\in I.
\]
Substitute $y=f^{-1}$ in the localization $R_f$. The last term vanishes, so $1\in IR_f$. Clearing a power of $f$ gives
\[
f^N\in I
\]
for some $N$, hence $f\in\sqrt I$.

Therefore
\[
\boxed{I(Z(I))=\sqrt I}.
\]
:::
