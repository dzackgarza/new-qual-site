---
schema: qual/card@1
id: P-AGHDIMTOPOLOGY
kind: problem
title: Dimension under subspaces, open covers, and closed subsets
classification:
  areas:
  - algebraic-geometry
  topics:
  - Dimension
  - Noetherian Spaces
  - Irreducibility
relations:
- kind: uses
  target: D-5LJUX
review: draft
---

::: problem
(a) If $Y$ is any subset of a topological space $X$, then $\dim Y \leq \dim X$.

(b) If $X$ is covered by open subsets $\ts{U_i}$, then $\dim X = \sup_i \dim U_i$.

(c) Give an example of a topological space $X$ with a dense open subset $U$ such that $\dim U < \dim X$.

(d) If $Y$ is a closed subset of an irreducible finite-dimensional space $X$ with $\dim Y = \dim X$, then $Y = X$.

(e) Give an example of a Noetherian topological space of infinite dimension.
:::

::: solution
**(a)** Let $(U_i)_{0 \leq i \leq n}$ be a strict chain of irreducible closed subsets of $Y$, so $U_i = V_i \intersect Y$ for some $V_i$ closed in $X$.
The $V_i$ need not form a chain; take partial unions $\tilde{V}_n = \Union_{i \leq n} V_i$, which do, and which remain strict.
So $\dim X \geq n$.

**(b)** By (a) it suffices to find one $U_i$ with $\dim U_i \geq \dim X$.
Take a strict chain $(C_j)_{0 \leq j \leq n}$ witnessing $\dim X = n$ and choose $i_0$ with $U_{i_0} \intersect C_0 \neq \emptyset$.
Then $(C_j \intersect U_{i_0})_j$ is a strict chain of length $n$ in $U_{i_0}$.

**(c)** $X = \AA^1_\CC = \Spec \CC[x]$ has dimension $1$; the open subset given by the generic point alone has dimension $0$ and is dense.

**(d)** Take a chain $(C_i)_{0 \leq i \leq n}$ in $Y$ with $n = \dim Y = \dim X$, arranged so that $C_n = Y$.
If $Y \subsetneq X$ then $C_0 \subsetneq \cdots \subsetneq C_n = Y \subsetneq X$ is a strict chain of length $n+1$ in $X$, since $X$ is irreducible and therefore itself an irreducible closed subset.
That contradicts $\dim X = n$.

**(e)** Take $X = \ZZ_{\geq 0}$ with closed sets $\emptyset$, $X$, and $\ts{1,\ldots,i}$ for each $i$.
The chain $\ts{1} \subsetneq \ts{1,2} \subsetneq \cdots$ is infinite, so $\dim X = \infty$, and every descending chain of closed sets is finite, so $X$ is Noetherian.
:::
