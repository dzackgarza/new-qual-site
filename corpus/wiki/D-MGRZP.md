---
schema: qual/card@1
id: D-MGRZP
kind: definition
title: "Nullhomotopic"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---
:::{.definition title="Nullhomotopic"}
A map $X\mapsvia{f} Y$ is *nullhomotopic* if it is homotopic to a constant map $X \mapsvia{g} \theset{y_{0}}$; that is, there exists a homotopy 
\[  
F: X\cross I &\to Y \\
\restrictionof{F}{X\cross\theset{0}} &= f \quad F(x, 0) = f(x) \\
\restrictionof{F}{X\cross\theset{1}} &= g  \quad F(x, 1) = g(x) = y_{0}\\
.\]

Alt:

If $f$ is homotopic to a constant map, say $f: x \mapsto y_0$ for some fixed $y_0 \in Y$, then $f$ is said to be *nullhomotopic*. In other words, if $f:X\into Y$ is nullhomotopic, then there exists a homotopy $H: X\cross I \into Y$ such that $H(x, 0) = f(x)$ and $H(x, 1) = y_0$.

Note that constant maps (or anything homotopic) induce zero homomorphisms.


:::
