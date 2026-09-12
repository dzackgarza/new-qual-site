---
schema: qual/card@1
id: E-KIN90
kind: problem
title: Collapsing K in the K-topology
classification:
  areas:
  - topology
  topics:
  - Quotient Topology
  - Separation Axioms
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Recall that $\mathbb{R}_K$ denotes the real line in the $K$-topology.
(See §13.) Let $Y$ be the quotient space obtained from $\mathbb{R}_K$ by collapsing the set $K$ to a point; let $p: \mathbb{R}_K \to Y$ be the quotient map.

(a) Show that $Y$ satisfies the $T_1$ axiom, but is not Hausdorff.

(b) Show that $p \times p: \mathbb{R}_K \times \mathbb{R}_K \to Y \times Y$ is not a quotient map.
[Hint: The diagonal is not closed in $Y \times Y$, but its inverse image is closed in $\mathbb{R}_K \times \mathbb{R}_K$.]
:::

::: {.solution}
Let $K=\{1/n:n\in\mathbb Z_+\}$ and let $q=p(K)\in Y$.

(a) The space $\mathbb R_K$ is $T_1$ because its topology is finer than the usual topology. The set $K$ is closed in $\mathbb R_K$: its complement is open since every $x\notin K$ has a basic neighborhood of the form $(a,b)-K$. Therefore every singleton in $Y$ has closed inverse image under $p$: the inverse image of $\{q\}$ is $K$, while the inverse image of any other singleton is a singleton of $\mathbb R_K$. By the quotient topology, singletons in $Y$ are closed. Hence $Y$ is $T_1$.

The space is not Hausdorff. Suppose $q$ and $p(0)$ had disjoint open neighborhoods $U,V$. Then $p^{-1}(U)$ is an open saturated set containing all of $K$, and $p^{-1}(V)$ is an open neighborhood of $0$. Shrinking inside $p^{-1}(V)$, choose
\[
(-\varepsilon,\varepsilon)-K\subseteq p^{-1}(V).
\]
Choose $n$ with $1/n<\varepsilon$. Since $1/n\in p^{-1}(U)$ and basic neighborhoods of a point of $K$ cannot be of the form $(a,b)-K$, openness of $p^{-1}(U)$ gives an ordinary interval about $1/n$ contained in it. Such an interval contains points of $(-\varepsilon,\varepsilon)-K$, contradicting disjointness. Thus $Y$ is not Hausdorff.

(b) In any space, Hausdorffness is equivalent to closedness of the diagonal. Hence
\[
\Delta_Y=\{(y,y):y\in Y\}
\]
is not closed in $Y\times Y$. Its inverse image under $p\times p$ is
\[
(p\times p)^{-1}(\Delta_Y)=\Delta_{\mathbb R_K}\cup(K\times K).
\]
The space $\mathbb R_K$ is Hausdorff (it is finer than the usual Hausdorff topology), so its diagonal is closed; $K$ is closed, so $K\times K$ is closed. Thus this inverse image is closed.

If $p\times p$ were a quotient map, closedness of a subset of $Y\times Y$ would be equivalent to closedness of its inverse image. We have found a nonclosed set with closed inverse image, so $p\times p$ is not quotient.
:::
