---
schema: qual/card@1
id: PR-MORFINCHAR
kind: proposition
title: Finite morphisms as proper quasi-finite morphisms
slogan: 'Over locally Noetherian schemes, a morphism is finite exactly when it is proper and quasi-finite, equivalently proper with finite fibres.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Finite Morphisms
  - Proper Morphisms
  - Quasi-finite Morphisms
relations:
- kind: uses
  target: D-MORFIN
- kind: uses
  target: D-8XX95
review: draft
prompts:
- Give a criterion for a morphism to be finite.
- How are finite, proper, and projective related?
---

::: {.proposition}
Let $\pi \colon X \to Y$ be a morphism of schemes.

1. $\pi$ is finite if and only if it is integral and locally of finite type.

2. If $\pi$ is finite, then it is quasi-finite: every fibre is a finite scheme over its residue field and therefore has finitely many points [@Har10a, Exercise II.3.5].

3. Every finite morphism is projective in the sense of [[D-MORPROJ]], hence proper.

4. Let $X$ and $Y$ be locally Noetherian. Then $\pi$ is finite exactly when it is proper and quasi-finite, equivalently proper with finite fibres [@Har10a, Exercise III.11.2].
:::

::: {.remark}
The implications
$$
\text{finite} \implies \text{projective} \implies \text{proper} \implies \text{universally closed},
$$
follow from [[D-MORPROJ]] and [[D-8XX95]]. The first implication is not reversible: $\PP^1_k\to\Spec k$ is projective and not finite.

For locally Noetherian schemes, the converse in part 4 is a consequence of Zariski's main theorem: a separated quasi-finite morphism factors as an open immersion followed by a finite morphism ([[T-MORZMT]]). If the original morphism is proper, [[PR-MORCANCEL]] applied to the finite second factor shows that the open immersion is proper; a proper open immersion is also closed. Its composite with the finite morphism is therefore finite.

The locally Noetherian hypothesis in part 4 is the scope of the cited Hartshorne result, not a replacement by local finite presentation outside that scope. In particular, a finite morphism over a non-Noetherian base need not be locally of finite presentation: if $A$ has a non-finitely-generated ideal $I$, then $A\to A/I$ is finite as a module map but is not finitely presented as an $A$-algebra.
:::
