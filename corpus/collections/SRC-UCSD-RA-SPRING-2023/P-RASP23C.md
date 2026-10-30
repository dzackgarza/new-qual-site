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

::: {.problem}
Let $\RR_+ = [0, \infty)$, $f, g \in L^1(\RR_+, m)$, and consider
$$
h(x) = \int_0^\infty f(y) g\!\left(\frac{x}{y}\right) \frac{dy}{y}.
$$
Show that $h$ is well-defined (i.e., $y \mapsto f(y) g(x/y) / y$ is in $L^1(\RR_+, m)$ for a.e. $x \in \RR_+$), $h \in L^1(\RR_+)$, and
$$
\norm{h}_{L^1} \leq \norm{f}_{L^1} \norm{g}_{L^1}.
$$

Comment: You may use without proof that $g(x/y)$ is Lebesgue measurable on $\RR_+^2$.
:::


::: {.solution}
Consider the nonnegative measurable function
$$
K(x,y):=\abs{f(y)}\,\abs{g(x/y)}\,\frac1y
$$
on $(0,\infty)^2$; the value at $y=0$ is irrelevant. By Tonelli,
$$
\begin{aligned}
\int_0^\infty\int_0^\infty K(x,y)\,dy\,dx
&=\int_0^\infty \abs{f(y)}\frac1y
  \left(\int_0^\infty \abs{g(x/y)}\,dx\right)dy.
\end{aligned}
$$
For fixed $y>0$, put $u=x/y$, so $dx=y\,du$. Then
$$
\int_0^\infty \abs{g(x/y)}\,dx
=y\int_0^\infty\abs{g(u)}\,du
=y\norm{g}_1.
$$
Therefore
$$
\int_0^\infty\int_0^\infty K(x,y)\,dy\,dx
=\norm{f}_1\norm{g}_1<\infty.
$$

Since the double integral is finite, Fubini--Tonelli implies that for almost every $x$,
$$
y\longmapsto f(y)g(x/y)/y
$$
belongs to $L^1(0,\infty)$. Hence $h(x)$ is well defined for almost every $x$.

Finally,
$$
\begin{aligned}
\norm{h}_1
&=\int_0^\infty
\abs{\int_0^\infty f(y)g(x/y)\frac{dy}{y}}dx\\
&\le\int_0^\infty\int_0^\infty
\abs{f(y)}\,\abs{g(x/y)}\frac{dy}{y}\,dx\\
&=\norm{f}_1\norm{g}_1.
\end{aligned}
$$
Thus
$$
\boxed{h\in L^1(\RR_+),\qquad
\norm{h}_1\le\norm{f}_1\norm{g}_1.}
$$
:::
