---
schema: qual/card@1
id: P-JHUFA10RA3
kind: problem
title: Schur's test for integral operators
classification:
  areas:
  - real-analysis
  topics:
  - Operator Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against the Fall 2010 JHU Analysis Qualifying Exam in the preserved exam compilation.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually verified Fall 2010 problem 3 on PDF page 26 and read both complete Schur-test cards. P-JHUMAY11ANK duplicates this single source item and was merged here rather than retained as a false May 2011 appearance."
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Retained the common weighted Cauchy–Schwarz proof and supplied the preceding Tonelli argument establishing absolute convergence of Tf almost everywhere."
---

::: {.problem}
Let $Tf(x) = \int_{\RR^n} K(x,y) f(y) \, dy$, where $K(x,y)$ is a nonnegative measurable function on $\RR^n \times \RR^n$.
Suppose that there are measurable functions $p(x) > 0$ and $q(x) > 0$ on $\RR^n$ and real numbers $\alpha, \beta > 0$ for which

$$\int K(x,y) q(y) \, dy \leq \alpha p(x),$$

for almost all $x$ and

$$\int p(x) K(x,y) \, dx \leq \beta q(y)$$

for almost all $y$.
Show that for $f \in L^2(\RR^n)$ we have

$$\norm{Tf}_{L^2} \leq \sqrt{\alpha \beta} \norm{f}_{L^2}.$$

(This is called Schur's test.)
:::

::: {.solution}
Let $f\in L^2(\RR^n)$.

::: pf

::: pf-step
The integral defining $Tf$ converges absolutely almost everywhere.

::: pf-proof
Set
$$
B(x)=\int_{\RR^n}K(x,y)\frac{\abs{f(y)}^2}{q(y)}\,dy.
$$
This is a nonnegative measurable function, possibly
initially infinite. Tonelli and the second kernel inequality
give [@Fol13]
$$
\begin{aligned}
\int_{\RR^n}p(x)B(x)\,dx
&=\int_{\RR^n}\frac{\abs{f(y)}^2}{q(y)}
\left(\int_{\RR^n}p(x)K(x,y)\,dx\right)dy\\
&\leq\beta\int_{\RR^n}\abs{f(y)}^2\,dy<\infty.
\end{aligned}
$$
Since $p(x)>0$, this implies $B(x)<\infty$ almost
everywhere. The first kernel inequality also gives
$A(x):=\int K(x,y)q(y)\,dy\leq\alpha p(x)<\infty$
for almost every $x$. For points where both bounds hold,
Cauchy–Schwarz applied to
$K^{1/2}q^{1/2}$ and $K^{1/2}\abs{f}q^{-1/2}$ yields
$$
\int K(x,y)\abs{f(y)}\,dy\leq A(x)^{1/2}B(x)^{1/2}<\infty
$$
[@Fol13]. Thus $Tf$ is defined almost everywhere, and
the usual parameter-integral measurability follows by
Tonelli applied to positive and negative real and imaginary
parts. Set $Tf=0$ on the exceptional null set.
:::

:::

::: pf-step
The same weighted inequality gives the claimed norm bound.

::: pf-proof
For almost every $x$, Cauchy–Schwarz in the $y$ variable gives
$$
\begin{aligned}
\abs{Tf(x)}^2
&=\abs{\int K(x,y)^{1/2}q(y)^{1/2}
\,K(x,y)^{1/2}q(y)^{-1/2}f(y)\,dy}^2\\
&\le
\left(\int K(x,y)q(y)\,dy\right)
\left(\int K(x,y)\frac{\abs{f(y)}^2}{q(y)}\,dy\right)\\
&\le \alpha p(x)
\int K(x,y)\frac{\abs{f(y)}^2}{q(y)}\,dy.
\end{aligned}
$$
Integrating in $x$ and using Tonelli's theorem gives [@Fol13]
$$
\begin{aligned}
\norm{Tf}_2^2
&\le \alpha
\int_{\RR^n} p(x)
\int_{\RR^n}K(x,y)\frac{\abs{f(y)}^2}{q(y)}\,dy\,dx\\
&=\alpha
\int_{\RR^n}\frac{\abs{f(y)}^2}{q(y)}
\left(\int_{\RR^n}p(x)K(x,y)\,dx\right)dy\\
&\le \alpha\beta\int_{\RR^n}\abs{f(y)}^2\,dy
=\alpha\beta\norm{f}_2^2.
\end{aligned}
$$
Taking square roots yields
$$
\norm{Tf}_{L^2}\le \sqrt{\alpha\beta}\,\norm{f}_{L^2}.
$$
:::

:::

:::
:::
