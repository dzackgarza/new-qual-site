---
schema: qual/card@1
id: P-TIE-S15-24
kind: problem
title: Integrals of $\abs{\psi_\alpha'}^2$ and $\abs{\psi_\alpha'}$ over the disk for a Blaschke factor
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2015, question 24.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Absorbed the duplicate P-TIE-S15-30, which the source prints again as Spring 2015, question 30, page 14 of Questions_from_Tie.pdf, and took over its typed statement and remark.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source states part (b) for all |alpha| < 1, where the printed right-hand side is undefined at alpha = 0. Part (b) now assumes 0 < |alpha| < 1.
---

::: {.problem}
Let $\psi_\alpha(z) = \frac{\alpha - z}{1 - \bar{\alpha}z}$ with $\abs{\alpha} < 1$ and $\DD = \{z : \abs{z} < 1\}$. Prove that

(a) $\displaystyle\frac{1}{\pi}\iint_{\DD} \abs{\psi_\alpha'}^2\,dx\,dy = 1$.

(b) for $0 < \abs{\alpha} < 1$, $\displaystyle\frac{1}{\pi}\iint_{\DD} \abs{\psi_\alpha'}\,dx\,dy = \frac{1 - \abs{\alpha}^2}{\abs{\alpha}^2}\log\frac{1}{1 - \abs{\alpha}^2}$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

One has
$$
\psi_\alpha'(z)
=
-\frac{1-\abs{\alpha}^2}
{(1-\overline\alpha z)^2}.
$$


::: pf-proof

Differentiate
$$
\psi_\alpha(z)
=
\frac{\alpha-z}{1-\overline\alpha z}.
$$
The quotient rule gives
$$
\begin{aligned}
\psi_\alpha'(z)
&=
\frac{
-(1-\overline\alpha z)
-
(\alpha-z)(-\overline\alpha)
}
{(1-\overline\alpha z)^2}\\
&=
\frac{-1+\abs{\alpha}^2}
{(1-\overline\alpha z)^2},
\end{aligned}
$$
which is the stated formula.

:::

:::

::: {.pf-step #s1-2}

The map $\psi_\alpha$ is a conformal automorphism of $\DD$.


::: pf-proof

For $\abs{\alpha}<1$,
$$
\psi_\alpha(z)
=
\frac{\alpha-z}{1-\overline\alpha z}
$$
is the standard Blaschke automorphism interchanging $0$ and $\alpha$. Direct calculation gives
$$
\psi_\alpha(\psi_\alpha(z))=z,
$$
so it is bijective with holomorphic inverse equal to itself. By step [](#s1-1){.pf-ref},
$$
\psi_\alpha'(z)\ne0
$$
on $\DD$.

:::

:::

::: {.pf-step #s1-3}

One has
$$
\boxed{
\frac1\pi
\iint_{\DD}
\abs{\psi_\alpha'(z)}^2\,dA(z)
=1.
}
$$


::: pf-proof

For a holomorphic map, the real Jacobian determinant is
$$
J_{\psi_\alpha}(z)
=
\abs{\psi_\alpha'(z)}^2.
$$
By step [](#s1-2){.pf-ref}, $\psi_\alpha$ is a conformal bijection of $\DD$ onto itself. The change-of-variables formula therefore gives
$$
\iint_{\DD}
\abs{\psi_\alpha'(z)}^2\,dA(z)
=
\operatorname{area}(\psi_\alpha(\DD))
=
\operatorname{area}(\DD)
=
\pi.
$$
Dividing by $\pi$ gives the result.

:::

:::

::: {.pf-step #s1-4}

Put
$$
r\coloneqq\abs{\alpha}.
$$
For $0\le\rho<1$,
$$
\int_0^{2\pi}
\frac{d\theta}
{\abs{1-r\rho e^{i\theta}}^2}
=
\frac{2\pi}{1-r^2\rho^2}.
$$


::: pf-proof

Rotating the variable $z$ does not change planar area, so the integral depends on $\alpha$ only through $r=\abs\alpha$. For $r\rho<1$,
$$
\frac1{1-r\rho e^{i\theta}}
=
\sum_{n=0}^{\infty}
r^n\rho^n e^{in\theta},
$$
uniformly in $\theta$. Hence
$$
\frac1{\abs{1-r\rho e^{i\theta}}^2}
=
\sum_{m,n\ge0}
r^{m+n}\rho^{m+n}e^{i(m-n)\theta}.
$$
Integrating over $0\le\theta\le2\pi$ kills all off-diagonal terms:
$$
\int_0^{2\pi}
\frac{d\theta}
{\abs{1-r\rho e^{i\theta}}^2}
=
2\pi
\sum_{n=0}^{\infty}
r^{2n}\rho^{2n}
=
\frac{2\pi}{1-r^2\rho^2}.
$$

:::

:::

::: {.pf-step #s1-5}

If $0<\abs{\alpha}<1$, then
$$
\boxed{
\frac1\pi
\iint_{\DD}
\abs{\psi_\alpha'(z)}\,dA(z)
=
\frac{1-\abs{\alpha}^2}{\abs{\alpha}^2}
\log\frac1{1-\abs{\alpha}^2}.
}
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
\abs{\psi_\alpha'(z)}
=
\frac{1-r^2}
{\abs{1-\overline\alpha z}^2}.
$$
Using polar coordinates and step [](#s1-4){.pf-ref},
$$
\begin{aligned}
\frac1\pi
\iint_{\DD}
\abs{\psi_\alpha'(z)}\,dA(z)
&=
\frac{1-r^2}{\pi}
\int_0^1
\int_0^{2\pi}
\frac{\rho\,d\theta\,d\rho}
{\abs{1-r\rho e^{i\theta}}^2}\\
&=
2(1-r^2)
\int_0^1
\frac{\rho}{1-r^2\rho^2}\,d\rho.
\end{aligned}
$$
For $r>0$,
$$
\int_0^1
\frac{\rho}{1-r^2\rho^2}\,d\rho
=
\frac1{2r^2}
\log\frac1{1-r^2}.
$$
Substitution gives
$$
\frac{1-r^2}{r^2}
\log\frac1{1-r^2}.
$$
Replacing $r$ by $\abs\alpha$ gives the formula.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves part (a), and step [](#s1-5){.pf-ref} proves part (b).

:::

:::

:::
