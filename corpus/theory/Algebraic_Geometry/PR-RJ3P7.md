---
schema: qual/card@1
id: PR-RJ3P7
kind: proposition
title: Going up and going down, read on spectra
classification:
  areas:
  - algebraic-geometry
  topics:
  - Going Up
  - Finite Morphisms
  - Flatness
relations:
- kind: uses
  target: D-VKR54
review: draft
prompts:
- What does the going up theorem mean in algebraic geometry?
- What does going down mean geometrically?
---

::: {.proposition title="Going up, geometrically"}
Let $A \to B$ be an integral ring extension, and $f: \Spec B \to \Spec A$ the induced map.
Then $f$ is **closed** and **surjective**, and it has finite fibres when the extension is finite.
:::

::: {.proposition title="Going down, geometrically"}
If $A \to B$ is flat, or if $A$ is normal, $B$ a domain and the extension integral, then $f$ is **open** onto its image, and every specialisation in $\Spec A$ lifts along $f$: a chain descending from a point of the image can be followed downstairs.
:::

::: {.remark}
The translation is the content of the answer: going up says that a chain of primes in $A$ ascending from one that is hit can be lifted, which is exactly the statement that the image of a closed set is closed.
So going up is the algebraic form of "a finite morphism is closed", hence of "a finite morphism is proper".

Going down is the dimension-preserving half.
It is what makes $\dim B = \dim A$ for an integral extension of domains, and it is why a finite surjective morphism cannot drop dimension.

The two are the reason finite morphisms behave like branched covers: closed, surjective, with finite fibres, and preserving dimension.
:::
