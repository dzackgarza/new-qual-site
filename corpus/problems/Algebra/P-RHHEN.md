---
schema: qual/card@1
id: P-RHHEN
kind: problem
title: Hilbert's Nullstellensatz
classification:
  areas:
  - algebra
  topics:
  - Geometry
  - Maximal Ideals
  - Commutative Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
(1) State the **Weak** and **Strong** forms of **Hilbert's Nullstellensatz** over an algebraically closed field $k$.
(2) State the geometric bijection between radical ideals in $k[x_1, \dots, x_n]$ and algebraic sets in $\mathbb{A}^n(k)$.
(3) Sketch the proof of the Nullstellensatz (Zariski's Lemma / Noether Normalization, and the Rabinowitsch trick).
:::

::: {.solution}
Let $k$ be algebraically closed and $R=k[x_1,\dots,x_n]$.

**Weak Nullstellensatz.** Every maximal ideal of $R$ has the form
\[
(x_1-a_1,\dots,x_n-a_n),\qquad a_i\in k.
\]
Equivalently, every proper ideal of $R$ has a common zero in $k^n$.

**Strong Nullstellensatz.** For every ideal $I\subseteq R$,
\[
I(V(I))=\sqrt I.
\]
Consequently, $I\mapsto V(I)$ and $X\mapsto I(X)$ give inclusion-reversing bijections between radical ideals of $R$ and algebraic subsets of $\mathbb A^n(k)$. Under this correspondence, maximal ideals correspond to points and prime ideals to irreducible algebraic sets.

For the weak theorem, if $\mathfrak m$ is maximal then $R/\mathfrak m$ is a field finitely generated as a $k$-algebra. Zariski's lemma makes it algebraic over $k$, hence equal to $k$ because $k$ is algebraically closed. The images of the $x_i$ therefore give the point $(a_1,\dots,a_n)$.

For the strong theorem, let $g$ vanish on $V(I)$ and consider
\[
J=(I,1-yg)\subset k[x_1,\dots,x_n,y].
\]
Then $V(J)=\varnothing$, so the weak theorem gives $J=(1)$. Writing $1$ as a combination of generators of $I$ and $1-yg$, then substituting $y=g^{-1}$ and clearing denominators, yields $g^N\in I$ for some $N$. Hence $g\in\sqrt I$.
:::
