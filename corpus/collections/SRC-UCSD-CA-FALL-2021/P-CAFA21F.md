---
schema: qual/card@1
id: P-CAFA21F
kind: problem
title: "Entire function with modulus 1 on the unit circle"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $f : \mathbb{C} \to \mathbb{C}$ be an entire function such that $|f(z)| = 1$ for $|z| = 1$.
Show that there exists $a \in \mathbb{C}$ and $n \geq 0$ such that $f(z) = az^n$.
:::

::: solution
The zeros of $f$ in $\mathbb D$ are finite in number, since $f$ has no zeros
on $|z|=1$. Let $a_1,\dots,a_m$ be those zeros with multiplicity and form the
finite Blaschke product
\[
B(z)=\prod_{j=1}^m\frac{z-a_j}{1-\overline{a_j}z}.
\]
Then $g=f/B$ is holomorphic and zero-free on a neighborhood of the closed disk
and satisfies $|g|=1$ on $|z|=1$. Applying the maximum principle to $g$ and
$1/g$ gives $|g|=1$ in the disk, hence $g$ is constant. Thus $f$ agrees on the
disk with a constant times a finite Blaschke product.

Since $f$ is entire, all denominator factors must cancel. After cancellation,
the only entire finite Blaschke products are monomials. Therefore
\[
f(z)=az^n
\]
for some $n\ge0$. The boundary condition gives $|a|=1$.
:::
