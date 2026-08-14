---
schema: qual/card@1
id: D-TK4QD
kind: definition
title: "Intersection Pairing"
classification:
  areas:
  - topology
  topics:
  - poincare-duality
  - cohomology
  - manifolds
relations: []
review: draft
---
:::{.definition title="Intersection Pairing"}
For a manifold $M$, a map on homology defined by
\[
H_{\hat i}M \tensor H_{\hat j}M \to H_{\widehat{i+j}}X\\
\alpha\tensor \beta \mapsto \left< \alpha, \beta \right>
\]
obtained by conjugating the cup product with Poincaré Duality, i.e. 

\[\left< \alpha, \beta \right> = [M] \frown ([\alpha]\dual \smile [\beta]\dual)
.\]

Then, if $[A], [B]$ are transversely intersecting submanifolds representing $\alpha, \beta$, then $$\left<\alpha, \beta\right> = [A\intersect B]$$.
If $\hat i = j$ then $\left< \alpha, \beta \right> \in H_{0} M = \ZZ$ is the signed number of intersection points.

Alt:
The pairing obtained from dualizing Poincare Duality to obtain $$\mathrm{F}(H_{i} M) \tensor \mathrm{F}(H_{n-i}M) \to \ZZ$$
Computed as an oriented intersection number between two homology classes (perturbed to be transverse).


:::
