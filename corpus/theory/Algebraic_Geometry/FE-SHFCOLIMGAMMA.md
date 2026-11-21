---
schema: qual/card@1
id: FE-SHFCOLIMGAMMA
kind: example
title: Global sections do not commute with filtered colimits of sheaves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Direct Limits
  - Counterexamples
relations:
- kind: uses
  target: PR-IP6ZG
review: draft
prompts:
- Does $\Gamma$ commute with filtered colimits of sheaves?
- Give a filtered colimit of sheaves whose sections are not the colimit of the sections.
---

::: {.example}
Let $X=\NN$ with the discrete topology, and for $i\in\NN$ let $\mcf_i$ be the sheaf with $\mcf_i(\theset{n})=\ZZ$ for $n\le i$ and $0$ for $n>i$.
The sheaves $\mcf_i$ form a filtered direct system, and $\colim_i\mcf_i$ is the constant sheaf $\ZZ$: at each point $n$ the transition maps $\mcf_i(\theset n)\to\mcf_j(\theset n)$ are the identity for $i\le j$ and $n\le i$, so the colimit of the stalks is $\ZZ$.
On the discrete space a sheaf is its ring of sections, so $\Gamma(X,\ZZ)=\prod_{n}\ZZ$ while $\Gamma(X,\mcf_i)=\bigoplus_{n\le i}\ZZ$ and hence $\colim_i\Gamma(X,\mcf_i)=\bigoplus_{n}\ZZ$.
The canonical map $\bigoplus_n\ZZ\to\prod_n\ZZ$ is injective and not surjective, so $\colim_i\Gamma(X,\mcf_i)\to\Gamma(X,\colim_i\mcf_i)$ is not an isomorphism ([[PR-IP6ZG]]).
:::
