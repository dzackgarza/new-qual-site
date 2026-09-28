---
schema: qual/card@1
id: P-S3BCC
kind: problem
title: The kernel of the conjugation homomorphism $G\to\mathrm{Aut}(G)$ is $Z(G)$
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
Let $G$ be a group and let $\gamma: G \to \operatorname{Aut}(G)$ be the conjugation homomorphism defined by $\gamma(g) = c_g$, where $c_g(h) = g h g^{-1}$ for all $h \in G$.
Show that the kernel of $\gamma$ is the center of $G$:
$$\ker(\gamma) = Z(G).$$
:::

::: {.solution}
For $g\in G$,
\[
g\in\ker\gamma
\iff c_g=\operatorname{id}_G
\iff ghg^{-1}=h\quad\forall h\in G.
\]
Multiplying on the right by $g$ gives
\[
gh=hg\quad\forall h\in G,
\]
which is exactly the condition $g\in Z(G)$. Hence
\[
\boxed{\ker\gamma=Z(G)}.
\]
By the first isomorphism theorem this also yields
\[
\operatorname{Inn}(G)\cong G/Z(G).
\]
:::
