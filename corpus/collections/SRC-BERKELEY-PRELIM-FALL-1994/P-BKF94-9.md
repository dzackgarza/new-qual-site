---
schema: qual/card@1
id: P-BKF94-9
kind: problem
title: The integral $\int_0^\infty(\log x)^2/(1+x^2)\,dx$
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Evaluated the Mellin parameter integral by a keyhole contour and
    differentiated it twice at s=1, with differentiation under the integral
    justified by an integrable uniform majorant.
---

::: {.problem}
Evaluate
\[
\int_0^{\infty}\frac{(\log x)^2}{x^2+1}\,dx.
\]
:::

::: {.solution}
For $0<s<2$, define
$$
I(s)\coloneqq
\int_0^\infty\frac{x^{s-1}}{1+x^2}\,dx.
$$

::: pf

::: {.pf-step #s1}

For $0<s<2$,
$$
I(s)
=
\frac{\pi}{2}
\csc\frac{\pi s}{2}.
$$

::: pf-proof

Set
$$
\alpha\coloneqq\frac{s}{2},
$$
so $0<\alpha<1$. The substitution $t=x^2$ gives
$$
I(s)
=
\frac12
\int_0^\infty\frac{t^{\alpha-1}}{1+t}\,dt.
$$
Write
$$
J(\alpha)
\coloneqq
\int_0^\infty\frac{t^{\alpha-1}}{1+t}\,dt.
$$

To evaluate $J(\alpha)$, use the branch
$$
z^{\alpha-1}
=
e^{(\alpha-1)\Log z},
\qquad
0<\arg z<2\pi,
$$
and integrate
$$
\frac{z^{\alpha-1}}{1+z}
$$
around a keyhole contour about the positive real axis. Since
$0<\alpha<1$, the integrals over the outer and inner circular arcs tend to
$0$ as their radii tend to $\infty$ and $0$, respectively. The upper ray
contributes $J(\alpha)$, while the lower ray is traversed in the opposite
direction and contributes
$$
-e^{2\pi i\alpha}J(\alpha).
$$
The only enclosed pole is $z=-1$, whose residue is
$$
e^{i\pi(\alpha-1)}.
$$
Therefore the residue theorem gives
$$
\bigl(1-e^{2\pi i\alpha}\bigr)J(\alpha)
=
2\pi i e^{i\pi(\alpha-1)}.
$$
Since
$$
1-e^{2\pi i\alpha}
=
-2ie^{i\pi\alpha}\sin(\pi\alpha),
$$
one obtains
$$
J(\alpha)
=
\frac{\pi}{\sin(\pi\alpha)}.
$$
Substituting $\alpha=s/2$ gives the formula for $I(s)$.

:::

:::

::: {.pf-step #s2}

One may differentiate $I(s)$ twice under the integral sign in a
neighborhood of $s=1$, and
$$
I''(1)
=
\int_0^\infty
\frac{(\log x)^2}{1+x^2}\,dx.
$$

::: pf-proof

For $1/2\leq s\leq3/2$, the second $s$-derivative of the integrand is
$$
\frac{x^{s-1}(\log x)^2}{1+x^2}.
$$
For $0<x\leq1$ its absolute value is at most
$$
x^{-1/2}(\log x)^2,
$$
and for $x\geq1$ it is at most
$$
x^{-3/2}(\log x)^2.
$$
Both majorants are integrable on their respective intervals. Dominated
convergence therefore justifies differentiating twice under the integral
sign, giving
$$
I''(s)
=
\int_0^\infty
\frac{x^{s-1}(\log x)^2}{1+x^2}\,dx.
$$
Set $s=1$.

:::

:::

::: {.pf-step #s3}

One has
$$
I''(1)=\frac{\pi^3}{8}.
$$

::: pf-proof

By step [](#s1){.pf-ref},
$$
I(s)
=
\frac{\pi}{2}
\csc u,
\qquad
u=\frac{\pi s}{2}.
$$
For
$$
h(u)=\csc u,
$$
one has
$$
h''(u)
=
\csc u\cot^2u+\csc^3u.
$$
At
$$
u=\frac{\pi}{2},
$$
this equals $1$. Applying the chain rule twice gives
$$
I''(1)
=
\frac{\pi}{2}
\left(\frac{\pi}{2}\right)^2
=
\frac{\pi^3}{8}.
$$

:::

:::

::: {.pf-step #s4}

Therefore
$$
\boxed{
\int_0^\infty
\frac{(\log x)^2}{1+x^2}\,dx
=
\frac{\pi^3}{8}
}.
$$

::: pf-proof

Combine steps [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} gives the requested value.

:::

:::

:::
