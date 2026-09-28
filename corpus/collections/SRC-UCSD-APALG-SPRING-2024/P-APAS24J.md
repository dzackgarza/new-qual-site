---
schema: qual/card@1
id: P-APAS24J
kind: problem
title: Hilbert series of invariants under diagonal $\pm 1$ matrices
classification:
  areas:
  - applied-algebra
  topics:
  - Invariant Theory
relations: []
review: draft
---

::: {.problem}
Let $n$ be a positive integer and let $G\subseteq\mathrm{GL}_n(\mathbb{C})$ be the subgroup
\[
G=\left\{\begin{pmatrix}
\varepsilon_1 & 0 & \cdots & 0 \\
0 & \varepsilon_2 & \cdots & 0 \\
 &  & \ddots &  \\
0 & 0 & \cdots & \varepsilon_n
\end{pmatrix}
\colon
\varepsilon_1,\varepsilon_2,\ldots,\varepsilon_n=\pm 1\right\}
\]
of diagonal matrices whose diagonal entries are $\pm 1$.
Find the Hilbert series of the invariant ring $\mathbb{C}[x_1,x_2,\ldots,x_n]^G$.
:::

::: {.solution}
A monomial
\[
x_1^{a_1}\cdots x_n^{a_n}
\]
transforms under
\[
g=\operatorname{diag}(\varepsilon_1,\ldots,\varepsilon_n)
\]
by the scalar
\[
\varepsilon_1^{a_1}\cdots\varepsilon_n^{a_n}.
\]
Because the signs $\varepsilon_i\in\{\pm1\}$ may be chosen independently, the monomial is $G$-invariant if and only if every exponent $a_i$ is even.

Therefore the invariant monomials are exactly the monomials in
\[
x_1^2,\ldots,x_n^2,
\]
so
\[
\boxed{\mathbb C[x_1,\ldots,x_n]^G
=\mathbb C[x_1^2,\ldots,x_n^2].}
\]
These $n$ algebraically independent generators all have degree $2$. Hence the Hilbert series is
\[
\boxed{
H_{\mathbb C[x_1,\ldots,x_n]^G}(t)
=\frac1{(1-t^2)^n}.
}
\]
:::
