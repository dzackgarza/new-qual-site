---
schema: qual/card@1
id: P-TRIV-RA08
kind: problem
title: Local extrema of $xy\log(x^2+y^2)$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 8, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find local minima and local maxima of the function $f(x, y) = xy\log(x^2 + y^2)$, $(x, y) \neq (0, 0)$.
:::

::: {.solution}

Use polar coordinates
$$
x=r\cos\theta,
\qquad
y=r\sin\theta,
\qquad
r>0,
$$
and set
$$
s=r^2>0.
$$

::: pf

::: {.pf-step #s1-1}

In the variables $(s,\theta)$,
$$
f
=
\frac12 s\log s\,\sin2\theta.
$$


::: pf-proof

One has
$$
xy
=
r^2\cos\theta\sin\theta
=
\frac{s}{2}\sin2\theta,
$$
and
$$
\log(x^2+y^2)=\log r^2=\log s.
$$

:::

:::

::: {.pf-step #s1-2}

The first derivatives are
$$
f_s
=
\frac12(\log s+1)\sin2\theta
$$
and
$$
f_\theta
=
s\log s\,\cos2\theta.
$$


::: pf-proof

Differentiate the expression from step [](#s1-1){.pf-ref}.

:::

:::

::: pf-step

If
$$
\sin2\theta=0,
$$
then a critical point requires
$$
s=1.
$$


::: pf-proof

If $\sin2\theta=0$, then $f_s=0$ automatically. Also
$$
\cos2\theta=\pm1,
$$
so $f_\theta=0$ requires
$$
s\log s=0.
$$
Since $s>0$, this means $\log s=0$, hence $s=1$.

:::

:::

::: {.pf-step #s1-4}

Thus four critical points are
$$
(\pm1,0),
\qquad
(0,\pm1).
$$


::: pf-proof

The condition $s=1$ gives $r=1$, while
$$
\sin2\theta=0
$$
means $\theta$ is a multiple of $\pi/2$.

:::

:::

::: pf-step

If
$$
\sin2\theta\neq0,
$$
then a critical point requires
$$
s=e^{-1}
$$
and
$$
\cos2\theta=0.
$$


::: pf-proof

Since $\sin2\theta\neq0$, the equation $f_s=0$ from step [](#s1-2){.pf-ref} gives
$$
\log s+1=0,
$$
so $s=e^{-1}$. Then $s\log s\neq0$, so $f_\theta=0$ forces
$$
\cos2\theta=0.
$$

:::

:::

::: pf-step

Put
$$
a=\frac1{\sqrt{2e}}.
$$
The remaining four critical points are
$$
(a,a),
\quad
(-a,-a),
\quad
(a,-a),
\quad
(-a,a).
$$


::: pf-proof

The condition $s=e^{-1}$ gives
$$
r=e^{-1/2}.
$$
The condition $\cos2\theta=0$ means the point lies on one of the diagonals
$y=\pm x$. Hence
$$
x^2=y^2=\frac{r^2}{2}=\frac1{2e}.
$$

:::

:::

::: {.pf-step #s1-7}

The second derivatives in $(s,\theta)$ are
$$
f_{ss}
=
\frac{1}{2s}\sin2\theta,
$$
$$
f_{s\theta}
=
(\log s+1)\cos2\theta,
$$
and
$$
f_{\theta\theta}
=
-2s\log s\,\sin2\theta.
$$


::: pf-proof

Differentiate the formulas in step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

At the points $(a,a)$ and $(-a,-a)$, the Hessian in $(s,\theta)$ is
positive definite.


::: pf-proof

At these points,
$$
s=e^{-1},
\qquad
\sin2\theta=1,
\qquad
\cos2\theta=0.
$$
Thus step [](#s1-7){.pf-ref} gives
$$
f_{ss}=\frac e2>0,
\qquad
f_{s\theta}=0,
\qquad
f_{\theta\theta}=\frac2e>0.
$$

:::

:::

::: {.pf-step #s1-9}

Hence $(a,a)$ and $(-a,-a)$ are local minima, with value
$$
\boxed{-\frac1{2e}}.
$$


::: pf-proof

The coordinate change $(x,y)\leftrightarrow(s,\theta)$ is locally smooth and
invertible away from the origin, so the positive-definite Hessian in step
[](#s1-8){.pf-ref} gives local minima. At either point,
$$
xy=\frac1{2e}
$$
and
$$
\log(x^2+y^2)=\log(e^{-1})=-1.
$$

:::

:::

::: {.pf-step #s1-10}

At the points $(a,-a)$ and $(-a,a)$, the Hessian is negative definite.


::: pf-proof

Now
$$
\sin2\theta=-1,
$$
while $s=e^{-1}$ and $\cos2\theta=0$. Thus
$$
f_{ss}=-\frac e2<0,
\qquad
f_{s\theta}=0,
\qquad
f_{\theta\theta}=-\frac2e<0.
$$

:::

:::

::: {.pf-step #s1-11}

Hence $(a,-a)$ and $(-a,a)$ are local maxima, with value
$$
\boxed{\frac1{2e}}.
$$


::: pf-proof

Step [](#s1-10){.pf-ref} gives negative-definite Hessian. At these points
$$
xy=-\frac1{2e}
$$
and the logarithmic factor is $-1$, so the product is $1/(2e)$.

:::

:::

::: {.pf-step #s1-12}

The four axis critical points from step [](#s1-4){.pf-ref} are saddle points.


::: pf-proof

At $s=1$ and $\sin2\theta=0$, step [](#s1-7){.pf-ref} gives
$$
f_{ss}=0,
\qquad
f_{\theta\theta}=0,
$$
while
$$
f_{s\theta}=\cos2\theta=\pm1.
$$
Thus the Hessian matrix is
$$
\begin{pmatrix}
0&\pm1\\
\pm1&0
\end{pmatrix},
$$
whose determinant is $-1<0$. Hence the critical point is a saddle.

:::

:::

::: {.pf-step #s1-13}

Therefore the complete list of local extrema is
$$
\boxed{
\begin{aligned}
\text{local minima: }&(a,a),(-a,-a),\\
\text{local maxima: }&(a,-a),(-a,a),
\end{aligned}
\qquad
a=\frac1{\sqrt{2e}}.
}
$$


::: pf-proof

Steps [](#s1-9){.pf-ref} and [](#s1-11){.pf-ref} classify the four non-axis critical points, while step
[](#s1-12){.pf-ref} shows the remaining critical points are not extrema.

:::

:::

::: pf-qed

Step [](#s1-13){.pf-ref} gives all local minima and maxima.

:::

:::

:::
