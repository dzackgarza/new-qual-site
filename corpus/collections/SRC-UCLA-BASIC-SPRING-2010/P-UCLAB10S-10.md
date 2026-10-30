---
schema: qual/card@1
id: P-UCLAB10S-10
kind: problem
title: Directional derivatives without differentiability at the origin
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
  note: Checked against Problem 10 of the retained UCLA Basic Examination, Spring 2010.
---

::: {.problem}
Define
$$
f(x,y)=\frac{xy}{\sqrt{x^2+y^2}}
$$
for $(x,y)\ne(0,0)$ and set $f(0,0)=0$.

(a) Compute the directional derivatives of $f$ at $(0,0)$ in all directions where they exist.

(b) Is $f$ differentiable at $(0,0)$?
Prove your answer.
:::

::: {.solution}

Let
$$
v=(a,b)\in\RR^2
$$
be a nonzero direction vector.

::: pf

::: {.pf-step #s1-1}

For $t\ne0$,
$$
f(tv)
=
\frac{t^2ab}
{\abs{t}\sqrt{a^2+b^2}}
=
\abs{t}
\frac{ab}{\sqrt{a^2+b^2}}.
$$


::: pf-proof

Substitute
$$
(x,y)=(ta,tb)
$$
into the formula for $f$:
$$
\begin{aligned}
f(ta,tb)
&=
\frac{(ta)(tb)}
{\sqrt{t^2a^2+t^2b^2}}\\
&=
\frac{t^2ab}
{\abs{t}\sqrt{a^2+b^2}}\\
&=
\abs{t}
\frac{ab}{\sqrt{a^2+b^2}}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-2}

The two-sided directional difference quotient at the origin is
$$
\frac{f(tv)-f(0,0)}{t}
=
\frac{\abs{t}}{t}
\frac{ab}{\sqrt{a^2+b^2}}.
$$


::: pf-proof

Since
$$
f(0,0)=0,
$$
divide the formula in step [](#s1-1){.pf-ref} by $t$.

:::

:::

::: {.pf-step #s1-3}

If
$$
ab\ne0,
$$
the directional derivative in direction $v$ does not exist.


::: pf-proof

For
$$
t>0,
$$
step [](#s1-2){.pf-ref} gives
$$
\frac{f(tv)}t
=
\frac{ab}{\sqrt{a^2+b^2}}.
$$
For
$$
t<0,
$$
it gives
$$
\frac{f(tv)}t
=
-
\frac{ab}{\sqrt{a^2+b^2}}.
$$
If
$$
ab\ne0,
$$
these one-sided limits are different.
Hence the two-sided limit does not exist.

:::

:::

::: {.pf-step #s1-4}

If
$$
ab=0,
$$
then the directional derivative exists and equals
$$
\boxed{0}.
$$


::: pf-proof

When
$$
ab=0,
$$
the quotient in step [](#s1-2){.pf-ref} is identically zero for every
$$
t\ne0.
$$
Thus its limit is zero.

:::

:::

::: {.pf-step #s1-5}

Therefore the directional derivatives at the origin exist exactly in the nonzero directions parallel to one of the coordinate axes, and all such derivatives equal $0$.


::: pf-proof

For a nonzero vector
$$
v=(a,b),
$$
the condition
$$
ab=0
$$
means exactly that
$$
a=0
\quad\text{or}\quad
b=0.
$$
Apply steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref}.
This answers part (a).

:::

:::

::: {.pf-step #s1-6}

If $f$ were differentiable at $(0,0)$, then its derivative would be the zero linear map.


::: pf-proof

Differentiability implies existence of the partial derivatives, and they are the directional derivatives in the coordinate directions.
By step [](#s1-4){.pf-ref},
$$
\frac{\partial f}{\partial x}(0,0)=0
\qquad\text{and}\qquad
\frac{\partial f}{\partial y}(0,0)=0.
$$
Thus the Jacobian matrix, and hence the derivative, would have to be
$$
Df(0,0)=0.
$$

:::

:::

::: {.pf-step #s1-7}

Along the line
$$
y=x,
$$
one has
$$
\frac{\abs{f(t,t)}}
{\norm{(t,t)}_2}
=
\frac12
$$
for every
$$
t\ne0.
$$


::: pf-proof

For
$$
t\ne0,
$$
$$
f(t,t)
=
\frac{t^2}{\sqrt{2t^2}}
=
\frac{\abs{t}}{\sqrt2}.
$$
Also
$$
\norm{(t,t)}_2
=
\sqrt2\,\abs{t}.
$$
Therefore
$$
\frac{\abs{f(t,t)}}{\norm{(t,t)}_2}
=
\frac{\abs{t}/\sqrt2}{\sqrt2\abs{t}}
=
\frac12.
$$

:::

:::

::: {.pf-step #s1-8}

The function $f$ is not differentiable at $(0,0)$.


::: pf-proof

If $f$ were differentiable there, step [](#s1-6){.pf-ref} says the derivative would be zero.
The differentiability condition would then require
$$
\frac{
\abs{f(h)-f(0,0)}
}{
\norm{h}_2
}
\to0
$$
as
$$
h\to0.
$$
But step [](#s1-7){.pf-ref} shows that along
$$
h=(t,t)\to(0,0),
$$
this quotient is constantly
$$
\frac12.
$$
Therefore the required limit is not zero.
Hence
$$
\boxed{f\text{ is not differentiable at }(0,0).}
$$

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} answers part (a), and step [](#s1-8){.pf-ref} answers part (b).

:::

:::

:::
