---
schema: qual/card@1
id: P-CASP25A
kind: problem
title: "Bound on |f(0)| + |f'(0)| implies at least two zeros in D"
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

::: problem
Let $f$ be a holomorphic function in a neighborhood of the closed unit disc $\overline{\mathbb{D}}$, and suppose that
$$
|f(0)| + |f'(0)| < \inf\{|f(z)| : |z| = 1\}.
$$
Show that $f$ has at least two zeros (counting multiplicity) in $\mathbb{D}$.

(Hint: Make use of the function $g(z) = f(0) + f'(0)z - f(z)$.)
:::

::: solution
Set
\[
g(z)=f(0)+f'(0)z-f(z).
\]
On $|z|=1$,
\[
|f(0)+f'(0)z|
\le |f(0)|+|f'(0)|
<|f(z)|.
\]
Therefore Rouché's theorem shows that
\[
-f(z)
\quad\text{and}\quad
g(z)=-f(z)+f(0)+f'(0)z
\]
have the same number of zeros in $\mathbb D$, counted with multiplicity.

But
\[
g(0)=0,
\qquad
g'(0)=0,
\]
so $g$ has a zero at $0$ of order at least $2$ unless $g\equiv0$, in which
case $f$ itself is linear and the boundary inequality is impossible. Hence
$g$ has at least two zeros in $\mathbb D$, counted with multiplicity, and so
does $f$.
:::
