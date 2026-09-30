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
For $X = \Spec A$ take $\mfa \definedas \Intersect_{\mfp \in Z} \mfp$, a radical ideal, and give $Z$ the structure $\Spec(A/\mfa)$.
These agree on overlaps, so they glue to a closed subscheme structure on $Z$ for any $X$: the \dfn{reduced induced structure} $Z^\red$.
:::

::: {.proposition}
$Z^\red$ is the unique reduced closed subscheme of $X$ with underlying space $Z$, and it is the smallest closed subscheme with that space: every closed subscheme supported on $Z$ contains $Z^\red$ as a closed subscheme.
Every morphism $T\to X$ from a reduced scheme $T$ whose image lies in $Z$ factors uniquely through $Z^\red$.
:::

::: {.remark}
Taking $Z = \abs{X}$ gives the reduction $X^\red \to X$, a homeomorphism that is an isomorphism if and only if $X$ is reduced.
For an ideal $\mfa\subseteq A$, $\bigcap_{\mfp\supseteq\mfa}\mfp=\sqrt{\mfa}$, so the reduced induced structure on $V(\mfa)\subseteq\Spec A$ is $\Spec(A/\sqrt{\mfa})$.
:::
