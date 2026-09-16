---
schema: qual/card@1
id: PR-OODAV
kind: proposition
title: Splitting lemma for short exact sequences
classification:
  areas:
  - algebra
  topics:
  - Exact Sequences
  - Projective Modules
  - Homological Algebra
relations: []
review: draft
---

::: {.proposition}
Let $R$ be a ring and let $\xi\colon 0 \to A \mapsvia{d_1} B \mapsvia{d_2} C \to 0$ be a short exact sequence of $R$-modules.
The following are equivalent:

- $\xi$ admits a [[D-3JJJN|right-splitting]]: an $R$-linear $s\colon C\to B$ with $d_2\circ s=\id_C$.

- $\xi$ admits a [[D-3JJJN|left-splitting]]: an $R$-linear $t\colon B\to A$ with $t\circ d_1=\id_A$.

- There is an isomorphism $\varphi\colon B\to A\oplus C$ with $\varphi\circ d_1=\iota_A$ and $\pi_C\circ\varphi=d_2$, where $\iota_A\colon A\to A\oplus C$ is the inclusion and $\pi_C\colon A\oplus C\to C$ is the projection.
:::

::: {.remark}
A [[D-RHJMK|projective]] or injective module characterizes splitting for all sequences at once:
$C$ is projective if and only if every short exact sequence of $R$-modules $0\to A'\to B'\to C\to 0$ splits, and $A$ is injective if and only if every short exact sequence $0\to A\to B'\to C'\to 0$ splits.
:::

::: {.example}
A single short exact sequence can split with $C$ not projective.
Over $\ZZ$, the sequence $0\to \ZZ/2\ZZ \to \ZZ/2\ZZ \oplus \ZZ/2\ZZ \to \ZZ/2\ZZ\to 0$ with the inclusion of the first summand and the projection onto the second splits, but $\ZZ/2\ZZ$ is not a projective $\ZZ$-module, since the surjection $\ZZ\to\ZZ/2\ZZ$ has no section.
:::
