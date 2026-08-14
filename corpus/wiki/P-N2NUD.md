---
schema: qual/card@1
id: P-N2NUD
kind: problem
title: "2. We need to show that $R$ is reflexive, transitive, and symmetric."
classification:
  areas:
  - prelim
  topics:
  - functions-and-relations
relations: []
review: draft
---
2. We need to show that $R$ is reflexive, transitive, and symmetric.
   1. Reflexive: this would say that $x\sim x \iff x^2-4x = x^2-4x$, which is true.
   2. Transitive: suppose $x\sim y$ and $y\sim z$, we want to show $x\sim z$. But we have
   $$
   x^2 - 4x = y^2-4y ~\&~ y^2-4y = z^2-4z \implies x^2-4x = y^2-4y = z^2-4z
   $$
   1. We want to show $x\sim y \implies y \sim x$, which follows because $x^2-4x = y^2-4y \iff y^2-4y = x^2-4x$.
   2. The equivalence classes:
   $$\begin{align*}
   x^2-4x &=  0:  &\theset{0, 4}\\
   x^2-4x &= -3: &\theset{1,3} \\
   x^2-4x &= -4: &\theset{2} \\
   x^2-4x &=  5: &\theset{5}
   \end{align*}$$

