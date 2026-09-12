---
schema: qual/card@1
id: P-RASP23C
kind: problem
title: "Multiplicative convolution on R_+"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 3 of the official UCSD Spring 2023 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $\mathbb{R}_+ = [0, \infty)$, $f, g \in L^1(\mathbb{R}_+, m)$, and consider
$$
h(x) = \int_0^\infty f(y) g\!\left(\frac{x}{y}\right) \frac{dy}{y}.
$$
Show that $h$ is well-defined (i.e., $y \mapsto f(y) g(x/y) / y$ is in $L^1(\mathbb{R}_+, m)$ for a.e. $x \in \mathbb{R}_+$), $h \in L^1(\mathbb{R}_+)$, and
$$
\|h\|_{L^1} \leq \|f\|_{L^1} \|g\|_{L^1}.
$$

Comment: You may use without proof that $g(x/y)$ is Lebesgue measurable on $\mathbb{R}_+^2$.
:::


::: solution
Consider the nonnegative measurable function
\[
K(x,y):=|f(y)|\,|g(x/y)|\,\frac1y
\]
on $(0,\infty)^2$; the value at $y=0$ is irrelevant. By Tonelli,
\[
\begin{aligned}
\int_0^\infty\int_0^\infty K(x,y)\,dy\,dx
&=\int_0^\infty |f(y)|\frac1y
  \left(\int_0^\infty |g(x/y)|\,dx\right)dy.
\end{aligned}
\]
For fixed $y>0$, put $u=x/y$, so $dx=y\,du$. Then
\[
\int_0^\infty |g(x/y)|\,dx
=y\int_0^\infty|g(u)|\,du
=y\|g\|_1.
\]
Therefore
\[
\int_0^\infty\int_0^\infty K(x,y)\,dy\,dx
=\|f\|_1\|g\|_1<\infty.
\]

Since the double integral is finite, Fubini--Tonelli implies that for almost every $x$,
\[
y\longmapsto f(y)g(x/y)/y
\]
belongs to $L^1(0,\infty)$. Hence $h(x)$ is well defined for almost every $x$.

Finally,
\[
\begin{aligned}
\|h\|_1
&=\int_0^\infty
\left|\int_0^\infty f(y)g(x/y)\frac{dy}{y}\right|dx\\
&\le\int_0^\infty\int_0^\infty
|f(y)|\,|g(x/y)|\frac{dy}{y}\,dx\\
&=\|f\|_1\|g\|_1.
\end{aligned}
\]
Thus
\[
\boxed{h\in L^1(\mathbb R_+),\qquad
\|h\|_1\le\|f\|_1\|g\|_1.}
\]
:::
