---
schema: qual/card@1
id: P-UCLAB14F-01
kind: problem
title: Existence of a global minimum off the diagonal
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
  note: Checked against Problem 1 of the retained UCLA Basic Examination, Fall 2014.
---

::: {.problem}
Problem 1. Show that the function
\[
H(x,y)=x^2+y^2+|x-y|^{-1}
\]
achieves its global minimum somewhere on the set
\[
\{(x,y)\in\mathbb R^2:x\neq y\}.
\]
:::

::: {.solution}
Let
\[
D=\{(x,y)\in\mathbb R^2:x\ne y\}.
\]
The function $H$ is continuous on $D$.

<1>1. The value
\[
H(0,1)=2.
\]

::: {.proof}
Direct substitution gives
\[
H(0,1)
=
0^2+1^2+|0-1|^{-1}
=
1+1
=2.
\]
:::

<1>2. Define
\[
K=\{(x,y)\in D:H(x,y)\le2\}.
\]
Then $K$ is nonempty.

::: {.proof}
By step <1>1,
\[
(0,1)\in K.
\]
:::

<1>3. Every $(x,y)\in K$ satisfies
\[
x^2+y^2\le2.
\]

::: {.proof}
All terms in $H$ are nonnegative, so
\[
x^2+y^2
\le
H(x,y)
\le2.
\]
:::

<1>4. Every $(x,y)\in K$ satisfies
\[
|x-y|\ge\frac12.
\]

::: {.proof}
Again,
\[
|x-y|^{-1}
\le
H(x,y)
\le2.
\]
Since $|x-y|>0$ on $D$, taking reciprocals gives
\[
|x-y|\ge\frac12.
\]
:::

<1>5. The set $K$ is compact in $\mathbb R^2$.

::: {.proof}
Step <1>3 shows that $K$ is bounded.

By step <1>4,
\[
K
\subseteq
\left\{(x,y):|x-y|\ge\frac12\right\}.
\]
On this closed set, the formula defining $H$ is continuous. Therefore
\[
K
=
\left\{
(x,y):
|x-y|\ge\frac12,
H(x,y)\le2
\right\}
\]
is closed in $\mathbb R^2$.
Thus $K$ is closed and bounded, hence compact by Heine--Borel.
:::

<1>6. The restriction
\[
H|_K
\]
attains a minimum at some
\[
(x_0,y_0)\in K.
\]

::: {.proof}
The set $K$ is nonempty and compact by steps <1>2 and <1>5, and $H$ is continuous on $K$.
The extreme value theorem therefore gives a minimizing point.
:::

<1>7. The point $(x_0,y_0)$ from step <1>6 is a global minimizer of $H$ on $D$.

::: {.proof}
Because $(0,1)\in K$,
\[
H(x_0,y_0)
\le
H(0,1)
=2.
\]
If
\[
(x,y)\in D\setminus K,
\]
then by definition of $K$,
\[
H(x,y)>2.
\]
Thus no point outside $K$ has smaller value than $(x_0,y_0)$, while step <1>6 gives minimality on $K$.
Hence $(x_0,y_0)$ is a global minimizer on $D$.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 proves that $H$ achieves its global minimum somewhere off the diagonal.
:::
:::
