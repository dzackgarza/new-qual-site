---
schema: qual/card@1
id: D-MFPYG
kind: definition
title: "Hyperbolic translations/Blaschke factors"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.definition title="Hyperbolic translations/Blaschke factors"}
For $a\in \DD$, the maps
\[
\psi_a \da {a-z\over 1-\bar{a}z}
\]
are *hyperbolic translations* because they preserve the hyperbolic metric on the Poincaré disc.
They're also commonly called **Blaschke factors**, and also sometimes taken to be
\[
\phi_a \da {z-a \over 1-\bar{a} z} = - \psi_a
.\]
A rational map of the form
\[
\Psi_{\vector a}(z) = \lambda \prod_{1\leq k\leq n} \psi_a(z) = \lambda \prod_{1\leq k \leq n} {a_i - z\over 1 - \bar{a_i} z},\qquad \vector a\da\tv{a_1,\cdots, a_n}
\]
with zeros $a_i \in \DD$ is called a **Blaschke product** and is a map $\DD\to \DD$ that preserves $S^1$.
:::
