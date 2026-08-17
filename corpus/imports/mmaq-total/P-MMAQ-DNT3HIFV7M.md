---
schema: qual/card@1
id: P-MMAQ-DNT3HIFV7M
kind: problem
title: A projective resolution of $k\simeq R/(x,y)$ over $R=k[x,y]$ and $\mathrm{Tor}_i^R((x,y),k)$
classification:
  areas:
  - algebra
  topics:
  - modules
  - homological-algebra
relations: []
review: draft
solved: false
---

::: problem
Let $R = k[x,y]$ where $k$ is a field, and let $I=(x,y)R$.

- Show that `\begin{align*} 0 \to R \mapsvia{\phi} R \oplus R \mapsvia{\psi} R \to k \to 0 \end{align*}`{=tex} where $\phi(a) = (-ya,xa)$, $\psi((a,b)) = xa+yb$ for $a,b \in R$, is a projective resolution of the $R$-module $k \simeq R/I$.

- Show that $I$ is not a flat $R$-module by computing $\Tor_i^R(I,k)$
:::
