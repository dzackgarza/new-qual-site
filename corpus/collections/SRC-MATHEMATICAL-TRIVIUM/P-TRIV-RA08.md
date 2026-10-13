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
Find local minima and local maxima of the function $f ( x , y ) = x y \log ( x ^ { 2 } + y ^ { 2 } )$ $( x , y ) \neq ( 0 , 0 )$
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

<1>1. In the variables $(s,\theta)$,
$$
f
=
\frac12 s\log s\,\sin2\theta.
$$

::: {.proof}
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

<1>2. The first derivatives are
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

::: {.proof}
Differentiate the expression from step <1>1.
:::

<1>3. If
$$
\sin2\theta=0,
$$
then a critical point requires
$$
s=1.
$$

::: {.proof}
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

<1>4. Thus four critical points are
$$
(\pm1,0),
\qquad
(0,\pm1).
$$

::: {.proof}
The condition $s=1$ gives $r=1$, while
$$
\sin2\theta=0
$$
means $\theta$ is a multiple of $\pi/2$.
:::

<1>5. If
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

::: {.proof}
Since $\sin2\theta\neq0$, the equation $f_s=0$ from step <1>2 gives
$$
\log s+1=0,
$$
so $s=e^{-1}$. Then $s\log s\neq0$, so $f_\theta=0$ forces
$$
\cos2\theta=0.
$$
:::

<1>6. Put
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

::: {.proof}
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

<1>7. The second derivatives in $(s,\theta)$ are
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

::: {.proof}
Differentiate the formulas in step <1>2.
:::

<1>8. At the points $(a,a)$ and $(-a,-a)$, the Hessian in $(s,\theta)$ is
positive definite.

::: {.proof}
At these points,
$$
s=e^{-1},
\qquad
\sin2\theta=1,
\qquad
\cos2\theta=0.
$$
Thus step <1>7 gives
$$
f_{ss}=\frac e2>0,
\qquad
f_{s\theta}=0,
\qquad
f_{\theta\theta}=\frac2e>0.
$$
:::

<1>9. Hence $(a,a)$ and $(-a,-a)$ are local minima, with value
$$
\boxed{-\frac1{2e}}.
$$

::: {.proof}
The coordinate change $(x,y)\leftrightarrow(s,\theta)$ is locally smooth and
invertible away from the origin, so the positive-definite Hessian in step
<1>8 gives local minima. At either point,
$$
xy=\frac1{2e}
$$
and
$$
\log(x^2+y^2)=\log(e^{-1})=-1.
$$
:::

<1>10. At the points $(a,-a)$ and $(-a,a)$, the Hessian is negative definite.

::: {.proof}
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

<1>11. Hence $(a,-a)$ and $(-a,a)$ are local maxima, with value
$$
\boxed{\frac1{2e}}.
$$

::: {.proof}
Step <1>10 gives negative-definite Hessian. At these points
$$
xy=-\frac1{2e}
$$
and the logarithmic factor is $-1$, so the product is $1/(2e)$.
:::

<1>12. The four axis critical points from step <1>4 are saddle points.

::: {.proof}
At $s=1$ and $\sin2\theta=0$, step <1>7 gives
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

<1>13. Therefore the complete list of local extrema is
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

::: {.proof}
Steps <1>9 and <1>11 classify the four non-axis critical points, while step
<1>12 shows the remaining critical points are not extrema.
:::

<1>14. Q.E.D.

::: {.proof}
Step <1>13 gives all local minima and maxima.
:::
:::
