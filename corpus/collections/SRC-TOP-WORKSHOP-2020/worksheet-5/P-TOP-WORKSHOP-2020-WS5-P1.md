---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS5-P1
kind: problem
title: Projections in the product topology are continuous and open; product is Hausdorff iff factors are
classification:
  areas:
  - topology
  topics:
  - Product Topology
  - Continuity
  - Hausdorff Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
(May 2013) Let $X_\alpha$ be non-empty topological spaces and suppose that $X=\prod_\alpha X_\alpha$ is endowed with the product topology.

(a) Prove that each projection map $\pi_\alpha$ is continuous and open.

(b) Prove that $X$ is Hausdorff if and only if each space $X_\alpha$ is Hausdorff.
:::

::: {.solution}
(a) A subbasis for the product topology consists of sets
\[
\pi_\alpha^{-1}(U_\alpha),
\]
with \(U_\alpha\subseteq X_\alpha\) open. Hence every projection \(\pi_\alpha\) is continuous.

To prove openness, it suffices to consider a basic open set
\[
B=\prod_\beta U_\beta,
\]
where each \(U_\beta\) is open and \(U_\beta=X_\beta\) except for finitely many indices. Since every factor is nonempty,
\[
\pi_\alpha(B)=U_\alpha,
\]
which is open. Arbitrary open sets are unions of basic ones, and projections preserve unions, so \(\pi_\alpha\) is open.

(b) If every \(X_\alpha\) is Hausdorff and \(x\ne y\) in \(X\), then \(x_\alpha\ne y_\alpha\) for some \(\alpha\). Choose disjoint open neighborhoods \(U,V\subseteq X_\alpha\) of these coordinates. Then
\[
\pi_\alpha^{-1}(U),\qquad\pi_\alpha^{-1}(V)
\]
are disjoint open neighborhoods of \(x,y\). Thus \(X\) is Hausdorff.

Conversely, suppose \(X\) is Hausdorff. Fix \(\alpha\) and choose one basepoint \(a_\beta\in X_\beta\) for every \(\beta\ne\alpha\). The map
\[
s_\alpha:X_\alpha\to X,
\qquad
s_\alpha(x)_\alpha=x,\quad s_\alpha(x)_\beta=a_\beta\ (\beta\ne\alpha),
\]
is an embedding, with inverse on its image given by \(\pi_\alpha\). Hence \(X_\alpha\) is homeomorphic to a subspace of the Hausdorff space \(X\), and is therefore Hausdorff.
:::
