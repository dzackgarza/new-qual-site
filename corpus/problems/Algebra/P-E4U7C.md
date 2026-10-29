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
- event: solution-written
  by: Claude Opus 5.5
  date: 2026-10-29
  note: Converted the prose solution to a STYLE-08 structured proof.
---

::: {.problem}
Describe the Galois theory of cyclotomic extensions $\QQ(\zeta_n)/\QQ$ (irreducibility of cyclotomic polynomials, Galois group isomorphism, and subfield structure).
:::

::: {.solution}
Let $\zeta_n$ be a primitive $n$th root of unity, and let $\Phi_n(x)=\prod_{(a,n)=1}(x-\zeta_n^a)$ be the $n$th cyclotomic polynomial.

::: pf

::: {.pf-step #degree}
$\Phi_n$ is a monic polynomial in $\ZZ[x]$ of degree $\varphi(n)$, irreducible over $\QQ$, and $[\QQ(\zeta_n):\QQ]=\varphi(n)$.

::: pf-proof
These are the standard properties of cyclotomic polynomials, and $\zeta_n$ is a root of $\Phi_n$.
:::

:::

::: {.pf-step #gal}
$\Gal(\QQ(\zeta_n)/\QQ)\cong(\ZZ/n\ZZ)^\times$ via $\sigma\mapsto a$ when $\sigma(\zeta_n)=\zeta_n^a$; in particular the extension is abelian.

::: pf-proof
$\QQ(\zeta_n)$ is the splitting field of $\Phi_n$, so it is Galois over $\QQ$.
An automorphism is determined by the image of $\zeta_n$, which is another primitive $n$th root of unity $\zeta_n^a$ with $(a,n)=1$, so the map is an injective homomorphism.
Both groups have order $\varphi(n)$ by step [](#degree){.pf-ref}, so it is an isomorphism.
:::

:::

::: pf-step
The intermediate fields of $\QQ(\zeta_n)/\QQ$ are in inclusion-reversing bijection with the subgroups of $(\ZZ/n\ZZ)^\times$.

::: pf-proof
This is the Galois correspondence combined with step [](#gal){.pf-ref}.
:::

:::

::: pf-step
For $n>2$, the fixed field of complex conjugation is the maximal real subfield $\QQ(\zeta_n)^+=\QQ(\zeta_n+\zeta_n^{-1})$, and $[\QQ(\zeta_n):\QQ(\zeta_n)^+]=2$; for $n=1,2$, $\QQ(\zeta_n)=\QQ$ and this index is $1$.

::: pf-proof
Complex conjugation sends $\zeta_n$ to $\zeta_n^{-1}$, so it corresponds to $-1\in(\ZZ/n\ZZ)^\times$, which has order $2$ when $n>2$.
Its fixed field has index $2$ and contains $\zeta_n+\zeta_n^{-1}$.
Since $\zeta_n$ is a root of $x^2-(\zeta_n+\zeta_n^{-1})x+1$, $[\QQ(\zeta_n):\QQ(\zeta_n+\zeta_n^{-1})]\le2$, so the fixed field equals $\QQ(\zeta_n+\zeta_n^{-1})$.
:::

:::

::: pf-step
For an odd prime $p$, $\QQ(\zeta_p)$ has a unique quadratic subfield, $\QQ\!\left(\sqrt{(-1)^{(p-1)/2}p}\right)$.

::: pf-proof
$(\ZZ/p\ZZ)^\times$ is cyclic, so it has a unique subgroup of index $2$, and the Galois correspondence gives a unique quadratic subfield.
The quadratic Gauss sum $g=\sum_{a=1}^{p-1}\left(\frac ap\right)\zeta_p^a$ lies in $\QQ(\zeta_p)$ and satisfies $g^2=(-1)^{(p-1)/2}p$.
:::

:::

::: pf-step
Every finite abelian extension of $\QQ$ is contained in some cyclotomic field.

::: pf-proof
This is the Kronecker--Weber theorem.
:::

:::

:::

:::
