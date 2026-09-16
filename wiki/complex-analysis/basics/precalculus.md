---
order: 1
title: Precalculus preliminaries
---

# Precalculus preliminaries

## Geometry

::: {.fact}
The interior angles of a convex $n$-gon sum to $(n-2)\pi$, so each interior angle of a regular $n$-gon is $\frac{n-2}{n}\pi$.

:::

::: {.fact title="Standard forms of conic sections"}
\envlist

- Circle: $x^2 + y^2 = r^2$, or $\abs{z-a}=r$.
  For $a\neq b$ and a constant $c>0$ with $c\neq 1$, the locus $\abs{z-a} = c\abs{z-b}$ of points whose distances $d_1, d_2$ to the two points $a, b$ have constant ratio $d_1/d_2 = c$ is also a circle:

![](figures/2021-12-04_00-49-30.png)

- Ellipse: $\qty{\frac x a}^2  + \qty{\frac y b}^2 = 1$, or $\abs{z-a} + \abs{z-b} = c$ with $c > \abs{a-b}$, the locus of points whose distances to $a$ and $b$ have constant sum $d_1 + d_2 = c$:

![](figures/2021-12-04_00-53-36.png)

- Hyperbola: $\qty{\frac x a}^2  - \qty{\frac y b}^2 = 1$, or $\abs{\abs{z-a} - \abs{z-b}} = c$ with $0 < c < \abs{a-b}$:

![](figures/2021-12-04_00-57-40.png)

  The rectangular hyperbola is $xy = \frac{c^2}{2}$.
- Parabola: $y^2 = 4ax$.

:::

::: {.fact title="Classification by the discriminant"}
For a nondegenerate real conic $Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0$ with discriminant $\Delta \coloneqq B^2 - 4AC$:

- $\Delta < 0$ if and only if the conic is an ellipse, and it is a circle if and only if moreover $A=C$ and $B=0$;
- $\Delta = 0$ if and only if the conic is a parabola;
- $\Delta > 0$ if and only if the conic is a hyperbola.

:::

::: {.fact title="Parameterizations"}
\envlist

- The ellipse $\qty{x\over a}^2 + \qty{y\over b}^2 = 1$ is parameterized by $t\mapsto (a\cos(t), b\sin(t))$:

![](figures/2021-12-30_19-31-42.png)

  - In complex form, $\gamma(t) = pe^{it} + qe^{-it}$ with $p \coloneqq \frac{a+b}{2}$ and $q \coloneqq \frac{a-b}{2}$, since $pe^{it} + qe^{-it} = a\cos(t) + ib\sin(t)$.
  - For $a\geq b$ the foci are $(\pm c, 0)$ with $c\coloneqq \sqrt{a^2-b^2}$, and the vertices are $(\pm a, 0)$ and $(0, \pm b)$:

    ![](figures/2022-01-01_00-11-24.png)

- The circle $(x-h)^2 + (y-k)^2 = r^2$ is parameterized by $t\mapsto (r\cos(t) + h, r\sin(t) + k)$, in complex form $\gamma(t) = z_0 + re^{it}$ with $z_0\coloneqq h + ik$.

- With $u\coloneqq \tan(t/2)$,
$$
\cos(t) = {1-u^2\over 1+u^2}, \qquad \sin(t) = {2u\over 1+u^2}.
$$
  This gives the rational parameterization of the ellipse
$$
u\mapsto a {1-u^2\over 1+u^2} +ib{2u\over 1+u^2},
$$
  and, for $a=b=R$, of the circle of radius $R$; each misses only the point $-a$.

- For $a\in\CC\setminus\ts{0}$ and $c\in\RR$, the set $\ts{z \st \bar{a}z + a\bar{z} + c = 0}$ is a line, and every line has this form.

:::

## Algebra

::: {.fact title="Numerical values"}
$\sqrt{2} \approx 1.4142$, $1/\sqrt{2} \approx 0.7071$, $\sqrt{3} \approx 1.7321$, $1/\sqrt{3} \approx 0.5774$, $e\approx 2.7183$, $\pi \approx 3.14159$.

:::

::: {.fact title="Completing the square"}
For $a\neq 0$,
$$
ax^2 + bx + c = a\qty{x + d}^2 + e, \qquad d \coloneqq \frac{b}{2a}, \quad e\coloneqq c - \frac{b^2}{4a}.
$$
In particular $x^2 + bx + c = \qty{x+ {b\over 2}}^2 + c - \qty{b\over 2}^2$.

:::

## Trigonometry

[[FF-ATMHV]] [[FF-ZQFSR]] [[FF-TGTS7]]

[[FF-CLFAB]] [[FF-W2TS2]] [[FF-VT2E7]]

[[FF-YBIQV]] [[FF-CIESS]] [[FF-SF7VN]]

[[FF-JLUCP]]

[[FF-Y6IOA]] [[FF-WDDTM]] [[FF-A7OEY]]

[[FF-7KQCC]] [[FF-2VUTS]] [[FF-2ABHQ]]

::: {.remark}
The root of unity $e^{2\pi i k/n}$ has rectangular coordinates $\qty{\cos(2\pi k/n), \sin(2\pi k/n)}$, and the values above give the rectangular forms of $e^{2\pi i/3}$ and $e^{2\pi i/6}$.

:::

[[FF-XEQFR]] [[FF-TGHJ5]]

[[FF-2OHYV]]

[[FF-TBIC5]]

## Hyperbolic functions

[[FD-XUGN3]]

[[FF-AGEQ4]] [[FF-MV5X6]]

[[FF-VFWB6]] [[FF-VR4UT]]

::: {.remark}
For $z = x+iy$, the addition formulas together with $\cos(iy) = \cosh(y)$ and $\sin(iy) = i\sinh(y)$ give $\cos(z) = \cos(x)\cosh(y) - i\sin(x)\sinh(y)$ and $\sin(z) = \sin(x)\cosh(y) + i\cos(x)\sinh(y)$.
The series expansions are on [[complex-analysis/basics/series-reference|Series reference]].

:::
