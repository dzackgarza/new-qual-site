---
schema: qual/card@1
id: P-EMCA7
kind: problem
title: A contour through a double pole and a Fourier-type integral
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared both integrals with Complex Analysis 7 in the retained source; the first circle passes through z=1 and was not altered."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Replaced the invalid residue-theorem answer by local one-sided divergence, checked the vanishing linear Taylor coefficient, and supplied the explicit large-arc bound for the second integral."
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Compared with Complex Analysis (7) of Arango-Piñeros, Some quals problems; merged the duplicate P-MMAQ-ZRGWQKRMTX, whose solution assigned the value 0 to the first integral although its contour passes through the double pole."
---

::: {.problem}
Compute the integrals
$$
\int_{|z-2|=1} \frac{e^z}{z(z-1)^2}\,dz, \qquad \int_0^\infty \frac{\cos 2x}{x^2 + 2}\,dx.
$$
:::

::: {.solution}
The first integral is not defined as an ordinary contour
integral, nor does its usual one-sided improper interpretation
converge. The second integral is
$$
\boxed{\frac{\pi}{2\sqrt2}e^{-2\sqrt2}}.
$$

<1>1. The first contour passes through a double pole,
and its one-sided integral diverges there.

::: {.proof}
One has $|1-2|=1$, so the pole at $z=1$ lies on
the path, not strictly inside it. Set $g(z)=e^z/z$,
which is holomorphic near $1$. Direct calculation gives
$g(1)=e$ and $g'(1)=0$. Taylor expansion therefore gives
$$
\frac{e^z}{z(z-1)^2}=\frac{e}{(z-1)^2}+h(z)
$$
for a function $h$ holomorphic near $1$ [@SS03].

Parametrize the circle by $z(t)=2+e^{it}$ for
$0\leq t\leq2\pi$. Then $z(\pi)=1$ and $|z'(t)|=1$.
Choose $\delta>0$ so the subarc with
$|t-\pi|\leq\delta$ is in the neighborhood where $h$
is holomorphic and bounded. On its left portion,
for $0<\varepsilon<\delta$, the principal part integrates
exactly to
$$
\int_{\pi-\delta}^{\pi-\varepsilon}
\frac{e\,z'(t)}{(z(t)-1)^2}\,dt
=-\frac{e}{z(\pi-\varepsilon)-1}
 +\frac{e}{z(\pi-\delta)-1}.
$$
The first term has modulus tending to infinity,
since its denominator tends to zero. The second
term is fixed. The contribution of $h(z(t))z'(t)$
has a finite limit because it is bounded and
continuous on the closed subarc. Thus the one-sided
integral of the full integrand cannot converge.
In particular the displayed contour integral has
no value in the ordinary sense. A zero residue
at a double pole does not remove this obstruction.
:::

<1>2. The second integral has the displayed value.

::: {.proof}
Put $F(z)=e^{2iz}/(z^2+2)$. For $R>\sqrt2$,
integrate over the interval $[-R,R]$ followed by
the counterclockwise upper semicircle $\Gamma_R$.
The only pole inside is $i\sqrt2$, and it is simple,
with residue $e^{-2\sqrt2}/(2i\sqrt2)$.
The residue theorem gives
$$
\int_{-R}^R\frac{e^{2ix}}{x^2+2}\,dx
+\int_{\Gamma_R}F(z)\,dz
=\frac{\pi}{\sqrt2}e^{-2\sqrt2}
$$
[@SS03]. On $\Gamma_R$, one has
$|e^{2iz}|=e^{-2\operatorname{Im}z}\leq1$ and
$|z^2+2|\geq R^2-2$. Consequently
$$
\left|\int_{\Gamma_R}F(z)\,dz\right|
\leq\frac{\pi R}{R^2-2}\longrightarrow0.
$$
The real-axis integral converges absolutely, since
its integrand has modulus $1/(x^2+2)$.
Letting $R\to\infty$ and taking real parts yields
$$
\int_{-\infty}^{\infty}\frac{\cos2x}{x^2+2}\,dx
=\frac{\pi}{\sqrt2}e^{-2\sqrt2}.
$$
The integrand is even, so its half-line integral
is half that value, as asserted.
:::
:::
