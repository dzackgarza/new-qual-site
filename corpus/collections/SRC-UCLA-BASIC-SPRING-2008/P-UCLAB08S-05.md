---
schema: qual/card@1
id: P-UCLAB08S-05
kind: problem
title: Vanishing square integrals and equality of mixed partials
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 5 of the retained UCLA Basic Examination, Spring 2008.
---
::: {.problem}

::: pf

::: {.pf-step #p1-s1}

Let $F\colon\RR^2\to\RR$ be continuous.
Suppose that for every square $S$ whose sides are parallel to the coordinate axes,
\[
\iint_S F(x,y)\,dx\,dy=0.
\]
Prove that $F(x,y)=0$ for all $(x,y)$.

:::

::: pf-step

Suppose $f$, $f_x$, $f_y$, $(f_x)_y$, and $(f_y)_x$ are continuous on $\RR^2$.

:::

:::

Use step [](#p1-s1){.pf-ref} to prove
\[
\frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right)
=
\frac{\partial}{\partial x}\left(\frac{\partial f}{\partial y}\right).
\]
You may use Fubini's theorem for the rectangular integrals involved.
:::

::: {.solution}

::: pf

::: {.pf-step #p2-s1}

Suppose
\[
F(p)>0
\]
at some point
\[
p=(x_0,y_0)\in\RR^2.
\]
Then there exists an axis-parallel square $S$ on which
\[
F>0.
\]

::: pf-proof

By continuity of $F$ at $p$, choose $\delta>0$ such that
\[
|F(x,y)-F(p)|
<
\frac12F(p)
\]
whenever
\[
\|(x,y)-p\|_2<\delta.
\]
Then
\[
F(x,y)>\frac12F(p)>0
\]
throughout the open ball
\[
B(p,\delta).
\]
Choose any sufficiently small closed square with sides parallel to the coordinate axes and contained in this ball.
On that square, $F$ is strictly positive.

:::

:::

::: {.pf-step #p2-s2}

The situation in step [](#p2-s1){.pf-ref} contradicts the hypothesis
\[
\iint_SF=0
\]
for every axis-parallel square.

::: pf-proof

On the compact square $S$ from step [](#p2-s1){.pf-ref}, the continuous function $F$ is positive.
Hence it has a positive minimum
\[
m>0.
\]
Therefore
\[
\iint_SF(x,y)\,dx\,dy
\ge
m\,\operatorname{area}(S)
>
0,
\]
contradicting the assumed zero integral.

:::

:::

::: {.pf-step #p2-s3}

No point can satisfy
\[
F(p)<0.
\]

::: pf-proof

Apply steps [](#p2-s1){.pf-ref} and [](#p2-s2){.pf-ref} to the continuous function
\[
-F.
\]
If
\[
F(p)<0,
\]
then
\[
(-F)(p)>0,
\]
so some square would have
\[
\iint_S(-F)>0,
\]
equivalently
\[
\iint_SF<0,
\]
again contradicting the hypothesis.

:::

:::

::: {.pf-step #p2-s4}

Therefore
\[
\boxed{F\equiv0}.
\]

::: pf-proof

At every point $p$, steps [](#p2-s2){.pf-ref} and [](#p2-s3){.pf-ref} rule out both
\[
F(p)>0
\]
and
\[
F(p)<0.
\]
Thus
\[
F(p)=0
\]
for every $p\in\RR^2$.
This proves part step [](#p2-s1){.pf-ref}.

:::

:::

::: {.pf-step #p2-s5}

For part step [](#p2-s2){.pf-ref}, define
\[
G(x,y)
=
(f_x)_y(x,y)
-
(f_y)_x(x,y).
\]
Then $G$ is continuous.

::: pf-proof

Both mixed partial derivatives are continuous by hypothesis, so their difference is continuous.

:::

:::

::: {.pf-step #p2-s6}

Let
\[
R=[a,b]\times[c,d]
\]
be any axis-parallel rectangle.
Then
\[
\iint_R(f_x)_y(x,y)\,dx\,dy
=
f(b,d)-f(a,d)-f(b,c)+f(a,c).
\]

::: pf-proof

Use Fubini and the fundamental theorem of calculus:
\[
\begin{aligned}
\iint_R(f_x)_y\,dx\,dy
&=
\int_a^b
\left(
\int_c^d(f_x)_y(x,y)\,dy
\right)\,dx\\
&=
\int_a^b
\bigl(
f_x(x,d)-f_x(x,c)
\bigr)\,dx\\
&=
\bigl(
f(b,d)-f(a,d)
\bigr)
-
\bigl(
f(b,c)-f(a,c)
\bigr).
\end{aligned}
\]
Rearranging gives the stated expression.

:::

:::

::: {.pf-step #p2-s7}

For the same rectangle,
\[
\iint_R(f_y)_x(x,y)\,dx\,dy
=
f(b,d)-f(a,d)-f(b,c)+f(a,c).
\]

::: pf-proof

Integrate in the other order:
\[
\begin{aligned}
\iint_R(f_y)_x\,dx\,dy
&=
\int_c^d
\left(
\int_a^b(f_y)_x(x,y)\,dx
\right)\,dy\\
&=
\int_c^d
\bigl(
f_y(b,y)-f_y(a,y)
\bigr)\,dy\\
&=
\bigl(
f(b,d)-f(b,c)
\bigr)
-
\bigl(
f(a,d)-f(a,c)
\bigr),
\end{aligned}
\]
which is the same quantity as in step [](#p2-s6){.pf-ref}.

:::

:::

::: {.pf-step #p2-s8}

Therefore
\[
\iint_R G(x,y)\,dx\,dy=0
\]
for every axis-parallel rectangle, and hence for every axis-parallel square.

::: pf-proof

Subtract the equal identities from steps [](#p2-s6){.pf-ref} and [](#p2-s7){.pf-ref}.

:::

:::

::: {.pf-step #p2-s9}

One has
\[
\boxed{
(f_x)_y
=
(f_y)_x
}
\]
everywhere on $\RR^2$.

::: pf-proof

The function $G$ is continuous by step [](#p2-s5){.pf-ref} and has zero integral over every axis-parallel square by step [](#p2-s8){.pf-ref}.
Part step [](#p2-s1){.pf-ref}, proved in step [](#p2-s4){.pf-ref}, therefore gives
\[
G\equiv0.
\]
Thus
\[
(f_x)_y=(f_y)_x.
\]

:::

:::

::: pf-qed

Step [](#p2-s4){.pf-ref} proves part step [](#p2-s1){.pf-ref}, and step [](#p2-s9){.pf-ref} proves part step [](#p2-s2){.pf-ref}.

:::

:::

:::
