---
schema: qual/card@1
id: P-TRIV-LA01
kind: problem
title: Conic sections of the cone $z^2=x^2+y^2$ by the planes $z-ax=1$
classification:
  areas: [prelim]
  topics:
  - Conic Sections
  - Quadric Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 1, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Describe the figures that can be obtained as intersection of the cone $z^2 = x^2 + y^2$ with the plane $z - ax = 1$, $0 < a < \infty$, in $\RR^3$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

On the plane
$$
z-ax=1,
$$
one has
$$
z=1+ax.
$$


::: pf-proof

This is an algebraic rearrangement of the plane equation.

:::

:::

::: {.pf-step #s1-2}

Substituting step [](#s1-1){.pf-ref} into the cone equation gives
$$
(1-a^2)x^2-2ax+y^2=1.
$$


::: pf-proof

The cone equation becomes
$$
(1+ax)^2=x^2+y^2.
$$
Expanding and moving all terms except the constant to the left gives
$$
1+2ax+a^2x^2=x^2+y^2,
$$
hence
$$
(1-a^2)x^2-2ax+y^2=1.
$$

:::

:::

::: {.pf-step #s1-3}

If
$$
0<a<1,
$$
the intersection is an ellipse.


::: pf-proof

Since
$$
1-a^2>0,
$$
complete the square in step [](#s1-2){.pf-ref}:
$$
(1-a^2)
\left(
x-\frac{a}{1-a^2}
\right)^2
+
y^2
=
\frac1{1-a^2}.
$$
Equivalently,
$$
\frac{
\left(
x-\frac{a}{1-a^2}
\right)^2
}{
\frac1{(1-a^2)^2}
}
+
\frac{y^2}{
\frac1{1-a^2}
}
=
1.
$$
Both quadratic coefficients are positive, so this is an ellipse in the
cutting plane.

:::

:::

::: {.pf-step #s1-4}

If
$$
a=1,
$$
the intersection is a parabola.


::: pf-proof

Step [](#s1-2){.pf-ref} becomes
$$
-2x+y^2=1,
$$
or
$$
y^2=2x+1.
$$
This is a parabola.

:::

:::

::: {.pf-step #s1-5}

If
$$
a>1,
$$
the intersection is a hyperbola.


::: pf-proof

Put
$$
b=a^2-1>0.
$$
Then step [](#s1-2){.pf-ref} reads
$$
-bx^2-2ax+y^2=1.
$$
Completing the square gives
$$
b
\left(
x+\frac{a}{b}
\right)^2
-
y^2
=
\frac1b.
$$
Equivalently,
$$
\frac{
\left(
x+\frac{a}{a^2-1}
\right)^2
}{
\frac1{(a^2-1)^2}
}
-
\frac{y^2}{
\frac1{a^2-1}
}
=
1.
$$
The quadratic terms have opposite signs, so the section is a hyperbola.

:::

:::

::: {.pf-step #s1-6}

Therefore the possible sections are
$$
\boxed{
\begin{array}{c|c}
0<a<1&\text{ellipse}\\
a=1&\text{parabola}\\
a>1&\text{hyperbola}
\end{array}
}.
$$


::: pf-proof

This is exactly the classification in steps [](#s1-3){.pf-ref} through [](#s1-5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} gives all possibilities for $0<a<\infty$.

:::

:::

:::
