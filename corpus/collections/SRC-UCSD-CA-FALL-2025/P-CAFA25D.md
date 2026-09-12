---
schema: qual/card@1
id: P-CAFA25D
kind: problem
title: "Holomorphic function with constant modulus on circles is a monomial"
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Principle
  - Holomorphic Functions
  - Radial Symmetry
relations: []
review: draft
---

::: problem
Let $f : \mathbb{D} \to \mathbb{C}$ be a holomorphic function in the unit disk.
Assume that $|f(z)|$ is constant on each circle $|z| = r$ for $0 < r < 1$; i.e., $|f(re^{i\theta})| = \varphi(r)$, for some non-negative function $\varphi$ on $0 < r < 1$.

(i) Assume that $f(0) \neq 0$.
Show that $f$ is constant.

(ii) Assume that $f$ has a zero of order $m > 0$ at $z = 0$.
Show that $f(z) = cz^m$ for some constant $c$.
:::

::: solution
(i) Suppose $f(0)\ne0$. Then $f$ has no zero anywhere in $\mathbb D$: if
$f(z_0)=0$ with $|z_0|=r>0$, the assumed radial constancy would give
$|f|=0$ on the whole circle $|z|=r$, and the identity theorem would force
$f\equiv0$, contradicting $f(0)\ne0$.

Fix $0<r<1$. On $|z|=r$, both $|f|$ and $|1/f|$ are constant. Applying the
maximum modulus principle to $f$ and to $1/f$ on $|z|<r$ shows that $|f|$ is
constant throughout that disk. Hence $f$ itself is constant by the open
mapping theorem. Since $r$ was arbitrary, $f$ is constant on $\mathbb D$.

(ii) Write
\[
f(z)=z^m h(z),
\]
where $h$ is holomorphic on $\mathbb D$ and $h(0)\ne0$. For each $r>0$,
\[
|h(re^{i\theta})|
=\frac{|f(re^{i\theta})|}{r^m}
\]
is independent of $\theta$. Part (i), applied to $h$, gives
\[
h\equiv c.
\]
Therefore
\[
\boxed{f(z)=cz^m.}
\]
:::
