---
schema: qual/card@1
id: E-SS8.EX-13
kind: exercise
title: "SS 8.13: The pseudo-hyperbolic metric and the Schwarz-Pick inequality"
classification:
  areas:
  - complex-analysis
  topics: ['Conformal Mappings', 'Riemann Mapping Theorem', 'Automorphisms']
relations: []
review: draft
solved: false
---

::: exercise
13. The pseudo-hyperbolic distance between two points $z , w \in \mathbb { D }$ is defined by

$$

\rho (z, w) = \left| \frac {z - w}{1 - \overline {{w}} z} \right|.

$$

(a) Prove that if $f : \mathbb { D } \to \mathbb { D }$ is holomorphic, then

$$

\rho (f (z), f (w)) \leq \rho (z, w) \quad \text {   for   all   } z, w \in \mathbb {D}.

$$

Moreover, prove that if $f$ is an automorphism of D then f preserves the pseudo-hyperbolic distance

$$

\rho (f (z), f (w)) = \rho (z, w) \quad \text {   for   all   } z, w \in \mathbb {D}.

$$

[Hint: Consider the automorphism $\psi _ { \alpha } ( z ) = ( z - \alpha ) / ( 1 - \overline { { \alpha } } z )$ and apply the Schwarz lemma to $\psi _ { f ( w ) } \circ f \circ \psi _ { w } ^ { - 1 } . ]$

(b) Prove that

$$

\frac {| f ^ {\prime} (z) |}{1 - | f (z) | ^ {2}} \leq \frac {1}{1 - | z | ^ {2}} \quad \text { for   all } z \in \mathbb {D}.

$$

This result is called the Schwarz-Pick lemma. See Problem 3 for an important application of this lemma.
:::
