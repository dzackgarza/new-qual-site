---
schema: qual/card@1
id: E-HAT-4.K-5
kind: exercise
title: "Quasifibrations"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
---

A map $p: E \to B$ with $B$ not necessarily path-connected is defined to be a quasifibration if the following equivalent conditions are satisfied:

(i) For all $b \in B$ and $x_0 \in p^{-1}(b)$, the map $p_*: \pi_i(E, p^{-1}(b), x_0) \to \pi_i(B, b)$ is an isomorphism for $i > 0$ and $\pi_0(p^{-1}(b), x_0) \to \pi_0(E, x_0) \to \pi_0(B, b)$ is exact.

(ii) The inclusion of the fiber $p^{-1}(b)$ into the homotopy fiber $F_b$ of $p$ over $b$ is a weak homotopy equivalence for all $b \in B$.

(iii) The restriction of $p$ over each path-component of $B$ is a quasifibration according to the definition in this section.

Show these three conditions are equivalent, and prove Lemma 4K.3 for quasifibrations over non-path-connected base spaces.
