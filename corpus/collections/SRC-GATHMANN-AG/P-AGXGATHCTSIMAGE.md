---
schema: qual/card@1
id: P-AGXGATHCTSIMAGE
kind: problem
title: Continuous images of connected and of irreducible spaces
classification:
  areas:
  - algebraic-geometry
  topics:
  - Irreducibility
  - Connectedness
  - Continuous Maps
relations: []
review: draft
---

::: {.problem}
Let $f:X\to Y$ be a continuous map of topological spaces.

(a) Show that if $X$ is connected then $f(X)$ is connected.

(b) Show that if $X$ is irreducible then $f(X)$ is irreducible.
:::

::: {.solution}
Give $f(X)\subseteq Y$ the subspace topology.
A subset of $f(X)$ is open (closed) in $f(X)$ exactly when it is $f(X)\cap V$ for some open (closed) $V\subseteq Y$, and then its preimage under $f$ is $f^{-1}(V)$, which is open (closed) in $X$.

::: pf

::: pf-step
If $X$ is connected, then $f(X)$ is connected.

::: pf-proof
Suppose $f(X)=Y_1\cup Y_2$ with $Y_1,Y_2$ disjoint, nonempty and open in $f(X)$.
Then $f^{-1}(Y_1)$ and $f^{-1}(Y_2)$ are open in $X$.
They are disjoint because $Y_1$ and $Y_2$ are disjoint, their union is $f^{-1}(f(X))=X$, and each is nonempty because each $Y_i$ is a nonempty subset of $f(X)$.
This separates $X$, which contradicts the connectedness of $X$.
Hence no such decomposition exists, and $f(X)$ is connected.
:::

:::

::: pf-step
If $X$ is irreducible, then $f(X)$ is irreducible.

::: pf-proof
The space $X$ is nonempty because it is irreducible, so $f(X)$ is nonempty.
Suppose $f(X)=Y_1\cup Y_2$ with $Y_1,Y_2$ closed in $f(X)$.
Then
$$
X=f^{-1}(Y_1)\cup f^{-1}(Y_2)
$$
with both preimages closed in $X$.
Since $X$ is irreducible, $X=f^{-1}(Y_i)$ for some $i$.
Then $f(X)\subseteq Y_i$, so $Y_i=f(X)$.
Hence $f(X)$ is not a union of two proper closed subsets, and $f(X)$ is irreducible.
:::

:::

:::
:::
