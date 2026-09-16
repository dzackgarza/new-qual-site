---
schema: qual/card@1
id: P-AGH269SINGCURVEPIC
kind: problem
title: The Picard group of a singular curve via normalization
classification:
  areas:
  - algebraic-geometry
  topics:
  - Picard Groups
  - Singular Curves
  - Normalization
relations: []
review: draft
---

::: {.problem}
Here we give another method of calculating the Picard group of a singular curve.
Let $X$ be a projective curve over $k$, let $\tilde X$ be its normalization, and let $\pi: \tilde X \to X$ be the projection map (Ex. 3.8).
For each point $P \in X$, let $\OO_P$ be its local ring, and let $\tilde\OO_P$ be the integral closure of $\OO_P$.
We use a $*$ to denote the group of units in a ring.

a. Show there is an exact sequence
\[
0 \to \bigoplus_{P \in X} \tilde\OO_P^* / \OO_P^* \to \Pic X \mapsvia{\pi^*} \Pic \tilde X \to 0
.\]
   *Hint:* represent $\Pic X$ and $\Pic \tilde X$ as the groups of Cartier divisors modulo principal divisors, and use the exact sequence of sheaves on $X$
\[
0 \to \pi_* \OO_{\tilde X}^* / \OO_X^* \to \mck^* / \OO_X^* \to \mck^* / \pi_* \OO_{\tilde X}^* \to 0
.\]

b. Use (a) to give another proof that if $X$ is a plane cuspidal cubic curve then there is an exact sequence
\[
0 \to \GG_a \to \Pic X \to \ZZ \to 0,
\]
   and if $X$ is a plane nodal cubic curve there is an exact sequence
\[
0 \to \GG_m \to \Pic X \to \ZZ \to 0
.\]
:::
