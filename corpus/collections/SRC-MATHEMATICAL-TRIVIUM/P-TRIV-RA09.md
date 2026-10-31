---
schema: qual/card@1
id: P-TRIV-RA09
kind: problem
title: Extrema of $x^2+y^2+z^2$ on an ellipsoid
classification:
  areas: [real-analysis]
  topics:
  - Lagrange Multipliers
  - Extrema
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 9, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find local minima and local maxima of the function $f(x, y, z) = x^2 + y^2 + z^2$ on a surface defined by equation $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$, $0 < a < b < c$.
:::

::: {.solution}

Let
$$
g(x,y,z)
=
\frac{x^2}{a^2}
+
\frac{y^2}{b^2}
+
\frac{z^2}{c^2}.
$$
The constraint is $g=1$.

::: pf

::: pf-step

At a constrained critical point, there is a scalar $\lambda$ such that
$$
\nabla f=\lambda\nabla g.
$$


::: pf-proof

The ellipsoid is a smooth surface because $\nabla g\neq0$ on $g=1$. Hence
the Lagrange multiplier theorem applies.

:::

:::

::: {.pf-step #s1-2}

The multiplier equations are
$$
x\left(1-\frac{\lambda}{a^2}\right)=0,
$$
$$
y\left(1-\frac{\lambda}{b^2}\right)=0,
$$
and
$$
z\left(1-\frac{\lambda}{c^2}\right)=0.
$$


::: pf-proof

Since
$$
\nabla f=(2x,2y,2z)
$$
and
$$
\nabla g=
\left(
\frac{2x}{a^2},
\frac{2y}{b^2},
\frac{2z}{c^2}
\right),
$$
the equations follow after dividing by $2$.

:::

:::

::: {.pf-step #s1-3}

At a critical point, at most one of $x,y,z$ is nonzero.


::: pf-proof

If two coordinates were nonzero, step [](#s1-2){.pf-ref} would force $\lambda$ to equal
two distinct numbers among
$$
a^2,
\qquad
b^2,
\qquad
c^2,
$$
which is impossible because
$$
0<a<b<c.
$$

:::

:::

::: {.pf-step #s1-4}

The constrained critical points are exactly
$$
(\pm a,0,0),
\qquad
(0,\pm b,0),
\qquad
(0,0,\pm c).
$$


::: pf-proof

By step [](#s1-3){.pf-ref}, exactly one coordinate is nonzero because the constraint equals
$1$. Substituting into the ellipsoid equation gives the displayed values.

:::

:::

::: {.pf-step #s1-5}

On the ellipsoid,
$$
a^2
\leq
x^2+y^2+z^2
\leq
c^2.
$$


::: pf-proof

Because
$$
a^2\leq b^2\leq c^2,
$$
one has
$$
x^2+y^2+z^2
\geq
a^2
\left(
\frac{x^2}{a^2}
+
\frac{y^2}{b^2}
+
\frac{z^2}{c^2}
\right)
=
a^2.
$$
Similarly,
$$
x^2+y^2+z^2
\leq
c^2
\left(
\frac{x^2}{a^2}
+
\frac{y^2}{b^2}
+
\frac{z^2}{c^2}
\right)
=
c^2.
$$

:::

:::

::: {.pf-step #s1-6}

The points
$$
\boxed{(\pm a,0,0)}
$$
are global, hence local, minima with value
$$
\boxed{a^2}.
$$


::: pf-proof

Equality in the lower bound from step [](#s1-5){.pf-ref} occurs exactly when
$$
y=z=0,
$$
which on the ellipsoid gives $x=\pm a$.

:::

:::

::: {.pf-step #s1-7}

The points
$$
\boxed{(0,0,\pm c)}
$$
are global, hence local, maxima with value
$$
\boxed{c^2}.
$$


::: pf-proof

Equality in the upper bound from step [](#s1-5){.pf-ref} occurs exactly when
$$
x=y=0,
$$
which gives $z=\pm c$.

:::

:::

::: {.pf-step #s1-8}

The points
$$
(0,\pm b,0)
$$
are saddle points on the ellipsoid.


::: pf-proof

Near $(0,b,0)$, restrict first to the ellipse $z=0$. Then the constraint gives
$$
y=b\sqrt{1-x^2/a^2},
$$
and
$$
f
=
x^2+b^2\left(1-\frac{x^2}{a^2}\right)
=
b^2
+
x^2\left(1-\frac{b^2}{a^2}\right)
<b^2
$$
for small nonzero $x$, because $b>a$.

Restrict instead to $x=0$. Then
$$
y=b\sqrt{1-z^2/c^2},
$$
and
$$
f
=
b^2
+
z^2\left(1-\frac{b^2}{c^2}\right)
>b^2
$$
for small nonzero $z$, because $c>b$.

Thus both larger and smaller nearby values occur. The same argument applies at
$(0,-b,0)$.

:::

:::

::: {.pf-step #s1-9}

Therefore the complete list of local extrema is
$$
\boxed{
\begin{aligned}
\text{local minima: }&(\pm a,0,0),\\
\text{local maxima: }&(0,0,\pm c).
\end{aligned}
}
$$


::: pf-proof

Steps [](#s1-6){.pf-ref} through [](#s1-8){.pf-ref} classify all critical points from step [](#s1-4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} gives all constrained local minima and maxima.

:::

:::

:::
