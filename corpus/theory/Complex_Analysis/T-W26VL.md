---
schema: qual/card@1
id: T-W26VL
kind: theorem
title: Automorphisms of the unit disc as rotated Blaschke factors
slogan: 'Every unit-disc automorphism is exactly a Blaschke factor followed by a rotation.'
classification:
  areas:
  - complex-analysis
  topics:
  - Biholomorphisms
  - Blaschke Factors
relations: []
review: draft
---

::: {.theorem}
For $a\in\DD$ let $\psi_a(z)\coloneqq\dfrac{a-z}{1-\overline{a}z}$ be the [[D-MFPYG|Blaschke factor]] at $a$.
The group $\Aut_\CC(\DD)$ of [[D-TM4TE|biholomorphisms]] $\DD\to\DD$ is
$$
\Aut_\CC(\DD)=\{\lambda\psi_a : a\in\DD,\ \lambda\in S^1\},
$$
so every automorphism of $\DD$ is a Blaschke factor followed by a rotation.

Written out, the group is the set of maps
$$
z\mapsto e^{i\theta}\,{\alpha-z\over 1-\overline{\alpha}z}, \qquad \theta\in\RR,\ \alpha\in\DD,
$$
the rotations composed with the Blaschke factors; this is [@SS03, Theorem 2.2 of Chapter 8 (p. 220)], where the proof runs the Schwarz lemma on $f\circ\psi_\alpha$ and on its inverse.
:::
