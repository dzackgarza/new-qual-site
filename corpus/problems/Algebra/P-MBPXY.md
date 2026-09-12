---
schema: qual/card@1
id: P-MBPXY
kind: problem
title: Hom–tensor adjunction
classification:
  areas:
  - algebra
  topics:
  - Tensor Products
  - Representation Theory
  - Modules
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Which is the connection between Hom and tensor product?
What is this called in representation theory?
:::

::: solution
For a commutative ring $R$ and $R$-modules $M,N,P$, there is a natural Hom--tensor adjunction
\[
\operatorname{Hom}_R(M\otimes_R N,P)
\cong
\operatorname{Hom}_R\!\left(M,\operatorname{Hom}_R(N,P)\right).
\]
The isomorphism sends $F:M\otimes_RN\to P$ to the map
\[
m\longmapsto(n\mapsto F(m\otimes n)).
\]
For noncommutative rings the same statement requires the usual left/right module and bimodule hypotheses.

In representation theory, the corresponding induction--restriction adjunction is **Frobenius reciprocity**. For $H\le G$,
\[
\operatorname{Hom}_{\mathbb C[G]}
\bigl(\mathbb C[G]\otimes_{\mathbb C[H]}V,W\bigr)
\cong
\operatorname{Hom}_{\mathbb C[H]}
\bigl(V,\operatorname{Res}_H^GW\bigr).
\]
Since
\[
\operatorname{Ind}_H^GV
=\mathbb C[G]\otimes_{\mathbb C[H]}V,
\]
this is usually written
\[
\operatorname{Hom}_G(\operatorname{Ind}_H^GV,W)
\cong
\operatorname{Hom}_H(V,\operatorname{Res}_H^GW).
\]
:::
