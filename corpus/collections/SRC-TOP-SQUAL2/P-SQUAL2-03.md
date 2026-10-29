---
schema: qual/card@1
id: P-SQUAL2-03
kind: problem
title: Products of completely Hausdorff spaces are completely Hausdorff
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
A topological space $X$ is called **completely Hausdorff** if for every pair of distinct points $a,b\in X$ there are open sets $U,V\subseteq X$ such that
$$a\in U,\qquad b\in V,\qquad \overline U\cap\overline V=\varnothing.$$
Show that the product of two completely Hausdorff spaces is completely Hausdorff.
:::

::: {.solution}

Let $X$ and $Y$ be completely Hausdorff, and let
$$
(x_1,y_1),(x_2,y_2)\in X\times Y
$$
be distinct.

::: pf

::: {.pf-step #s1-1}

Since the two points are distinct, at least one coordinate differs:
$$
\boxed{
x_1\ne x_2
\quad\text{or}\quad
y_1\ne y_2}.
$$


::: pf-proof

If both coordinates were equal, the ordered pairs would be equal.

:::

:::

::: {.pf-step #s1-2}

Since $X$ is completely Hausdorff, there exist open sets
$$
U_1,U_2\subseteq X
$$
such that
$$
x_1\in U_1,
\qquad
x_2\in U_2,
$$
and
$$
\boxed{
\overline{U_1}\cap\overline{U_2}=\varnothing}.
$$


::: pf-proof

Apply the definition of complete Hausdorffness in $X$ to the distinct points $x_1,x_2$.

:::

:::

::: pf-step

Define
$$
W_1=U_1\times Y,
\qquad
W_2=U_2\times Y.
$$


::: pf-proof

These are the natural product neighborhoods of the two points.

:::

:::

::: {.pf-step #s1-4}

The sets $W_1,W_2$ are open in $X\times Y$.


::: pf-proof

Each is a product of an open subset of $X$ with the open set $Y\subseteq Y$.

:::

:::

::: {.pf-step #s1-5}

One has
$$
(x_1,y_1)\in W_1
$$
and
$$
(x_2,y_2)\in W_2.
$$


::: pf-proof

This follows from the containments in step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

For every subset $A\subseteq X$,
$$
\boxed{
\overline{A\times Y}
=
\overline A\times Y}.
$$


::: pf-proof

First,
$$
A\times Y\subseteq\overline A\times Y.
$$
The set $\overline A\times Y$ is closed in $X\times Y$, so
$$
\overline{A\times Y}
\subseteq
\overline A\times Y.
$$

Conversely, let
$$
(x,y)\in\overline A\times Y.
$$
Every basic neighborhood
$$
P\times Q
$$
of $(x,y)$ has $P\cap A\ne\varnothing$ because $x\in\overline A$, and $Q\ne\varnothing$ because $y\in Q$. Hence
$$
(P\times Q)\cap(A\times Y)\ne\varnothing.
$$
Thus
$$
(x,y)\in\overline{A\times Y}.
$$

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\overline{W_1}
=
\overline{U_1}\times Y
$$
and
$$
\overline{W_2}
=
\overline{U_2}\times Y.
$$


::: pf-proof

Apply step [](#s1-6){.pf-ref} with $A=U_1$ and $A=U_2$.

:::

:::

::: {.pf-step #s1-8}

Hence
$$
\boxed{
\overline{W_1}\cap\overline{W_2}
=
\varnothing}.
$$


::: pf-proof

By step [](#s1-7){.pf-ref},
$$
\overline{W_1}\cap\overline{W_2}
=
(\overline{U_1}\cap\overline{U_2})\times Y,
$$
which is empty by step [](#s1-2){.pf-ref}.

:::

:::

::: pf-step

If $x_1=x_2$, then $y_1\ne y_2$, and there exist open sets
$$
V_1,V_2\subseteq Y
$$
such that
$$
y_1\in V_1,
\qquad
y_2\in V_2,
$$
and
$$
\boxed{
\overline{V_1}\cap\overline{V_2}=\varnothing}.
$$


::: pf-proof

Apply complete Hausdorffness of $Y$ to the distinct points $y_1,y_2$.

:::

:::

::: {.pf-step #s1-10}

Define
$$
W_1=X\times V_1,
\qquad
W_2=X\times V_2.
$$
Then $W_1,W_2$ are open neighborhoods of the two points and
$$
\boxed{
\overline{W_1}\cap\overline{W_2}
=
\varnothing}.
$$


::: pf-proof

The argument from steps [](#s1-4){.pf-ref} through [](#s1-8){.pf-ref} applies with the factors reversed:
$$
\overline{X\times V_i}
=
X\times\overline{V_i}.
$$
Thus the intersection of the closures is
$$
X\times
(\overline{V_1}\cap\overline{V_2})
=
\varnothing.
$$

:::

:::

::: {.pf-step #s1-11}

Therefore every pair of distinct points in $X\times Y$ has open neighborhoods with disjoint closures.


::: pf-proof

By step [](#s1-1){.pf-ref}, either Case 1 or Case 2 applies. The required neighborhoods are supplied by step [](#s1-8){.pf-ref} or step [](#s1-10){.pf-ref}.

:::

:::

::: {.pf-step #s1-12}

Hence
$$
\boxed{
X\times Y
\text{ is completely Hausdorff}.}
$$


::: pf-proof

Step [](#s1-11){.pf-ref} is exactly the definition of complete Hausdorffness.

:::

:::

::: pf-qed

Step [](#s1-12){.pf-ref} is the required conclusion.

:::

:::

:::
