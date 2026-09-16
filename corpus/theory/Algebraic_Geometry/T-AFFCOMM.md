---
schema: qual/card@1
id: T-AFFCOMM
kind: theorem
title: The affine communication lemma
classification:
  areas:
  - algebraic-geometry
  topics:
  - Affine Schemes
  - Open Covers
  - Schemes
relations:
- kind: uses
  target: D-VKR54
- kind: uses
  target: PR-SCHUNITCOVER
- kind: related-to
  target: D-MORLOCAL
review: draft
prompts:
- State the affine communication lemma.
- Why is integrality not an affine-local property?
---

::: {.theorem title="Affine communication lemma"}
Let $X$ be a scheme and $P$ a property of affine open subschemes of $X$ such that

1. if $\Spec A \subseteq X$ has $P$ and $f \in A$, then $\Spec A_f \subseteq X$ has $P$, and

2. if $\Spec A \subseteq X$ is an affine open, $f_1, \ldots, f_n \in A$ generate the unit ideal, and every $\Spec A_{f_i}$ has $P$, then $\Spec A$ has $P$.

If $X$ has a cover by affine opens $\Spec A_i$ with $P$, then every affine open of $X$ has $P$ [@Vak25, Lemma 5.3.2].
:::

::: {.example}
Being Noetherian, and for a scheme over a ring $R$ being of finite type over $R$, satisfy both hypotheses, so they can be checked on one affine cover; so do properties defined on stalks, such as being reduced.
:::

::: {.example}
Integrality does not satisfy hypothesis 2.
For nonzero integral domains $A$ and $B$, the elements $e_1 = (1, 0)$ and $e_2 = (0, 1)$ of $A \times B$ generate the unit ideal, and $(A \times B)_{e_1} \cong A$ and $(A \times B)_{e_2} \cong B$ are integral domains, but $A \times B$ is not, since $e_1 e_2 = 0$.
Geometrically, $\Spec(A \times B) = \Spec A \sqcup \Spec B$ is covered by integral affine opens and is not irreducible.
:::
