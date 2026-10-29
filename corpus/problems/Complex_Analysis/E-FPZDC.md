---
schema: qual/card@1
id: E-FPZDC
kind: problem
title: Analyticity of $\Gamma$ on $\Re(s)>0$ and Euler's reflection formula
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

::: {.exercise}
(a) For real $s>0$, define
$$
\Gamma(s)=\int_0^\infty e^{-t}t^{s-1}\,dt.
$$
Show that the same integral defines an analytic function in the half-plane $\Re(s)>0$.

(b) Using
$$
\int_0^\infty {x^{a-1}\over1+x^n}\,dx
={\pi\over n\sin(a\pi/n)},
\qquad 0<a<n,
$$
show that, for $0<\Re(s)<1$,
$$
\Gamma(s)\Gamma(1-s)=\frac{\pi}{\sin \pi s}.
$$
:::

::: {.hint}
For (b), use $\displaystyle{\Gamma(1-s)=t \int_0^{\infty}e^{-vt}(vt)^{-s}\, dv}$ for $t>0$.
:::

::: {.solution}

::: pf

::: {.pf-step #holomorphic}
(a) $\Gamma(s)=\int_0^\infty e^{-t}t^{s-1}\,dt$ is holomorphic on $\Re s>0$.

::: pf-proof
Fix a compact $K\subset\{\Re s>0\}$, and let $\sigma_0=\min_K\Re s>0$ and $\sigma_1=\max_K\Re s$.
For $s\in K$, $\abs{e^{-t}t^{s-1}}\le t^{\sigma_0-1}$ on $0<t\le1$ and $\abs{e^{-t}t^{s-1}}\le e^{-t}t^{\sigma_1-1}$ on $t\ge1$, and both majorants are integrable.
With an extra factor $\abs{\log t}^m$ the majorants stay integrable, so differentiation under the integral sign is valid locally uniformly and $\Gamma^{(m)}(s)=\int_0^\infty e^{-t}t^{s-1}(\log t)^m\,dt$.
In particular $\Gamma$ is holomorphic on $\Re s>0$.
:::

:::

::: {.pf-step #mellin}
For $0<\Re s<1$, $\Gamma(s)\Gamma(1-s)=\int_0^\infty\frac{v^{-s}}{1+v}\,dv$.

::: pf-proof
For $t>0$ the substitution $u=vt$ gives $\Gamma(1-s)=t\int_0^\infty e^{-vt}(vt)^{-s}\,dv$.
The double integral converges absolutely, so by Fubini
$$
\Gamma(s)\Gamma(1-s)=\int_0^\infty\!\!\int_0^\infty e^{-t}t^{s-1}\,te^{-vt}(vt)^{-s}\,dv\,dt=\int_0^\infty v^{-s}\qty(\int_0^\infty e^{-(1+v)t}\,dt)dv=\int_0^\infty\frac{v^{-s}}{1+v}\,dv.
$$
:::

:::

::: {.pf-step #continuation}
$M(a)\coloneqq\int_0^\infty\frac{v^{a-1}}{1+v}\,dv$ equals $\frac\pi{\sin\pi a}$ for $0<\Re a<1$.

::: pf-proof
The majorant argument of step [](#holomorphic){.pf-ref} shows that $M$ is holomorphic on the strip $0<\Re a<1$, and so is $\frac\pi{\sin\pi a}$.
The given formula with $n=1$ makes them equal for real $a\in(0,1)$, and the identity theorem extends the equality to the strip.
:::

:::

::: pf-step
(b) $\Gamma(s)\Gamma(1-s)=\frac\pi{\sin\pi s}$ for $0<\Re s<1$.

::: pf-proof
Take $a=1-s$ in step [](#continuation){.pf-ref} and combine with step [](#mellin){.pf-ref}: $\Gamma(s)\Gamma(1-s)=\frac\pi{\sin(\pi(1-s))}=\frac\pi{\sin\pi s}$.
:::

:::

:::

:::
