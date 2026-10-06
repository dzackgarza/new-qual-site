---
schema: qual/card@1
id: P-UCLARA15F-11
kind: problem
title: Phragmén--Lindelöf principle for subharmonic functions in the quadrant
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the retained UCLA Analysis Qualifying Exam Solutions compendium, Fall 2015 section; the official exam PDF is image-only.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retranscribed the font-garbled statement in LaTeX from Problem 11 on page 2 of the official analysis-15F.pdf exam, checked against the Fall 2015 section of UCLA_Solutions.pdf.
---

::: {.problem}
Let $\Omega = \{(x,y) \in \mathbb{R}^2 ; x > 0, y > 0\}$ and let $u$ be subharmonic in $\Omega$, continuous in $\overline{\Omega}$, such that
\[
u(x,y) \leq |x + iy|,
\]
for large $(x,y) \in \Omega$. Assume that
\[
u(x,0) \leq ax, \quad u(0,y) \leq by, \quad x, y \geq 0,
\]
for some $a, b > 0$. Show that
\[
u(x,y) \leq ax + by, \quad (x,y) \in \Omega.
\]
:::

::: {.solution}
Set
\[
v(x,y)=u(x,y)-ax-by.
\]

<1>1. The function \(v\) is subharmonic in \(\Omega\) and continuous on \(\overline\Omega\).

::: {.proof}
The function \(u\) is subharmonic, while
\[
(x,y)\longmapsto ax+by
\]
is harmonic. Subtracting a harmonic function preserves subharmonicity. Continuity is preserved as well.
:::

<1>2. On the boundary rays,
\[
\boxed{
v(x,0)\le0,
\qquad
v(0,y)\le0}.
\]

::: {.proof}
By hypothesis,
\[
u(x,0)\le ax
\]
and
\[
u(0,y)\le by.
\]
Subtract the corresponding linear terms.
:::

Choose once and for all a number
\[
p\in(1,2).
\]
Write
\[
z=x+iy=re^{i\theta},
\qquad
0\le\theta\le\frac{\pi}{2}.
\]

<1>3. Define
\[
\boxed{
h(r,\theta)
=
r^p
\cos\!\left(
p\left(\theta-\frac{\pi}{4}\right)
\right)}.
\]

::: {.proof}
This is the real part of the holomorphic branch
\[
e^{-ip\pi/4}z^p
\]
on the quadrant.
:::

<1>4. The function \(h\) is harmonic in \(\Omega\).

::: {.proof}
The quadrant is simply connected and does not meet the negative real axis after choosing a branch of \(z^p\). The real part of a holomorphic function is harmonic.
:::

<1>5. The function \(h\) is strictly positive on
\[
\overline\Omega\setminus\{0\}.
\]

::: {.proof}
For
\[
0\le\theta\le\frac{\pi}{2},
\]
one has
\[
-\frac{\pi}{4}
\le
\theta-\frac{\pi}{4}
\le
\frac{\pi}{4}.
\]
Hence
\[
\left|
p\left(\theta-\frac{\pi}{4}\right)
\right|
\le
\frac{p\pi}{4}
<
\frac{\pi}{2},
\]
because \(p<2\). Therefore the cosine factor is positive. Also \(r^p>0\) for \(r>0\).
:::

<1>6. More precisely, there is a constant
\[
c_p>0
\]
such that
\[
\boxed{
h(r,\theta)\ge c_p r^p}
\]
throughout the closed quadrant.

::: {.proof}
Take
\[
c_p
=
\cos\frac{p\pi}{4}>0.
\]
The minimum of
\[
\cos\!\left(
p(\theta-\pi/4)
\right)
\]
on \([0,\pi/2]\) is attained at the endpoints and equals \(c_p\).
:::

Fix
\[
\varepsilon>0
\]
and define
\[
\boxed{
v_\varepsilon
=
v-\varepsilon h}.
\]

<1>7. The function \(v_\varepsilon\) is subharmonic in \(\Omega\).

::: {.proof}
The function \(v\) is subharmonic by step <1>1, and \(h\) is harmonic by step <1>4. Subtracting \(\varepsilon h\) preserves subharmonicity.
:::

<1>8. On the two coordinate axes,
\[
\boxed{
v_\varepsilon\le0}.
\]

::: {.proof}
By step <1>2,
\[
v\le0
\]
on the axes, while by step <1>5,
\[
h\ge0.
\]
Thus
\[
v_\varepsilon=v-\varepsilon h\le0.
\]
:::

By the growth hypothesis, there exists \(R_0>0\) such that
\[
u(x,y)\le |x+iy|=r
\]
whenever \(r\ge R_0\) in the quadrant.

<1>9. For \(r\ge R_0\),
\[
\boxed{
v(x,y)\le r}.
\]

::: {.proof}
Since \(a,b>0\) and \(x,y\ge0\),
\[
ax+by\ge0.
\]
Therefore
\[
v
=
u-ax-by
\le
u
\le
r.
\]
:::

<1>10. On the quarter-circle
\[
r=R\ge R_0,
\]
one has
\[
v_\varepsilon
\le
R-\varepsilon c_pR^p.
\]

::: {.proof}
Use step <1>9 and the lower bound
\[
h\ge c_pR^p
\]
from step <1>6.
:::

<1>11. Since \(p>1\), there exists \(R_\varepsilon\ge R_0\) such that
\[
\boxed{
R-\varepsilon c_pR^p<0}
\]
for every \(R\ge R_\varepsilon\).

::: {.proof}
Factor:
\[
R-\varepsilon c_pR^p
=
R\left(
1-\varepsilon c_pR^{p-1}
\right).
\]
Because \(p-1>0\),
\[
R^{p-1}\to\infty.
\]
Thus eventually
\[
\varepsilon c_pR^{p-1}>1.
\]
:::

Fix \(R\ge R_\varepsilon\), and let
\[
Q_R
=
\Omega\cap\{x^2+y^2<R^2\}
\]
be the open quarter-disk.

<1>12. The boundary values of \(v_\varepsilon\) on \(\partial Q_R\) are nonpositive.

::: {.proof}
On the two radial sides, use step <1>8. On the circular arc, use steps <1>10--<1>11.
:::

<1>13. By the maximum principle for subharmonic functions,
\[
\boxed{
v_\varepsilon\le0
\quad\text{throughout }Q_R}.
\]

::: {.proof}
The function \(v_\varepsilon\) is subharmonic in \(Q_R\) by step <1>7 and continuous on its closure. Since its boundary values are nonpositive by step <1>12, the subharmonic maximum principle gives
\[
\sup_{Q_R}v_\varepsilon
\le
\sup_{\partial Q_R}v_\varepsilon
\le0.
\]
:::

<1>14. Let \((x,y)\in\Omega\) be arbitrary. Then
\[
\boxed{
v(x,y)\le\varepsilon h(x,y)}
\]
for every \(\varepsilon>0\).

::: {.proof}
Choose
\[
R>\max\{R_\varepsilon,\sqrt{x^2+y^2}\}.
\]
Then \((x,y)\in Q_R\), so step <1>13 gives
\[
v_\varepsilon(x,y)
=
v(x,y)-\varepsilon h(x,y)
\le0.
\]
Rearrange.
:::

<1>15. Letting \(\varepsilon\downarrow0\),
\[
\boxed{
v(x,y)\le0}.
\]

::: {.proof}
For fixed \((x,y)\), the number \(h(x,y)\) is finite. Step <1>14 holds for every \(\varepsilon>0\), so
\[
v(x,y)\le\inf_{\varepsilon>0}\varepsilon h(x,y)=0.
\]
:::

<1>16. Therefore
\[
\boxed{
u(x,y)\le ax+by}
\]
for every \((x,y)\in\Omega\).

::: {.proof}
Recall
\[
v=u-ax-by.
\]
Step <1>15 gives \(v\le0\).
:::

<1>17. Q.E.D.

::: {.proof}
Step <1>16 is the required Phragmén--Lindelöf bound.
:::
:::
