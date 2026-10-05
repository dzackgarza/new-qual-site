---
schema: qual/card@1
id: P-UCLAB11S-10
kind: problem
title: Differentiability from continuous partial derivatives
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 10 of the retained UCLA Basic Examination, Spring 2011.
---

::: {.problem}
Let $f$ be defined on an open set $G\subset\mathbb R^2$, and let $(x_0,y_0)\in G$.

<1>1. Define what it means for $f$ to be differentiable at $(x_0,y_0)$.
<1>2. Prove that if $\partial f/\partial x$ and $\partial f/\partial y$ exist and are continuous on an open neighborhood of $(x_0,y_0)$, then $f$ is differentiable at $(x_0,y_0)$.
:::

::: {.solution}
<1>1. The function $f$ is differentiable at
\[
p_0=(x_0,y_0)
\]
if there exists a linear map
\[
L:\mathbb R^2\to\mathbb R
\]
such that
\[
\boxed{
\lim_{h\to0}
\frac{
|f(p_0+h)-f(p_0)-L(h)|
}{
\|h\|_2
}
=0.
}
\]

::: {.proof}
This is the definition of Fréchet differentiability.
When $f_x$ and $f_y$ exist at $p_0$, the only possible derivative is
\[
L(h,k)
=
f_x(x_0,y_0)h
+
f_y(x_0,y_0)k.
\]
:::

<1>2. Let
\[
\varepsilon>0.
\]
By continuity of $f_x$ and $f_y$ at $(x_0,y_0)$, there exists $\delta>0$ such that whenever
\[
\|(x,y)-(x_0,y_0)\|_2<\delta,
\]
one has
\[
|f_x(x,y)-f_x(x_0,y_0)|<\varepsilon
\]
and
\[
|f_y(x,y)-f_y(x_0,y_0)|<\varepsilon.
\]

::: {.proof}
Both partial derivatives are continuous on a neighborhood of $(x_0,y_0)$ by hypothesis.
Choose a ball centered at $(x_0,y_0)$ contained in that neighborhood and small enough that both displayed inequalities hold there.
:::

<1>3. For sufficiently small $h,k$, there exists $\xi$ between $x_0$ and $x_0+h$ such that
\[
f(x_0+h,y_0+k)-f(x_0,y_0+k)
=
f_x(\xi,y_0+k)\,h.
\]

::: {.proof}
Fix $k$ and apply the one-variable mean value theorem to the function
\[
x\longmapsto f(x,y_0+k)
\]
on the interval with endpoints $x_0$ and $x_0+h$.
The required partial derivative exists and is continuous in the chosen neighborhood.
:::

<1>4. For sufficiently small $k$, there exists $\eta$ between $y_0$ and $y_0+k$ such that
\[
f(x_0,y_0+k)-f(x_0,y_0)
=
f_y(x_0,\eta)\,k.
\]

::: {.proof}
Apply the one-variable mean value theorem to
\[
y\longmapsto f(x_0,y)
\]
between $y_0$ and $y_0+k$.
:::

<1>5. Therefore
\[
\begin{aligned}
&f(x_0+h,y_0+k)-f(x_0,y_0)\\
&\qquad=
f_x(\xi,y_0+k)h
+
f_y(x_0,\eta)k.
\end{aligned}
\]

::: {.proof}
Add the identities from steps <1>3 and <1>4:
\[
\begin{aligned}
f(x_0+h,y_0+k)-f(x_0,y_0)
&=
\bigl[
f(x_0+h,y_0+k)-f(x_0,y_0+k)
\bigr]\\
&\quad+
\bigl[
f(x_0,y_0+k)-f(x_0,y_0)
\bigr].
\end{aligned}
\]
:::

<1>6. Let
\[
L(h,k)
=
f_x(x_0,y_0)h
+
f_y(x_0,y_0)k.
\]
Then
\[
\begin{aligned}
R(h,k)
&:=
f(x_0+h,y_0+k)-f(x_0,y_0)-L(h,k)\\
&=
\bigl(
f_x(\xi,y_0+k)-f_x(x_0,y_0)
\bigr)h\\
&\quad+
\bigl(
f_y(x_0,\eta)-f_y(x_0,y_0)
\bigr)k.
\end{aligned}
\]

::: {.proof}
Subtract
\[
f_x(x_0,y_0)h+f_y(x_0,y_0)k
\]
from the identity in step <1>5 and collect coefficients of $h$ and $k$.
:::

<1>7. If
\[
\sqrt{h^2+k^2}<\delta/2,
\]
then
\[
|R(h,k)|
\le
\varepsilon(|h|+|k|).
\]

::: {.proof}
The intermediate point
\[
(\xi,y_0+k)
\]
lies within distance less than $\delta$ of $(x_0,y_0)$ when $(h,k)$ is sufficiently small, and likewise for
\[
(x_0,\eta).
\]
Hence step <1>2 gives
\[
|f_x(\xi,y_0+k)-f_x(x_0,y_0)|<\varepsilon
\]
and
\[
|f_y(x_0,\eta)-f_y(x_0,y_0)|<\varepsilon.
\]
Apply the triangle inequality to step <1>6.
:::

<1>8. One has
\[
\frac{|R(h,k)|}{\sqrt{h^2+k^2}}
\le
\sqrt2\,\varepsilon
\]
for all sufficiently small nonzero $(h,k)$.

::: {.proof}
By Cauchy--Schwarz,
\[
|h|+|k|
\le
\sqrt2\,\sqrt{h^2+k^2}.
\]
Combine this with step <1>7 and divide by the positive denominator.
:::

<1>9. Therefore
\[
\lim_{(h,k)\to(0,0)}
\frac{
|f(x_0+h,y_0+k)-f(x_0,y_0)-L(h,k)|
}{
\sqrt{h^2+k^2}
}
=0.
\]

::: {.proof}
The number $\varepsilon>0$ in steps <1>2--<1>8 was arbitrary.
Thus for every positive tolerance, the quotient is eventually bounded by a constant multiple of that tolerance.
Equivalently, given $\eta>0$, begin the argument with
\[
\varepsilon=\frac{\eta}{\sqrt2}.
\]
Then the quotient is eventually less than $\eta$.
:::

<1>10. Hence $f$ is differentiable at $(x_0,y_0)$, with
\[
\boxed{
Df(x_0,y_0)(h,k)
=
f_x(x_0,y_0)h
+
f_y(x_0,y_0)k.
}
\]

::: {.proof}
Step <1>9 is exactly the differentiability criterion from step <1>1 for the linear map $L$ defined in step <1>6.
:::

<1>11. Q.E.D.

::: {.proof}
Step <1>1 answers part <1>1, and steps <1>2--<1>10 prove part <1>2.
:::
:::
