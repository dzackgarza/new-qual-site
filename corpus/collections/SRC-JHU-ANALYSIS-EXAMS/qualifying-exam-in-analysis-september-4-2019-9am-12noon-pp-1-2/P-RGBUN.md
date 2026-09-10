---
schema: qual/card@1
id: P-RGBUN
kind: problem
title: '$\int_0^\infty\frac{\log x}{x^2+2}\,dx$ by contour integration'
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Residues
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the integral, prescribed upper semicircle, and indentation requirement with September 2019 Complex Analysis 1 in the retained JHU extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the logarithm branch on both real segments, orientation of the small arc, the residue, absolute convergence, and both vanishing arc estimates."
---

::: problem
Evaluate $\int_0^\infty \frac{\log x}{x^2+2}\,dx$ by contour integration using the positively oriented contour from $-R$ to $R$ on the real axis, indented at the origin, and the positively oriented semicircle $|z|=R$, $\operatorname{Im}z>0$. Choose an appropriate branch of logarithm.
:::

::: solution
The value is $\boxed{\pi\log2/(4\sqrt2)}$.

<1>1. The chosen branch gives an identity for the truncated integral.

::: proof
Use $\operatorname{Log}z=\log|z|+i\arg z$ with
$-\pi/2<\arg z<3\pi/2$, whose cut is the nonpositive
imaginary axis. This branch is holomorphic on a neighborhood
of the closed upper half-plane away from zero [@SS03].
Let $0<\varepsilon<1<\sqrt2<R$, and take the contour
consisting, in order, of $[-R,-\varepsilon]$, the clockwise
upper semicircle of radius $\varepsilon$, $[\varepsilon,R]$,
and the counterclockwise upper semicircle of radius $R$.
It bounds the upper half-annulus positively.

The function $F(z)=\operatorname{Log}z/(z^2+2)$ has
only the simple pole $i\sqrt2$ inside this contour, with
$$
\operatorname{Res}_{i\sqrt2}F
=\frac{\log\sqrt2+i\pi/2}{2i\sqrt2}.
$$
For $x>0$ the boundary values are
$\operatorname{Log}x=\log x$ and
$\operatorname{Log}(-x)=\log x+i\pi$. Substituting
$z=-x$ on the negatively located real segment therefore
makes the sum of the two real-segment integrals equal to
$$
2\int_\varepsilon^R\frac{\log x}{x^2+2}\,dx
+i\pi\int_\varepsilon^R\frac{dx}{x^2+2}.
$$
Adding the two arc integrals, the residue theorem says
that this expression equals
$\pi(\log\sqrt2+i\pi/2)/\sqrt2$ [@SS03].
:::

<1>2. Both arcs vanish in the limit, and taking real parts
determines the required integral.

::: proof
On either upper arc, $|\arg z|\leq\pi$. On the large arc
$\Gamma_R$, the reverse triangle inequality gives
$|z^2+2|\geq R^2-2$, so
$$
\left|\int_{\Gamma_R}F(z)\,dz\right|
\leq\frac{\pi R(\log R+\pi)}{R^2-2}\longrightarrow0.
$$
On the small arc $\gamma_\varepsilon$ one similarly has
$$
\left|\int_{\gamma_\varepsilon}F(z)\,dz\right|
\leq\frac{\pi\varepsilon(|\log\varepsilon|+\pi)}
{2-\varepsilon^2}\longrightarrow0.
$$
The real logarithmic integral converges absolutely:
near zero its absolute integrand is at most
$|\log x|/2$, and for $x\geq1$ it is at most
$\log x/x^2$. Both comparison integrals are finite.
The integral of $1/(x^2+2)$ also converges.

Letting $R\to\infty$ and $\varepsilon\to0$ in step <1>1
and taking real parts gives
$$
2\int_0^\infty\frac{\log x}{x^2+2}\,dx
=\frac{\pi}{\sqrt2}\log\sqrt2
=\frac{\pi\log2}{2\sqrt2}.
$$
Dividing by two proves the displayed answer.
:::
:::
