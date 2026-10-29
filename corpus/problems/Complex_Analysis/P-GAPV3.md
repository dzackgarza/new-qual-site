---
schema: qual/card@1
id: P-GAPV3
kind: problem
title: Holomorphy of $\Gamma$ on $\operatorname{Re}s>0$ and the reflection formula
  $\Gamma(s)\Gamma(1-s)=\pi/\sin(\pi s)$
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

(a) Show that the gamma function is analytic in the half-plane $\Re (s)>0$, and is still given there by the integral formula above.

(b) Apply the formula in the previous question to show that
$$
\Gamma(s)\Gamma(1-s)=\frac{\pi}{\sin \pi s}.
$$
:::

::: {.hint}
The change of variables $u=vt$ gives $\displaystyle{\Gamma(1-s)=t \int_0^{\infty}e^{-vt}(vt)^{-s} dv}$ for $t>0$.
:::

::: {.solution}
Throughout, $t^{s-1}=e^{(s-1)\log t}$ with the real logarithm on $(0,\infty)$.

::: pf

::: pf-step
(a) The integral converges for $\Re s>0$ and defines a holomorphic function there.

::: pf-proof
Fix a compact $K\subset\theset{\Re s>0}$ and choose $0<\sigma_0\le\Re s\le\sigma_1$ for $s\in K$. Then $\abs{e^{-t}t^{s-1}}\le t^{\sigma_0-1}$ on $(0,1]$ and $\le e^{-t}t^{\sigma_1-1}$ on $[1,\infty)$, and similarly
$$
\abs{e^{-t}t^{s-1}\log t}\le t^{\sigma_0-1}\abs{\log t}\ \text{on } (0,1],\qquad \abs{e^{-t}t^{s-1}\log t}\le e^{-t}t^{\sigma_1-1}\log t\ \text{on } [1,\infty).
$$
All majorants are integrable and independent of $s\in K$, so the integral converges and may be differentiated under the integral sign. Hence $\Gamma$ is holomorphic on $\Re s>0$, agrees with the real definition for $s>0$, and $\Gamma'(s)=\int_0^\infty e^{-t}t^{s-1}\log t\,dt$.
:::

:::

::: {.pf-step #mellin}
For $0<\Re s<1$, $\Gamma(s)\Gamma(1-s)=\displaystyle\int_0^\infty \frac{x^{s-1}}{1+x}\,dx$.

::: pf-proof
By the hint and Tonelli–Fubini (the integrand is absolutely integrable),
$$
\Gamma(s)\Gamma(1-s)=\int_0^\infty\int_0^\infty e^{-t(1+v)}v^{-s}\,dt\,dv=\int_0^\infty\frac{v^{-s}}{1+v}\,dv.
$$
The substitution $v=1/x$ turns the last integral into $\int_0^\infty x^{s-1}/(1+x)\,dx$.
:::

:::

::: {.pf-step #keyhole}
For $0<\Re s<1$, $\displaystyle\int_0^\infty \frac{x^{s-1}}{1+x}\,dx=\frac{\pi}{\sin\pi s}$.

::: pf-proof
Write $I(s)$ for the integral and integrate $F(z)=z^{s-1}/(1+z)$, with $0<\arg z<2\pi$, over a keyhole contour around the positive real axis. The small and large circular arcs contribute $0$ in the limit because $0<\Re s<1$. The upper bank contributes $I(s)$ and the lower bank $-e^{2\pi i(s-1)}I(s)$. The only enclosed pole is $z=-1$, with residue $e^{i\pi(s-1)}$. So
$$
\qty{1-e^{2\pi i(s-1)}}I(s)=2\pi i e^{i\pi(s-1)}.
$$
Since $1-e^{2\pi i(s-1)}=-2i e^{i\pi(s-1)}\sin(\pi(s-1))=2i e^{i\pi(s-1)}\sin(\pi s)$, we get $I(s)=\pi/\sin\pi s$.
:::

:::

::: pf-step
(b) $\Gamma(s)\Gamma(1-s)=\dfrac{\pi}{\sin\pi s}$ for $0<\Re s<1$, and for every $s\notin\ZZ$ after meromorphic continuation of $\Gamma$.

::: pf-proof
Steps [](#mellin){.pf-ref} and [](#keyhole){.pf-ref} give the identity on the strip. Both sides are meromorphic on $\CC$ with poles only at the integers, so the identity theorem extends it to every $s\notin\ZZ$.
:::

:::

:::

:::
