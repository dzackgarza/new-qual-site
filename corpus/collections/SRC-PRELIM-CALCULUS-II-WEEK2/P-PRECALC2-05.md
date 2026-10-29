---
schema: qual/card@1
id: P-PRECALC2-05
kind: problem
title: Antiderivative of $\frac{x+2}{x^3-x^2+2x-2}$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Compute $\int { \frac { x + 2 } { x ^ { 3 } - x ^ { 2 } + 2 x - 2 } } d x .$
:::

::: {.solution}

::: pf

::: pf-step

Factor the denominator:
$$
\boxed{
x^3-x^2+2x-2
=
(x-1)(x^2+2)}.
$$


::: pf-proof

Group terms:
$$
x^3-x^2+2x-2
=
x^2(x-1)+2(x-1)
=
(x-1)(x^2+2).
$$

:::

:::

::: {.pf-step #s1-2}

Seek constants $A,B,C$ such that
$$
\frac{x+2}{(x-1)(x^2+2)}
=
\frac{A}{x-1}
+
\frac{Bx+C}{x^2+2}.
$$


::: pf-proof

The denominator has one linear factor and one irreducible quadratic factor,
so this is the standard partial-fraction form.

:::

:::

::: pf-step

Clearing denominators gives
$$
x+2
=
A(x^2+2)
+
(Bx+C)(x-1).
$$


::: pf-proof

Multiply the identity in step [](#s1-2){.pf-ref} by
$$
(x-1)(x^2+2).
$$

:::

:::

::: {.pf-step #s1-4}

Expanding the right-hand side gives
$$
x+2
=
(A+B)x^2
+
(C-B)x
+
(2A-C).
$$


::: pf-proof

$$
\begin{aligned}
A(x^2+2)+(Bx+C)(x-1)
&=
Ax^2+2A+Bx^2-Bx+Cx-C\\
&=
(A+B)x^2+(C-B)x+(2A-C).
\end{aligned}
$$

:::

:::

::: pf-step

Comparing coefficients gives
$$
A+B=0,
$$
$$
C-B=1,
$$
and
$$
2A-C=2.
$$


::: pf-proof

The polynomial on the left is
$$
0x^2+1x+2.
$$
Equate corresponding coefficients with step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

The unique solution is
$$
\boxed{
A=1,\qquad
B=-1,\qquad
C=0}.
$$


::: pf-proof

From
$$
A+B=0
$$
one gets
$$
B=-A.
$$
Then
$$
C-B=1
$$
gives
$$
C=1-A.
$$
Finally,
$$
2A-C=2
$$
becomes
$$
2A-(1-A)=2,
$$
so
$$
3A=3
$$
and $A=1$. Hence $B=-1$ and $C=0$.

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{
\frac{x+2}{x^3-x^2+2x-2}
=
\frac1{x-1}
-
\frac{x}{x^2+2}}.
$$


::: pf-proof

Substitute the coefficients from step [](#s1-6){.pf-ref} into step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

Integrating term by term,
$$
\int\frac{dx}{x-1}
=
\log|x-1|.
$$


::: pf-proof

Use the standard antiderivative
$$
\int\frac{du}{u}
=
\log|u|.
$$

:::

:::

::: {.pf-step #s1-9}

Also,
$$
\int\frac{x}{x^2+2}\,dx
=
\frac12\log(x^2+2).
$$


::: pf-proof

Set
$$
u=x^2+2,
\qquad
du=2x\,dx.
$$
Then
$$
\int\frac{x}{x^2+2}\,dx
=
\frac12\int\frac{du}{u}
=
\frac12\log u.
$$
Since
$$
x^2+2>0,
$$
no absolute value is needed.

:::

:::

::: {.pf-step #s1-10}

Hence
$$
\boxed{
\int
\frac{x+2}{x^3-x^2+2x-2}\,dx
=
\log|x-1|
-
\frac12\log(x^2+2)
+
C}.
$$


::: pf-proof

Combine steps [](#s1-7){.pf-ref} through [](#s1-9){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} is the requested antiderivative.

:::

:::

:::
