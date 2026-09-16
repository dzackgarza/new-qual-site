---
schema: qual/card@1
id: D-HENSEL
kind: definition
title: Hensel's lemma and henselization
classification:
  areas:
  - algebraic-geometry
  topics:
  - Henselian Rings
  - Complete Local Rings
  - Etale Morphisms
relations:
- kind: related-to
  target: D-MORETALE
review: draft
prompts:
- What is Hensel's lemma?
- What is the henselization of a local ring?
---

::: {.theorem title="Hensel's lemma"}
Let $(R, \mfm, k)$ be a complete Noetherian local ring and $f \in R[x]$ monic.
If the reduction $\bar{f} \in k[x]$ factors as $\bar{f} = g_0 h_0$ with $g_0, h_0$ monic and coprime, then $f = g h$ with $g, h \in R[x]$ monic, $\bar{g} = g_0$ and $\bar{h} = h_0$.
In particular a simple root of $\bar{f}$ in $k$ lifts to a root of $f$ in $R$.
:::

::: {.definition title="Henselian ring and henselization"}
A local ring $(R, \mfm)$ is \dfn{henselian} if the conclusion of Hensel's lemma holds for every monic $f \in R[x]$.
The \dfn{henselization} $R^h$ of a local ring $R$ is a henselian local ring with a local homomorphism $R \to R^h$ through which every local homomorphism from $R$ to a henselian local ring factors uniquely.
It is the colimit of the local rings $\OO_{U,u}$ over étale neighbourhoods $(U, u) \to (\Spec R, \mfm)$ with trivial residue field extension.
:::

::: {.example}
Complete local rings are henselian, and $R \to R^h \to \hat{R}$.
For $R = k[x]_{(x)}$, $R^h$ is the ring of power series in $k[[x]]$ that are algebraic over $k(x)$; it contains $\sqrt{1+x}$ in characteristic not $2$, which $R$ does not, and it does not contain $e^x$ when $k = \CC$.
:::
