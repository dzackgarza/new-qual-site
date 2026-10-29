---
schema: qual/card@1
id: P-WESTOP03-07
kind: problem
title: One-point compactification and metrizability from a countable basis
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Let $X$ be locally compact and Hausdorff.

1. Describe the one-point compactification $X^*$ of $X$.
2. If $X$ also has a countable basis, prove that $X^*$ is metrizable.
:::

::: {.solution}

If $X$ is already compact, one may take $X^*=X\sqcup\{\infty\}$ with $\infty$ isolated. The usual noncompact case is described below; the same metrizability argument covers both cases.

::: pf

::: {.pf-step #s1-1}

As a set, define
$$
X^*=X\sqcup\{\infty\},
$$
where $\infty\notin X$.


::: pf-proof

This adjoins exactly one new point to $X$.

:::

:::

::: {.pf-step #s1-2}

Declare a subset $U\subseteq X^*$ to be open if either
$$
U\subseteq X\text{ is open in }X,
$$
or
$$
\infty\in U
\quad\text{and}\quad
X^*\setminus U\text{ is a compact subset of }X.
$$


::: pf-proof

These sets form a topology. Arbitrary unions are immediate: if a union contains $\infty$, its complement is a closed subset of the compact complement of any one member containing $\infty$, hence compact because $X$ is Hausdorff. For finite intersections of neighborhoods of $\infty$, the complement is a finite union of compact subsets of $X$, hence compact. Intersections with open subsets of $X$ remain open in $X$ because compact subsets of a Hausdorff space are closed.

:::

:::

::: {.pf-step #s1-3}

The subspace topology induced on $X\subseteq X^*$ is the original topology of $X$.


::: pf-proof

Every open subset of $X$ was explicitly declared open in $X^*$. Conversely, intersecting any open set of $X^*$ with $X$ gives an open subset of $X$ by step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

The space $X^*$ is compact.


::: pf-proof

Let $\mathcal U$ be an open cover of $X^*$. Choose $U_\infty\in\mathcal U$ containing $\infty$. Then
$$
K=X^*\setminus U_\infty
$$
is compact in $X$. The remaining members of $\mathcal U$ cover $K$, so finitely many of them cover $K$. Together with $U_\infty$, they form a finite subcover of $X^*$.

:::

:::

::: {.pf-step #s1-5}

The space $X^*$ is Hausdorff.


::: pf-proof

Two points of $X$ have disjoint neighborhoods because $X$ is Hausdorff. Now fix $x\in X$. Local compactness and regularity of locally compact Hausdorff spaces give an open neighborhood $V$ of $x$ whose closure $K=\overline V$ is compact. Then
$$
V
\qquad\text{and}\qquad
X^*\setminus K
$$
are disjoint open neighborhoods of $x$ and $\infty$, respectively.

:::

:::

::: {.pf-step #s1-6}

Now suppose $X$ has a countable basis $\{B_n:n\geq1\}$. Then $X$ is $\sigma$-compact: there exist compact sets
$$
K_1\subseteq K_2\subseteq\cdots
$$
such that
$$
X=\bigcup_{n=1}^\infty K_n.
$$


::: pf-proof

For each $x\in X$, local compactness gives an open neighborhood $V_x$ with compact closure. Choose a basis element $B_{n(x)}$ with
$$
x\in B_{n(x)}\subseteq V_x.
$$
Thus the basis elements having compact closure cover $X$. There are only countably many of them; enumerate their compact closures as $C_1,C_2,\ldots$ and set
$$
K_n=C_1\cup\cdots\cup C_n.
$$
Each $K_n$ is compact, the sequence is increasing, and its union is $X$.

:::

:::

::: {.pf-step #s1-7}

The sets
$$
U_n=X^*\setminus K_n
$$
form a countable neighborhood basis at $\infty$.


::: pf-proof

Each $U_n$ is a neighborhood of $\infty$ by the definition in step [](#s1-2){.pf-ref}. If $U$ is any neighborhood of $\infty$, then
$$
C=X^*\setminus U
$$
is compact in $X$. The interiors of the compact sets $K_n$ constructed from the compact-closure basis cover $X$ after, if necessary, replacing $K_n$ by the finite unions of those closures; compactness of $C$ therefore places $C$ in some $K_N$. Hence
$$
U_N=X^*\setminus K_N\subseteq X^*\setminus C=U.
$$

:::

:::

::: {.pf-step #s1-8}

Combining the countable basis of $X$ with $\{U_n:n\geq1\}$ gives a countable basis for $X^*$.


::: pf-proof

At points of $X$, the original basis elements form a neighborhood basis by step [](#s1-3){.pf-ref}. At $\infty$, step [](#s1-7){.pf-ref} supplies the countable neighborhood basis. Their union is countable and is a basis for all of $X^*$.

:::

:::

::: {.pf-step #s1-9}

Since $X^*$ is compact Hausdorff and second countable, it is metrizable.


::: pf-proof

A compact Hausdorff space is regular. By step [](#s1-8){.pf-ref}, $X^*$ is second countable. The Urysohn metrization theorem states that every regular second-countable $T_1$ space is metrizable. The $T_1$ property follows from Hausdorffness in step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-10}

Thus the one-point compactification is the space described in steps [](#s1-1){.pf-ref} through [](#s1-5){.pf-ref}, and if $X$ has a countable basis then
$$
\boxed{X^*\text{ is metrizable}.}
$$


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-5){.pf-ref} construct and verify the one-point compactification. Steps [](#s1-6){.pf-ref} through [](#s1-9){.pf-ref} prove the metrizability assertion.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} contains both requested conclusions.

:::

:::

:::
