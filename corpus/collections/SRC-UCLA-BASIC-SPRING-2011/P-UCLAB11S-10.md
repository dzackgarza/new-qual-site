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
Let $f$ be defined on an open set $G\subset\RR^2$, and let $(x_0,y_0)\in G$.

::: pf

::: pf-step

Define what it means for $f$ to be differentiable at $(x_0,y_0)$.

:::

::: pf-step

Prove that if $\partial f/\partial x$ and $\partial f/\partial y$ exist and are continuous on an open neighborhood of $(x_0,y_0)$, then $f$ is differentiable at $(x_0,y_0)$.

:::

:::

:::

::: {.solution}

::: pf

::: {.pf-step #p2-s1}

The function $f$ is differentiable at
$$
p_0=(x_0,y_0)
$$
if there exists a linear map
$$
L:\RR^2\to\RR
$$
such that
$$
\boxed{
\lim_{h\to0}
\frac{
\abs{f(p_0+h)-f(p_0)-L(h)}
}{
\norm{h}_2
}
=0.
}
$$

::: pf-proof

This is the definition of Fréchet differentiability.
When $f_x$ and $f_y$ exist at $p_0$, the only possible derivative is
$$
L(h,k)
=
f_x(x_0,y_0)h
+
f_y(x_0,y_0)k.
$$

:::

:::

::: {.pf-step #p2-s2}

Let
$$
\varepsilon>0.
$$
By continuity of $f_x$ and $f_y$ at $(x_0,y_0)$, there exists $\delta>0$ such that whenever
$$
\norm{(x,y)-(x_0,y_0)}_2<\delta,
$$
one has
$$
\abs{f_x(x,y)-f_x(x_0,y_0)}<\varepsilon
$$
and
$$
\abs{f_y(x,y)-f_y(x_0,y_0)}<\varepsilon.
$$

::: pf-proof

Both partial derivatives are continuous on a neighborhood of $(x_0,y_0)$ by hypothesis.
Choose a ball centered at $(x_0,y_0)$ contained in that neighborhood and small enough that both displayed inequalities hold there.

:::

:::

::: {.pf-step #p2-s3}

For sufficiently small $h,k$, there exists $\xi$ between $x_0$ and $x_0+h$ such that
$$
f(x_0+h,y_0+k)-f(x_0,y_0+k)
=
f_x(\xi,y_0+k)\,h.
$$

::: pf-proof

Fix $k$ and apply the one-variable mean value theorem to the function
$$
x\longmapsto f(x,y_0+k)
$$
on the interval with endpoints $x_0$ and $x_0+h$.
The required partial derivative exists and is continuous in the chosen neighborhood.

:::

:::

::: {.pf-step #p2-s4}

For sufficiently small $k$, there exists $\eta$ between $y_0$ and $y_0+k$ such that
$$
f(x_0,y_0+k)-f(x_0,y_0)
=
f_y(x_0,\eta)\,k.
$$

::: pf-proof

Apply the one-variable mean value theorem to
$$
y\longmapsto f(x_0,y)
$$
between $y_0$ and $y_0+k$.

:::

:::

::: {.pf-step #p2-s5}

Therefore
$$
\begin{aligned}
&f(x_0+h,y_0+k)-f(x_0,y_0)\\
&\qquad=
f_x(\xi,y_0+k)h
+
f_y(x_0,\eta)k.
\end{aligned}
$$

::: pf-proof

Add the identities from steps [](#p2-s3){.pf-ref} and [](#p2-s4){.pf-ref}:
$$
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
$$

:::

:::

::: {.pf-step #p2-s6}

Let
$$
L(h,k)
=
f_x(x_0,y_0)h
+
f_y(x_0,y_0)k.
$$
Then
$$
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
$$

::: pf-proof

Subtract
$$
f_x(x_0,y_0)h+f_y(x_0,y_0)k
$$
from the identity in step [](#p2-s5){.pf-ref} and collect coefficients of $h$ and $k$.

:::

:::

::: {.pf-step #p2-s7}

If
$$
\sqrt{h^2+k^2}<\delta/2,
$$
then
$$
\abs{R(h,k)}
\le
\varepsilon(\abs{h}+\abs{k}).
$$

::: pf-proof

The intermediate point
$$
(\xi,y_0+k)
$$
lies within distance less than $\delta$ of $(x_0,y_0)$ when $(h,k)$ is sufficiently small, and likewise for
$$
(x_0,\eta).
$$
Hence step [](#p2-s2){.pf-ref} gives
$$
\abs{f_x(\xi,y_0+k)-f_x(x_0,y_0)}<\varepsilon
$$
and
$$
\abs{f_y(x_0,\eta)-f_y(x_0,y_0)}<\varepsilon.
$$
Apply the triangle inequality to step [](#p2-s6){.pf-ref}.

:::

:::

::: {.pf-step #p2-s8}

One has
$$
\frac{\abs{R(h,k)}}{\sqrt{h^2+k^2}}
\le
\sqrt2\,\varepsilon
$$
for all sufficiently small nonzero $(h,k)$.

::: pf-proof

By Cauchy--Schwarz,
$$
\abs{h}+\abs{k}
\le
\sqrt2\,\sqrt{h^2+k^2}.
$$
Combine this with step [](#p2-s7){.pf-ref} and divide by the positive denominator.

:::

:::

::: {.pf-step #p2-s9}

Therefore
$$
\lim_{(h,k)\to(0,0)}
\frac{
\abs{f(x_0+h,y_0+k)-f(x_0,y_0)-L(h,k)}
}{
\sqrt{h^2+k^2}
}
=0.
$$

::: pf-proof

The number $\varepsilon>0$ in steps [](#p2-s2){.pf-ref}, [](#p2-s3){.pf-ref}, [](#p2-s4){.pf-ref}, [](#p2-s5){.pf-ref}, [](#p2-s6){.pf-ref}, [](#p2-s7){.pf-ref} and [](#p2-s8){.pf-ref} was arbitrary.
Thus for every positive tolerance, the quotient is eventually bounded by a constant multiple of that tolerance.
Equivalently, given $\eta>0$, begin the argument with
$$
\varepsilon=\frac{\eta}{\sqrt2}.
$$
Then the quotient is eventually less than $\eta$.

:::

:::

::: {.pf-step #p2-s10}

Hence $f$ is differentiable at $(x_0,y_0)$, with
$$
\boxed{
Df(x_0,y_0)(h,k)
=
f_x(x_0,y_0)h
+
f_y(x_0,y_0)k.
}
$$

::: pf-proof

Step [](#p2-s9){.pf-ref} is exactly the differentiability criterion from step [](#p2-s1){.pf-ref} for the linear map $L$ defined in step [](#p2-s6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#p2-s1){.pf-ref} answers part step [](#p2-s1){.pf-ref}, and steps [](#p2-s2){.pf-ref}, [](#p2-s3){.pf-ref}, [](#p2-s4){.pf-ref}, [](#p2-s5){.pf-ref}, [](#p2-s6){.pf-ref}, [](#p2-s7){.pf-ref}, [](#p2-s8){.pf-ref}, [](#p2-s9){.pf-ref} and [](#p2-s10){.pf-ref} prove part step [](#p2-s2){.pf-ref}.

:::

:::

:::
