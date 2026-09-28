---
schema: qual/card@1
id: P-CASP13C
kind: problem
title: "Laurent series expansions of 1/(z^3 - 4z) in two annuli"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Determine the Laurent series expansions of the function $f: \mathbb{C} \setminus \{0, \pm 2\} \to \mathbb{C}$ given by $$f(z) = \frac{1}{z^3 - 4z}$$ in the annuli $\mathbb{A}(0; 0, 2)$ and $\mathbb{A}(0; 2, \infty)$.
:::

::: {.solution}
First decompose
\[
\frac1{z(z-2)(z+2)}=-\frac1{4z}+\frac1{8(z-2)}+\frac1{8(z+2)}.
\]

For $0<|z|<2$,
\[
\frac1{z-2}=-\frac12\frac1{1-z/2}
=-\frac12\sum_{n=0}^\infty \left(\frac z2\right)^n,
\]
and
\[
\frac1{z+2}=\frac12\frac1{1+z/2}
=\frac12\sum_{n=0}^\infty (-1)^n\left(\frac z2\right)^n.
\]
Hence
\[
\boxed{
f(z)=-\frac1{4z}
+\frac1{16}\sum_{n=0}^\infty\bigl((-1)^n-1\bigr)
\left(\frac z2\right)^n,\qquad 0<|z|<2.}
\]

For $|z|>2$, factor instead in negative powers:
\[
\frac1{z-2}=\frac1z\frac1{1-2/z}
=\frac1z\sum_{n=0}^\infty \left(\frac2z\right)^n,
\]
\[
\frac1{z+2}=\frac1z\frac1{1+2/z}
=\frac1z\sum_{n=0}^\infty (-1)^n\left(\frac2z\right)^n.
\]
Therefore
\[
\boxed{
f(z)=-\frac1{4z}
+\frac1{8z}\sum_{n=0}^\infty\bigl(1+(-1)^n\bigr)
\left(\frac2z\right)^n,\qquad |z|>2.}
\]
:::
