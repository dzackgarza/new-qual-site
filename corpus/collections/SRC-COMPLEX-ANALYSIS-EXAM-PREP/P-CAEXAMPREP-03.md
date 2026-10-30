---
schema: qual/card@1
id: P-CAEXAMPREP-03
kind: problem
title: Evaluate an integral of $x^2/(1+x^4)$
classification: {areas: [complex-analysis], topics: [Contour Integration]}
relations: []
review: draft
audit:
  - event: source-checked
    by: gpt-5.6-sol
    date: 2026-09-14
    note: Checked against the deterministic MinerU Flash extraction assets/attachments/Complex_Analysis_Exam_Prep_Solutions_extracted.md.
---

::: {.problem}
Evaluate
$$
\int_{-\infty}^{\infty}\frac{x^2}{1+x^4}\,dx.
$$
:::

::: {.solution}

Set
$$
f(z)=\frac{z^2}{1+z^4}.
$$

::: pf

::: {.pf-step #s1-1}

The improper integral in the statement converges absolutely.


::: pf-proof

The integrand is continuous on every bounded interval. For $\abs{x}\ge1$,
$$
0\le\frac{x^2}{1+x^4}\le\frac1{x^2},
$$
and $\int_1^\infty x^{-2}\,dx<\infty$. Thus both tails converge absolutely.

:::

:::

::: {.pf-step #s1-2}

The poles of $f$ in the upper half-plane are the simple poles
$$
z_1=e^{i\pi/4},
\qquad
z_2=e^{3i\pi/4},
$$
and
$$
\operatorname{Res}_{z=z_1}f+\operatorname{Res}_{z=z_2}f
=-\frac{i\sqrt2}{4}.
$$


::: pf-proof

The zeros of $1+z^4$ are $e^{(2j+1)i\pi/4}$, $j=0,1,2,3$, and each is simple because the derivative $4z^3$ is nonzero there. The two with positive imaginary part are $z_1,z_2$. At either such root $z_k$,
$$
\operatorname{Res}_{z=z_k}f
=\frac{z_k^2}{4z_k^3}
=\frac1{4z_k}.
$$
Hence
$$
\begin{aligned}
\operatorname{Res}_{z=z_1}f+\operatorname{Res}_{z=z_2}f
&=\frac14\left(e^{-i\pi/4}+e^{-3i\pi/4}\right)\\
&=-\frac{i\sqrt2}{4}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

If $C_R$ is the upper semicircle $z=Re^{i\theta}$, $0\le\theta\le\pi$, then
$$
\int_{C_R}f(z)\,dz\longrightarrow0
\qquad\text{as }R\to\infty.
$$


::: pf-proof

For $R>1$ and $\abs{z}=R$,
$$
\abs{1+z^4}\ge R^4-1,
\qquad
\abs{f(z)}\le\frac{R^2}{R^4-1}.
$$
The length of $C_R$ is $\pi R$, so the ML estimate gives
$$
\abs{\int_{C_R}f(z)\,dz}
\le\frac{\pi R^3}{R^4-1}
\longrightarrow0.
$$

:::

:::

::: {.pf-step #s1-4}

The requested integral is
$$
\boxed{\frac{\pi}{\sqrt2}}.
$$


::: pf-proof

For $R>1$, integrate $f$ counterclockwise around the boundary of the upper half-disc of radius $R$. By the residue theorem and step [](#s1-2){.pf-ref},
$$
\int_{-R}^{R}\frac{x^2}{1+x^4}\,dx
+\int_{C_R}f(z)\,dz
=2\pi i\left(-\frac{i\sqrt2}{4}\right)
=\frac{\pi}{\sqrt2}.
$$
Let $R\to\infty$. Step [](#s1-1){.pf-ref} identifies the limit of the real-axis integral with the improper integral in the problem, and step [](#s1-3){.pf-ref} makes the semicircle contribution vanish. The displayed value follows.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the required evaluation.

:::

:::

:::
