---
schema: qual/card@1
id: P-TRIV-VP05
kind: problem
title: Extremal of $\int_0^1(360x^2f-f''^2)\,dx$ with clamped endpoints
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Variational Principle, Problem 5, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find an extremum of the functional $J [ f ] = \int _ { 0 } ^ { 1 } d x ( 3 6 0 x ^ { 2 } f - f ^ { \prime \prime 2 } )$ in a class of functions $f \in C ^ { 3 } [ 0 , 1 ]$ satisfying the boundary conditions $f ( 0 ) = 0 , f ^ { \prime } ( 0 ) = 1$ $f ( 1 ) = 0 , f ^ { \prime } ( 1 ) = 2 . 5$
:::

::: {.solution}
<1>1. For a functional depending on $f''$, the Euler--Lagrange equation is
$$
\frac{\partial L}{\partial f}
-
\frac d{dx}
\frac{\partial L}{\partial f'}
+
\frac{d^2}{dx^2}
\frac{\partial L}{\partial f''}
=0.
$$

::: {.proof}
This is the second-order Euler--Poisson equation for a Lagrangian
$L(x,f,f',f'')$ when both $f$ and $f'$ are fixed at the endpoints.
:::

<1>2. Here
$$
L(x,f,f'')
=
360x^2f-(f'')^2,
$$
so the Euler--Lagrange equation becomes
$$
360x^2-2f^{(4)}=0.
$$

::: {.proof}
One has
$$
\frac{\partial L}{\partial f}=360x^2,
\qquad
\frac{\partial L}{\partial f'}=0,
\qquad
\frac{\partial L}{\partial f''}=-2f''.
$$
Substitute into step <1>1.
:::

<1>3. Therefore
$$
\boxed{f^{(4)}=180x^2}.
$$

::: {.proof}
Rearrange step <1>2.
:::

<1>4. Integrating four times gives
$$
f(x)
=
\frac12x^6
+
\frac{C_1}{6}x^3
+
\frac{C_2}{2}x^2
+
C_3x
+
C_4.
$$

::: {.proof}
Successive integrations of $f^{(4)}=180x^2$ give
$$
f'''=60x^3+C_1,
$$
$$
f''=15x^4+C_1x+C_2,
$$
$$
f'=3x^5+\frac{C_1}{2}x^2+C_2x+C_3,
$$
and then the displayed formula.
:::

<1>5. The conditions at $x=0$ give
$$
C_4=0,
\qquad
C_3=1.
$$

::: {.proof}
Substitute $x=0$ into the formulas for $f$ and $f'$ from step <1>4.
:::

<1>6. The condition $f(1)=0$ gives
$$
C_1+3C_2=-9.
$$

::: {.proof}
Using step <1>5,
$$
0
=
\frac12
+
\frac{C_1}{6}
+
\frac{C_2}{2}
+1.
$$
Multiply by $6$.
:::

<1>7. The condition $f'(1)=5/2$ gives
$$
C_1+2C_2=-3.
$$

::: {.proof}
With $C_3=1$,
$$
\frac52
=
3
+
\frac{C_1}{2}
+
C_2
+1.
$$
Multiply the resulting equation by $2$.
:::

<1>8. Solving steps <1>6--<1>7 gives
$$
C_1=9,
\qquad
C_2=-6.
$$

::: {.proof}
Subtract the second linear equation from the first to obtain
$$
C_2=-6,
$$
then substitute back to obtain $C_1=9$.
:::

<1>9. Hence the unique stationary function is
$$
\boxed{
f_*(x)
=
\frac12x^6
+
\frac32x^3
-
3x^2
+
x.
}
$$

::: {.proof}
Substitute the constants from steps <1>5 and <1>8 into step <1>4.
:::

<1>10. Let
$$
f=f_*+\eta,
$$
where the endpoint constraints imply
$$
\eta(0)=\eta'(0)=\eta(1)=\eta'(1)=0.
$$
Then
$$
J[f]-J[f_*]
=
-\int_0^1(\eta'')^2\,dx.
$$

::: {.proof}
Expand
$$
360x^2(f_*+\eta)-(f_*''+\eta'')^2.
$$
The linear term is
$$
\int_0^1
\left(
360x^2\eta
-
2f_*''\eta''
\right)dx.
$$
Integrating the second term by parts twice gives
$$
-2[f_*''\eta']_0^1
+
2[f_*'''\eta]_0^1
-
2\int_0^1f_*^{(4)}\eta\,dx.
$$
The boundary terms vanish by the conditions on $\eta$, and step <1>3 gives
$$
360x^2-2f_*^{(4)}=0.
$$
Thus the linear contribution vanishes, leaving only
$$
-\int_0^1(\eta'')^2dx.
$$
:::

<1>11. Every nonzero admissible variation satisfies
$$
J[f]-J[f_*]<0.
$$

::: {.proof}
If
$$
\int_0^1(\eta'')^2dx=0,
$$
then $\eta''=0$, so $\eta$ is affine. The four homogeneous endpoint
conditions force $\eta\equiv0$. Thus every nonzero admissible variation has
strictly positive $\int(\eta'')^2$, and step <1>10 is strictly negative.
:::

<1>12. Therefore $f_*$ is the unique strict maximizer of $J$.

::: {.proof}
Step <1>11 shows every other admissible function has smaller functional value.
:::

<1>13. Its value is
$$
\boxed{J[f_*]=-59}.
$$

::: {.proof}
For the function in step <1>9,
$$
360x^2f_*-(f_*'')^2
=
-45x^8
+
270x^5
-
900x^4
+
360x^3
-
81x^2
+
108x
-
36.
$$
Integrating term by term on $[0,1]$ gives
$$
-5+45-180+90-27+54-36
=
-59.
$$
:::

<1>14. Q.E.D.

::: {.proof}
Steps <1>9, <1>12, and <1>13 give the extremizing function, its type, and
its value.
:::
:::
