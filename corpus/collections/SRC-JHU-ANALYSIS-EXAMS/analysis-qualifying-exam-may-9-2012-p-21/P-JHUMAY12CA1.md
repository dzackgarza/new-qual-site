---
schema: qual/card@1
id: P-JHUMAY12CA1
kind: problem
title: Residue evaluation of $\int_0^\infty (1+x^2)^{-2}\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - Residue Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the half-line integral and required residue method with May 2012 problem 1 in the retained JHU extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the double-pole residue, vanishing semicircle estimate, absolute convergence and factor of two between the line and half-line integrals."
---

::: {.problem}
Use residues to calculate the integral $\int_0^\infty \frac{1}{(1 + x^2)^2} \, dx$.
:::

::: {.solution}
<1>1. The upper-half-plane contour integral is $\pi/2$.

::: {.proof}
Let $F(z)=(1+z^2)^{-2}$. For $R>1$, use the contour
formed by $[-R,R]$ followed by the counterclockwise
upper semicircle $\Gamma_R$ of radius $R$. The only
enclosed pole is the double pole at $i$. Factoring
$F(z)=(z-i)^{-2}(z+i)^{-2}$ gives
$$
\operatorname{Res}_{i}F
=\left.\frac{d}{dz}(z+i)^{-2}\right|_{z=i}
=-\frac{2}{(2i)^3}=\frac{1}{4i}.
$$
The [[T-HRPNO|residue theorem]] therefore gives
$$
\int_{-R}^R\frac{dx}{(1+x^2)^2}
+\int_{\Gamma_R}F(z)\,dz
=2\pi i\frac{1}{4i}=\frac\pi2
$$
:::

<1>2. The requested integral is
$$
\boxed{\int_0^\infty \frac{dx}{(1+x^2)^2}=\frac{\pi}{4}}.
$$

::: {.proof}
For $\abs{z}=R$, the inequality $\abs{1+z^2}\geq R^2-1$ yields
$$
\abs{\int_{\Gamma_R}F(z)\,dz}
\leq\frac{\pi R}{(R^2-1)^2}\longrightarrow0.
$$
The real integral converges absolutely, since its integrand
is bounded by one on $[-1,1]$ and by $\abs{x}^{-4}$ outside
that interval. Letting $R\to\infty$ in step <1>1 thus
gives $\int_{-\infty}^\infty(1+x^2)^{-2}\,dx=\pi/2$.
The integrand is even, so the requested half-line integral
is one half of this value, namely $\pi/4$.
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>2 gives the requested value.
:::
:::
