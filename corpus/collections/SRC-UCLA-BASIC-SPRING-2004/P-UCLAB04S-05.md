---
schema: qual/card@1
id: P-UCLAB04S-05
kind: problem
title: Differentiability and a mean-value bound for vector-valued maps
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 5 of the official UCLA Basic Exam Spring 2004 PDF. The source uses $p,q$ in the estimate without explicitly naming them as the endpoints of the line segment $I$; that intended role is made explicit here.
---

::: {.problem}
Suppose $G\subset\RR^n$ is open, $f:G\to\RR^m$ is a function, and $x_0\in G$.

(a) Carefully define what is meant by the derivative
\[
f'(x_0):\RR^n\to\RR^m.
\]

(b) Let $I$ be the line segment from $p$ to $q$ contained in $G$, and suppose that $f$ is differentiable at every point of $I$.
Show that for some $c\in I$,
\[
\|f(q)-f(p)\|_2
\leq
\|f'(c)\|\,\|q-p\|_2.
\]

Hint: let $w$ be a unit vector such that
\[
\|f(q)-f(p)\|_2=(f(q)-f(p))\mathbin{\cdot}w.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The derivative
\[
f'(x_0):\RR^n\to\RR^m
\]
exists if there is a linear map
\[
L:\RR^n\to\RR^m
\]
such that
\[
\lim_{h\to0}
\frac{
\|f(x_0+h)-f(x_0)-Lh\|_2
}{
\|h\|_2
}
=0.
\]
In that case,
\[
\boxed{f'(x_0)=L}.
\]


::: pf-proof

This is the definition of Fréchet differentiability at $x_0$.
The linear map $L$, if it exists, is unique.

Indeed, if both $L_1$ and $L_2$ satisfy the limit condition, then for any nonzero $u\in\RR^n$ and scalar $t\ne0$,
\[
\|(L_1-L_2)u\|
\le
\frac{\|f(x_0+tu)-f(x_0)-tL_1u\|}{|t|}
+
\frac{\|f(x_0+tu)-f(x_0)-tL_2u\|}{|t|}.
\]
Letting $t\to0$ gives
\[
(L_1-L_2)u=0.
\]
Thus $L_1=L_2$.

:::

:::

::: {.pf-step #s1-2}

Suppose
\[
f(q)=f(p).
\]
Then the estimate in part (b) holds for every
\[
c\in I.
\]


::: pf-proof

The left-hand side is
\[
\|f(q)-f(p)\|_2=0,
\]
while the right-hand side is nonnegative.

:::

:::

::: {.pf-step #s1-3}

Suppose now that
\[
f(q)\ne f(p).
\]
Define
\[
w=
\frac{f(q)-f(p)}
{\|f(q)-f(p)\|_2}.
\]
Then
\[
\|w\|_2=1
\]
and
\[
(f(q)-f(p))\cdot w
=
\|f(q)-f(p)\|_2.
\]


::: pf-proof

The vector is well-defined because
\[
f(q)-f(p)\ne0.
\]
Its norm is $1$ by construction, and
\[
\begin{aligned}
(f(q)-f(p))\cdot w
&=
\frac{
\|f(q)-f(p)\|_2^2
}{
\|f(q)-f(p)\|_2
}\\
&=
\|f(q)-f(p)\|_2.
\end{aligned}
\]

:::

:::

::: {.pf-step #s1-4}

Parametrize the segment $I$ by
\[
\gamma(t)=p+t(q-p),
\qquad
0\le t\le1,
\]
and define
\[
\phi(t)=f(\gamma(t))\cdot w.
\]
Then $\phi$ is differentiable on $(0,1)$ and continuous on $[0,1]$.


::: pf-proof

The map $\gamma$ is smooth and has image equal to the segment $I$.
By hypothesis, $f$ is differentiable at every point of $I$.
Differentiability implies continuity, so $f\circ\gamma$ is continuous on $[0,1]$ and differentiable on $(0,1)$.
Taking the Euclidean inner product with the fixed vector $w$ preserves these properties.

:::

:::

::: {.pf-step #s1-5}

There exists
\[
t_0\in(0,1)
\]
such that
\[
\phi(1)-\phi(0)
=
\phi'(t_0).
\]


::: pf-proof

Apply the one-variable mean value theorem to $\phi$ on $[0,1]$.
Since the interval length is $1$,
\[
\phi(1)-\phi(0)
=
\phi'(t_0)(1-0)
=
\phi'(t_0)
\]
for some $t_0\in(0,1)$.

:::

:::

::: {.pf-step #s1-6}

If
\[
c=\gamma(t_0),
\]
then
\[
\phi'(t_0)
=
\bigl(f'(c)(q-p)\bigr)\cdot w.
\]


::: pf-proof

The chain rule gives
\[
(f\circ\gamma)'(t_0)
=
f'(c)\gamma'(t_0).
\]
Since
\[
\gamma'(t)=q-p,
\]
one has
\[
(f\circ\gamma)'(t_0)
=
f'(c)(q-p).
\]
Differentiating the scalar product with the constant vector $w$ gives
\[
\phi'(t_0)
=
\bigl(f'(c)(q-p)\bigr)\cdot w.
\]

:::

:::

::: {.pf-step #s1-7}

One has
\[
\|f(q)-f(p)\|_2
\le
\|f'(c)\|\,\|q-p\|_2.
\]


::: pf-proof

By steps [](#s1-3){.pf-ref} and [](#s1-5){.pf-ref}, and [](#s1-6){.pf-ref},
\[
\begin{aligned}
\|f(q)-f(p)\|_2
&=
(f(q)-f(p))\cdot w\\
&=
\phi(1)-\phi(0)\\
&=
\bigl(f'(c)(q-p)\bigr)\cdot w.
\end{aligned}
\]
By Cauchy--Schwarz,
\[
\bigl(f'(c)(q-p)\bigr)\cdot w
\le
\|f'(c)(q-p)\|_2\,\|w\|_2.
\]
Since
\[
\|w\|_2=1,
\]
and by the definition of the operator norm,
\[
\|f'(c)(q-p)\|_2
\le
\|f'(c)\|\,\|q-p\|_2.
\]
Combining the inequalities proves the claim.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} answers part (a).
Step [](#s1-2){.pf-ref} handles the case $f(q)=f(p)$ in part (b), and steps [](#s1-3){.pf-ref} through [](#s1-7){.pf-ref} prove the estimate when $f(q)\ne f(p)$.

:::

:::

:::
