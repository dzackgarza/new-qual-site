---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F08-07
kind: problem
title: The Hausdorff criterion for a product of two spaces
classification:
  areas:
  - topology
  topics:
  - Hausdorff Spaces
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Checked against Part One, question 7 of the Topology Ph.D. Qualifying Exam
    dated January 17, 2009 in assets/attachments/F08phdtop.pdf. The literal
    converse needs both factors nonempty: if Y is empty, X times Y is empty and
    therefore Hausdorff for every X.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Proved the forward product theorem by separating points in a differing
    coordinate. For the converse under nonemptiness, each factor is homeomorphic
    to a coordinate slice of the Hausdorff product and Hausdorffness passes to
    subspaces.
---

::: {.problem}
Prove that the product topological space $X\times Y$ is Hausdorff if and only if $X$ and $Y$ are Hausdorff.
:::

::: {.solution}
The implication from "$X\times Y$ is Hausdorff" to "$X$ and $Y$ are Hausdorff" requires $X$ and $Y$ to be nonempty: if $Y=\varnothing$, then
\[
X\times Y=\varnothing
\]
is Hausdorff even when $X$ is not.

::: pf

::: {.pf-step #reverse-implication}
If $X$ and $Y$ are Hausdorff, then $X\times Y$ is Hausdorff.

::: pf-proof
Take distinct points
\[
(x_1,y_1),(x_2,y_2)\in X\times Y.
\]
Since they are distinct, either
\[
x_1\ne x_2
\]
or
\[
y_1\ne y_2.
\]

Suppose first that $x_1\ne x_2$.
Since $X$ is Hausdorff, there are disjoint open sets $U_1,U_2\subseteq X$ with
\[
x_1\in U_1,
\qquad
x_2\in U_2.
\]
Then
\[
U_1\times Y
\qquad\text{and}\qquad
U_2\times Y
\]
are disjoint open neighborhoods of $(x_1,y_1)$ and $(x_2,y_2)$ in the product topology.

If instead $y_1\ne y_2$, choose disjoint open neighborhoods $V_1,V_2\subseteq Y$ of $y_1,y_2$ and use
\[
X\times V_1
\qquad\text{and}\qquad
X\times V_2.
\]
Thus any two distinct points of $X\times Y$ have disjoint open neighborhoods, so the product is Hausdorff.
:::

:::

::: {.pf-step #subspace-hausdorff}
Every subspace of a Hausdorff space is Hausdorff.

::: pf-proof
Let $A$ be a subspace of a Hausdorff space $Z$, and take distinct $a,b\in A$.
Choose disjoint open sets $U,V\subseteq Z$ with
\[
a\in U,
\qquad
b\in V.
\]
Then
\[
U\cap A
\qquad\text{and}\qquad
V\cap A
\]
are disjoint open neighborhoods of $a,b$ in the subspace $A$.
Hence $A$ is Hausdorff.
:::

:::

::: {.pf-step #x-hausdorff}
Assume $X\ne\varnothing$, $Y\ne\varnothing$, and $X\times Y$ is Hausdorff.
Then $X$ is Hausdorff.

::: pf-proof
Choose $y_0\in Y$.
The map
\[
i_X:X\longrightarrow X\times\{y_0\},
\qquad
i_X(x)=(x,y_0),
\]
is a homeomorphism: it is continuous, and its inverse is the restriction of the first coordinate projection
\[
p_X:X\times Y\to X.
\]
By step [](#subspace-hausdorff){.pf-ref}, the slice $X\times\{y_0\}$ is Hausdorff as a subspace of the Hausdorff product.
Hausdorffness is preserved by homeomorphism, so $X$ is Hausdorff.
:::

:::

::: {.pf-step #y-hausdorff}
Under the same assumptions, $Y$ is Hausdorff.

::: pf-proof
Choose $x_0\in X$.
The map
\[
i_Y:Y\longrightarrow\{x_0\}\times Y,
\qquad
i_Y(y)=(x_0,y),
\]
is a homeomorphism whose inverse is the restriction of the second coordinate projection.
The slice $\{x_0\}\times Y$ is Hausdorff by step [](#subspace-hausdorff){.pf-ref}, so $Y$ is Hausdorff.
:::

:::

::: pf-step
Therefore, for nonempty spaces $X$ and $Y$,
\[
\boxed{X\times Y\text{ is Hausdorff}\iff X\text{ and }Y\text{ are Hausdorff}.}
\]

::: pf-proof
The forward implication follows from steps [](#x-hausdorff){.pf-ref} and [](#y-hausdorff){.pf-ref}, and the reverse implication is step [](#reverse-implication){.pf-ref}.
:::

:::

:::

:::
