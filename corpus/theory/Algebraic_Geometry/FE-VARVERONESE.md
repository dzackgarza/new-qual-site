---
schema: qual/card@1
id: FE-VARVERONESE
kind: example
title: The Veronese embedding
classification:
  areas:
  - algebraic-geometry
  topics:
  - Veronese Embedding
  - Projective Varieties
  - Very Ample Sheaves
relations:
- kind: uses
  target: PR-VA4S3
- kind: related-to
  target: T-DIVMAPPN
review: draft
prompts:
- What is the $d$-uple (Veronese) embedding?
- Why is the Veronese embedding a closed immersion?
- What is the homogeneous coordinate ring of the Veronese image?
---

::: {.example title="The $d$-uple embedding"}
Let $n,d\ge1$ and let $M_0,\ldots,M_N$ be the monomials of degree $d$ in $x_0,\ldots,x_n$, so that $N=\binom{n+d}{n}-1$.
The map
$$
v_d\colon\PP^n\longrightarrow\PP^N,\qquad
\thevector{x_0:\cdots:x_n}\longmapsto\thevector{M_0(x):\cdots:M_N(x)}
$$
is a morphism, and it is an isomorphism onto its image [@Har77, Exercise I.2.12 and Exercise I.3.4].
The image is the vanishing locus of the quadratic relations among the monomials of degree $d$, and its homogeneous coordinate ring is the Veronese subring $k[x_0,\ldots,x_n]^{(d)}$ [@Har77, Exercise I.2.12].
For $d=2$ and $n=2$ the image is the Veronese surface in $\PP^5$ [@Har77, Exercise I.2.13].
:::
