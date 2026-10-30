---
schema: qual/card@1
id: P-CAEXAMPREP-04
kind: problem
title: Fourier integral of $1/(1+x^2)$
classification: {areas: [complex-analysis], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against the deterministic MinerU Flash extraction assets/attachments/Complex_Analysis_Exam_Prep_Solutions_extracted.md.
---

::: {.problem}
Let $a\in\RR\setminus\{0\}$.
Evaluate
$$
\int_{-\infty}^{\infty}\frac{\cos(ax)}{1+x^2}\,dx.
$$
:::

::: {.solution}

Put $b=\abs{a}>0$. Since $\cos(ax)=\cos(bx)$, it is enough to evaluate the integral with $b>0$.

::: pf

::: {.pf-step #s1-1}

For
$$
F(z)=\frac{e^{ibz}}{1+z^2},
$$
the only pole in the upper half-plane is the simple pole $z=i$, and
$$
\operatorname{Res}_{z=i}F=\frac{e^{-b}}{2i}.
$$


::: pf-proof

The denominator factors as $(z-i)(z+i)$, so the only upper-half-plane pole is $i$, and it is simple. Therefore
$$
\operatorname{Res}_{z=i}F
=\lim_{z\to i}\frac{(z-i)e^{ibz}}{(z-i)(z+i)}
=\frac{e^{ib i}}{2i}
=\frac{e^{-b}}{2i}.
$$

:::

:::

::: {.pf-step #s1-2}

If $C_R$ is the upper semicircle $z=Re^{i\theta}$, $0\le\theta\le\pi$, then
$$
\int_{C_R}F(z)\,dz\longrightarrow0
\qquad\text{as }R\to\infty.
$$


::: pf-proof

On $C_R$,
$$
\abs{e^{ibz}}=e^{-b\operatorname{Im}z}\le1
$$
and, for $R>1$,
$$
\abs{1+z^2}\ge R^2-1.
$$
Since the length of $C_R$ is $\pi R$, the ML estimate gives
$$
\abs{\int_{C_R}F(z)\,dz}
\le\frac{\pi R}{R^2-1}
\longrightarrow0.
$$

:::

:::

::: {.pf-step #s1-3}

One has
$$
\int_{-\infty}^{\infty}\frac{e^{ibx}}{1+x^2}\,dx
=\pi e^{-b}.
$$


::: pf-proof

For $R>1$, integrate $F$ counterclockwise around the boundary of the upper half-disc of radius $R$. The residue theorem and step [](#s1-1){.pf-ref} give
$$
\int_{-R}^{R}\frac{e^{ibx}}{1+x^2}\,dx
+\int_{C_R}F(z)\,dz
=2\pi i\frac{e^{-b}}{2i}
=\pi e^{-b}.
$$
The real-axis integrand is absolutely integrable because its modulus is $(1+x^2)^{-1}$. Letting $R\to\infty$ and using step [](#s1-2){.pf-ref} gives the displayed identity.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
\int_{-\infty}^{\infty}\frac{\cos(ax)}{1+x^2}\,dx
=\pi e^{-\abs{a}}}.
$$


::: pf-proof

Taking real parts in step [](#s1-3){.pf-ref} yields
$$
\int_{-\infty}^{\infty}\frac{\cos(bx)}{1+x^2}\,dx
=\pi e^{-b}.
$$
Since $b=\abs{a}$ and $\cos(ax)=\cos(bx)$, this is exactly the claimed formula.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the required evaluation.

:::

:::

:::
