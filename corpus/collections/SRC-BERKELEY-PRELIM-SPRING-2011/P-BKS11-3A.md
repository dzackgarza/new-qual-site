---
schema: qual/card@1
id: P-BKS11-3A
kind: problem
title: Evaluation of $\int_0^\infty dx/(x^4+1)$ by residues
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with page 2 of the retained Spring 2011 solution PDF and independently reviewed the upper-half-plane residue computation.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the arc decay, both upper-half-plane residues, and the evenness factor from the real line to the half-line.
---

::: {.problem}
Use residues to compute

$$
\int _ { 0 } ^ { \infty } { \frac { d x } { x ^ { 4 } + 1 } } .
$$
:::

::: {.solution}
Set
$$
F(z)\coloneqq\frac{1}{z^4+1}.
$$
For $R>1$, let $C_R$ be the upper semicircle of radius $R$, oriented from
$R$ to $-R$.

::: pf

::: {.pf-step #arc-vanishes}
The semicircular contribution tends to zero:
$$
\lim_{R\to\infty}\int_{C_R}F(z)\,dz=0.
$$

::: pf-proof
On $C_R$,
$$
\abs{z^4+1}
\geq
R^4-1.
$$
The length of $C_R$ is $\pi R$, so
$$
\abs{
\int_{C_R}F(z)\,dz
}
\leq
\frac{\pi R}{R^4-1}
\longrightarrow0.
$$
:::

:::

::: pf-step
The poles of $F$ in the upper half-plane are
$$
\alpha=e^{i\pi/4}
=
\frac{1+i}{\sqrt2}
$$
and
$$
\beta=e^{3i\pi/4}
=
\frac{-1+i}{\sqrt2}.
$$

::: pf-proof
The roots of $z^4+1=0$ are
$$
e^{i(2k+1)\pi/4},
\qquad
k=0,1,2,3.
$$
Exactly the roots with arguments $\pi/4$ and $3\pi/4$ lie in the upper
half-plane.
:::

:::

::: pf-step
The sum of the two upper-half-plane residues is
$$
\operatorname{Res}_{z=\alpha}F
+
\operatorname{Res}_{z=\beta}F
=
-\frac{i}{2\sqrt2}.
$$

::: pf-proof
Every root of $z^4+1$ is simple, so at a root $\rho$,
$$
\operatorname{Res}_{z=\rho}F
=
\frac{1}{4\rho^3}.
$$
Since
$$
\alpha^3=\beta
\qquad\text{and}\qquad
\beta^3=\alpha,
$$
one gets
$$
\begin{aligned}
\operatorname{Res}_{z=\alpha}F
+
\operatorname{Res}_{z=\beta}F
&=
\frac14
\left(
\frac1\beta+\frac1\alpha
\right)\\
&=
\frac14
\left(
\frac{-1-i}{\sqrt2}
+
\frac{1-i}{\sqrt2}
\right)\\
&=
-\frac{i}{2\sqrt2}.
\end{aligned}
$$
:::

:::

::: {.pf-step #full-line-value}
The integral over the whole real line is
$$
\int_{-\infty}^{\infty}\frac{dx}{x^4+1}
=
\frac{\pi}{\sqrt2}.
$$

::: pf-proof
The residue theorem on the contour formed by $[-R,R]$ and $C_R$ gives
$$
\int_{-R}^{R}\frac{dx}{x^4+1}
+
\int_{C_R}F(z)\,dz
=
2\pi i
\left(
-\frac{i}{2\sqrt2}
\right).
$$
Let $R\to\infty$ and apply step [](#arc-vanishes){.pf-ref}.
:::

:::

::: {.pf-step #final-value}
The requested integral is
$$
\boxed{
\int_0^\infty\frac{dx}{x^4+1}
=
\frac{\pi}{2\sqrt2}
}.
$$

::: pf-proof
The integrand is even, so the integral over $[0,\infty)$ is one half of
the full-line integral in step [](#full-line-value){.pf-ref}.
:::

:::

::: pf-qed
Step [](#final-value){.pf-ref} is the required residue evaluation.
:::

:::

:::
