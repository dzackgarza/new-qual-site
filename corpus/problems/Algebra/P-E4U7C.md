---
schema: qual/card@1
id: P-E4U7C
kind: problem
title: Galois theory of cyclotomic extensions
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Roots of Unity
  - Field Extensions
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
Describe the Galois theory of cyclotomic extensions $\mathbb{Q}(\zeta_n)/\mathbb{Q}$ (irreducibility of cyclotomic polynomials, Galois group isomorphism, and subfield structure).
:::

::: {.solution}
Let $\zeta_n$ be a primitive $n$th root of unity. The cyclotomic polynomial is
\[
\Phi_n(x)=\prod_{(a,n)=1}(x-\zeta_n^a).
\]
It lies in $\mathbb Z[x]$, is monic, has degree $\varphi(n)$, and is irreducible over $\mathbb Q$. Hence
\[
[\mathbb Q(\zeta_n):\mathbb Q]=\varphi(n).
\]

The field $\mathbb Q(\zeta_n)$ is the splitting field of $\Phi_n$, so it is Galois over $\mathbb Q$. Every automorphism is determined by the image of $\zeta_n$, and that image must be another primitive $n$th root. Thus
\[
\operatorname{Gal}(\mathbb Q(\zeta_n)/\mathbb Q)
\longrightarrow (\mathbb Z/n\mathbb Z)^\times,
\qquad
\sigma\longmapsto a
\quad\text{when }\sigma(\zeta_n)=\zeta_n^a,
\]
is an injective homomorphism. Both groups have order $\varphi(n)$, so it is an isomorphism:
\[
\operatorname{Gal}(\mathbb Q(\zeta_n)/\mathbb Q)
\cong(\mathbb Z/n\mathbb Z)^\times.
\]
In particular the extension is abelian.

By Galois correspondence, intermediate fields are in inclusion-reversing bijection with subgroups of $(\mathbb Z/n\mathbb Z)^\times$.

For $n>2$, complex conjugation corresponds to $-1\in(\mathbb Z/n\mathbb Z)^\times$ and has order $2$. Its fixed field is the maximal real subfield
\[
\mathbb Q(\zeta_n)^+
=\mathbb Q(\zeta_n+\zeta_n^{-1}),
\]
with
\[
[\mathbb Q(\zeta_n):\mathbb Q(\zeta_n)^+]=2.
\]
For $n=1,2$, the cyclotomic field is already $\mathbb Q$, so this index is $1$.

For an odd prime $p$, $(\mathbb Z/p\mathbb Z)^\times$ is cyclic, hence has a unique subgroup of index $2$; correspondingly $\mathbb Q(\zeta_p)$ has a unique quadratic subfield,
\[
\mathbb Q\!\left(\sqrt{(-1)^{(p-1)/2}p}\right).
\]
Finally, the Kronecker--Weber theorem states that every finite abelian extension of $\mathbb Q$ is contained in some cyclotomic field.
:::
