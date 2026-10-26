---
schema: qual/card@1
id: P-TIE-F09-19
kind: problem
title: 'Hadamard''s example: ill-posedness of the Cauchy problem for Laplace''s equation'
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2009, question 19.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Part (2) corrected to lim sup as printed under Fall 2009, question 19, of Questions_from_Tie.pdf.
---

::: {.problem}
(1) Show that the function $u=u(x,y)$ given by
\[
u(x,y)=\frac{e^{ny}-e^{-ny}}{2n^2}\sin nx\qquad\text{for }n\in\mathbb{N}
\]
is the solution on $D=\{(x,y)\mid x^2+y^2<1\}$ of the Cauchy problem for the Laplace equation
\[
\frac{\partial^2u}{\partial x^2}+\frac{\partial^2u}{\partial y^2}=0,\qquad u(x,0)=0,\qquad\frac{\partial u}{\partial y}(x,0)=\frac{\sin nx}{n}.
\]

(2) Show that there exist points $(x,y)\in D$ such that $\limsup_{n\to\infty}|u(x,y)|=\infty$.
:::

Write
$$
u_n(x,y)
=
\frac{e^{ny}-e^{-ny}}{2n^2}\sin(nx).
$$

::: pf

::: pf-step

The second derivative with respect to $x$ is
$$
\frac{\partial^2u_n}{\partial x^2}
=
-\frac{e^{ny}-e^{-ny}}2\sin(nx).
$$


::: pf-proof

Differentiate twice:
$$
\frac{\partial u_n}{\partial x}
=
\frac{e^{ny}-e^{-ny}}{2n}\cos(nx),
$$
and therefore
$$
\frac{\partial^2u_n}{\partial x^2}
=
-\frac{e^{ny}-e^{-ny}}2\sin(nx).
$$

:::

:::

::: pf-step

The second derivative with respect to $y$ is
$$
\frac{\partial^2u_n}{\partial y^2}
=
\frac{e^{ny}-e^{-ny}}2\sin(nx).
$$


::: pf-proof

First,
$$
\frac{\partial u_n}{\partial y}
=
\frac{e^{ny}+e^{-ny}}{2n}\sin(nx).
$$
Differentiating once more gives
$$
\frac{\partial^2u_n}{\partial y^2}
=
\frac{e^{ny}-e^{-ny}}2\sin(nx).
$$

:::

:::

::: pf-step

The function $u_n$ satisfies the Laplace equation on $D$:
$$
\boxed{
\frac{\partial^2u_n}{\partial x^2}
+
\frac{\partial^2u_n}{\partial y^2}
=0
}.
$$


::: pf-proof

The expressions in steps <1>1 and <1>2 cancel.

:::

:::

::: pf-step

On $y=0$, the Cauchy data are
$$
\boxed{
u_n(x,0)=0,
\qquad
\frac{\partial u_n}{\partial y}(x,0)=\frac{\sin(nx)}n
}.
$$


::: pf-proof

Substituting $y=0$ into the formula for $u_n$ gives
$$
u_n(x,0)
=
\frac{1-1}{2n^2}\sin(nx)
=0.
$$
Using the first $y$-derivative from step <1>2 gives
$$
\frac{\partial u_n}{\partial y}(x,0)
=
\frac{1+1}{2n}\sin(nx)
=
\frac{\sin(nx)}n.
$$

:::

:::

::: pf-step

The point
$$
(x,y)=\left(\frac\pi6,\frac12\right)
$$
lies in $D$.


::: pf-proof

One has
$$
x^2+y^2
=
\frac{\pi^2}{36}+\frac14
<1.
$$
Indeed, this inequality is equivalent to $\pi^2<27$.

:::

:::

::: pf-step

Along the subsequence
$$
n=12k+3,
$$
one has
$$
\left|
\sin\left(\frac{n\pi}{6}\right)
\right|
=1.
$$


::: pf-proof

For $n=12k+3$,
$$
\frac{n\pi}{6}
=
2k\pi+\frac\pi2,
$$
whose sine is $1$.

:::

:::

::: pf-step

At the point from step <1>5,
$$
\limsup_{n\to\infty}|u_n(x,y)|=\boxed{\infty}.
$$


::: pf-proof

Along the subsequence from step <1>6,
$$
\begin{aligned}
\left|
u_n\left(\frac\pi6,\frac12\right)
\right|
&=
\frac{e^{n/2}-e^{-n/2}}{2n^2}
\left|
\sin\left(\frac{n\pi}{6}\right)
\right|\\
&=
\frac{e^{n/2}-e^{-n/2}}{2n^2}.
\end{aligned}
$$
The last expression tends to $\infty$, because exponential growth dominates the polynomial
$n^2$. Hence the limsup over all $n$ is infinite.

:::

:::

::: pf-qed

Steps <1>1--<1>4 prove part (1), and steps <1>5--<1>7 prove part (2).

:::

:::
