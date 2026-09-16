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
:::

::: {.proof}
1. There is a natural map $f_* \mathcal{F} \otimes \mathcal{E} \to f_*(\mathcal{F} \otimes f^* \mathcal{E})$, adjoint to $f^* f_* \mathcal{F} \otimes f^* \mathcal{E} \to \mathcal{F} \otimes f^* \mathcal{E}$.
2. Whether it is an isomorphism is local on $Y$, so assume $\mathcal{E} = \OO_Y^{\oplus r}$; both sides become $(f_* \mathcal{F})^{\oplus r}$ compatibly.
3. For $i > 0$, take an injective resolution $\mathcal{F} \to \mathcal{I}^\bullet$ and apply the map of step 1 termwise, giving $f_* \mathcal{I}^\bullet \otimes \mathcal{E} \to f_*(\mathcal{I}^\bullet \otimes f^* \mathcal{E})$.
   Over an open $V \subseteq Y$ where $\mathcal{E}|_V$ is free of rank $r$, the restriction of an injective module to $f^{-1}V$ is injective, so $\mathcal{I}^\bullet \otimes f^* \mathcal{E}$ restricts to the injective resolution $(\mathcal{I}^\bullet|_{f^{-1}V})^{\oplus r}$ of $(\mathcal{F} \otimes f^* \mathcal{E})|_{f^{-1}V}$, and both sides have cohomology $(R^i f_* \mathcal{F}|_V)^{\oplus r}$, compatibly with the map.
:::

::: {.example}
For $\pi \colon \PP(\mathcal{V}) \to Y$ a projective bundle and $\mathcal{L}$ a line bundle on $Y$, $\pi_*(\OO(m) \otimes \pi^* \mathcal{L}) \cong \Sym^m \mathcal{V} \otimes \mathcal{L}$ for $m \geq 0$.
:::
