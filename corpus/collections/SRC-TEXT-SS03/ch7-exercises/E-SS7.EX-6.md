---
schema: qual/card@1
id: E-SS7.EX-6
kind: problem
title: A vertical contour integral for the step function
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
relations: []
review: draft
---

::: {.exercise}
Show that for every $c>0$,
$$
\lim_{N\to\infty}\frac{1}{2\pi i}\int_{c-iN}^{c+iN}\frac{a^s}{s}\,ds
=\begin{cases}
1,&a>1,\\
\frac12,&a=1,\\
0,&0\leq a<1.
\end{cases}
$$
The integral follows the vertical segment from $c-iN$ to $c+iN$.
:::
