---
schema: qual/card@1
id: P-AGXVAREXWEIERSTRASS
kind: problem
title: Nonsingularity of the Weierstrass cubic and the discriminant
classification:
  areas:
  - algebraic-geometry
  topics:
  - Weierstrass Form
  - Elliptic Curves
  - Discriminants
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read the Weierstrass-cubic item in Zaidenberg Exercise 8.5 in the recorded
    source. It gives the homogeneous equation
    y^2z-(x^3+g_2xz^2+g_3z^3)=0 over C and asks that it be nonsingular exactly
    when p(x)=x^3+g_2x+g_3 has no multiple root. The source gives no solution
    for this item.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Checked the point at infinity directly and checked that, on the affine
    z=1 chart, the Jacobian criterion identifies singular points precisely
    with common roots of p and p'.
---

::: {.problem}
Define the Weierstrass cubic as $X\da V(y^{2} z-(x^{3}+g_{2} x z^{2}+g_{3} z^{3}) )$ for $g_2, g_3 \in \CC$.
Show that $X$ is nonsingular iff $p(x) \da x^3 + g_2 x + g_3$ has no multiple roots.
:::

::: {.solution}
Put
$$
F(x,y,z)
=
y^2z-x^3-g_2xz^2-g_3z^3
$$
and
$$
p(x)=x^3+g_2x+g_3.
$$

::: pf

::: {.pf-step #point-at-infinity-nonsingular}
The only point of $X$ on the line $z=0$ is
$$
O=(0:1:0),
$$
and $O$ is nonsingular.

::: pf-proof
On $z=0$ the equation $F=0$ becomes
$$
-x^3=0,
$$
so $x=0$. Since $(x:y:z)$ is a projective point, $y\ne0$, and hence the
only such point is $O=(0:1:0)$.

The partial derivative with respect to $z$ is
$$
F_z
=
y^2-2g_2xz-3g_3z^2.
$$
Therefore
$$
F_z(O)=1\ne0.
$$
By the projective Jacobian criterion, $O$ is nonsingular.
:::

:::

::: {.pf-step #affine-singular-criterion}
A point $(a:b:1)\in X$ is singular if and only if
$$
b=0,
\qquad
p(a)=0,
\qquad
p'(a)=0.
$$

::: pf-proof
On the affine chart $z=1$, the curve is
$$
f(x,y)
=
y^2-p(x)
=
0.
$$
Its partial derivatives are
$$
f_x=-p'(x)=-(3x^2+g_2),
\qquad
f_y=2y.
$$
Since the ground field is $\CC$, the affine Jacobian criterion says that
$(a,b)$ is singular exactly when
$$
f(a,b)=f_x(a,b)=f_y(a,b)=0.
$$
The equation $f_y(a,b)=0$ is equivalent to $b=0$. With $b=0$, the remaining
two equations are precisely
$$
p(a)=0
\qquad\text{and}\qquad
p'(a)=0.
$$
This proves the claim.
:::

:::

::: {.pf-step #singular-iff-multiple-root}
The curve $X$ is singular if and only if $p$ has a multiple root.

::: pf-proof
By step [](#point-at-infinity-nonsingular){.pf-ref}, the point at infinity is nonsingular, so every singular point
of $X$ lies in the chart $z=1$. By step [](#affine-singular-criterion){.pf-ref}, such a singular point exists
exactly when there is some $a\in\CC$ satisfying
$$
p(a)=p'(a)=0.
$$
A root of a polynomial over a field of characteristic zero is multiple if
and only if it is also a root of the derivative. Thus the displayed
condition is equivalent to $p$ having a multiple root.
:::

:::

::: {.pf-step #discriminant-criterion}
Equivalently,
$$
X\text{ is nonsingular}
\quad\Longleftrightarrow\quad
4g_2^3+27g_3^2\ne0.
$$

::: pf-proof
Suppose first that $a$ is a multiple root of $p$. Then
$$
3a^2+g_2=0
\qquad\text{and}\qquad
a^3+g_2a+g_3=0.
$$
The first equation gives $g_2=-3a^2$, and substituting this into the second
gives $g_3=2a^3$. Hence
$$
4g_2^3+27g_3^2
=
4(-3a^2)^3+27(2a^3)^2
=
0.
$$

Conversely, suppose
$$
4g_2^3+27g_3^2=0.
$$
If $g_2=0$, then $g_3=0$, and $a=0$ is a common root of $p$ and $p'$.
If $g_2\ne0$, put
$$
a=-\frac{3g_3}{2g_2}.
$$
The displayed relation gives
$$
a^2
=
\frac{9g_3^2}{4g_2^2}
=
-\frac{g_2}{3},
$$
so $p'(a)=3a^2+g_2=0$. Moreover,
$$
\begin{aligned}
p(a)
&=a(a^2+g_2)+g_3\\
&=\frac23ag_2+g_3\\
&=0.
\end{aligned}
$$
Thus $p$ has a multiple root. Therefore its discriminant
$$
-4g_2^3-27g_3^2
$$
is nonzero exactly when $X$ is nonsingular, by step [](#singular-iff-multiple-root){.pf-ref}.
:::

:::

::: pf-qed
Step [](#singular-iff-multiple-root){.pf-ref} proves the required equivalence, and step [](#discriminant-criterion){.pf-ref} records it in the
usual discriminant form.
:::

:::

:::
