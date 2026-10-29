---
schema: qual/card@1
id: P-SQUAL1-02
kind: problem
title: Disjoint compact subsets of a Hausdorff space have disjoint open neighborhoods
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Let $A,B$ be disjoint compact subsets of a Hausdorff space $X$.
Show that there are disjoint open sets $U,V\subseteq X$ such that
$$A\subseteq U,\qquad B\subseteq V.$$
:::

::: {.solution}

Fix
$$
a\in A.
$$

::: pf

::: {.pf-step #s1-1}

For every
$$
b\in B,
$$
choose disjoint open neighborhoods
$$
U_{a,b}\ni a
$$
and
$$
V_{a,b}\ni b.
$$


::: pf-proof

The space $X$ is Hausdorff and $a\ne b$ because $A\cap B=\varnothing$.
Therefore $a$ and $b$ have disjoint open neighborhoods.

:::

:::

::: pf-step

The family
$$
\{V_{a,b}:b\in B\}
$$
is an open cover of $B$.


::: pf-proof

Each point $b\in B$ belongs to its chosen neighborhood $V_{a,b}$.

:::

:::

::: {.pf-step #s1-3}

By compactness of $B$, choose
$$
b_1,\dots,b_m\in B
$$
such that
$$
\boxed{
B\subseteq
V_{a,b_1}\cup\cdots\cup V_{a,b_m}}.
$$


::: pf-proof

Every open cover of a compact set has a finite subcover.

:::

:::

::: pf-step

Define
$$
\boxed{
U_a
=
\bigcap_{j=1}^{m}U_{a,b_j}}
$$
and
$$
\boxed{
V_a
=
\bigcup_{j=1}^{m}V_{a,b_j}}.
$$


::: pf-proof

These are finite intersections and finite unions of open sets.

:::

:::

::: {.pf-step #s1-5}

The set $U_a$ is open and contains $a$.


::: pf-proof

Every $U_{a,b_j}$ is open and contains $a$, so their finite intersection is open and still contains $a$.

:::

:::

::: {.pf-step #s1-6}

The set $V_a$ is open and contains $B$.


::: pf-proof

It is a finite union of open sets, and containment of $B$ follows from step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

One has
$$
\boxed{
U_a\cap V_a=\varnothing}.
$$


::: pf-proof

Suppose
$$
x\in U_a\cap V_a.
$$
Since $x\in V_a$, there is some $j$ with
$$
x\in V_{a,b_j}.
$$
Since $x\in U_a$, one has
$$
x\in U_{a,b_j}.
$$
But
$$
U_{a,b_j}\cap V_{a,b_j}=\varnothing
$$
by step [](#s1-1){.pf-ref}, contradiction.

:::

:::

::: {.pf-step #s1-8}

The family
$$
\{U_a:a\in A\}
$$
is an open cover of $A$.


::: pf-proof

Each $a\in A$ lies in its corresponding open set $U_a$ by step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

By compactness of $A$, choose
$$
a_1,\dots,a_r\in A
$$
such that
$$
\boxed{
A\subseteq
U_{a_1}\cup\cdots\cup U_{a_r}}.
$$


::: pf-proof

Apply compactness of $A$ to the open cover from step [](#s1-8){.pf-ref}.

:::

:::

::: {.pf-step #s1-10}

Define
$$
\boxed{
U=
\bigcup_{i=1}^{r}U_{a_i}}
$$
and
$$
\boxed{
V=
\bigcap_{i=1}^{r}V_{a_i}}.
$$


::: pf-proof

These are respectively a finite union and a finite intersection of open sets.

:::

:::

::: {.pf-step #s1-11}

The set $U$ is open and contains $A$.


::: pf-proof

Openness follows from the union in step [](#s1-10){.pf-ref}, and containment follows from step [](#s1-9){.pf-ref}.

:::

:::

::: {.pf-step #s1-12}

The set $V$ is open and contains $B$.


::: pf-proof

Every $V_{a_i}$ is open and contains $B$ by step [](#s1-6){.pf-ref}. Therefore their finite intersection is open and still contains $B$.

:::

:::

::: {.pf-step #s1-13}

The sets $U$ and $V$ are disjoint:
$$
\boxed{
U\cap V=\varnothing}.
$$


::: pf-proof

Suppose
$$
x\in U\cap V.
$$
Since $x\in U$, there exists $i$ with
$$
x\in U_{a_i}.
$$
Since $x\in V$, one has
$$
x\in V_{a_i}.
$$
This contradicts
$$
U_{a_i}\cap V_{a_i}=\varnothing
$$
from step [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-14}

Therefore there exist disjoint open sets $U,V\subseteq X$ such that
$$
\boxed{
A\subseteq U,
\qquad
B\subseteq V}.
$$


::: pf-proof

Use steps [](#s1-11){.pf-ref} through [](#s1-13){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-14){.pf-ref} is the required conclusion.

:::

:::

:::
