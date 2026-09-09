---
schema: qual/card@1
id: P-CAF11D
kind: problem
title: "Analytic functions on a strip that do not extend beyond any boundary point"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $G$ be the open strip $\{z \in \mathbb{C} : 1 < \operatorname{Im} z < 2\}$.

(a) Prove that there exists a function $f \in H(G)$ with the following property: For any $z \in \partial G$ and any $\epsilon > 0$ there is no function $g \in H(B(z; \epsilon))$ such that $g(z) = f(z)$ for all $z \in G \cap B(z; \epsilon)$.
(This means that $f$ does not extend analytically beyond any boundary point of $G$.)

(b) Prove or disprove: There is a function $f \in H(G)$ satisfying the conditions of (a) and such that $f$ has no zeroes in $G$.
:::

::: solution
We construct a zero-free example, which proves both parts simultaneously.

First map the strip conformally to the unit disk. Put
\[
\psi(z)=e^{\pi(z-i)},
\]
which maps $G$ onto the upper half-plane, and then set
\[
\phi(z)=\frac{\psi(z)-i}{\psi(z)+i}.
\]
Thus $\phi:G\to\mathbb D$ is conformal.

Choose a countable dense set $\{\zeta_n\}_{n\ge1}$ on the unit circle. Define
\[
H(w)=\sum_{n=1}^\infty 2^{-n}\frac{\zeta_n+w}{\zeta_n-w},
\qquad |w|<1.
\]
On every compact subset of $\mathbb D$ the series converges uniformly, hence
$H$ is holomorphic. Moreover,
\[
\operatorname{Re}\frac{\zeta+w}{\zeta-w}
=\frac{1-|w|^2}{|\zeta-w|^2}>0
\qquad (|\zeta|=1,\ |w|<1).
\]
Therefore
\[
F(w)=e^{-H(w)}
\]
is holomorphic and has no zeros in $\mathbb D$.

Fix $n$. Along the radius $w=r\zeta_n$ with $r\uparrow1$, the $n$-th summand
of $\operatorname{Re}H$ tends to $+\infty$, while all other summands are
nonnegative. Hence
\[
F(r\zeta_n)\longrightarrow0.
\]

Suppose $F$ admitted a holomorphic extension across some boundary point
$\eta\in\partial\mathbb D$. The extension would exist on a small disk about
$\eta$. Because the $\zeta_n$ are dense on the unit circle, that disk contains
infinitely many $\zeta_n$ accumulating at a point of the disk. By continuity of
the extension and the radial limits above, the extension would vanish at all
those $\zeta_n$. The identity theorem would then force the extension, and hence
$F$, to vanish identically, contradiction.

Thus $F$ has no analytic continuation across any point of $\partial\mathbb D$.
Finally set
\[
f=F\circ\phi.
\]
Then $f\in H(G)$, $f$ has no zeros in $G$, and any analytic continuation of $f$
across a boundary point of $G$ would, via the conformal map $\phi$, produce an
analytic continuation of $F$ across a point of $\partial\mathbb D$. Therefore
$f$ has no analytic continuation across any boundary point of the strip.
:::
