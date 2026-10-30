---
schema: qual/card@1
id: P-WESTOP12-5
kind: problem
title: Closed subsets of compact spaces and compact subsets of Hausdorff spaces
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
1. Show that every closed subspace of a compact space is compact.
2. Show that every compact subspace of a Hausdorff space is closed.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Let
$$
X
$$
be compact and let
$$
F\subseteq X
$$
be closed.
Then $F$ is compact.


::: pf-proof

Let
$$
\{U_\alpha\}_{\alpha\in A}
$$
be an open cover of $F$ in the subspace topology.
For each $\alpha$, choose an open set
$$
V_\alpha\subseteq X
$$
such that
$$
U_\alpha
=
F\cap V_\alpha.
$$

Since $F$ is closed,
$$
X\setminus F
$$
is open.
Therefore
$$
\{V_\alpha\}_{\alpha\in A}
\cup
\{X\setminus F\}
$$
is an open cover of $X$.

Compactness of $X$ gives finitely many indices
$$
\alpha_1,\dots,\alpha_m
$$
such that
$$
X
=
V_{\alpha_1}
\cup\cdots\cup
V_{\alpha_m}
\cup
(X\setminus F).
$$
Intersect with $F$:
$$
F
=
U_{\alpha_1}
\cup\cdots\cup
U_{\alpha_m}.
$$
Thus the original cover of $F$ has a finite subcover.
Hence $F$ is compact.

:::

:::

::: pf-step

Let
$$
X
$$
be Hausdorff and let
$$
K\subseteq X
$$
be compact.
Fix
$$
x\in X\setminus K.
$$
For each
$$
y\in K,
$$
choose disjoint open neighborhoods
$$
U_y\ni x,
\qquad
V_y\ni y.
$$


::: pf-proof

Because $X$ is Hausdorff and
$$
x\ne y,
$$
such disjoint neighborhoods exist for every
$$
y\in K.
$$

:::

:::

::: pf-step

The family
$$
\{V_y:y\in K\}
$$
is an open cover of $K$.
By compactness, choose
$$
y_1,\dots,y_m\in K
$$
such that
$$
K
\subseteq
V_{y_1}
\cup\cdots\cup
V_{y_m}.
$$


::: pf-proof

Every point $y\in K$ lies in its own neighborhood $V_y$, so the family
covers $K$.
Compactness gives a finite subcover.

:::

:::

::: {.pf-step #s1-4}

Define
$$
U
\coloneqq
U_{y_1}
\cap\cdots\cap
U_{y_m}.
$$
Then
$$
U
$$
is an open neighborhood of $x$ disjoint from $K$.


::: pf-proof

Finite intersections of open sets are open, and each $U_{y_j}$ contains
$x$, so
$$
x\in U.
$$

Suppose
$$
z\in U\cap K.
$$
Since
$$
K
\subseteq
V_{y_1}\cup\cdots\cup V_{y_m},
$$
there is some $j$ with
$$
z\in V_{y_j}.
$$
But
$$
z\in U
\subseteq
U_{y_j},
$$
contradicting
$$
U_{y_j}\cap V_{y_j}
=
\varnothing.
$$
Thus
$$
U\cap K=\varnothing.
$$

:::

:::

::: {.pf-step #s1-5}

Hence
$$
X\setminus K
$$
is open, so $K$ is closed.


::: pf-proof

Step [](#s1-4){.pf-ref} shows that every
$$
x\in X\setminus K
$$
has an open neighborhood contained in
$$
X\setminus K.
$$
Therefore the complement is open.

:::

:::

::: {.pf-step #s1-6}

Thus:
$$
\boxed{
\begin{aligned}
&F\subseteq X\text{ closed and }X\text{ compact}
\Longrightarrow
F\text{ compact},\\
&K\subseteq X\text{ compact and }X\text{ Hausdorff}
\Longrightarrow
K\text{ closed}.
\end{aligned}}
$$


::: pf-proof

The first implication is step [](#s1-1){.pf-ref} and the second is step [](#s1-5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} records both requested results.

:::

:::

:::
