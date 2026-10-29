---
schema: qual/card@1
id: P-HKZVN
kind: problem
title: "Separate measurability and section functions of a measurable function of two variables"
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Product Measures
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Question 1.2 of the JHU Spring 2019 Analysis Qualifying Exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Question 1.2. Fix a measurable function $f : \RR ^ { 2 }$ R and, for every $x , y \in \RR ,$ , let

$$
f _ { x } : \RR \to \RR a n d f _ { y } : \RR \to \RR
$$

be given by $f _ { x } ( z ) = f ( x , z )$ and $f _ { y } ( z ) = f ( z , y )$ . Show that there exists such an f so that $f _ { x } \in L ^ { 1 } ( \RR )$ for a.e. x and $f _ { y } \in L ^ { 1 } ( \RR )$ for a.e. y but

$$
\int _ { \RR } \left( \int _ { \RR } f _ { x } ( y ) d y \right) d x \neq \int _ { \RR } \left( \int _ { \RR } f _ { y } ( x ) d x \right) d y .
$$

What does Fubini’s theorem imply about such $f ?$ What about Tonelli’s theorem?
:::

::: {.solution}

::: pf

::: pf-step

Define a measurable function with conditionally convergent iterated integrals.

::: pf-proof

Set
$$
f(x,y)=
\mathbf1_{(0,1)^2}(x,y)
\frac{x^2-y^2}{(x^2+y^2)^2},
$$
and define $f=0$ on the coordinate axes. This is measurable on $\RR^2$.

For each fixed $x\in(0,1)$,
$$
\frac{x^2-y^2}{(x^2+y^2)^2}
=\frac{d}{dy}\left(\frac{y}{x^2+y^2}\right),
$$
so
$$
\int_{\RR}f_x(y)\,dy
=\int_0^1\frac{x^2-y^2}{(x^2+y^2)^2}\,dy
=\frac1{1+x^2}.
$$
Thus $f_x\in L^1(\RR)$ for every $x\ne0$.

For each fixed $y\in(0,1)$,
$$
\frac{x^2-y^2}{(x^2+y^2)^2}
=-\frac{d}{dx}\left(\frac{x}{x^2+y^2}\right),
$$
hence
$$
\int_{\RR}f_y(x)\,dx
=-\frac1{1+y^2}.
$$
Thus $f_y\in L^1(\RR)$ for every $y\ne0$.

:::

:::

::: pf-step

Compute the two iterated integrals.

::: pf-proof

Therefore
$$
\int_{\RR}\left(\int_{\RR}f_x(y)\,dy\right)dx
=\int_0^1\frac{dx}{1+x^2}
=\frac\pi4,
$$
whereas
$$
\int_{\RR}\left(\int_{\RR}f_y(x)\,dx\right)dy
=-\int_0^1\frac{dy}{1+y^2}
=-\frac\pi4.
$$
Hence the iterated integrals exist but are unequal.

:::

:::

::: pf-step

Explain what Fubini and Tonelli imply.

::: pf-proof

Fubini's theorem says that if $f\in L^1(\RR^2)$, then the two iterated integrals must agree. Since they do not, this example necessarily satisfies
$$
f\notin L^1(\RR^2).
$$

This can also be seen directly from Tonelli's theorem applied to $|f|$. In polar coordinates in the first quadrant,
$$
|f(r\cos\theta,r\sin\theta)|
=\frac{|\cos(2\theta)|}{r^2}.
$$
On any angular subinterval where $|\cos(2\theta)|\ge c>0$, the contribution near $r=0$ is bounded below by a positive constant times
$$
\int_0^\varepsilon\frac{dr}{r}=\infty.
$$
Hence
$$
\iint_{\RR^2}|f(x,y)|\,dx\,dy=\infty.
$$
So Tonelli confirms that absolute integrability fails, exactly as required for the two iterated integrals to differ.

:::

:::

:::

:::
