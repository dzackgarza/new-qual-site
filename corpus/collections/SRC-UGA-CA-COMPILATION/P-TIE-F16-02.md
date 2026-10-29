---
schema: qual/card@1
id: P-TIE-F16-02
kind: problem
title: Orthogonality of level curves of $\operatorname{Re} f$ and $\operatorname{Im} f$
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2016, question 2.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Cleaned the LaTeX, restored the label (i) printed as (c), and added a remark on the missing = 0 in (b)(ii), against Fall 2016, question 2, page 15 of Questions_from_Tie.pdf.
---

::: {.problem}
(a) $f(z) = u(x,y) + iv(x,y)$ be analytic in a domain $D \subset \CC$. Let $z_0 = (x_0, y_0)$ be a point in $D$ which is in the intersection of the curves $u(x,y) = c_1$ and $v(x,y) = c_2$, where $c_1$ and $c_2$ are constants. Suppose that $f'(z_0) \ne 0$. Prove that the lines tangent to these curves at $z_0$ are perpendicular.

(b) Let $f(z) = z^2$ be defined in $\CC$.

(i) Describe the level curves of $\operatorname{Re}(f)$ and of $\operatorname{Im}(f)$.

(ii) What are the angles of intersections between the level curves $\operatorname{Re}(f) = 0$ and $\operatorname{Im}(f)$? Is your answer in agreement with part a) of this question?
:::

::: {.remark}
The source labels the first subpart of (b) "(c)"; it is subpart (i) of the list (i), (ii).
In (b)(ii) the source reads "the level curves $\operatorname{Re}(f) = 0$ and $\operatorname{Im}(f)$", evidently meaning the level curves $\operatorname{Re}(f) = 0$ and $\operatorname{Im}(f) = 0$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

At $z_0$, both gradients
$$
\nabla u(z_0)
\qquad\text{and}\qquad
\nabla v(z_0)
$$
are nonzero.


::: pf-proof

Since
$$
f'(z_0)\ne0,
$$
one has
$$
u_x(z_0)+iv_x(z_0)\ne0.
$$
Thus
$$
u_x(z_0)^2+v_x(z_0)^2>0.
$$
By the Cauchy--Riemann equations,
$$
v_x=-u_y,
\qquad
v_y=u_x.
$$
Hence
$$
\abs{\nabla u(z_0)}^2
=
u_x(z_0)^2+u_y(z_0)^2
=
u_x(z_0)^2+v_x(z_0)^2
>0,
$$
and similarly
$$
\abs{\nabla v(z_0)}^2
=
v_x(z_0)^2+v_y(z_0)^2
>0.
$$

:::

:::

::: {.pf-step #s1-2}

The gradients $\nabla u(z_0)$ and $\nabla v(z_0)$ are perpendicular.


::: pf-proof

Using the Cauchy--Riemann equations,
$$
\begin{aligned}
\nabla u\cdot\nabla v
&=
u_xv_x+u_yv_y\\
&=
u_x(-u_y)+u_yu_x\\
&=
0.
\end{aligned}
$$
Thus the two nonzero gradients are orthogonal at $z_0$.

:::

:::

::: {.pf-step #s1-3}

The tangent lines to the level curves
$$
u=c_1
\qquad\text{and}\qquad
v=c_2
$$
at $z_0$ are perpendicular.


::: pf-proof

By step [](#s1-1){.pf-ref} and the implicit function theorem, both level sets are smooth curves near $z_0$. Their tangent lines are perpendicular to their respective gradients. Rotating both perpendicular gradient vectors through $90^\circ$ preserves the angle between them, so by step [](#s1-2){.pf-ref} the two tangent lines are perpendicular.

:::

:::

::: {.pf-step #s1-4}

For
$$
f(z)=z^2,
\qquad
z=x+iy,
$$
one has
$$
\operatorname{Re}f=x^2-y^2,
\qquad
\operatorname{Im}f=2xy.
$$


::: pf-proof

Expand:
$$
z^2
=(x+iy)^2
=
x^2-y^2+2ixy.
$$

:::

:::

::: {.pf-step #s1-5}

The level curves of $\operatorname{Re}f$ are
$$
x^2-y^2=c.
$$
For $c>0$ these are hyperbolas opening in the $x$-direction; for $c<0$ they are hyperbolas opening in the $y$-direction; and for $c=0$ they are the two lines
$$
y=x,
\qquad
y=-x.
$$


::: pf-proof

This is the standard classification of the real conics
$$
x^2-y^2=c
$$
obtained from step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

The level curves of $\operatorname{Im}f$ are
$$
2xy=c.
$$
For $c\ne0$ these are rectangular hyperbolas, while for $c=0$ they are the coordinate axes
$$
x=0
\qquad\text{or}\qquad
y=0.
$$


::: pf-proof

This follows directly from
$$
\operatorname{Im}f=2xy
$$
in step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

The zero level curves
$$
\operatorname{Re}f=0
\qquad\text{and}\qquad
\operatorname{Im}f=0
$$
meet only at the origin, and their branches meet there at acute angle
$$
\boxed{\frac\pi4}.
$$


::: pf-proof

The first zero level set is
$$
y=\pm x,
$$
and the second is
$$
x=0
\quad\text{or}\quad
y=0.
$$
Their only common point is $(0,0)$. Each line $y=\pm x$ makes an angle of $\pi/4$ with each coordinate axis, so the acute intersection angle is $\pi/4$.

:::

:::

::: {.pf-step #s1-8}

This does not contradict part (a).


::: pf-proof

For
$$
f(z)=z^2,
$$
one has
$$
f'(z)=2z.
$$
At the only intersection point of the two zero level sets,
$$
z=0,
$$
one has
$$
f'(0)=0.
$$
Thus the nonvanishing-derivative hypothesis of part (a) fails exactly at the point where the level curves are not orthogonal.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} prove part (a), and steps [](#s1-4){.pf-ref} through [](#s1-8){.pf-ref} answer part (b).

:::

:::

:::
