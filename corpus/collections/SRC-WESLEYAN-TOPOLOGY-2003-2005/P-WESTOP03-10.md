---
schema: qual/card@1
id: P-WESTOP03-10
kind: problem
title: A minimal compact subspace surjecting onto a Hausdorff image
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Let
$$
f:X\to Y
$$
be continuous and onto, where $X$ is compact Hausdorff and $Y$ is Hausdorff. Prove that there is a subspace $F\subseteq X$ minimal, under inclusion, among compact subspaces $Z\subseteq X$ satisfying
$$
f(Z)=Y.
$$
:::

::: {.solution}

Let
$$
\mathcal C=\{Z\subseteq X: Z\text{ is compact and }f(Z)=Y\},
$$
ordered by inclusion.

::: pf

::: {.pf-step #s1-1}

The partially ordered set $\mathcal C$ is nonempty.


::: pf-proof

The space $X$ itself is compact and $f(X)=Y$ because $f$ is onto. Hence $X\in\mathcal C$.

:::

:::

::: {.pf-step #s1-2}

Let $\mathcal T\subseteq\mathcal C$ be a chain and set
$$
F_{\mathcal T}=\bigcap_{Z\in\mathcal T}Z.
$$
Then $F_{\mathcal T}$ is compact.


::: pf-proof

Because $X$ is Hausdorff, every compact subset $Z\subseteq X$ is closed. Thus $F_{\mathcal T}$ is an intersection of closed subsets of the compact space $X$, hence closed in $X$ and therefore compact.

:::

:::

::: {.pf-step #s1-3}

For every $y\in Y$, the family
$$
\{Z\cap f^{-1}(y):Z\in\mathcal T\}
$$
consists of nonempty compact subsets of $X$ and has the finite intersection property.


::: pf-proof

For each $Z\in\mathcal T$, surjectivity $f(Z)=Y$ gives a point of $Z\cap f^{-1}(y)$, so this set is nonempty. Since $Y$ is Hausdorff, $\{y\}$ is closed, hence $f^{-1}(y)$ is closed in $X$; intersecting it with compact $Z$ gives a compact set. Finally, because $\mathcal T$ is totally ordered by inclusion, any finite collection $Z_1,\ldots,Z_m$ has a smallest member, say $Z_j$, and
$$
\bigcap_{i=1}^m(Z_i\cap f^{-1}(y))
=Z_j\cap f^{-1}(y)\ne\varnothing.
$$

:::

:::

::: {.pf-step #s1-4}

Hence for every $y\in Y$,
$$
F_{\mathcal T}\cap f^{-1}(y)\ne\varnothing.
$$


::: pf-proof

The compact space $X$ has the property that every family of closed subsets with the finite intersection property has nonempty total intersection. Apply this to the family in step [](#s1-3){.pf-ref}:
$$
\bigcap_{Z\in\mathcal T}(Z\cap f^{-1}(y))
=\left(\bigcap_{Z\in\mathcal T}Z\right)\cap f^{-1}(y)
=F_{\mathcal T}\cap f^{-1}(y).
$$

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
f(F_{\mathcal T})=Y,
$$
so $F_{\mathcal T}\in\mathcal C$ and is a lower bound for the chain $\mathcal T$.


::: pf-proof

Step [](#s1-4){.pf-ref} says that every $y\in Y$ has a preimage lying in $F_{\mathcal T}$, so the restriction of $f$ to $F_{\mathcal T}$ is onto. Compactness is step [](#s1-2){.pf-ref}. By definition of intersection, $F_{\mathcal T}\subseteq Z$ for every $Z\in\mathcal T$.

:::

:::

::: {.pf-step #s1-6}

Apply Zorn's lemma to $\mathcal C$ with the reverse inclusion order
$$
Z\preceq W\quad\Longleftrightarrow\quad W\subseteq Z.
$$
There exists a maximal element $F$ for $\preceq$.


::: pf-proof

In the reverse order, an upper bound for a chain is exactly a lower bound under ordinary inclusion. Step [](#s1-5){.pf-ref} supplies such an element for every chain. Since $\mathcal C$ is nonempty by step [](#s1-1){.pf-ref}, Zorn's lemma gives a maximal element.

:::

:::

::: {.pf-step #s1-7}

This $F$ is minimal under ordinary inclusion among compact subsets $Z\subseteq X$ satisfying $f(Z)=Y$.


::: pf-proof

Suppose $Z\in\mathcal C$ and $Z\subseteq F$. Then, in the reverse order, $F\preceq Z$. Maximality of $F$ forces $Z=F$. Thus no proper compact subset of $F$ belongs to $\mathcal C$.

:::

:::

::: {.pf-step #s1-8}

Therefore there exists a compact subspace
$$
\boxed{F\subseteq X}
$$
minimal among compact subspaces mapping onto $Y$.


::: pf-proof

Step [](#s1-6){.pf-ref} gives $F\in\mathcal C$, so it is compact and satisfies $f(F)=Y$; step [](#s1-7){.pf-ref} proves the required minimality.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is exactly the assertion of the problem.

:::

:::

:::
