---
schema: qual/card@1
id: PR-QX0VL
kind: proposition
title: Two morphisms agreeing on a dense open agree
classification:
  areas:
  - algebraic-geometry
  topics:
  - Separated Morphisms
  - Reduced Schemes
  - Density
relations:
- kind: uses
  target: D-T2J3Q
review: draft
prompts:
- Name a good property of separated morphisms.
- If two morphisms agree on a dense open subset, do they agree?
---

::: {.proposition}
Let $f : X \to Y$ be separated, let $Z$ be a **reduced** scheme over $Y$, and let $g, h : Z \to X$ be $Y$-morphisms agreeing on a dense open $U \subseteq Z$.
Then $g = h$.
:::

::: {.remark}
This is the good property to name, and the proof shows why both hypotheses are there.
The pair $(g,h)$ gives $Z \to X \fiberprod{Y} X$, and the locus where $g$ and $h$ agree is the preimage of the diagonal.
Separatedness makes that preimage **closed**; it contains the dense $U$, so it is all of $Z$ topologically.
Reducedness upgrades the topological statement to an equality of morphisms, because a closed subscheme of a reduced scheme with the whole space as support is the whole scheme.

So the analogue for quasi-separated is weaker in exactly the way the diagonal is: quasicompactness of the diagonal gives a retrocompact agreement locus, not a closed one, and the conclusion fails.
Quasi-separatedness is what one assumes to make cohomology and direct images behave, not to make morphisms equal.
:::
