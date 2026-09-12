---
schema: qual/card@1
id: P-SMK7Q
kind: problem
title: An analytic self-map of the disk with $|f|=1$ on the circle is a finite Blaschke
  product
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Zeros
  - Maximum Modulus Principle
relations: []
review: draft
---

::: problem
Suppose $f:\DD\to\DD$ is analytic and admits a continuous extension $\tilde f: \bar \DD \to \bar \DD$ such that $\abs{z} = 1 \implies \abs{f(z)} = 1$.

Prove that $f$ is a rational function.

Suppose that $z=0$ is the unique zero of $f$.
Show that
\[  
\exists n\in \NN, \lambda \in S^1 \qtext{ such that }f(z) = \lambda z^n
.\]

Suppose that $a_1, \cdots, a_n \in \DD$ are the zeros of $f$ and prove that
\[  
\exists \lambda \in S^1 \qtext{such that} f(z) = \lambda \prod_{j=1}^n {z - a_j \over 1 - \bar{a_j} z}
.\]
:::

::: solution
Because $|f|=1$ on $\partial\mathbb D$ and the extension is continuous, there
is an annular neighborhood of the boundary on which $f$ has no zeros. Hence all
zeros of $f$ lie in a compact subset of $\mathbb D$. Since zeros of a
nonzero holomorphic function are isolated, there are only finitely many of
them, counted with multiplicity; write them as $a_1,\dots,a_n$.

For each zero define the Blaschke factor
\[
B_{a_j}(z)=\frac{z-a_j}{1-\overline{a_j}z}.
\]
It has the same zero multiplicity contribution as $f$ and satisfies
$|B_{a_j}(z)|=1$ on $|z|=1$. Therefore
\[
g(z)=\frac{f(z)}{\prod_{j=1}^n B_{a_j}(z)}
\]
extends holomorphically and without zeros to $\mathbb D$, continuously to the
closed disk, and satisfies $|g|=1$ on the boundary.

The maximum modulus principle gives $|g|\le1$ in $\mathbb D$. Since $g$ has no
zeros, $1/g$ is holomorphic and has boundary modulus $1$, so the same principle
gives $|1/g|\le1$, i.e. $|g|\ge1$. Thus $|g|\equiv1$, and the open mapping
theorem forces $g$ to be constant. Hence for some $\lambda\in S^1$,
\[
\boxed{f(z)=\lambda\prod_{j=1}^n
\frac{z-a_j}{1-\overline{a_j}z}.}
\]
This is rational, proving the first assertion as well.

If $0$ is the unique zero and has multiplicity $n$, every $a_j=0$, so the
formula reduces to
\[
\boxed{f(z)=\lambda z^n.}
\]
:::
