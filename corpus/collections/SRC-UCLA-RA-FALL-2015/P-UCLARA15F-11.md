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
Let $\Omega = \{(x,y) \in \RR^2 ; x > 0, y > 0\}$ and let $u$ be subharmonic in $\Omega$, continuous in $\overline{\Omega}$, such that
$$
u(x,y) \leq |x + iy|,
$$
for large $(x,y) \in \Omega$. Assume that
$$
u(x,0) \leq ax, \quad u(0,y) \leq by, \quad x, y \geq 0,
$$
for some $a, b > 0$. Show that
$$
u(x,y) \leq ax + by, \quad (x,y) \in \Omega.
$$
:::

::: {.solution}

Set
$$
v(x,y)=u(x,y)-ax-by.
$$

::: pf

::: {.pf-step #s1-1}

The function $v$ is subharmonic in $\Omega$ and continuous on $\overline\Omega$.


::: pf-proof

The function $u$ is subharmonic, while
$$
(x,y)\longmapsto ax+by
$$
is harmonic. Subtracting a harmonic function preserves subharmonicity. Continuity is preserved as well.

:::

:::

::: {.pf-step #s1-2}

On the boundary rays,
$$
\boxed{
v(x,0)\le0,
\qquad
v(0,y)\le0}.
$$


::: pf-proof

By hypothesis,
$$
u(x,0)\le ax
$$
and
$$
u(0,y)\le by.
$$
Subtract the corresponding linear terms.

:::

:::

::: pf-step

Define
$$
\boxed{
h(r,\theta)
=
r^p
\cos\!\left(
p\left(\theta-\frac{\pi}{4}\right)
\right)}.
$$


::: pf-proof

This is the real part of the holomorphic branch
$$
e^{-ip\pi/4}z^p
$$
on the quadrant.

:::

:::

::: {.pf-step #s1-4}

The function $h$ is harmonic in $\Omega$.


::: pf-proof

The quadrant is simply connected and does not meet the negative real axis after choosing a branch of $z^p$. The real part of a holomorphic function is harmonic.

:::

:::

::: {.pf-step #s1-5}

The function $h$ is strictly positive on
$$
\overline\Omega\setminus\{0\}.
$$


::: pf-proof

For
$$
0\le\theta\le\frac{\pi}{2},
$$
one has
$$
-\frac{\pi}{4}
\le
\theta-\frac{\pi}{4}
\le
\frac{\pi}{4}.
$$
Hence
$$
\left|
p\left(\theta-\frac{\pi}{4}\right)
\right|
\le
\frac{p\pi}{4}
<
\frac{\pi}{2},
$$
because $p<2$. Therefore the cosine factor is positive. Also $r^p>0$ for $r>0$.

:::

:::

::: {.pf-step #s1-6}

More precisely, there is a constant
$$
c_p>0
$$
such that
$$
\boxed{
h(r,\theta)\ge c_p r^p}
$$
throughout the closed quadrant.


::: pf-proof

Take
$$
c_p
=
\cos\frac{p\pi}{4}>0.
$$
The minimum of
$$
\cos\!\left(
p(\theta-\pi/4)
\right)
$$
on $[0,\pi/2]$ is attained at the endpoints and equals $c_p$.

:::

:::

::: {.pf-step #s1-7}

The function $v_\varepsilon$ is subharmonic in $\Omega$.


::: pf-proof

The function $v$ is subharmonic by step [](#s1-1){.pf-ref}, and $h$ is harmonic by step [](#s1-4){.pf-ref}. Subtracting $\varepsilon h$ preserves subharmonicity.

:::

:::

::: {.pf-step #s1-8}

On the two coordinate axes,
$$
\boxed{
v_\varepsilon\le0}.
$$


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
v\le0
$$
on the axes, while by step [](#s1-5){.pf-ref},
$$
h\ge0.
$$
Thus
$$
v_\varepsilon=v-\varepsilon h\le0.
$$

:::

:::

::: {.pf-step #s1-9}

For $r\ge R_0$,
$$
\boxed{
v(x,y)\le r}.
$$


::: pf-proof

Since $a,b>0$ and $x,y\ge0$,
$$
ax+by\ge0.
$$
Therefore
$$
v
=
u-ax-by
\le
u
\le
r.
$$

:::

:::

::: {.pf-step #s1-10}

On the quarter-circle
$$
r=R\ge R_0,
$$
one has
$$
v_\varepsilon
\le
R-\varepsilon c_pR^p.
$$


::: pf-proof

Use step [](#s1-9){.pf-ref} and the lower bound
$$
h\ge c_pR^p
$$
from step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-11}

Since $p>1$, there exists $R_\varepsilon\ge R_0$ such that
$$
\boxed{
R-\varepsilon c_pR^p<0}
$$
for every $R\ge R_\varepsilon$.


::: pf-proof

Factor:
$$
R-\varepsilon c_pR^p
=
R\left(
1-\varepsilon c_pR^{p-1}
\right).
$$
Because $p-1>0$,
$$
R^{p-1}\to\infty.
$$
Thus eventually
$$
\varepsilon c_pR^{p-1}>1.
$$

:::

:::

::: {.pf-step #s1-12}

The boundary values of $v_\varepsilon$ on $\partial Q_R$ are nonpositive.


::: pf-proof

On the two radial sides, use step [](#s1-8){.pf-ref}. On the circular arc, use steps [](#s1-10){.pf-ref} through [](#s1-11){.pf-ref}.

:::

:::

::: {.pf-step #s1-13}

By the maximum principle for subharmonic functions,
$$
\boxed{
v_\varepsilon\le0
\quad\text{throughout }Q_R}.
$$


::: pf-proof

The function $v_\varepsilon$ is subharmonic in $Q_R$ by step [](#s1-7){.pf-ref} and continuous on its closure. Since its boundary values are nonpositive by step [](#s1-12){.pf-ref}, the subharmonic maximum principle gives
$$
\sup_{Q_R}v_\varepsilon
\le
\sup_{\partial Q_R}v_\varepsilon
\le0.
$$

:::

:::

::: {.pf-step #s1-14}

Let $(x,y)\in\Omega$ be arbitrary. Then
$$
\boxed{
v(x,y)\le\varepsilon h(x,y)}
$$
for every $\varepsilon>0$.


::: pf-proof

Choose
$$
R>\max\{R_\varepsilon,\sqrt{x^2+y^2}\}.
$$
Then $(x,y)\in Q_R$, so step [](#s1-13){.pf-ref} gives
$$
v_\varepsilon(x,y)
=
v(x,y)-\varepsilon h(x,y)
\le0.
$$
Rearrange.

:::

:::

::: {.pf-step #s1-15}

Letting $\varepsilon\downarrow0$,
$$
\boxed{
v(x,y)\le0}.
$$


::: pf-proof

For fixed $(x,y)$, the number $h(x,y)$ is finite. Step [](#s1-14){.pf-ref} holds for every $\varepsilon>0$, so
$$
v(x,y)\le\inf_{\varepsilon>0}\varepsilon h(x,y)=0.
$$

:::

:::

::: {.pf-step #s1-16}

Therefore
$$
\boxed{
u(x,y)\le ax+by}
$$
for every $(x,y)\in\Omega$.


::: pf-proof

Recall
$$
v=u-ax-by.
$$
Step [](#s1-15){.pf-ref} gives $v\le0$.

:::

:::

::: pf-qed

Step [](#s1-16){.pf-ref} is the required Phragmén--Lindelöf bound.

:::

:::

:::
