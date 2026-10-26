---
schema: qual/card@1
id: P-TRIV-RA31
kind: problem
title: $\int_0^\infty e^{-ax}\frac{\sin xy}{x}\,dx$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 31, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Calculate $J ( y ) = \int _ { 0 } ^ { \infty } e ^ { - a x } \frac { \sin x y } { x } d x , a > 0 .$
:::

::: pf

::: pf-step

For each fixed $y\in\mathbb R$, the integral defining $J(y)$ converges.


::: pf-proof

Near $x=0$,
$$
\frac{\sin(xy)}{x}\longrightarrow y,
$$
so the integrand is bounded. For large $x$,
$$
\left|
e^{-ax}\frac{\sin(xy)}x
\right|
\leq
\frac{e^{-ax}}x,
$$
which is integrable because $a>0$.

:::

:::

::: pf-step

One may differentiate under the integral sign, obtaining
$$
J'(y)
=
\int_0^\infty e^{-ax}\cos(xy)\,dx.
$$


::: pf-proof

The derivative of the integrand with respect to $y$ is
$$
e^{-ax}\cos(xy).
$$
Its absolute value is bounded by $e^{-ax}$, whose integral on $[0,\infty)$ is
finite. Dominated convergence therefore justifies differentiation under the
integral sign.

:::

:::

::: pf-step

The Laplace integral in step <1>2 equals
$$
\frac{a}{a^2+y^2}.
$$


::: pf-proof

Using complex exponentials,
$$
\int_0^\infty e^{-ax}\cos(xy)\,dx
=
\operatorname{Re}
\int_0^\infty e^{-(a-iy)x}\,dx.
$$
Since $a>0$,
$$
\int_0^\infty e^{-(a-iy)x}\,dx
=
\frac1{a-iy}
=
\frac{a+iy}{a^2+y^2}.
$$
Taking real parts gives the result.

:::

:::

::: pf-step

Hence
$$
J'(y)=\frac{a}{a^2+y^2}.
$$


::: pf-proof

Combine steps <1>2--<1>3.

:::

:::

::: pf-step

One has
$$
J(0)=0.
$$


::: pf-proof

The integrand vanishes identically when $y=0$.

:::

:::

::: pf-step

Therefore
$$
\boxed{
J(y)=\arctan\frac ya.
}
$$


::: pf-proof

An antiderivative of
$$
\frac{a}{a^2+y^2}
$$
is
$$
\arctan\frac ya.
$$
Thus
$$
J(y)=\arctan\frac ya+C.
$$
Step <1>5 gives $C=0$.

:::

:::

::: pf-qed

Step <1>6 is the required value.

:::

:::
