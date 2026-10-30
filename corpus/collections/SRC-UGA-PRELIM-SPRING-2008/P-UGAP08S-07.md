---
schema: qual/card@1
id: P-UGAP08S-07
kind: problem
title: Continuity at the origin of two rational functions on $\RR^2$
classification:
  areas: [prelim]
  topics:
  - Continuity
  - Multivariable Calculus
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Determine, with proof, which, if either, of the following functions $\RR^2\to\RR$ are continuous:

(a)
$$
f(x,y)=
\begin{cases}
\dfrac{xy}{x^2+y^2},&(x,y)\ne(0,0),\\
0,&(x,y)=(0,0),
\end{cases}
$$

(b)
$$
g(x,y)=
\begin{cases}
\dfrac{x^2y}{x^2+y^2},&(x,y)\ne(0,0),\\
0,&(x,y)=(0,0).
\end{cases}
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Away from the origin, both $f$ and $g$ are continuous.


::: pf-proof

For
$$
(x,y)\ne(0,0),
$$
the denominator
$$
x^2+y^2
$$
is nonzero.
Thus each displayed formula is a quotient of polynomial functions with
nonvanishing denominator.

:::

:::

::: pf-step

Along the line
$$
y=x,
$$
with
$$
x\ne0,
$$
one has
$$
f(x,x)=\frac12.
$$


::: pf-proof

Substitute:
$$
f(x,x)
=
\frac{x^2}{x^2+x^2}
=
\frac12.
$$

:::

:::

::: {.pf-step #s1-3}

Hence
$$
f
$$
is not continuous at
$$
(0,0).
$$


::: pf-proof

Along the sequence
$$
(x_n,y_n)
=
\left(
\frac1n,\frac1n
\right),
$$
one has
$$
(x_n,y_n)\to(0,0)
$$
but
$$
f(x_n,y_n)
=
\frac12
\not\to
0
=
f(0,0).
$$
Thus the limit at the origin does not equal the defined value.

:::

:::

::: {.pf-step #s1-4}

For
$$
(x,y)\ne(0,0),
$$
$$
\abs{g(x,y)}
=
\frac{x^2\abs{y}}{x^2+y^2}
\le
\abs{y}.
$$


::: pf-proof

Since
$$
0
\le
\frac{x^2}{x^2+y^2}
\le
1,
$$
multiply by
$$
\abs{y}.
$$

:::

:::

::: {.pf-step #s1-5}

Also
$$
\abs{y}
\le
\sqrt{x^2+y^2}.
$$


::: pf-proof

Because
$$
y^2
\le
x^2+y^2,
$$
taking square roots gives the inequality.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
g(x,y)\to0
$$
as
$$
(x,y)\to(0,0).
$$


::: pf-proof

By steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref},
$$
\abs{g(x,y)}
\le
\sqrt{x^2+y^2}.
$$
The right-hand side tends to $0$ at the origin.
The squeeze theorem gives
$$
g(x,y)\to0.
$$
Since
$$
g(0,0)=0,
$$
$g$ is continuous at the origin.

:::

:::

::: {.pf-step #s1-7}

Hence
$$
\boxed{
f\text{ is not continuous on }\RR^2,
\qquad
g\text{ is continuous on }\RR^2.
}
$$


::: pf-proof

Step [](#s1-3){.pf-ref} shows $f$ fails continuity at the origin.
Step [](#s1-1){.pf-ref} gives continuity elsewhere.

Steps [](#s1-1){.pf-ref} and [](#s1-6){.pf-ref} show $g$ is continuous both away from and at the
origin.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} gives the requested classification.

:::

:::

:::
