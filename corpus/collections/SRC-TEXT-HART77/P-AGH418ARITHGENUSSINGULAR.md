---
schema: qual/card@1
id: P-AGH418ARITHGENUSSINGULAR
kind: problem
title: The arithmetic genus of a singular curve and the local invariants $\delta_P$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Genus
  - Curves
  - Riemann-Roch
relations: []
review: draft
---

::: {.problem}
Let $X$ be an integral projective scheme of dimension 1 over $k$, and let $\tilde{X}$ be its normalization (II, Ex.
3.8). Then there is an exact sequence of sheaves on $X$,
$$
0 \to \OO_X \to f_* \OO_{\tilde X} \to \sum_{P \in X} \tilde\OO_P/\OO_P \to 0
$$
where $\tilde\OO_P$ is the integral closure of $\OO_P$.
For each $P \in X$, let $\delta_P=\operatorname{length}(\tilde\OO_P/\OO_P)$.

a. Show that $p_a(X)=p_a(\tilde{X})+\sum_{P \in X} \delta_P$.
Hint: Use (III, Ex.
4.1) and (III, Ex.
5.3).

b. If $p_a(X)=0$, show that $X$ is already nonsingular and in fact isomorphic to $\PP^1$.
This strengthens (1.3.5).

c. \* If $P$ is a node or an ordinary cusp (I, Ex.
5.6, Ex.
5.14), show that $\delta_P=1$.
Hint: Show first that $\delta_P$ depends only on the analytic isomorphism class of the singularity at $P$.
Then compute $\delta_P$ for the node and cusp of suitable plane cubic curves.
See (V, 3.9.3) for another method.
:::
