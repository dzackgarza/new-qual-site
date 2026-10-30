---
schema: qual/card@1
id: P-CASP25A
kind: problem
title: 'If $\abs{f(0)}+\abs{f''(0)}<\min_{\abs z=1}\abs f$, then $f$ has at least two zeros in $\DD$'
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Holomorphic Functions
  - Zeros
relations: []
review: draft
---

::: {.problem}
Let $f$ be a holomorphic function in a neighborhood of the closed unit disc $\overline{\DD}$, and suppose that
$$
\abs{f(0)} + \abs{f'(0)} < \inf\{\abs{f(z)} : \abs{z} = 1\}.
$$
Show that $f$ has at least two zeros (counting multiplicity) in $\DD$.

(Hint: Make use of the function $g(z) = f(0) + f'(0)z - f(z)$.)
:::

::: {.solution}
Set
$$
g(z)=f(0)+f'(0)z-f(z).
$$
On $\abs{z}=1$,
$$
\abs{f(0)+f'(0)z}
\le \abs{f(0)}+\abs{f'(0)}
<\abs{f(z)}.
$$
Therefore Rouché's theorem shows that
$$
-f(z)
\quad\text{and}\quad
g(z)=-f(z)+f(0)+f'(0)z
$$
have the same number of zeros in $\DD$, counted with multiplicity.

But
$$
g(0)=0,
\qquad
g'(0)=0,
$$
so $g$ has a zero at $0$ of order at least $2$ unless $g\equiv0$, in which
case $f$ itself is linear and the boundary inequality is impossible. Hence
$g$ has at least two zeros in $\DD$, counted with multiplicity, and so
does $f$.
:::
