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
Let $Tf(x) = \int_{\mathbb{R}^n} K(x,y) f(y) \, dy$, where $K(x,y)$ is a nonnegative measurable function on $\mathbb{R}^n \times \mathbb{R}^n$.
Suppose that there are measurable functions $p(x) > 0$ and $q(x) > 0$ on $\mathbb{R}^n$ and real numbers $\alpha, \beta > 0$ for which

$$\int K(x,y) q(y) \, dy \leq \alpha p(x),$$

for almost all $x$ and

$$\int p(x) K(x,y) \, dx \leq \beta q(y)$$

for almost all $y$.
Show that for $f \in L^2(\mathbb{R}^n)$ we have

$$\|Tf\|_{L^2} \leq \sqrt{\alpha \beta} \|f\|_{L^2}.$$

(This is called Schur's test.)
:::

::: {.solution}
Let $f\in L^2(\mathbb R^n)$.

<1>1. The integral defining $Tf$ converges absolutely almost everywhere.
::: {.proof}
Set
$$
B(x)=\int_{\mathbb R^n}K(x,y)\frac{|f(y)|^2}{q(y)}\,dy.
$$
This is a nonnegative measurable function, possibly
initially infinite. Tonelli and the second kernel inequality
give [@Fol13]
$$
\begin{aligned}
\int_{\mathbb R^n}p(x)B(x)\,dx
&=\int_{\mathbb R^n}\frac{|f(y)|^2}{q(y)}
\left(\int_{\mathbb R^n}p(x)K(x,y)\,dx\right)dy\\
&\leq\beta\int_{\mathbb R^n}|f(y)|^2\,dy<\infty.
\end{aligned}
$$
Since $p(x)>0$, this implies $B(x)<\infty$ almost
everywhere. The first kernel inequality also gives
$A(x):=\int K(x,y)q(y)\,dy\leq\alpha p(x)<\infty$
for almost every $x$. For points where both bounds hold,
Cauchy–Schwarz applied to
$K^{1/2}q^{1/2}$ and $K^{1/2}|f|q^{-1/2}$ yields
$$
\int K(x,y)|f(y)|\,dy\leq A(x)^{1/2}B(x)^{1/2}<\infty
$$
[@Fol13]. Thus $Tf$ is defined almost everywhere, and
the usual parameter-integral measurability follows by
Tonelli applied to positive and negative real and imaginary
parts. Set $Tf=0$ on the exceptional null set.
:::

<1>2. The same weighted inequality gives the claimed norm bound.
::: {.proof}
For almost every $x$, Cauchy–Schwarz in the $y$ variable gives
\[
\begin{aligned}
|Tf(x)|^2
&=\left|\int K(x,y)^{1/2}q(y)^{1/2}
\,K(x,y)^{1/2}q(y)^{-1/2}f(y)\,dy\right|^2\\
&\le
\left(\int K(x,y)q(y)\,dy\right)
\left(\int K(x,y)\frac{|f(y)|^2}{q(y)}\,dy\right)\\
&\le \alpha p(x)
\int K(x,y)\frac{|f(y)|^2}{q(y)}\,dy.
\end{aligned}
\]
Integrating in $x$ and using Tonelli's theorem gives [@Fol13]
\[
\begin{aligned}
\|Tf\|_2^2
&\le \alpha
\int_{\mathbb R^n} p(x)
\int_{\mathbb R^n}K(x,y)\frac{|f(y)|^2}{q(y)}\,dy\,dx\\
&=\alpha
\int_{\mathbb R^n}\frac{|f(y)|^2}{q(y)}
\left(\int_{\mathbb R^n}p(x)K(x,y)\,dx\right)dy\\
&\le \alpha\beta\int_{\mathbb R^n}|f(y)|^2\,dy
=\alpha\beta\|f\|_2^2.
\end{aligned}
\]
Taking square roots yields
\[
\|Tf\|_{L^2}\le \sqrt{\alpha\beta}\,\|f\|_{L^2}.
\]
:::
:::
