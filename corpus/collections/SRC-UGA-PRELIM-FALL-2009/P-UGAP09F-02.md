---
schema: qual/card@1
id: P-UGAP09F-02
kind: problem
title: Three calculus computations involving differentiation, Taylor series, and a triple integral
classification:
  areas: [prelim]
  topics:
  - Differentiation
  - Taylor Series
  - Multivariable Calculus
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Work the following calculus problems.

(a) Compute the derivative of
$$
f(x)=\sec^3\!\bigl(\tan(x^2)\bigr).
$$

(b) Find the Taylor expansion for $f(x)=\ln x$ about $a=2$, and determine its radius of convergence.

(c) Set up, but do not evaluate, the triple integral needed to compute the integral of
$$
f(x,y,z)=x\sin(y+z)
$$
over the region
$$
R=\{(x,y,z)\in\RR^3:x\ge0,\ y+z\ge2,\ x^2+y^2+z^2\le4\}.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For part (a),
$$
\boxed{
f'(x)=6x\sec^3\!\bigl(\tan(x^2)\bigr)
\tan\!\bigl(\tan(x^2)\bigr)\sec^2(x^2).
}
$$


::: pf-proof

Set $g(x)=\tan(x^2)$. Then
$$
g'(x)=2x\sec^2(x^2).
$$
Since $f(x)=\sec^3(g(x))$, the chain rule gives
$$
\begin{aligned}
f'(x)
&=3\sec^2(g(x))\bigl(\sec(g(x))\tan(g(x))\bigr)g'(x)\\
&=6x\sec^3\!\bigl(\tan(x^2)\bigr)
\tan\!\bigl(\tan(x^2)\bigr)\sec^2(x^2).
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-2}

For part (b), the Taylor expansion about $a=2$ is
$$
\boxed{
\ln x
=\ln 2+
\sum_{n=1}^{\infty}
\frac{(-1)^{n+1}}{n}
\left(\frac{x-2}{2}\right)^n,
\qquad \abs{x-2}<2,
}
$$
and its radius of convergence is $\boxed{2}$.


::: pf-proof

Write
$$
\ln x
=\ln 2+\ln\!\left(1+\frac{x-2}{2}\right).
$$
For $\abs{u}<1$,
$$
\ln(1+u)=\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}u^n.
$$
Substituting $u=(x-2)/2$ gives the displayed expansion. For the $n$th term of the resulting power series, the ratio of successive absolute values tends to
$$
\frac{\abs{x-2}}{2}.
$$
Hence the series converges for $\abs{x-2}<2$ and diverges for $\abs{x-2}>2$, so its radius of convergence is $2$.

:::

:::

::: {.pf-step #s1-3}

For part (c), one suitable iterated integral is
$$
\boxed{
\int_0^2
\int_{2-y}^{\sqrt{4-y^2}}
\int_0^{\sqrt{4-y^2-z^2}}
x\sin(y+z)\,dx\,dz\,dy.
}
$$


::: pf-proof

Project $R$ onto the $yz$-plane. The conditions there are
$$
y^2+z^2\le4,
\qquad
y+z\ge2.
$$
The line $z=2-y$ meets the circle $y^2+z^2=4$ at $(0,2)$ and $(2,0)$. Therefore the projected region is described by
$$
0\le y\le2,
\qquad
2-y\le z\le\sqrt{4-y^2}.
$$
For such $(y,z)$, the remaining conditions $x\ge0$ and $x^2+y^2+z^2\le4$ give
$$
0\le x\le\sqrt{4-y^2-z^2}.
$$
Using these three bounds with the integrand $x\sin(y+z)$ gives the displayed iterated integral.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} answers part (a), step [](#s1-2){.pf-ref} answers part (b), and step [](#s1-3){.pf-ref} answers part (c).

:::

:::

:::
