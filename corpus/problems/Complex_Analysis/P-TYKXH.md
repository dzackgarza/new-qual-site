---
schema: qual/card@1
id: P-TYKXH
kind: problem
title: Analyticity of $\Gamma(s)$ for $\Re(s)>0$ and the reflection formula
classification:
  areas:
  - complex-analysis
  topics:
  - Gamma Function
  - Holomorphic Functions
  - Residues
relations: []
review: draft
---

::: {.problem}
For $s>0$, the **gamma function** is defined by $\displaystyle{\Gamma(s)=\int_0^{\infty} e^{-t}t^{s-1} dt}$.

1. Show that the gamma function is analytic in the half-plane $\Re (s)>0$, and is still given there by the integral formula above.

2. Apply the formula in the previous question to show that $$\Gamma(s)\Gamma(1-s)=\frac{\pi}{\sin \pi s}.$$

> Hint: You may need $\displaystyle{\Gamma(1-s)=t \int_0^{\infty}e^{-vt}(vt)^{-s} dv}$ for $t>0$.
:::

::: {.solution}
For $\Re s>0$ define
\[
\Gamma(s)=\int_0^\infty e^{-t}t^{s-1}\,dt.
\]
On every compact subset of the half-plane $\Re s>0$, both the integrand and
its $s$-derivative
\[
e^{-t}t^{s-1}\log t
\]
are dominated by an integrable function: near $0$ use
$t^{\sigma-1}(1+|\log t|)$ with $\sigma>0$, and near infinity use
$e^{-t}t^M(1+\log t)$. Hence differentiation under the integral sign is valid,
so $\Gamma$ is holomorphic on $\Re s>0$.

For $0<\Re s<1$, the change of variables $u=vt$ in the second factor gives
\[
\Gamma(1-s)
=t\int_0^\infty e^{-vt}(vt)^{-s}\,dv.
\]
Multiplying by the integral for $\Gamma(s)$ and applying Fubini,
\[
\Gamma(s)\Gamma(1-s)
=\int_0^\infty\int_0^\infty e^{-t(1+v)}v^{-s}\,dt\,dv
=\int_0^\infty\frac{v^{-s}}{1+v}\,dv.
\]
Replacing $s$ by $1-s$ yields
\[
\Gamma(s)\Gamma(1-s)
=\int_0^\infty\frac{x^{s-1}}{1+x}\,dx.
\]

Evaluate the last integral by a keyhole contour for
$z^{s-1}/(1+z)$ with branch $0<\arg z<2\pi$. The two sides of the cut differ
by the factor $e^{2\pi i(s-1)}$, and the only enclosed pole is at $z=-1$.
The small and large circular arcs vanish because $0<\Re s<1$. Thus
\[
(1-e^{2\pi i(s-1)})
\int_0^\infty\frac{x^{s-1}}{1+x}\,dx
=2\pi i e^{i\pi(s-1)}.
\]
Since
\[
1-e^{2\pi i(s-1)}
=2i e^{i\pi(s-1)}\sin(\pi s),
\]
we obtain
\[
\boxed{\Gamma(s)\Gamma(1-s)=\frac{\pi}{\sin\pi s}},
\qquad 0<\Re s<1.
\]
After the usual meromorphic continuation of $\Gamma$, the identity extends to
all $s\notin\mathbb Z$.
:::
