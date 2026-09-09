---
schema: qual/card@1
id: E-HAT-4.2-20
kind: problem
title: "Trivial $\\pi_1$-action on $\\pi_n$ of products"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 20; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Let $G$ be a group and $X$ a simply-connected space.
Show that for the product $K(G, 1) \times X$ the action of $\pi_1$ on $\pi_n$ is trivial for all $n > 1$.

::: {.solution}
Let \(K=K(G,1)\) and let
\[
p:\widetilde K\times X\longrightarrow K\times X
\]
be the universal covering. Since \(X\) is simply connected, the deck group is \(G\), acting by
\[
g\cdot(u,x)=(gu,x).
\]
The projection
\[
\widetilde K\times X\to X
\]
is a homotopy equivalence because \(\widetilde K\) is contractible. Under the induced identification
\[
\pi_n(K\times X)\cong\pi_n(\widetilde K\times X)\cong\pi_n(X),
\qquad n>1,
\]
every deck transformation acts as the identity on the \(X\)-factor. Hence it induces the identity on \(\pi_n\).

By the description of the \(\pi_1\)-action via deck transformations,
\[
\boxed{\pi_1(K(G,1)\times X)\text{ acts trivially on }\pi_n(K(G,1)\times X),\ n>1.}
\]
:::
