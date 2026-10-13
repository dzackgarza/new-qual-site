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
\[
f:X\to Y
\]
be continuous and onto, where $X$ is compact Hausdorff and $Y$ is Hausdorff. Prove that there is a subspace $F\subseteq X$ minimal, under inclusion, among compact subspaces $Z\subseteq X$ satisfying
\[
f(Z)=Y.
\]
:::

::: {.solution}
Let
\[
\mathcal C=\{Z\subseteq X: Z\text{ is compact and }f(Z)=Y\},
\]
ordered by inclusion.

<1>1. The partially ordered set $\mathcal C$ is nonempty.

::: {.proof}
The space $X$ itself is compact and $f(X)=Y$ because $f$ is onto. Hence $X\in\mathcal C$.
:::

<1>2. Let $\mathcal T\subseteq\mathcal C$ be a chain and set
\[
F_{\mathcal T}=\bigcap_{Z\in\mathcal T}Z.
\]
Then $F_{\mathcal T}$ is compact.

::: {.proof}
Because $X$ is Hausdorff, every compact subset $Z\subseteq X$ is closed. Thus $F_{\mathcal T}$ is an intersection of closed subsets of the compact space $X$, hence closed in $X$ and therefore compact.
:::

<1>3. For every $y\in Y$, the family
\[
\{Z\cap f^{-1}(y):Z\in\mathcal T\}
\]
consists of nonempty compact subsets of $X$ and has the finite intersection property.

::: {.proof}
For each $Z\in\mathcal T$, surjectivity $f(Z)=Y$ gives a point of $Z\cap f^{-1}(y)$, so this set is nonempty. Since $Y$ is Hausdorff, $\{y\}$ is closed, hence $f^{-1}(y)$ is closed in $X$; intersecting it with compact $Z$ gives a compact set. Finally, because $\mathcal T$ is totally ordered by inclusion, any finite collection $Z_1,\ldots,Z_m$ has a smallest member, say $Z_j$, and
\[
\bigcap_{i=1}^m(Z_i\cap f^{-1}(y))
=Z_j\cap f^{-1}(y)\ne\varnothing.
\]
:::

<1>4. Hence for every $y\in Y$,
\[
F_{\mathcal T}\cap f^{-1}(y)\ne\varnothing.
\]

::: {.proof}
The compact space $X$ has the property that every family of closed subsets with the finite intersection property has nonempty total intersection. Apply this to the family in step <1>3:
\[
\bigcap_{Z\in\mathcal T}(Z\cap f^{-1}(y))
=\left(\bigcap_{Z\in\mathcal T}Z\right)\cap f^{-1}(y)
=F_{\mathcal T}\cap f^{-1}(y).
\]
:::

<1>5. Therefore
\[
f(F_{\mathcal T})=Y,
\]
so $F_{\mathcal T}\in\mathcal C$ and is a lower bound for the chain $\mathcal T$.

::: {.proof}
Step <1>4 says that every $y\in Y$ has a preimage lying in $F_{\mathcal T}$, so the restriction of $f$ to $F_{\mathcal T}$ is onto. Compactness is step <1>2. By definition of intersection, $F_{\mathcal T}\subseteq Z$ for every $Z\in\mathcal T$.
:::

<1>6. Apply Zorn's lemma to $\mathcal C$ with the reverse inclusion order
\[
Z\preceq W\quad\Longleftrightarrow\quad W\subseteq Z.
\]
There exists a maximal element $F$ for $\preceq$.

::: {.proof}
In the reverse order, an upper bound for a chain is exactly a lower bound under ordinary inclusion. Step <1>5 supplies such an element for every chain. Since $\mathcal C$ is nonempty by step <1>1, Zorn's lemma gives a maximal element.
:::

<1>7. This $F$ is minimal under ordinary inclusion among compact subsets $Z\subseteq X$ satisfying $f(Z)=Y$.

::: {.proof}
Suppose $Z\in\mathcal C$ and $Z\subseteq F$. Then, in the reverse order, $F\preceq Z$. Maximality of $F$ forces $Z=F$. Thus no proper compact subset of $F$ belongs to $\mathcal C$.
:::

<1>8. Therefore there exists a compact subspace
\[
\boxed{F\subseteq X}
\]
minimal among compact subspaces mapping onto $Y$.

::: {.proof}
Step <1>6 gives $F\in\mathcal C$, so it is compact and satisfies $f(F)=Y$; step <1>7 proves the required minimality.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 is exactly the assertion of the problem.
:::
:::
