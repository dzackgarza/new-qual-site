---
schema: qual/card@1
id: P-TRIV-CA14
kind: problem
title: Fourier transform of $1/(x^2+m^2)$ by residues
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 14, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Compute $\int _ { - \infty } ^ { \infty } { \frac { e ^ { i \alpha x } } { x ^ { 2 } + m ^ { 2 } } }$ dx with $\alpha , m \in \RR$ and $m\ne0$ (hint: consider the two cases of positive or negative α separately);
:::

::: {.remark}
The source allows $m=0$, but then the ordinary improper integral diverges at
$x=0$. The finite Fourier-transform formula therefore requires $m\ne0$.
:::

::: {.solution}

Set
$$
a=|m|>0
$$
and
$$
F(z)=\frac{e^{i\alpha z}}{z^2+a^2}.
$$

::: pf

::: {.pf-step #s1-1}

Suppose $\alpha>0$. On the upper semicircle
$$
z=Re^{it},
\qquad
0\leq t\leq\pi,
$$
one has
$$
|e^{i\alpha z}|
=
e^{-\alpha\operatorname{Im}z}
\leq1.
$$


::: pf-proof

On the upper half-plane,
$$
\operatorname{Im}z\geq0.
$$
Thus
$$
|e^{i\alpha z}|
=
e^{-\alpha\operatorname{Im}z}
\leq1
$$
because $\alpha>0$.

:::

:::

::: {.pf-step #s1-2}

For $R>a$, the upper-semicircle contribution tends to zero as
$R\to\infty$.


::: pf-proof

On $|z|=R$,
$$
|z^2+a^2|
\geq
R^2-a^2.
$$
By step [](#s1-1){.pf-ref},
$$
|F(z)|
\leq
\frac1{R^2-a^2}.
$$
The arc length is $\pi R$, so
$$
\left|
\int_{\Gamma_R}F(z)\,dz
\right|
\leq
\frac{\pi R}{R^2-a^2}
\longrightarrow0.
$$

:::

:::

::: {.pf-step #s1-3}

If $\alpha>0$, then
$$
\int_{-\infty}^{\infty}
\frac{e^{i\alpha x}}{x^2+a^2}\,dx
=
\frac\pi a e^{-\alpha a}.
$$


::: pf-proof

The upper half-plane contains the simple pole $z=ia$. Its residue is
$$
\operatorname{Res}_{z=ia}F(z)
=
\frac{e^{i\alpha(ia)}}{2ia}
=
\frac{e^{-\alpha a}}{2ia}.
$$
The residue theorem gives
$$
\int_{-R}^{R}F(x)\,dx
+
\int_{\Gamma_R}F(z)\,dz
=
2\pi i
\frac{e^{-\alpha a}}{2ia}
=
\frac\pi a e^{-\alpha a}.
$$
Let $R\to\infty$ and use step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

Suppose $\alpha<0$. On the lower semicircle,
$$
|e^{i\alpha z}|
\leq1.
$$


::: pf-proof

If $\operatorname{Im}z\leq0$ and $\alpha<0$, then
$$
\alpha\operatorname{Im}z\geq0.
$$
Therefore
$$
|e^{i\alpha z}|
=
e^{-\alpha\operatorname{Im}z}
\leq1.
$$

:::

:::

::: {.pf-step #s1-5}

The lower-semicircle contribution tends to zero as $R\to\infty$.


::: pf-proof

The denominator estimate from step [](#s1-2){.pf-ref} remains valid:
$$
|z^2+a^2|
\geq
R^2-a^2.
$$
Together with step [](#s1-4){.pf-ref} and the arc length $\pi R$, the $ML$ estimate gives
$$
\left|
\int_{\Gamma_R^-}F(z)\,dz
\right|
\leq
\frac{\pi R}{R^2-a^2}
\longrightarrow0.
$$

:::

:::

::: {.pf-step #s1-6}

If $\alpha<0$, then
$$
\int_{-\infty}^{\infty}
\frac{e^{i\alpha x}}{x^2+a^2}\,dx
=
\frac\pi a e^{\alpha a}.
$$


::: pf-proof

Close the contour in the lower half-plane. Its orientation is clockwise, so
the residue theorem contributes a factor $-2\pi i$. The enclosed pole is
$z=-ia$, with residue
$$
\operatorname{Res}_{z=-ia}F(z)
=
\frac{e^{i\alpha(-ia)}}{-2ia}
=
\frac{e^{\alpha a}}{-2ia}.
$$
Hence
$$
\int_{-R}^{R}F(x)\,dx
+
\int_{\Gamma_R^-}F(z)\,dz
=
-2\pi i
\frac{e^{\alpha a}}{-2ia}
=
\frac\pi a e^{\alpha a}.
$$
Let $R\to\infty$ and use step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

If $\alpha=0$, then
$$
\int_{-\infty}^{\infty}
\frac{dx}{x^2+a^2}
=
\frac\pi a.
$$


::: pf-proof

This is step [](#s1-3){.pf-ref} with $\alpha=0$; equivalently, the same upper-semicircle
residue calculation applies because the exponential factor is identically
$1$.

:::

:::

::: {.pf-step #s1-8}

For every real $\alpha$ and every $m\ne0$,
$$
\boxed{
\int_{-\infty}^{\infty}
\frac{e^{i\alpha x}}{x^2+m^2}\,dx
=
\frac{\pi}{|m|}
e^{-|alpha||m|}.
}
$$


::: pf-proof

Recall $a=|m|$. For $\alpha>0$, step [](#s1-3){.pf-ref} gives
$$
\frac\pi a e^{-\alpha a}.
$$
For $\alpha<0$, step [](#s1-6){.pf-ref} gives
$$
\frac\pi a e^{\alpha a}
=
\frac\pi a e^{-|alpha|a}.
$$
Step [](#s1-7){.pf-ref} handles $\alpha=0$. These are exactly the displayed unified
formula.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the required Fourier-transform integral in every convergent case.

:::

:::

:::
