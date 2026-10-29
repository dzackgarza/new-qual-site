---
schema: qual/card@1
id: PR-E4T3S
kind: proposition
title: Galois groups of irreducible quartics over $\QQ$
slogan: 'Discriminant, resolvent, and one quadratic-extension test determine an irreducible quartic''s Galois group.'
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Classification
  - Polynomials
relations: []
review: draft
---

::: {.proposition}
Let $f \in \QQ[x]$ be a monic irreducible quartic with [[D-W3DSO|discriminant]] $\Delta$ and [[D-4DWC5|resolvent cubic]] $R_4$, and let $G \leq S_4$ be the Galois group of a splitting field of $f$ over $\QQ$ [@Hun74].

- If $\sqrt{\Delta} \in \QQ$, then $G = A_4$ or $G = V_4 \cong C_2^2$: $G = A_4$ if $R_4$ is irreducible over $\QQ$, and $G = V_4$ otherwise.

- If $\sqrt{\Delta} \notin \QQ$, then $G = S_4$, $D_4$, or $C_4$: $G = S_4$ if $R_4$ is irreducible over $\QQ$.
  Otherwise $G = D_4$ if $f$ is irreducible over $\QQ(\sqrt{\Delta})$, and $G = C_4$ if $f$ is reducible over $\QQ(\sqrt{\Delta})$.
:::

::: {.remark}
The discriminant of $R_4$ equals $\Delta$.
So when $R_4$ is reducible over $\QQ$, it splits into linear factors over $\QQ$ if $\sqrt\Delta\in\QQ$ and has exactly one root in $\QQ$ if $\sqrt\Delta\notin\QQ$.
In terms of $R_4$ alone: $G=V_4$ if and only if $R_4$ splits into linear factors over $\QQ$, and $G\in\theset{D_4,C_4}$ if and only if $R_4$ has exactly one root in $\QQ$.
:::

::: {.remark}
The groups $D_4$ and $C_4$ can also be distinguished by cycle types: the copy of $D_4$ in $S_4$ contains transpositions, whereas $C_4$ contains only $4$-cycles, the identity, and one product of two transpositions.
:::
