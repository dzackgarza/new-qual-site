---
schema: qual/card@1
id: P-TIE-S15-32
kind: problem
title: $\int_0^\infty\frac{x^{a-1}}{1+x^n}\,dx$ and $\int_0^\infty\frac{\log x}{(1+x^2)^2}\,dx$
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2015, question 32.
---

::: {.problem}
Compute the following integrals.
(i) $\int _ { 0 } ^ { \infty } { \frac { x ^ { a - 1 } } { 1 + x ^ { n } } } d x , 0 < a < n$

$$
{ \mathrm { ( i i ) } } \int _ { 0 } ^ { \infty } { \frac { \log x } { ( 1 + x ^ { 2 } ) ^ { 2 } } } d x
$$
:::

::: pf

::: pf-step

For $0<a<n$,
$$
\boxed{
\int_0^\infty
\frac{x^{a-1}}{1+x^n}\,dx
=
\frac{\pi}{n}
\csc\frac{\pi a}{n}.
}
$$


::: pf-proof

Set $t=x^n$. Then
$$
dx=\frac1n t^{1/n-1}\,dt,
$$
so
$$
\int_0^\infty
\frac{x^{a-1}}{1+x^n}\,dx
=
\frac1n
\int_0^\infty
\frac{t^{a/n-1}}{1+t}\,dt.
$$
Because $0<a/n<1$,
$$
\int_0^\infty
\frac{t^{a/n-1}}{1+t}\,dt
=
\Gamma\left(\frac an\right)
\Gamma\left(1-\frac an\right)
=
\frac{\pi}{\sin(\pi a/n)}
$$
by Euler's beta integral and the reflection formula. Multiplying by $1/n$ gives the result.

:::

:::

::: pf-step

Define, for $0<s<4$,
$$
J(s)
\coloneqq
\int_0^\infty
\frac{x^{s-1}}{(1+x^2)^2}\,dx.
$$
Then
$$
J(s)
=
\frac{\pi(2-s)}
{4\sin(\pi s/2)}.
$$


::: pf-proof

With $t=x^2$,
$$
\begin{aligned}
J(s)
&=
\frac12
\int_0^\infty
\frac{t^{s/2-1}}{(1+t)^2}\,dt\\
&=
\frac12
B\left(\frac s2,2-\frac s2\right)\\
&=
\frac12
\Gamma\left(\frac s2\right)
\Gamma\left(2-\frac s2\right).
\end{aligned}
$$
Using
$$
\Gamma\left(2-\frac s2\right)
=
\left(1-\frac s2\right)
\Gamma\left(1-\frac s2\right)
$$
and the reflection formula gives
$$
J(s)
=
\frac{\pi(2-s)}
{4\sin(\pi s/2)}.
$$

:::

:::

::: pf-step

One has
$$
\boxed{
\int_0^\infty
\frac{\log x}{(1+x^2)^2}\,dx
=
-\frac\pi4.
}
$$


::: pf-proof

For $s$ near $1$, differentiation under the integral sign is justified by an integrable majorant for
$$
\frac{x^{s-1}\log x}{(1+x^2)^2}.
$$
Thus
$$
J'(1)
=
\int_0^\infty
\frac{\log x}{(1+x^2)^2}\,dx.
$$
Differentiating the closed form from step <1>2 and evaluating at $s=1$, where
$$
\cot\frac\pi2=0,
$$
gives
$$
J'(1)
=
-\frac\pi4.
$$

:::

:::

::: pf-qed

Step <1>1 proves part (i), and step <1>3 proves part (ii).

:::

:::
