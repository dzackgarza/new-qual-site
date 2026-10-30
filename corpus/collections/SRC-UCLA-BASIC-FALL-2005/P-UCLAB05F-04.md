---
schema: qual/card@1
id: P-UCLAB05F-04
kind: problem
title: Arc length bound for a strictly concave graph
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 4 of the official UCLA Basic Examination, September 2005 PDF.
---

::: {.problem}
Suppose $F:[0,1]\to[0,1]$ is a $C^2$ function with
$$
F(0)=F(1)=0
\qquad\text{and}\qquad
F''(x)<0
$$
for all $x\in[0,1]$.
Prove that the arc length of the curve
$$
\{(x,F(x)):x\in[0,1]\}
$$
is less than $3$.

Suggestion: in the arc-length formula, use
$$
\sqrt{a^2+b^2}<\abs{a}+\abs{b}.
$$
:::

::: {.solution}

Let $L$ denote the arc length of the graph of $F$.

::: pf

::: {.pf-step #s1-1}

The derivative $F'$ is strictly decreasing on $[0,1]$.


::: pf-proof

Since
$$
F''(x)<0
$$
for every $x\in[0,1]$, the mean value theorem applied to $F'$ shows that if $x<y$, then
$$
F'(y)-F'(x)=F''(\xi)(y-x)<0
$$
for some $\xi\in(x,y)$. Hence $F'(y)<F'(x)$.

:::

:::

::: {.pf-step #s1-2}

There is a unique $c\in(0,1)$ such that
$$
F'(c)=0,
$$
with
$$
F'(x)>0\quad(0\le x<c)
$$
and
$$
F'(x)<0\quad(c<x\le1).
$$


::: pf-proof

Because
$$
F(1)-F(0)=\int_0^1F'(x)\,dx=0,
$$
$F'$ cannot be nonpositive everywhere, and it cannot be nonnegative everywhere, since by step [](#s1-1){.pf-ref} it is strictly decreasing. Thus
$$
F'(0)>0
\qquad\text{and}\qquad
F'(1)<0.
$$
Continuity of $F'$ gives a point $c\in(0,1)$ with $F'(c)=0$. Strict decrease makes this point unique and gives the stated signs.

:::

:::

::: {.pf-step #s1-3}

One has
$$
\int_0^1\abs{F'(x)}\,dx=2F(c).
$$


::: pf-proof

Using the sign information from step [](#s1-2){.pf-ref},
$$
\begin{aligned}
\int_0^1\abs{F'(x)}\,dx
&=
\int_0^cF'(x)\,dx
-
\int_c^1F'(x)\,dx\\
&=
\bigl(F(c)-F(0)\bigr)
-
\bigl(F(1)-F(c)\bigr)\\
&=
2F(c),
\end{aligned}
$$
because $F(0)=F(1)=0$.

:::

:::

::: {.pf-step #s1-4}

One has
$$
\int_0^1\abs{F'(x)}\,dx\le2.
$$


::: pf-proof

The codomain condition
$$
F:[0,1]\to[0,1]
$$
implies
$$
0\le F(c)\le1.
$$
Apply step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

The arc length satisfies
$$
L<1+\int_0^1\abs{F'(x)}\,dx.
$$


::: pf-proof

The arc-length formula gives
$$
L=\int_0^1\sqrt{1+F'(x)^2}\,dx.
$$
For every real $u$,
$$
\sqrt{1+u^2}\le1+\abs{u},
$$
with strict inequality whenever $u\ne0$. By step [](#s1-2){.pf-ref}, $F'(x)\ne0$ except at the single point $c$. Hence the inequality is strict on two intervals of positive length, so
$$
\int_0^1\sqrt{1+F'(x)^2}\,dx
<
\int_0^1\bigl(1+\abs{F'(x)}\bigr)\,dx
=
1+\int_0^1\abs{F'(x)}\,dx.
$$

:::

:::

::: {.pf-step #s1-6}

The arc length is strictly less than $3$:
$$
\boxed{L<3}.
$$


::: pf-proof

By steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref},
$$
L
<
1+\int_0^1\abs{F'(x)}\,dx
\le
1+2
=3.
$$

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required estimate.

:::

:::

:::
