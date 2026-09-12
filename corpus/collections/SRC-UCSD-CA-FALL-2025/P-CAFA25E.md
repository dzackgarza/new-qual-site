---
schema: qual/card@1
id: P-CAFA25E
kind: problem
title: "If {f(nz)} is a normal family on an annulus, then f is constant"
classification:
  areas:
  - complex-analysis
  topics:
  - Normal Families
  - Entire Functions
  - Montel
relations: []
review: draft
---

::: problem
Let $f : \mathbb{C} \to \mathbb{C}$ be an entire function, and define $f_n(z) = f(nz)$.
Suppose that $\mathcal{F} = \{f_n : n \geq 1\}$ is a normal family on the annulus $\{1 < |z| < 2\}$.
Show that $f$ is constant.
:::

::: solution
Write the Taylor series of the entire function as
\[
f(w)=\sum_{m=0}^\infty a_m w^m.
\]
Then on the annulus
\[
A=\{1<|z|<2\},
\]
we have
\[
f_n(z)=f(nz)=\sum_{m=0}^\infty a_m n^m z^m.
\]

Since $\{f_n:n\ge1\}$ is normal in the compact-open sense, the sequence
$(f_n)$ has a subsequence $(f_{n_j})$ converging uniformly on compact subsets
of $A$ to a holomorphic function $g$. Fix $1<r<2$. Uniform convergence on the
circle $|z|=r$ implies convergence of every Laurent coefficient. For $m\ge0$,
\[
a_m n_j^m
=\frac1{2\pi i}
\int_{|z|=r}\frac{f_{n_j}(z)}{z^{m+1}}\,dz
\longrightarrow
\frac1{2\pi i}
\int_{|z|=r}\frac{g(z)}{z^{m+1}}\,dz.
\]
The right-hand side is finite. If $m\ge1$ and $a_m\ne0$, however,
$|a_m|n_j^m\to\infty$, a contradiction. Thus
\[
a_m=0
\qquad(m\ge1),
\]
so $f\equiv a_0$ is constant.
:::
