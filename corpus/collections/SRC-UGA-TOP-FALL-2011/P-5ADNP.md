---
schema: qual/card@1
id: P-5ADNP
kind: problem
title: $\operatorname{cl}_X(B)\cap A=\operatorname{cl}_A(B)$ for $B\subset A\subset X$
classification:
  areas:
  - topology
  topics:
  - Closure
  - Subspace Topology
relations: []
review: draft
audit:
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Replaced the migrated proof, which swapped A, B, and Y, by a source-faithful closure argument.
---

:::{.problem}
Let $X$ be a topological space, and $B \subset A \subset X$. 
Equip $A$ with the subspace topology, and write $\cl_X (B)$ or $\cl_A (B)$ for the closure of $B$ as a subset of, respectively, $X$ or $A$. 

Determine, with proof, the general relationship between $\cl_X (B) \cap A$ and $\cl_A (B)$ 

> I.e., are they always equal? Is one always contained in the other but not conversely? Neither?

:::

:::{.concept}
\envlist

- Definition of closure: for $A\subseteq X$, $\cl_X(A)$ is the intersection of all $B\supseteq A$ which are closed in $X$.
- Definition of "relative" closure: for $A\subseteq Y \subseteq X$, $\Cl_Y(A)$ is the intersection of all $B$ such that $Y\supseteq B \supseteq A$ which are closed in $Y$.
- Closed sets in a subspace: $C \subseteq Y\subseteq X$ is closed in $Y$ iff $C = F\intersect Y$ for some closed $F\subseteq X$.
:::

:::{.strategy}
Use that closed subsets of $A$ are intersections of $A$ with closed subsets of $X$.

![figures/image_2021-05-20-23-58-56.png](../../assets/figures/image_2021-05-20-23-58-56.png)

:::

:::{.solution}
<1>1. The set $A\cap\cl_X(B)$ is closed in $A$ and contains $B$.
::: {.proof}
The set $\cl_X(B)$ is closed in $X$, so its intersection with $A$ is closed in the subspace $A$.
Also
\[
B\subseteq A
\qquad\text{and}\qquad
B\subseteq\cl_X(B),
\]
hence
\[
B\subseteq A\cap\cl_X(B).
\]
:::

<1>2. $\cl_A(B)\subseteq A\cap\cl_X(B)$.
::: {.proof}
By definition, $\cl_A(B)$ is the smallest closed subset of $A$ containing $B$.
Apply <1>1.
:::

<1>3. Let $C$ be any closed subset of $A$ containing $B$.
Then
\[
A\cap\cl_X(B)\subseteq C.
\]
::: {.proof}
Because $C$ is closed in the subspace $A$, there is a closed set $F\subseteq X$ such that
\[
C=A\cap F.
\]
Since $B\subseteq C\subseteq F$ and $F$ is closed in $X$, minimality of the closure in $X$ gives
\[
\cl_X(B)\subseteq F.
\]
Intersecting with $A$ yields
\[
A\cap\cl_X(B)\subseteq A\cap F=C.
\]
:::

<1>4. $A\cap\cl_X(B)\subseteq\cl_A(B)$.
::: {.proof}
The closure $\cl_A(B)$ is the intersection of all closed subsets $C\subseteq A$ containing $B$.
By <1>3, $A\cap\cl_X(B)$ lies in every such $C$, hence in their intersection.
:::

<1>5. Therefore
\[
\boxed{\cl_A(B)=A\cap\cl_X(B)}.
\]
::: {.proof}
Combine <1>2 and <1>4.
:::
:::
