---
schema: qual/card@1
id: P-CASP07B
kind: problem
title: "Zero-free disk for bounded analytic functions and characterization of extremal functions"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $f(z)$ be analytic with $|f(z)| \leq M$ in $\mathbb{D}$ and $f(0) = \alpha > 0$.

(a) Show that $f(z)$ has no zeros in the disk $|z| < \alpha/M$.

(b) Find all functions $f(z)$ (satisfying the above) such that $f(z)$ has a zero on the circle $|z| = \alpha/M$.
:::

::: solution
If $M=0$ there is nothing to prove, so assume $M>0$ and put
\[
h(z)=\frac{f(z)}M,
\qquad a=\frac\alpha M\in(0,1].
\]
Then $h:\mathbb D\to\overline{\mathbb D}$ is holomorphic and $h(0)=a$.
If $h$ is nonconstant, in fact $h(\mathbb D)\subset\mathbb D$.

Suppose $h(z_0)=0$. Schwarz--Pick gives
\[
\left|\frac{h(z_0)-h(0)}{1-\overline{h(0)}h(z_0)}\right|
\le |z_0|,
\]
hence
\[
a\le |z_0|.
\]
This proves (a).

For equality, assume first $a<1$ and $|z_0|=a$. Equality holds in
Schwarz--Pick at two distinct points, so $h$ is a disk automorphism. Every
extremal therefore has the form
\[
h(z)=e^{i\theta}\frac{z-z_0}{1-\overline{z_0}z},
\qquad |z_0|=a,
\]
and the condition $h(0)=a>0$ forces
\[
e^{i\theta}=-\frac{a}{z_0}.
\]
Thus all extremals are
\[
\boxed{
f(z)=-M\frac{a}{z_0}
\frac{z-z_0}{1-\overline{z_0}z},
\qquad |z_0|=a=\alpha/M.}
\]

If $a=1$, the maximum principle forces $h\equiv1$, so there is no zero in
$\mathbb D$ and hence no extremal of the requested kind.
:::
