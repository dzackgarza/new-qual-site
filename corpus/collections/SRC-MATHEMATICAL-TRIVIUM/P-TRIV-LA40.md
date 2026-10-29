---
schema: qual/card@1
id: P-TRIV-LA40
kind: problem
title: Homogeneous linear systems and their solution spaces
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 40, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Labeled part (b) and cleaned both systems against Linear Algebra Problem 40 on page 6 of the source PDF.
---

::: {.problem}
Solve the following systems of linear equations

(a) $\begin{cases} x + y + z = 0 \\ x + 2y + 3z = 0 \\ 2x + 3y + 4z = 0 \end{cases}$

(b) $\begin{cases} x_1 + x_2 + x_3 - x_4 = 0 \\ 3x_1 + 2x_2 + x_3 - x_5 = 0 \end{cases}$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

In part (a), subtracting the first equation from the second gives
$$
y+2z=0.
$$


::: pf-proof

One has
$$
(x+2y+3z)-(x+y+z)=y+2z.
$$
Both original left-hand sides equal $0$.

:::

:::

::: {.pf-step #s1-2}

Hence
$$
y=-2z.
$$


::: pf-proof

Rearrange the equation from step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

Substituting into the first equation gives
$$
x=z.
$$


::: pf-proof

The first equation becomes
$$
x-2z+z=0,
$$
so
$$
x=z.
$$

:::

:::

::: pf-step

The third equation is then automatically satisfied.


::: pf-proof

Substitute
$$
x=z,
\qquad
y=-2z:
$$

$$
2x+3y+4z
=
2z-6z+4z
=0.
$$

:::

:::

::: {.pf-step #s1-5}

Therefore the solution set of part (a) is
$$
\boxed{
(x,y,z)
=
t(1,-2,1),
\qquad
t\in\RR.
}
$$


::: pf-proof

Take $t=z$ in steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

For part (b), write the two equations as
$$
x_1+x_2=-x_3+x_4
$$
and
$$
3x_1+2x_2=-x_3+x_5.
$$


::: pf-proof

Move the remaining variables to the right-hand side.

:::

:::

::: {.pf-step #s1-7}

Subtract twice the first equation in step [](#s1-6){.pf-ref} from the second to obtain
$$
x_1=x_3-2x_4+x_5.
$$


::: pf-proof

The left-hand side becomes
$$
(3x_1+2x_2)-2(x_1+x_2)=x_1.
$$
The right-hand side becomes
$$
(-x_3+x_5)-2(-x_3+x_4)
=
x_3-2x_4+x_5.
$$

:::

:::

::: {.pf-step #s1-8}

Substituting step [](#s1-7){.pf-ref} into the first equation in step [](#s1-6){.pf-ref} gives
$$
x_2=-2x_3+3x_4-x_5.
$$


::: pf-proof

One has
$$
x_2
=
-x_3+x_4-x_1.
$$
Use the expression for $x_1$ from step [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

Thus the solution set of part (b) is
$$
\boxed{
\begin{aligned}
(x_1,x_2,x_3,x_4,x_5)
&=
s(1,-2,1,0,0)\\
&\quad
+t(-2,3,0,1,0)\\
&\quad
+u(1,-1,0,0,1),
\end{aligned}
}
$$
with
$$
s,t,u\in\RR.
$$


::: pf-proof

Set
$$
s=x_3,
\qquad
t=x_4,
\qquad
u=x_5
$$
in steps [](#s1-7){.pf-ref} through [](#s1-8){.pf-ref} and collect coefficients.

:::

:::

::: pf-qed

Steps [](#s1-5){.pf-ref} and [](#s1-9){.pf-ref} give the complete solution spaces for parts (a) and (b).

:::

:::

:::
