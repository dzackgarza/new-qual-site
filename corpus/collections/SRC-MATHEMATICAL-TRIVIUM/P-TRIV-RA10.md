---
schema: qual/card@1
id: P-TRIV-RA10
kind: problem
title: Triple product rule for partial derivatives of an implicit function
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 10, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider the implicit function of three arguments, $f(x, y, z) = 0$. Show that $\frac{\partial z}{\partial y} \cdot \frac{\partial y}{\partial x} \cdot \frac{\partial x}{\partial z} = -1$. Give an analogue of this statement for the implicit function of $n$ arguments, $f(x_1, \ldots, x_n) = 0$.
:::

::: {.remark}
Each displayed derivative is taken while holding the remaining variables fixed,
and the corresponding partial derivatives of $f$ are assumed nonzero so that
the implicit derivatives are locally defined.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Along the surface
$$
f(x,y,z)=0,
$$
with $x$ held fixed,
$$
f_y,dy+f_z,dz=0.
$$


::: pf-proof

The total differential is
$$
df=f_x,dx+f_y,dy+f_z,dz.
$$
Along the level surface $df=0$, and holding $x$ fixed gives $dx=0$.

:::

:::

::: {.pf-step #s1-2}

Hence
$$
\left(\frac{\partial z}{\partial y}\right)_x
=
-\frac{f_y}{f_z}.
$$


::: pf-proof

Solve the relation in step [](#s1-1){.pf-ref} for $dz/dy$.

:::

:::

::: {.pf-step #s1-3}

Similarly,
$$
\left(\frac{\partial y}{\partial x}\right)_z
=
-\frac{f_x}{f_y}
$$
and
$$
\left(\frac{\partial x}{\partial z}\right)_y
=
-\frac{f_z}{f_x}.
$$


::: pf-proof

Repeat step [](#s1-1){.pf-ref} while holding $z$ fixed and then while holding $y$ fixed.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
\left(\frac{\partial z}{\partial y}\right)_x
\left(\frac{\partial y}{\partial x}\right)_z
\left(\frac{\partial x}{\partial z}\right)_y
=
-1.
}
$$


::: pf-proof

Multiply the three formulas from steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref}:
$$
\left(-\frac{f_y}{f_z}\right)
\left(-\frac{f_x}{f_y}\right)
\left(-\frac{f_z}{f_x}\right)
=
-1.
$$
All factors involving derivatives of $f$ cancel.

:::

:::

::: {.pf-step #s1-5}

Now let
$$
f(x_1,\ldots,x_n)=0,
$$
and set
$$
x_{n+1}=x_1.
$$
Holding all variables except $x_i$ and $x_{i+1}$ fixed gives
$$
f_{x_i},dx_i
+
f_{x_{i+1}},dx_{i+1}
=0.
$$


::: pf-proof

In the total differential
$$
df
=
\sum_{j=1}^{n}f_{x_j},dx_j,
$$
all differentials except $dx_i$ and $dx_{i+1}$ vanish under the stated
constraint, while $df=0$ along the level hypersurface.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\left(
\frac{\partial x_{i+1}}{\partial x_i}
\right)_{\text{all other }x_j}
=
-\frac{f_{x_i}}{f_{x_{i+1}}}.
$$


::: pf-proof

Solve step [](#s1-5){.pf-ref} for $dx_{i+1}/dx_i$.

:::

:::

::: {.pf-step #s1-7}

Multiplying cyclically for $i=1,\ldots,n$ gives
$$
\boxed{
\prod_{i=1}^{n}
\left(
\frac{\partial x_{i+1}}{\partial x_i}
\right)_{\text{all other }x_j}
=
(-1)^n,
\qquad
x_{n+1}=x_1.
}
$$


::: pf-proof

By step [](#s1-6){.pf-ref},
$$
\prod_{i=1}^{n}
\left(
-\frac{f_{x_i}}{f_{x_{i+1}}}
\right)
=
(-1)^n
\frac{f_{x_1}f_{x_2}\cdots f_{x_n}}
{f_{x_2}f_{x_3}\cdots f_{x_n}f_{x_1}}
=
(-1)^n.
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves the three-variable identity, and step [](#s1-7){.pf-ref} gives its
$n$-variable analogue.

:::

:::

:::
