---
schema: qual/card@1
id: P-TRIV-VP06
kind: problem
title: Euler--Lagrange equations for a particle in a potential
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Variational Principle, Problem 6, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider the functional $S [ x , y , z ] = \int _ { t _ { 1 } } ^ { t _ { 2 } } d t L ( x , y , z , x ^ { \prime } , y ^ { \prime } , z ^ { \prime } )$ , where

$$
L = { \frac { m } { 2 } } ( x ^ { \prime 2 } + y ^ { \prime 2 } + z ^ { \prime 2 } ) - U ( x , y , z ) ,\tag{14}
$$

and U is $\mathrm { ~ a ~ } C ^ { 1 }$ function of $x , y , z$ . Write the system of equations on $x ( t ) , y ( t ) , z ( t )$ whose solution is an extremum of $S [ x , y , z ]$ in a class of $C ^ { 2 } ( [ t _ { 1 } , t _ { 2 } ] )$ functions with fixed boundary conditions.
:::

::: {.solution}
<1>1. For the coordinate $x$, the Euler--Lagrange equation is
$$
\frac d{dt}
\frac{\partial L}{\partial x'}
-
\frac{\partial L}{\partial x}
=0.
$$

::: {.proof}
The endpoint values are fixed, so admissible variations vanish at
$t_1,t_2$. The usual first-variation argument for the coordinate $x$ gives
the Euler--Lagrange equation.
:::

<1>2. One has
$$
\frac{\partial L}{\partial x'}=mx'
$$
and
$$
\frac{\partial L}{\partial x}=-U_x.
$$

::: {.proof}
Differentiate
$$
L
=
\frac m2
\left(
(x')^2+(y')^2+(z')^2
\right)
-
U(x,y,z)
$$
with respect to $x'$ and $x$.
:::

<1>3. Therefore
$$
\boxed{mx''=-U_x(x,y,z)}.
$$

::: {.proof}
Substitute step <1>2 into step <1>1:
$$
\frac d{dt}(mx')+U_x=0.
$$
:::

<1>4. The same argument for the coordinate $y$ gives
$$
\boxed{my''=-U_y(x,y,z)}.
$$

::: {.proof}
Now
$$
\frac{\partial L}{\partial y'}=my',
\qquad
\frac{\partial L}{\partial y}=-U_y.
$$
Substitute into the Euler--Lagrange equation for $y$.
:::

<1>5. The same argument for the coordinate $z$ gives
$$
\boxed{mz''=-U_z(x,y,z)}.
$$

::: {.proof}
Use
$$
\frac{\partial L}{\partial z'}=mz',
\qquad
\frac{\partial L}{\partial z}=-U_z.
$$
:::

<1>6. Hence the extremals satisfy
$$
\boxed{
m
\begin{pmatrix}
x''\\
y''\\
z''
\end{pmatrix}
=
-\nabla U(x,y,z).
}
$$

::: {.proof}
Collect the three scalar equations from steps <1>3--<1>5 into vector form.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required Euler--Lagrange system.
:::
:::
