---
schema: qual/card@1
id: P-UCLAB12-06
kind: problem
title: Equality of mixed partial derivatives via vanishing integrals over squares
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
(a) Let $F(x, y)$ be a continuous function on the plane such that for every square $S$ having its sides parallel to the axes, $\iint_S F(x, y)\,dx\,dy = 0$. Prove $F(x, y) = 0$ for all $(x, y)$.

(b) Assume $f(x, y)$, $\frac{\partial f(x, y)}{\partial x}$, $\frac{\partial f(x, y)}{\partial y}$, $\frac{\partial}{\partial y}\Big(\frac{\partial f(x, y)}{\partial x}\Big)$ and $\frac{\partial}{\partial x}\Big(\frac{\partial f(x, y)}{\partial y}\Big)$ are all continuous in the plane.
Use part (a) to prove that

$$
\frac{\partial}{\partial y}\Big(\frac{\partial f(x, y)}{\partial x}\Big) = \frac{\partial}{\partial x}\Big(\frac{\partial f(x, y)}{\partial y}\Big).
$$

Hint: You may assume the double integral in (a) equals the iterated integral $\int\Big(\int F(x, y)\,dx\Big)dy$ and equals the iterated integral $\int\Big(\int F(x, y)\,dy\Big)dx$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Under the hypotheses of part (a), one has
$$
\boxed{F(x,y)=0}
$$
for every $(x,y)\in\RR^2$.


::: pf-proof

Fix $(x_0,y_0)\in\RR^2$. Suppose, for contradiction, that
$$
F(x_0,y_0)>0.
$$
By continuity, there exists $\delta>0$ such that
$$
F(x,y)>\frac12F(x_0,y_0)>0
$$
whenever
$$
|x-x_0|<\delta,
\qquad
|y-y_0|<\delta.
$$
Choose a square $S$ centered at $(x_0,y_0)$ with sides parallel to the axes and contained in this neighborhood. Then
$$
\iint_S F(x,y)\,dx\,dy>0,
$$
contradicting the hypothesis that the integral over every such square is zero.

The case
$$
F(x_0,y_0)<0
$$
is identical, giving a square on which $F<0$ and hence a strictly negative integral. Therefore neither sign is possible, so
$$
F(x_0,y_0)=0.
$$
Since the point was arbitrary, $F\equiv0$.

:::

:::

::: {.pf-step #s1-2}

Define
$$
G(x,y)
=
\frac{\partial}{\partial y}
\left(\frac{\partial f}{\partial x}\right)(x,y)
-
\frac{\partial}{\partial x}
\left(\frac{\partial f}{\partial y}\right)(x,y).
$$
Then $G$ is continuous.


::: pf-proof

Both mixed partial derivatives appearing in the definition are continuous by hypothesis, so their difference is continuous.

:::

:::

::: {.pf-step #s1-3}

Let
$$
S=[a,b]\times[c,d]
$$
be any square with sides parallel to the axes. Then
$$
\iint_S
\frac{\partial}{\partial y}
\left(\frac{\partial f}{\partial x}\right)
\,dx\,dy
=
f(b,d)-f(a,d)-f(b,c)+f(a,c).
$$


::: pf-proof

Using the permitted iterated-integral interpretation,
$$
\begin{aligned}
\iint_S
(f_x)_y\,dx\,dy
&=
\int_a^b
\left(
\int_c^d
(f_x)_y(x,y)\,dy
\right)dx\\
&=
\int_a^b
\bigl(f_x(x,d)-f_x(x,c)\bigr)\,dx\\
&=
\bigl(f(b,d)-f(a,d)\bigr)
-
\bigl(f(b,c)-f(a,c)\bigr).
\end{aligned}
$$
This is the displayed expression.

:::

:::

::: {.pf-step #s1-4}

For the same square $S$,
$$
\iint_S
\frac{\partial}{\partial x}
\left(\frac{\partial f}{\partial y}\right)
\,dx\,dy
=
f(b,d)-f(a,d)-f(b,c)+f(a,c).
$$


::: pf-proof

Using the other order of integration,
$$
\begin{aligned}
\iint_S
(f_y)_x\,dx\,dy
&=
\int_c^d
\left(
\int_a^b
(f_y)_x(x,y)\,dx
\right)dy\\
&=
\int_c^d
\bigl(f_y(b,y)-f_y(a,y)\bigr)\,dy\\
&=
\bigl(f(b,d)-f(b,c)\bigr)
-
\bigl(f(a,d)-f(a,c)\bigr),
\end{aligned}
$$
which simplifies to the same quantity as in step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

For every square $S$ with sides parallel to the axes,
$$
\iint_S G(x,y)\,dx\,dy=0.
$$


::: pf-proof

Subtract the equal values in steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{
\frac{\partial}{\partial y}
\left(\frac{\partial f}{\partial x}\right)
=
\frac{\partial}{\partial x}
\left(\frac{\partial f}{\partial y}\right)
}
$$
everywhere in the plane.


::: pf-proof

The function $G$ is continuous by step [](#s1-2){.pf-ref} and has integral zero over every axis-parallel square by step [](#s1-5){.pf-ref}. Part (a), proved in step [](#s1-1){.pf-ref}, therefore gives
$$
G\equiv0.
$$
This is exactly the stated equality of mixed partial derivatives.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves part (a), and steps [](#s1-2){.pf-ref} through [](#s1-6){.pf-ref} prove part (b).

:::

:::

:::
