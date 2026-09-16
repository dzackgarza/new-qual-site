---
schema: qual/card@1
id: P-AGH2121VARSHEAVES
kind: problem
title: Ideal sheaves on varieties and the failure of exactness of global sections
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Ideal Sheaves
  - Global Sections
relations: []
review: draft
---

::: {.problem}
Let $X$ be a variety over an algebraically closed field $k$, and let $\OO_X$ be the sheaf of regular functions on $X$.

a. Let $Y$ be a closed subset of $X$.
For each open set $U \subseteq X$, let $\mci_Y(U)$ be the ideal in the ring $\OO_X(U)$ consisting of those regular functions which vanish at all points of $Y \intersect U$.
Show that the presheaf $U \mapsto \mci_Y(U)$ is a sheaf.
It is called the **sheaf of ideals** $\mci_Y$ of $Y$, and it is a subsheaf of the sheaf of rings $\OO_X$.

b. If $Y$ is a subvariety, show that the quotient sheaf $\OO_X / \mci_Y$ is isomorphic to $i_* \OO_Y$, where $i: Y \to X$ is the inclusion and $\OO_Y$ is the sheaf of regular functions on $Y$.

c. Now let $X = \PP^1$ and let $Y$ be the union of two distinct points $P, Q \in X$.
Then with $\mcf = i_* \OO_P \oplus i_* \OO_Q$ there is an exact sequence of sheaves on $X$
\[
0 \to \mci_Y \to \OO_X \to \mcf \to 0.
\]
Show however that the induced map on global sections $\Gamma(X, \OO_X) \to \Gamma(X, \mcf)$ is not surjective.
This shows that the global section functor $\Gamma(X, \wait)$ is not exact.

d. Again let $X = \PP^1$ and let $\OO$ be the sheaf of regular functions.
Let $\mck$ be the constant sheaf on $X$ associated to the function field $K$ of $X$.
Show that there is a natural injection $\OO \to \mck$.
Show that the quotient sheaf $\mck / \OO$ is isomorphic to the direct sum of sheaves $\bigoplus_{P \in X} i_P(I_P)$, where $I_P$ is the group $K/\OO_P$ and $i_P(I_P)$ denotes the skyscraper sheaf given by $I_P$ at the point $P$.

e. Finally, show that in the case of (d) the sequence
\[
0 \to \Gamma(X, \OO) \to \Gamma(X, \mck) \to \Gamma(X, \mck/\OO) \to 0
\]
is exact.
:::

::: {.remark}
Part (e) is an analogue of the first Cousin problem in several complex variables; see Gunning and Rossi.
:::
