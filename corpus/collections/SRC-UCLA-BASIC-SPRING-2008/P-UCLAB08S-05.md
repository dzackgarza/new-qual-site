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
<1>1. Let $F\colon\mathbb R^2\to\mathbb R$ be continuous.
Suppose that for every square $S$ whose sides are parallel to the coordinate axes,
\[
\iint_S F(x,y)\,dx\,dy=0.
\]
Prove that $F(x,y)=0$ for all $(x,y)$.

<1>2. Suppose $f$, $f_x$, $f_y$, $(f_x)_y$, and $(f_y)_x$ are continuous on $\mathbb R^2$.
Use <1>1 to prove
\[
\frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right)
=
\frac{\partial}{\partial x}\left(\frac{\partial f}{\partial y}\right).
\]
You may use Fubini's theorem for the rectangular integrals involved.
:::

::: {.solution}
<1>1. Suppose
\[
F(p)>0
\]
at some point
\[
p=(x_0,y_0)\in\mathbb R^2.
\]
Then there exists an axis-parallel square $S$ on which
\[
F>0.
\]

::: {.proof}
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

<1>2. The situation in step <1>1 contradicts the hypothesis
\[
\iint_SF=0
\]
for every axis-parallel square.

::: {.proof}
On the compact square $S$ from step <1>1, the continuous function $F$ is positive.
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

<1>3. No point can satisfy
\[
F(p)<0.
\]

::: {.proof}
Apply steps <1>1--<1>2 to the continuous function
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

<1>4. Therefore
\[
\boxed{F\equiv0}.
\]

::: {.proof}
At every point $p$, steps <1>2--<1>3 rule out both
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
for every $p\in\mathbb R^2$.
This proves part <1>1.
:::

<1>5. For part <1>2, define
\[
G(x,y)
=
(f_x)_y(x,y)
-
(f_y)_x(x,y).
\]
Then $G$ is continuous.

::: {.proof}
Both mixed partial derivatives are continuous by hypothesis, so their difference is continuous.
:::

<1>6. Let
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

::: {.proof}
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

<1>7. For the same rectangle,
\[
\iint_R(f_y)_x(x,y)\,dx\,dy
=
f(b,d)-f(a,d)-f(b,c)+f(a,c).
\]

::: {.proof}
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
which is the same quantity as in step <1>6.
:::

<1>8. Therefore
\[
\iint_R G(x,y)\,dx\,dy=0
\]
for every axis-parallel rectangle, and hence for every axis-parallel square.

::: {.proof}
Subtract the equal identities from steps <1>6 and <1>7.
:::

<1>9. One has
\[
\boxed{
(f_x)_y
=
(f_y)_x
}
\]
everywhere on $\mathbb R^2$.

::: {.proof}
The function $G$ is continuous by step <1>5 and has zero integral over every axis-parallel square by step <1>8.
Part <1>1, proved in step <1>4, therefore gives
\[
G\equiv0.
\]
Thus
\[
(f_x)_y=(f_y)_x.
\]
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>4 proves part <1>1, and step <1>9 proves part <1>2.
:::
:::
