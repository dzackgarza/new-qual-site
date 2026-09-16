---
schema: qual/card@1
id: D-SCHRED
kind: definition
title: The reduced induced structure on a closed subset
classification:
  areas:
  - algebraic-geometry
  topics:
  - Subschemes
  - Reduced Schemes
  - Ideal Sheaves
relations:
- kind: uses
  target: D-SCHSUB
- kind: related-to
  target: PR-6TCSJ
review: draft
prompts:
- What is the reduced induced scheme structure on a closed subset?
- In what sense is it canonical?
---

::: {.definition}
Let $Z \subseteq \abs{X}$ be closed.
For $X = \Spec A$ take $\mfa \da \Intersect_{\mfp \in Z} \mfp$, a radical ideal, and give $Z$ the structure $\Spec(A/\mfa)$.
These agree on overlaps, so they glue to a closed subscheme structure on $Z$ for any $X$: the \dfn{reduced induced structure} $Z^\red$.
:::

::: {.proposition}
$Z^\red$ is the unique reduced closed subscheme of $X$ with underlying space $Z$, and it is the *smallest* closed subscheme with that space: every closed subscheme supported on $Z$ contains $Z^\red$ as a closed subscheme.
:::

::: {.remark}
"Canonical" here means a universal property, and that is what should be volunteered: any morphism from a reduced scheme $T \to X$ whose image lies in $Z$ factors uniquely through $Z^\red$.
Taking $Z = \abs{X}$ gives the reduction $X^\red \to X$, a homeomorphism which is not an isomorphism unless $X$ was already reduced.

The ideal is radical by construction, which is where the classical Nullstellensatz dictionary sits: $\mci(V(\mfa)) = \sqrt{\mfa}$ says that passing to the reduced structure is taking the radical.
The scheme language keeps the non-radical ideals, and the reduced induced structure is the functor that throws them away.
:::
