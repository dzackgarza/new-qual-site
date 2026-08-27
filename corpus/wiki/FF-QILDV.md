---
schema: qual/card@1
id: FF-QILDV
kind: fact
title: Flat modules over a Noetherian ring are free
prompts:
- Give a categorical/homological corollary of Nakayama's lemma.
classification:
  areas:
  - algebra
  topics:
  - Nakayama's Lemma
  - Free Modules
  - Modules
relations: []
review: draft
---

::: {.fact}
For $ R $ Noetherian, $ M\in   {}_{R}{\mathsf{Mod}} $ flat, then $ M $ is free:

Take a presentation $ K\hookrightarrow R^n \twoheadrightarrow M $, reduce to $ k $ to get $ K'\hookrightarrow k^n \twoheadrightarrow M' $ where $ K'=0 \implies K=0 $.

Thus flat coherent sheaves over a Noetherian scheme are vector bundles.
:::
