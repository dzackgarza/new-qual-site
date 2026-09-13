---
schema: qual/card@1
id: P-AGXGATHRELNSS
kind: problem
title: Relative Nullstellensatz over the coordinate ring of a variety
classification:
  areas:
  - algebraic-geometry
  topics:
  - Nullstellensatz
  - Coordinate Rings
  - Radical Ideals
relations: []
review: draft
---

::: problem
Let $Y\subset \AA^n/k$ be an affine variety and define $A(Y)$ by the quotient
\[
\pi: k[x_1,\cdots, x_n] \to A(Y) \da k[x_1, \cdots, x_n]/I(Y)
.\]

a. Show that $V_Y(J) = V(\pi^{-1}(J))$ for every $J\normal A(Y)$.

b. Show that $\pi^{-1} (I_Y(X)) = I(X)$ for every affine subvariety $X\subseteq Y$.

c. Using the fact that $I(V(J)) \subset \sqrt{J}$ for every $J\normal k[x_1, \cdots, x_n]$, deduce that $I_Y(V_Y(J)) \subset \sqrt{J}$ for every $J\normal A(Y)$.

Conclude that there is an inclusion-reversing bijection
\[
\correspond{\text{Affine subvarieties}\\ \text{of } Y} \iff \correspond{\text{Radical ideals} \\ \text{in } A(Y)}
.\]
:::
