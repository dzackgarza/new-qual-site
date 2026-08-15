---
schema: qual/card@1
id: D-VP4LC
kind: definition
title: "Kronecker Pairing"
classification:
  areas:
  - topology
  topics:
  - cohomology
  - homology
relations:
- kind: related-to
  target: D-Y73BB
review: draft
---

::: {.definition title="Kronecker Pairing"}
Evaluating a cochain on a chain, $\inner{\varphi}{\alpha} \da \varphi(\alpha)$, is compatible with the differentials, since $\inner{\delta\varphi}{\alpha} = \inner{\varphi}{\del\alpha}$.
It therefore descends to a pairing on (co)homology,
\[
\inner{\wait}{\wait}: H^n(X; R) \cross H_n(X; R) \to R
,\]
the **Kronecker product**, also written as the Kronecker pairing.
It is natural in the sense that $\inner{f^*\beta}{x} = \inner{\beta}{f_*x}$ for $f: X\to Y$, $\beta\in H^n(Y;R)$ and $x \in H_n(X;R)$.
Its adjoint is the evaluation homomorphism
\[
h: H^n(X; R) \to \Hom_R(H_n(X;R), R)
,\]
which is the surjection appearing in the universal coefficient theorem; $h$ is an isomorphism exactly when the $\Ext$ term vanishes, so cohomology is *not* simply the dual of homology.
:::

::: {.concept}
See Hatcher, §3.1, Theorem 3.2 for the universal coefficient sequence that $h$ sits in.
The related card *Kronecker Pairing* states the same map under that other name.
:::
