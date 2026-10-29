---
schema: qual/card@1
id: P-YPKW5
kind: problem
title: 'Real differentiability: definition, partials without differentiability, and
  real but nowhere complex differentiability'
classification:
  areas:
  - complex-analysis
  topics:
  - Calculus
  - Cauchy-Riemann
  - Counterexamples
relations: []
review: draft
audit:
- event: source-corrected
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Part (a) read "real-differentiable a point"; corrected to "real-differentiable at a point".'
---

::: {.problem}
(a) Complete this definition: "$f: \RR^n\to \RR^m$ is real-differentiable at a point $p\in \RR^n$ iff there exists a linear transformation..."

(b) Give an example of a function $f:\RR^2\to \RR$ whose first-order partial derivatives exist everywhere but $f$ is not differentiable at $(0, 0)$.

(c) Give an example of a function $f: \RR^2 \to \RR$ which is real-differentiable everywhere but nowhere complex-differentiable.
:::

::: {.solution}

::: pf

::: pf-step
(a) $f$ is real-differentiable at $p$ if and only if there is a linear map $L:\RR^n\to\RR^m$ with
$$
\lim_{h\to0}\frac{\norm{f(p+h)-f(p)-Lh}}{\norm{h}}=0.
$$

::: pf-proof
This is the definition; such an $L$ is unique and is the derivative $Df(p)$.
:::

:::

::: pf-step
(b) The function $f(x,y)=\dfrac{x^3}{x^2+y^2}$ for $(x,y)\ne(0,0)$, $f(0,0)=0$, has first partial derivatives everywhere and is not differentiable at $(0,0)$.

::: pf-proof
Away from the origin $f$ is smooth. At the origin, $f(x,0)=x$ and $f(0,y)=0$, so $f_x(0,0)=1$ and $f_y(0,0)=0$.
If $f$ were differentiable there, its derivative would be $L(x,y)=x$. Along $y=x$, $f(x,x)-L(x,x)=\frac{x}{2}-x=-\frac{x}{2}$, and $\abs{-x/2}/(\sqrt2\abs{x})=1/(2\sqrt2)$ does not tend to $0$.
:::

:::

::: pf-step
(c) Under $\RR^2\cong\CC$, the function $f(x,y)=x=\Re z$ is real-differentiable everywhere and nowhere complex-differentiable.

::: pf-proof
$f$ is real-linear, hence real-differentiable everywhere. Its real and imaginary parts are $u=x$ and $v=0$, and the Cauchy--Riemann equation $u_x=v_y$ would require $1=0$ at every point.
:::

:::

:::

:::
