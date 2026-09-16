---
schema: qual/card@1
id: P-JHUSP05ANF
kind: problem
title: "Residue evaluation of a rational-times-sine integral"
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the numerator, both quadratic factors and full-line endpoints with Spring 2005 problem 6 in the retained JHU extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the two simple residues, the upper-arc decay and absolute convergence before taking the imaginary part of the complex integral."
---

::: {.problem}
Use residues to evaluate the integral

$$
\int_{-\infty}^{\infty} \frac{x \sin x \, dx}{(x^{2}+1)(x^{2}+4)}.
$$
:::

::: solution
The value is $\boxed{\frac\pi3(e^{-1}-e^{-2})}$.

<1>1. A complex exponential produces the required sine integral as its imaginary part.
::: proof
Set $F(z)=ze^{iz}/((z^2+1)(z^2+4))$. For real $x$,
the imaginary part of $F(x)$ is the integrand in the
question. The complex integral is absolutely convergent:
$|F(x)|$ is bounded for $|x|\leq1$, and for $|x|\geq1$
it is at most $|x|^{-3}$. Thus imaginary parts commute
with this integral, and the same assertion holds for
limits of its truncated integrals.
:::

<1>2. The upper-half-plane residues determine the complex integral.
::: proof
The only poles in the upper half-plane are the simple
poles $i$ and $2i$. Factoring the corresponding quadratic
terms gives
$$
\operatorname{Res}_{i}F
=\frac{i e^{-1}}{(2i)(i^2+4)}=\frac{e^{-1}}6,
\qquad
\operatorname{Res}_{2i}F
=\frac{2i e^{-2}}{((2i)^2+1)(4i)}=-\frac{e^{-2}}6.
$$
For $R>2$, integrate over $[-R,R]$ followed by the
counterclockwise upper semicircle $\Gamma_R$. The residue
theorem gives
$$
\int_{-R}^{R}F(x)\,dx+\int_{\Gamma_R}F(z)\,dz
=\frac{\pi i}{3}(e^{-1}-e^{-2})
$$
[@SS03]. On the arc, $|e^{iz}|=e^{-\operatorname{Im}z}\leq1$,
and consequently
$$
\left|\int_{\Gamma_R}F(z)\,dz\right|
\leq\frac{\pi R^2}{(R^2-1)(R^2-4)}\longrightarrow0.
$$
Letting $R\to\infty$ and taking imaginary parts now
gives the displayed real value. Absolute convergence
from step <1>1 ensures an ordinary integral, not just
a principal value.
:::
:::
