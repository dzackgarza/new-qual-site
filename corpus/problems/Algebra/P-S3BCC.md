---
schema: qual/card@1
id: P-S3BCC
kind: problem
title: The kernel of the conjugation homomorphism $G\to\Aut(G)$ is $Z(G)$
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Centralizers and Normalizers
  - Homomorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Let $G$ be a group and let $\gamma: G \to \Aut(G)$ be the conjugation homomorphism defined by $\gamma(g) = c_g$, where $c_g(h) = g h g^{-1}$ for all $h \in G$.
Show that the kernel of $\gamma$ is the center of $G$:
$$\ker(\gamma) = Z(G).$$
:::

::: {.solution}

::: pf

::: pf-step

For $g\in G$, $g\in\ker\gamma$ if and only if $ghg^{-1}=h$ for all $h\in G$.

::: pf-proof

$g\in\ker\gamma$ means $c_g=\operatorname{id}_G$, that is, $c_g(h)=h$ for every $h$.

:::

:::

::: pf-qed

Multiplying $ghg^{-1}=h$ on the right by $g$ shows that it is equivalent to $gh=hg$. So $g\in\ker\gamma$ exactly when $g$ commutes with every $h\in G$, that is, when $g\in Z(G)$. Hence $\ker\gamma=Z(G)$, and the first isomorphism theorem gives $\Inn(G)\cong G/Z(G)$.

:::

:::

:::
