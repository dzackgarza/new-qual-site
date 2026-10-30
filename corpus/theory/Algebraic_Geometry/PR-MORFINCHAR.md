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

2. If $\pi$ is finite, then it is quasi-finite: every fibre is a finite scheme over its residue field and therefore has finitely many points [@Har77, Exercise II.3.5].

3. Every finite morphism is proper [@Har77, Exercise II.4.1]. If $Y$ is affine, every finite morphism $X\to Y$ is projective in the sense of [[D-MORPROJ|projective morphisms]].

4. Let $X$ and $Y$ be locally Noetherian. Then $\pi$ is finite exactly when it is proper and quasi-finite, equivalently proper with finite fibres [@Har77, Exercise III.11.2].
:::

::: {.remark}
The implications
$$
\text{finite} \implies \text{proper} \implies \text{universally closed}
$$
follow from the [[D-8XX95|valuative criteria]]. Over an affine base $Y=\Spec A$, a finite morphism $X=\Spec B\to Y$ is projective: generators $b_1,\ldots,b_N$ of $B$ as an $A$-module give a closed immersion $X\hookrightarrow\AA^N_Y\subseteq\PP^N_Y$, and its image is closed in $\PP^N_Y$ because $X$ is proper over $Y$. Proper does not imply finite: $\PP^1_k\to\Spec k$ is projective and not finite.

For locally Noetherian schemes, the converse in part 4 is a consequence of [[T-MORZMT|Zariski's main theorem]]: a separated quasi-finite morphism factors as an open immersion followed by a finite morphism. If the original morphism is proper, the [[PR-MORCANCEL|cancellation theorem]] applied to the finite second factor shows that the open immersion is proper; a proper open immersion is also closed. Its composite with the finite morphism is therefore finite.

Over a non-Noetherian base, a finite morphism need not be of finite presentation: if $A$ has an ideal $I$ that is not finitely generated, then $A/I$ is a finite $A$-module but is not finitely presented as an $A$-algebra.
:::
