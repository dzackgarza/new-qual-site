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

::: problem
Let $f:X\to Y$ be a continuous map of topological spaces.

a. Show that if $X$ is connected then $f(X)$ is connected.

b. Show that if $X$ is irreducible then $f(X)$ is irreducible.
:::

::: solution
**Part a**: Toward a contradiction, if $f(X) = Y_1 {\textstyle\coprod} Y_2$ with $Y_1, Y_2$ nonempty and open in $Y$, then
\[
f^{-1}(f(X)) \subseteq X
\]
on one hand, and
\[
f^{-1}(f(X)) = f^{-1}(Y_1) {\textstyle\coprod} f^{-1}(Y_2)
\]
on the other.
If $f$ is continuous, the preimages $f^{-1}(Y_i)$ are open (and nonempty), so $X$ contains a disconnected subset.
However, every subset of a connected set must be connected, contradicting the connectedness of $X$.

**Part b**: Suppose $f(X) = Y_1 \union Y_2$ with $Y_i$ proper closed subsets of $Y$.
Then $f^{-1}(Y_1) \union f^{-1}(Y_2) = (f^{-1} \circ f)(X) \subseteq X$ are closed in $X$, since $f$ is continuous.
Since $X$ is irreducible, without loss of generality (by relabeling) this forces $X_1 = \emptyset$.
But then $f(X_1) = \emptyset$, forcing $f(X) = Y_2$.
:::

::: {.remark}
Erratum: both parts of the argument above contain false or undefined steps.

- Part a rests on the claim that every subset of a connected space is connected, which is false: $\ts{0,1}\subset\RR$ is disconnected. The decomposition should be taken with $Y_1,Y_2$ disjoint, nonempty and open in the subspace $f(X)$; then $f^{-1}(Y_1)$ and $f^{-1}(Y_2)$ are disjoint nonempty open subsets of $X$ whose union is all of $X$, which contradicts connectedness of $X$ directly.
- In part b the sets $Y_i$ should be proper closed subsets of the subspace $f(X)$, and $X_1$ is never defined. Since $X=f^{-1}(Y_1)\union f^{-1}(Y_2)$ with both preimages closed, irreducibility of $X$ gives $X=f^{-1}(Y_i)$ for some $i$, hence $f(X)\subseteq Y_i$, contradicting properness of $Y_i$.
:::
