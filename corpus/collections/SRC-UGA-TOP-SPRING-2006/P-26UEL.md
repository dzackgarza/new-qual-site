---
schema: qual/card@1
id: P-26UEL
kind: problem
title: Cellular structure of a product of finite CW complexes and $\chi(M\times N)=\chi(M)\chi(N)$
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
  - Euler Characteristic
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked both parts against problem 9 of the official UGA Spring 2006 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: >-
    Used the standard product CW structure: each pair of cells e^i in M and
    e^j in N gives one cell e^i x e^j of dimension i+j. Thus the n-cell count
    is the convolution of the cell counts, and the alternating sum factors as
    chi(M x N) = chi(M)chi(N). The product-cell construction and agreement with
    the ordinary product topology in the finite case are Hatcher, Algebraic
    Topology, Appendix, Theorem A.6; multiplicativity is Section 2.2,
    Exercise 20.
---

::: problem
Let $M$ and $N$ be finite CW complexes.

a. Describe a cellular structure of $M \times N$ in terms of the cellular structures of $M$ and $N$.

b. Show that the Euler characteristic of $M \times N$ is the product of the Euler characteristics of $M$ and $N$.
:::

::: {.solution}
For each $i,j\ge0$, let $c_i(M)$ and $c_j(N)$ denote the numbers of $i$-cells of $M$ and $j$-cells of $N$, respectively.

<1>1. For every $i$-cell $e^i_\alpha\subset M$ and every $j$-cell $e^j_\beta\subset N$, the product
\[
e^i_\alpha\times e^j_\beta
\]
is an $(i+j)$-cell of $M\times N$.
::: {.proof}
Choose characteristic maps
\[
\varphi_\alpha:D^i\longrightarrow M,
\qquad
\psi_\beta:D^j\longrightarrow N
\]
for the two cells.
Their product
\[
\varphi_\alpha\times\psi_\beta:
D^i\times D^j\longrightarrow M\times N
\]
restricts to a homeomorphism from
\[
\operatorname{int}(D^i)\times\operatorname{int}(D^j)
\]
onto $e^i_\alpha\times e^j_\beta$.
Since
\[
D^i\times D^j\cong D^{i+j},
\]
this product is an open cell of dimension $i+j$.

Moreover,
\[
\partial(D^i\times D^j)
=
(\partial D^i\times D^j)\cup(D^i\times\partial D^j),
\]
and the product characteristic map sends this boundary into products in which at least one factor lies in a lower skeleton.
Thus these product cells attach along lower-dimensional product cells.
:::

<1>2. The product cells in <1>1 form a CW structure on $M\times N$, with
\[
(M\times N)^n
=
\bigcup_{i+j\le n} M^i\times N^j.
\]
::: {.proof}
The open cells of $M$ partition $M$, and the open cells of $N$ partition $N$.
Hence the products
\[
e^i_\alpha\times e^j_\beta
\]
partition $M\times N$.
By <1>1 each is an open cell of dimension $i+j$, attached to the union of cells of smaller total dimension.

Because $M$ and $N$ are finite CW complexes, only finitely many such cells occur.
Hence the weak topology determined by these cells agrees with the ordinary product topology, so this is a CW structure on the given topological product.
:::

<1>3. The number of $n$-cells in this product CW structure is
\[
c_n(M\times N)
=
\sum_{i+j=n}c_i(M)c_j(N).
\]
::: {.proof}
By <1>1--<1>2, an $n$-cell is exactly a product of an $i$-cell of $M$ and a $j$-cell of $N$ with $i+j=n$.
There are $c_i(M)c_j(N)$ such pairs for fixed $(i,j)$, and summing over $i+j=n$ gives the formula.
:::

<1>4. The Euler characteristic satisfies
\[
\boxed{\chi(M\times N)=\chi(M)\chi(N)}.
\]
::: {.proof}
Using <1>3 and the definition of Euler characteristic for a finite CW complex,
\[
\begin{aligned}
\chi(M\times N)
&=\sum_n(-1)^n c_n(M\times N)\\
&=\sum_n(-1)^n\sum_{i+j=n}c_i(M)c_j(N)\\
&=\sum_{i,j}(-1)^{i+j}c_i(M)c_j(N)\\
&=\left(\sum_i(-1)^i c_i(M)\right)
  \left(\sum_j(-1)^j c_j(N)\right)\\
&=\chi(M)\chi(N).
\end{aligned}
\]
All sums are finite because $M$ and $N$ are finite CW complexes.
:::
:::
