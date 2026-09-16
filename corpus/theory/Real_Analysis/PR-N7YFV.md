---
schema: qual/card@1
id: PR-N7YFV
kind: proposition
title: $L^1$ embeds isometrically in $(L^\infty)^*$ but not surjectively
classification:
  areas:
  - real-analysis
  topics:
  - Dual Spaces
  - L∞
  - L¹
relations: []
review: draft
---

::: {.proposition}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure space]].
For $g\in L^1(\mu)$, the map $\phi_g\colon L^\infty(\mu)\to\CC$, $\phi_g(f)\coloneqq\int_X fg\dmu$, is a bounded linear functional with $\norm{\phi_g}=\norm{g}_1$, so $g\mapsto\phi_g$ is an isometric linear embedding $L^1(\mu)\to(L^\infty(\mu))^*$ [@Fol13].
For Lebesgue measure on $[0,1]$ this embedding is not surjective.
:::

::: {.example}
The functional $f\mapsto f(0)$ on the subspace $C([0,1])\subseteq L^\infty([0,1])$ has norm $1$, and by the Hahn--Banach theorem it extends to some $\Lambda\in(L^\infty([0,1]))^*$.
No $g\in L^1([0,1])$ satisfies $\Lambda=\phi_g$.
:::
