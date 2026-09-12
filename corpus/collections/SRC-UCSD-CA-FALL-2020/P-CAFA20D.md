---
schema: qual/card@1
id: P-CAFA20D
kind: problem
title: "Entire functions with prescribed modulus on the unit circle and third derivative"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Find all entire functions $f: \mathbb{C} \to \mathbb{C}$ such that $|f(z)| = 2$ everywhere on $\{|z| = 1\}$, and $f^{(3)}(0) = -12$.
:::

::: solution
Let the zeros of $f$ in $\mathbb D$ be $a_1,\dots,a_m$, counted with
multiplicity. Since $|f|=2$ on the unit circle, there are no boundary zeros.
Form the finite Blaschke product
\[
B(z)=\prod_{j=1}^m\frac{z-a_j}{1-\overline{a_j}z}.
\]
Then $|B|=1$ on $|z|=1$, and $g=f/B$ is holomorphic and zero-free in a
neighborhood of the closed disk. On the unit circle, $|g|=2$. Applying the
maximum principle to $g$ and to $1/g$ gives $|g|=2$ throughout the disk, so
$g$ is constant. Thus on the disk, and hence everywhere by the identity
theorem, $f$ is a constant multiple of a finite Blaschke product.

But $f$ is entire. If some $a_j\ne0$, the corresponding denominator
$1-\overline{a_j}z$ gives a pole outside the disk unless canceled. After all
cancellations, an entire finite Blaschke product is necessarily a monomial.
Hence
\[
f(z)=c z^m,
\qquad |c|=2.
\]
The condition $f^{(3)}(0)=-12$ forces $m=3$ and
\[
6c=-12,
\]
so $c=-2$. Therefore the unique function is
\[
\boxed{f(z)=-2z^3}.
\]
:::
