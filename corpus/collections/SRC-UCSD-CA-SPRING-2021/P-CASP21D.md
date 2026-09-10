---
schema: qual/card@1
id: P-CASP21D
kind: problem
title: "Bound on |f(0)| for a holomorphic function vanishing at four points in B(0,2)"
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Blaschke Products
  - Holomorphic Functions
relations: []
review: draft
---

::: problem
Let $f : G \to \mathbb{C}$ be a holomorphic function in $G = \{z : |z| < 2\}$ such that $|f(z)| < 1$ for $z \in G$.
Assume that $f(1) = f(-1) = f(i) = f(-i) = 0$.
Show that $|f(0)| \leq \frac{1}{15}$.
:::

::: solution
Scale to the unit disk by setting
\[
F(w)=f(2w).
\]
Then $F:\mathbb D\to\mathbb D$ and $F$ vanishes at
\[
\frac12,-\frac12,\frac i2,-\frac i2.
\]
For $a\in\mathbb D$, let
\[
\phi_a(w)=\frac{w-a}{1-\bar a w}.
\]
Successively applying the Schwarz lemma after dividing out these four
Blaschke factors gives a holomorphic map $H:\mathbb D\to\overline{\mathbb D}$
such that
\[
F(w)=H(w)
\prod_{a\in\{1/2,-1/2,i/2,-i/2\}}\phi_a(w).
\]
Therefore
\[
|f(0)|=|F(0)|
\le \prod_a|a|
=\left(\frac12\right)^4
=\frac1{16}
<\frac1{15}.
\]
Thus the requested bound follows, in fact with the stronger constant $1/16$.
:::
