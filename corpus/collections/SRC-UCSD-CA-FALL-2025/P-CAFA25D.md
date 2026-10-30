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

::: {.problem}
Let $f : \DD \to \CC$ be a holomorphic function in the unit disk.
Assume that $\abs{f(z)}$ is constant on each circle $\abs{z} = r$ for $0 < r < 1$; i.e., $\abs{f(re^{i\theta})} = \varphi(r)$, for some non-negative function $\varphi$ on $0 < r < 1$.

(i) Assume that $f(0) \neq 0$.
Show that $f$ is constant.

(ii) Assume that $f$ has a zero of order $m > 0$ at $z = 0$.
Show that $f(z) = cz^m$ for some constant $c$.
:::

::: {.solution}
(i) Suppose $f(0)\ne0$. Then $f$ has no zero anywhere in $\DD$: if
$f(z_0)=0$ with $\abs{z_0}=r>0$, the assumed radial constancy would give
$\abs{f}=0$ on the whole circle $\abs{z}=r$, and the identity theorem would force
$f\equiv0$, contradicting $f(0)\ne0$.

Fix $0<r<1$. On $\abs{z}=r$, both $\abs{f}$ and $\abs{1/f}$ are constant. Applying the
maximum modulus principle to $f$ and to $1/f$ on $\abs{z}<r$ shows that $\abs{f}$ is
constant throughout that disk. Hence $f$ itself is constant by the open
mapping theorem. Since $r$ was arbitrary, $f$ is constant on $\DD$.

(ii) Write
$$
f(z)=z^m h(z),
$$
where $h$ is holomorphic on $\DD$ and $h(0)\ne0$. For each $r>0$,
$$
\abs{h(re^{i\theta})}
=\frac{\abs{f(re^{i\theta})}}{r^m}
$$
is independent of $\theta$. Part (i), applied to $h$, gives
$$
h\equiv c.
$$
Therefore
$$
\boxed{f(z)=cz^m.}
$$
:::
