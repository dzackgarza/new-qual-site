---
schema: qual/card@1
id: PR-SCHPROJFORM
kind: proposition
title: The projection formula
classification:
  areas:
  - algebraic-geometry
  topics:
  - Direct Image Functor
  - Locally Free Sheaves
  - Higher Direct Images
relations:
- kind: uses
  target: D-MODPULL
review: draft
prompts:
- What is Serre's projection formula?
---

::: {.proposition title="Projection formula"}
Let $f \colon X \to Y$ be a morphism of ringed spaces, $\mathcal{F}$ an $\OO_X$-module, and $\mathcal{E}$ a locally free $\OO_Y$-module of finite rank.
Then there are natural isomorphisms
\[
R^i f_* (\mathcal{F} \otimes_{\OO_X} f^* \mathcal{E}) \cong R^i f_* \mathcal{F} \otimes_{\OO_Y} \mathcal{E}
\]
for all $i \geq 0$.
[@Har10a, Exercise III.8.3]
:::

::: {.example}
For $\pi \colon \PP(\mathcal{V}) \to Y$ a projective bundle and $\mathcal{L}$ a line bundle on $Y$, $\pi_*(\OO(m) \otimes \pi^* \mathcal{L}) \cong \Sym^m \mathcal{V} \otimes \mathcal{L}$ for $m \geq 0$.
:::
