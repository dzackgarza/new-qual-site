---
schema: qual/card@1
id: P-BKS05-6B
kind: problem
title: Evaluation of $\int_0^\infty x\sin x/(x^2+a^2)\,dx$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against fresh deterministic MinerU Flash extractions of the UC Berkeley Spring 2005 exam and its companion solution packet; unambiguous duplicated-statement extraction defects were normalized.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Independently checked the contour argument and supplied an explicit upper-semicircle
    estimate in place of the source solution's invocation of Jordan's lemma.
---

::: {.problem}
Evaluate the integral $\int _ { 0 } ^ { \infty } { \frac { x \sin x } { x ^ { 2 } + a ^ { 2 } } } d x$ , where $a > 0$
:::

::: {.solution}
For $R>a$, let $C_R$ denote the upper semicircular arc
$$
z=Re^{i\theta},
\qquad
0\leq\theta\leq\pi,
$$
oriented from $R$ to $-R$, and set
$$
f(z)\coloneqq\frac{ze^{iz}}{z^2+a^2}.
$$

::: pf

::: {.pf-step #arc-contribution-vanishes}
The contribution from the semicircular arc tends to zero:
$$
\lim_{R\to\infty}\int_{C_R}f(z)\,dz=0.
$$

::: pf-proof
On $C_R$ one has
$$
\abs{z^2+a^2}
\geq
R^2-a^2,
$$
and, for $z=Re^{i\theta}$,
$$
\abs{e^{iz}}=e^{-R\sin\theta}.
$$
Hence
$$
\abs{\int_{C_R}f(z)\,dz}
\leq
\frac{R^2}{R^2-a^2}
\int_0^\pi e^{-R\sin\theta}\,d\theta.
$$
For $0\leq\theta\leq\pi/2$,
$$
\sin\theta\geq\frac{2\theta}{\pi},
$$
so symmetry gives
$$
\int_0^\pi e^{-R\sin\theta}\,d\theta
\leq
2\int_0^{\pi/2}e^{-2R\theta/\pi}\,d\theta
\leq
\frac{\pi}{R}.
$$
Therefore
$$
\abs{\int_{C_R}f(z)\,dz}
\leq
\frac{\pi R}{R^2-a^2}
\longrightarrow0.
$$
:::

:::

::: {.pf-step #contour-integral-limit}
One has
$$
\lim_{R\to\infty}
\int_{-R}^{R}\frac{xe^{ix}}{x^2+a^2}\,dx
=
\pi i e^{-a}.
$$

::: pf-proof
For $R>a$, the positively oriented contour formed by $[-R,R]$ and $C_R$
contains only the pole $z=ia$ of $f$. Its residue is
$$
\operatorname{Res}_{z=ia}f(z)
=
\frac{ia\,e^{-a}}{2ia}
=
\frac{e^{-a}}{2}.
$$
The residue theorem therefore gives
$$
\int_{-R}^{R}\frac{xe^{ix}}{x^2+a^2}\,dx
+
\int_{C_R}f(z)\,dz
=
2\pi i\frac{e^{-a}}{2}
=
\pi i e^{-a}.
$$
Letting $R\to\infty$ and applying step [](#arc-contribution-vanishes){.pf-ref} proves the claim.
:::

:::

::: {.pf-step #integral-value}
The requested improper integral is
$$
\boxed{\frac{\pi}{2}e^{-a}}.
$$

::: pf-proof
Taking imaginary parts in step [](#contour-integral-limit){.pf-ref} yields
$$
\lim_{R\to\infty}
\int_{-R}^{R}\frac{x\sin x}{x^2+a^2}\,dx
=
\pi e^{-a}.
$$
The integrand is even, so for every $R>0$,
$$
\int_{-R}^{R}\frac{x\sin x}{x^2+a^2}\,dx
=
2\int_0^R\frac{x\sin x}{x^2+a^2}\,dx.
$$
Thus the one-sided improper integral exists and equals
$$
\frac{1}{2}\pi e^{-a}.
$$
:::

:::

::: pf-qed
Step [](#integral-value){.pf-ref} gives the required value.
:::

:::

:::
