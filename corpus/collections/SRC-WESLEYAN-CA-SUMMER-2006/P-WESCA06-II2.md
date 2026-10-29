---
schema: qual/card@1
id: P-WESCA06-II2
kind: problem
title: "A differentiable but nowhere analytic function"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis Problems, problem 2 (August 9, 2006) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
Let
$$
f(z)=x^2+i y^2,
\qquad z=x+iy.
$$
Show that $f$ is differentiable at every point on the line $y=x$ but is nowhere analytic.
:::

::: {.solution}

Write
$$
f=u+iv,
\qquad
u(x,y)=x^2,
\qquad
v(x,y)=y^2.
$$

::: pf

::: {.pf-step #s1-1}

The first partial derivatives are
$$
u_x=2x,
\qquad
u_y=0,
\qquad
v_x=0,
\qquad
v_y=2y.
$$


::: pf-proof

Differentiate the polynomial functions
$$
u(x,y)=x^2
$$
and
$$
v(x,y)=y^2.
$$
All partial derivatives are continuous everywhere.

:::

:::

::: {.pf-step #s1-2}

The Cauchy--Riemann equations are
$$
u_x=v_y
\qquad\text{and}\qquad
u_y=-v_x.
$$
For this function they reduce to
$$
2x=2y
\qquad\text{and}\qquad
0=0.
$$


::: pf-proof

Substitute the derivatives from step [](#s1-1){.pf-ref} into the Cauchy--Riemann
equations.

:::

:::

::: {.pf-step #s1-3}

Hence the Cauchy--Riemann equations hold exactly at the points
$$
(x,y)
$$
with
$$
y=x.
$$


::: pf-proof

The second equation is automatic.
The first is equivalent to
$$
x=y.
$$

:::

:::

::: {.pf-step #s1-4}

The function $f$ is complex differentiable at every point on the line
$$
y=x.
$$


::: pf-proof

The partial derivatives of $u$ and $v$ are continuous everywhere by
step [](#s1-1){.pf-ref}.
Therefore the standard Cauchy--Riemann differentiability theorem applies:
at every point where the Cauchy--Riemann equations hold, $f$ is complex
differentiable.

By step [](#s1-3){.pf-ref}, this includes every point of the line
$$
y=x.
$$

:::

:::

::: pf-step

At a point
$$
z=x+ix
$$
on that line,
$$
\boxed{
f'(z)=2x.
}
$$


::: pf-proof

At a complex-differentiability point,
$$
f'
=
u_x+i v_x.
$$
Using step [](#s1-1){.pf-ref},
$$
f'(z)
=
2x+i\cdot0
=
2x.
$$

:::

:::

::: {.pf-step #s1-6}

The function is not complex differentiable at any point off the line
$$
y=x.
$$


::: pf-proof

If
$$
x\ne y,
$$
then step [](#s1-2){.pf-ref} gives
$$
u_x
=
2x
\ne
2y
=
v_y.
$$
The Cauchy--Riemann equations are necessary for complex differentiability,
so $f$ cannot be complex differentiable there.

:::

:::

::: {.pf-step #s1-7}

The line
$$
L
=
\{x+iy:y=x\}
$$
has empty interior in
$$
\CC.
$$


::: pf-proof

Every open disk centered at a point of $L$ contains points with
$$
y\ne x.
$$
Hence no nonempty open disk is contained in $L$.

:::

:::

::: {.pf-step #s1-8}

The function $f$ is nowhere analytic.


::: pf-proof

Suppose $f$ were analytic at some point
$$
z_0.
$$
Then there would be an open neighborhood
$$
U\ni z_0
$$
on which $f$ is holomorphic, hence complex differentiable at every point of
$U$.

By step [](#s1-6){.pf-ref}, every complex-differentiability point lies on
$$
L.
$$
Thus
$$
U\subseteq L,
$$
contradicting step [](#s1-7){.pf-ref} because $U$ is nonempty and open.
Therefore no point has a neighborhood on which $f$ is analytic.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves differentiability along
$$
y=x,
$$
and step [](#s1-8){.pf-ref} proves that $f$ is nowhere analytic.

:::

:::

:::
