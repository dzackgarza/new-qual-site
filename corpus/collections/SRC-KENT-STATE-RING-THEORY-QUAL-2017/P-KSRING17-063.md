---
schema: qual/card@1
id: P-KSRING17-063
kind: problem
title: 'Primary ideals: zero divisors in the quotient and prime radicals'
classification:
  areas: [algebra]
  topics:
  - Primary Ideals
  - Radical of an Ideal
  - Zero Divisors
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 63 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let $R$ be a commutative ring with $1$. An ideal $I$ of $R$ is called a primary ideal if $I \neq R$ and for all $x, y \in R$ with $xy \in I$, either $x \in I$ or $y^{n} \in I$ for some integer $n \geqslant 1$.

(a) Show that an ideal $I$ of $R$ is primary if and only if $R/I \ne 0$ and every zero-divisor in $R/I$ is nilpotent.

(b) Show that if $I$ is a primary ideal of $R$ then the radical $\operatorname{Rad}(I)$ of $I$ is a prime ideal. (Recall that $\operatorname{Rad}(I) = \{x \in R \st x^{n} \in I \text{ for some } n\}$.)
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Assume $I$ is primary. Then
$$
R/I\ne0.
$$


::: pf-proof

By definition, a primary ideal satisfies
$$
I\ne R.
$$
Hence the quotient ring
$$
R/I
$$
is nonzero.

:::

:::

::: {.pf-step #s1-2}

Assume $I$ is primary and let
$$
\overline y
\in
R/I
$$
be a zero divisor. Then
$$
\overline y
$$
is nilpotent.


::: pf-proof

Because
$$
\overline y
$$
is a zero divisor, there exists
$$
0\ne\overline x\in R/I
$$
such that
$$
\overline x\,\overline y=0.
$$
Choose representatives
$$
x,y\in R.
$$
Then
$$
xy\in I.
$$
Also
$$
\overline x\ne0
$$
means
$$
x\notin I.
$$

Since $I$ is primary and
$$
xy\in I
$$
with
$$
x\notin I,
$$
there exists
$$
n\ge1
$$
such that
$$
y^n\in I.
$$
Therefore
$$
\overline y^{\,n}
=
\overline{y^n}
=
0,
$$
so
$$
\overline y
$$
is nilpotent.

:::

:::

::: {.pf-step #s1-3}

Hence if $I$ is primary, then
$$
\boxed{
R/I\ne0
\text{ and every zero divisor of }R/I\text{ is nilpotent}.
}
$$


::: pf-proof

Combine steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

Conversely, assume
$$
R/I\ne0
$$
and every zero divisor of
$$
R/I
$$
is nilpotent.
Then
$$
I\ne R.
$$


::: pf-proof

If
$$
I=R,
$$
then
$$
R/I=0,
$$
contrary to the hypothesis.

:::

:::

::: {.pf-step #s1-5}

Suppose
$$
xy\in I
$$
and
$$
x\notin I.
$$
Then
$$
\overline y
\in
R/I
$$
is a zero divisor.


::: pf-proof

In the quotient,
$$
\overline x\,\overline y
=
\overline{xy}
=
0.
$$
Because
$$
x\notin I,
$$
one has
$$
\overline x\ne0.
$$
Thus
$$
\overline y
$$
is annihilated by a nonzero element and is therefore a zero divisor.

:::

:::

::: {.pf-step #s1-6}

Under the assumptions of step [](#s1-5){.pf-ref}, there exists
$$
n\ge1
$$
such that
$$
y^n\in I.
$$


::: pf-proof

By step [](#s1-5){.pf-ref},
$$
\overline y
$$
is a zero divisor.
By hypothesis, every zero divisor in
$$
R/I
$$
is nilpotent.
Therefore
$$
\overline y^{\,n}=0
$$
for some
$$
n\ge1.
$$
Equivalently,
$$
y^n\in I.
$$

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{
I\text{ is primary}
\iff
R/I\ne0
\text{ and every zero divisor of }R/I\text{ is nilpotent}.
}
$$


::: pf-proof

The forward implication is step [](#s1-3){.pf-ref}.
For the converse, step [](#s1-4){.pf-ref} gives
$$
I\ne R,
$$
and steps [](#s1-5){.pf-ref} through [](#s1-6){.pf-ref} give the defining primary condition.

:::

:::

::: {.pf-step #s1-8}

Now assume $I$ is primary and set
$$
\sqrt I
\coloneqq
\{x\in R:x^n\in I\text{ for some }n\ge1\}.
$$
Then
$$
\sqrt I
\ne
R.
$$


::: pf-proof

If
$$
1\in\sqrt I,
$$
then
$$
1^n=1\in I
$$
for some
$$
n\ge1.
$$
This would imply
$$
I=R,
$$
contradicting primaryness.
Thus
$$
1\notin\sqrt I.
$$

:::

:::

::: {.pf-step #s1-9}

Suppose
$$
xy\in\sqrt I.
$$
Then
$$
x\in\sqrt I
\quad\text{or}\quad
y\in\sqrt I.
$$


::: pf-proof

Because
$$
xy\in\sqrt I,
$$
there exists
$$
n\ge1
$$
such that
$$
(xy)^n
=
x^ny^n
\in
I.
$$
Since $I$ is primary, either
$$
x^n\in I
$$
or there exists
$$
m\ge1
$$
such that
$$
(y^n)^m
=
y^{nm}
\in
I.
$$
In the first case,
$$
x\in\sqrt I.
$$
In the second,
$$
y\in\sqrt I.
$$

:::

:::

::: {.pf-step #s1-10}

Therefore
$$
\boxed{
\sqrt I
\text{ is a prime ideal}.
}
$$


::: pf-proof

Step [](#s1-8){.pf-ref} gives properness, and step [](#s1-9){.pf-ref} gives the prime-product condition.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} proves part (a), and step [](#s1-10){.pf-ref} proves part (b).

:::

:::

:::
