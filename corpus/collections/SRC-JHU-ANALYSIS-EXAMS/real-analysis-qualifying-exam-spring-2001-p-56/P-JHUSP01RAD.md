---
schema: qual/card@1
id: P-JHUSP01RAD
kind: problem
title: 'Interpolation inequality between the $L^{4/3}$, $L^2$, and $L^4$ norms'
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 4 of the JHU Real Analysis Qualifying Exam, Spring 2001, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
For which real numbers $\alpha,\beta$ does
\[
\|f\|_2\le\|f\|_{4/3}^{\alpha}\|f\|_4^{\beta}
\]
hold for all measurable $f$ for which the right-hand side is finite?
:::

::: {.solution}
The inequality holds exactly for
\[
\boxed{\alpha=\beta=\frac12}.
\]

<1>1. Necessity.
::: {.proof}
Apply the inequality to $cf$ with $c>0$. Homogeneity forces
\[
1=\alpha+\beta.
\]
Next take $f=\mathbf1_E$ for measurable sets $E$ of arbitrary finite positive measure $m(E)=m$. Then
\[
\|f\|_2=m^{1/2},
\qquad
\|f\|_{4/3}=m^{3/4},
\qquad
\|f\|_4=m^{1/4}.
\]
Thus
\[
m^{1/2}\le m^{3\alpha/4+\beta/4}
\qquad\text{for every }m>0.
\]
For this to hold both as $m\downarrow0$ and $m\to\infty$, the exponents must agree:
\[
\frac12=\frac{3\alpha+\beta}{4}.
\]
Together with $\alpha+\beta=1$, this gives
\[
\alpha=\beta=\frac12.
\]
:::

<1>2. Sufficiency.
::: {.proof}
By Hölder's inequality with exponents $4/3$ and $4$,
\[
\int |f|^2
=\int |f|\,|f|
\le\left(\int|f|^{4/3}\right)^{3/4}\left(\int|f|^4\right)^{1/4}.
\]
Taking square roots gives
\[
\|f\|_2\le\|f\|_{4/3}^{1/2}\|f\|_4^{1/2}.
\]
Thus the claimed pair is both necessary and sufficient.
:::
:::
