---
schema: qual/card@1
id: P-WESCA04-E2
kind: problem
title: "Cauchy–Riemann equations everywhere do not imply analyticity"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis section 1.2, item 2 (August 2, 2004) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
Define
\[
f(z)=
\begin{cases}
e^{-1/z^4},&z\ne0,\\
0,&z=0.
\end{cases}
\]
The source states that $f$ satisfies the Cauchy–Riemann equations at every point of $\mathbb C$ but is not analytic.
Explain how this is possible.
:::

Write
\[
f=u+iv.
\]

::: pf

::: pf-step

At every point
\[
z\ne0,
\]
the function $f$ is holomorphic and therefore satisfies the
Cauchy--Riemann equations.


::: pf-proof

On
\[
\mathbb C\setminus\{0\},
\]
the function
\[
z\longmapsto -\frac1{z^4}
\]
is holomorphic, and the exponential function is entire. Their composition
\[
e^{-1/z^4}
\]
is therefore holomorphic there.

Every holomorphic function satisfies the Cauchy--Riemann equations.

:::

:::

::: pf-step

Along the real axis,
\[
f(x)=e^{-1/x^4}
\qquad
(x\ne0),
\]
and
\[
\lim_{x\to0}
\frac{f(x)-f(0)}{x}
=
0.
\]


::: pf-proof

For $x\ne0$,
\[
\left|
\frac{f(x)}x
\right|
=
\frac{e^{-1/x^4}}{|x|}.
\]
Set
\[
t=\frac1{x^4}.
\]
Then $t\to\infty$ as $x\to0$, and
\[
\frac{e^{-1/x^4}}{|x|}
=
t^{1/4}e^{-t}
\longrightarrow
0.
\]
Exponential decay dominates every power, proving the limit.

:::

:::

::: pf-step

Along the imaginary axis,
\[
f(iy)=e^{-1/y^4}
\qquad
(y\ne0),
\]
and
\[
\lim_{y\to0}
\frac{f(iy)-f(0)}{y}
=
0.
\]


::: pf-proof

Since
\[
(iy)^4=y^4,
\]
one has
\[
f(iy)=e^{-1/y^4},
\]
which is real.

Exactly as in step <1>2,
\[
\frac{e^{-1/y^4}}{|y|}
\longrightarrow0.
\]

:::

:::

::: pf-step

All four first partial derivatives of $u$ and $v$ exist at the
origin and satisfy
\[
u_x(0,0)
=
u_y(0,0)
=
v_x(0,0)
=
v_y(0,0)
=
0.
\]


::: pf-proof

Along the real axis,
\[
v(x,0)=0
\]
because $f(x)$ is real. Step <1>2 therefore gives
\[
u_x(0,0)=0,
\qquad
v_x(0,0)=0.
\]

Along the imaginary axis,
\[
v(0,y)=0
\]
because $f(iy)$ is real. Step <1>3 therefore gives
\[
u_y(0,0)=0,
\qquad
v_y(0,0)=0.
\]

:::

:::

::: pf-step

Hence the Cauchy--Riemann equations hold at the origin:
\[
u_x(0,0)=v_y(0,0),
\qquad
u_y(0,0)=-v_x(0,0).
\]


::: pf-proof

By step <1>4, both sides of both equations are zero.

:::

:::

::: pf-step

Nevertheless, $f$ is not continuous at the origin.


::: pf-proof

Approach the origin along the ray
\[
z
=
r e^{i\pi/4},
\qquad
r>0.
\]
Then
\[
z^4
=
r^4e^{i\pi}
=
-r^4.
\]
Therefore
\[
-\frac1{z^4}
=
\frac1{r^4},
\]
and hence
\[
f\left(re^{i\pi/4}\right)
=
e^{1/r^4}
\longrightarrow
+\infty
\qquad
(r\downarrow0).
\]
But
\[
f(0)=0.
\]
Thus $f$ is not continuous at $0$.

:::

:::

::: pf-step

Consequently $f$ is not complex differentiable at the origin and
is not analytic on $\mathbb C$.


::: pf-proof

Complex differentiability at a point implies continuity at that point.
Step <1>6 shows that $f$ is not continuous at $0$, so it cannot be complex
differentiable there.

Hence $f$ is not holomorphic on any neighborhood of $0$ and therefore is
not analytic on all of $\mathbb C$.

:::

:::

::: pf-step

The example is possible because the Cauchy--Riemann equations at a
point, by themselves, do not imply complex differentiability there.


::: pf-proof

Steps <1>1 and <1>5 show that the Cauchy--Riemann equations hold at every
point. Step <1>7 shows that complex differentiability nevertheless fails at
$0$.

The usual converse theorem requires additional regularity, for example
continuity of the first partial derivatives in a neighborhood. Those
hypotheses fail here dramatically because the function itself is not
continuous at the origin.

:::

:::

::: pf-qed

Step <1>8 explains exactly why there is no contradiction.

:::

:::
