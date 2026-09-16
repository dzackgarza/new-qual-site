---
schema: qual/card@1
id: P-AGH282GENERICSECTION
kind: problem
title: A nowhere-vanishing section of a high-rank locally free sheaf
classification:
  areas:
  - algebraic-geometry
  topics:
  - Locally Free Sheaves
  - Global Sections
  - Bertini's Theorem
relations: []
review: draft
---

::: {.problem}
Let $X$ be a variety of dimension $n$ over $k$.
Let $\mce$ be a locally free sheaf of rank $> n$ on $X$, and let $V \subseteq \Gamma(X, \mce)$ be a vector space of global sections which generate $\mce$.
Then show that there is an element $s \in V$ such that for each $x \in X$ we have $s_x \not\in \mfm_x \mce_x$.
Conclude that there is a morphism $\OO_X \to \mce$ giving rise to an exact sequence
\[
0 \to \OO_X \to \mce \to \mce' \to 0,
\]
where $\mce'$ is also locally free.

*Hint:* use a method similar to the proof of Bertini's theorem (8.18).
:::
