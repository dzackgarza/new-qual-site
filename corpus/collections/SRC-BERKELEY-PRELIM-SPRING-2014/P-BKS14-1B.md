---
schema: qual/card@1
id: P-BKS14-1B
kind: problem
title: Failure of a vector-valued mean value theorem for gradients
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
  note: Checked against the vendored UC Berkeley Spring 2014 preliminary examination PDF.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the unit-gradient formula, nonconstancy of its direction, and the strict norm bound for its average.
---

::: {.problem}
Let $f:[0,1]^2\to\RR$ be the distance to a fixed point outside the unit square.
Show that there is no point $(x_0,y_0)$ in the square at which $\nabla f(x_0,y_0)$ equals the average value of $\nabla f$ over the square.
Thus the obvious analogue of the mean value theorem for functions of two variables is false.

Hint: first determine the length of $\nabla f$.
:::

::: {.solution}
Let
$$
D=[0,1]^2
$$
and let
$$
p\in\RR^2\setminus D
$$
be the fixed point. Thus
$$
f(x)=\norm{x-p}
$$
for $x\in D$.

<1>1. For every $x\in D$,
$$
\nabla f(x)
=
\frac{x-p}{\norm{x-p}},
$$
and therefore
$$
\norm{\nabla f(x)}=1.
$$

::: {.proof}
Because $p\notin D$, the denominator never vanishes on $D$. Differentiating
the Euclidean norm gives
$$
\nabla\norm{x-p}
=
\frac{x-p}{\norm{x-p}}.
$$
The displayed vector is a normalized nonzero vector, so its norm is $1$.
:::

<1>2. The vector field
$$
v(x)\coloneqq\nabla f(x)
$$
is not constant on $D$.

::: {.proof}
If $v$ were constant, then all vectors
$$
x-p,
\qquad
x\in D,
$$
would point in the same direction. Hence every point of $D$ would lie on
one line through $p$, which is impossible because the square contains
three noncollinear points.
:::

<1>3. Let
$$
c
\coloneqq
\int_Dv(x)\,dx
$$
be the average value of the gradient. Then
$$
\norm{c}<1.
$$

::: {.proof}
The square has area $1$, so its integral is its average.

If $c=0$, the conclusion is immediate. Suppose $c\neq0$ and set
$$
u\coloneqq\frac{c}{\norm{c}}.
$$
For every $x\in D$, Cauchy--Schwarz and step <1>1 give
$$
u\cdot v(x)
\leq
\norm{u}\norm{v(x)}
=
1.
$$
Equality holds only when $v(x)=u$, because both are unit vectors.

By step <1>2, $v$ is not identically equal to $u$. Hence there is some
$x_1\in D$ with
$$
u\cdot v(x_1)<1.
$$
Continuity of $v$ gives a relatively open neighborhood of $x_1$ in $D$
on which the inequality remains strict by a fixed positive amount. That
neighborhood has positive area. Consequently
$$
\int_Du\cdot v(x)\,dx
<
\int_D1\,dx
=
1.
$$
But
$$
\int_Du\cdot v(x)\,dx
=
u\cdot c
=
\norm{c}.
$$
Thus $\norm{c}<1$.
:::

<1>4. There is no point
$$
(x_0,y_0)\in D
$$
such that
$$
\nabla f(x_0,y_0)=c.
$$

::: {.proof}
By step <1>1, every pointwise gradient has norm $1$. By step <1>3, the
average vector $c$ has norm strictly less than $1$. Therefore they cannot
be equal.
:::

<1>5. Hence the proposed multivariable analogue of the mean value theorem
fails.

::: {.proof}
Step <1>4 gives exactly the counterexample requested in the problem.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 proves the claim.
:::
:::
