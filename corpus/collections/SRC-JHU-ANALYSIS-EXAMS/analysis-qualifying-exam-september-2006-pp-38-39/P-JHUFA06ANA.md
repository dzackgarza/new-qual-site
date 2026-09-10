---
schema: qual/card@1
id: P-JHUFA06ANA
kind: problem
title: The integral of $1/(x^4+4)$ by residues
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
  note: "Compared the quartic denominator, half-line endpoints and required residue method with September 2006 problem 1 in the retained JHU source."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked both upper-half-plane residues, their sum, absolute convergence and the semicircle estimate before dividing the full-line value by two."
---

1. Use residues to calculate the integral

$$
\int _ { 0 } ^ { \infty } { \frac { d x } { x ^ { 4 } + 4 } } .
$$

::: solution
The value is $\boxed{\pi/8}$.

<1>1. The two upper-half-plane residues have sum $-i/8$.

::: proof
The four roots of $z^4+4$ are $1+i$, $-1+i$, $-1-i$
and $1-i$. Each is simple since $4z^3\ne0$ there.
For $F(z)=1/(z^4+4)$, the upper-half-plane residues are
$$
\operatorname{Res}_{1+i}F=\frac1{4(1+i)^3}
=\frac{-1-i}{16},\qquad
\operatorname{Res}_{-1+i}F=\frac1{4(-1+i)^3}
=\frac{1-i}{16}.
$$
Their sum is $-i/8$.
:::

<1>2. The upper semicircle evaluates the integral.

::: proof
For $R>2$, integrate along $[-R,R]$ and the
counterclockwise upper semicircle $\Gamma_R$. The residue
theorem gives the contour integral
$2\pi i(-i/8)=\pi/4$ [@SS03]. On $\Gamma_R$,
$|z^4+4|\geq R^4-4$, hence
$$
\left|\int_{\Gamma_R}F(z)\,dz\right|
\leq\frac{\pi R}{R^4-4}\longrightarrow0.
$$
The real integrand is bounded near zero and bounded
by $|x|^{-4}$ for $|x|\geq1$, so the full-line integral
converges absolutely. Passing to the limit gives
$$
\int_{-\infty}^{\infty}\frac{dx}{x^4+4}=\frac\pi4.
$$
Evenness of the integrand makes the required half-line
integral equal to half this value, namely $\pi/8$.
:::
:::
