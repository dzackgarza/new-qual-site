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

::: {.problem}
(a) Which is the connection between Hom and tensor product?

(b) What is this called in representation theory?
:::

::: {.solution}

::: pf

::: pf-step
(a) For a commutative ring $R$ and $R$-modules $M,N,P$ there is an isomorphism, natural in $M$, $N$ and $P$,
$$
\Hom_R(M\otimes_R N,P)\cong\Hom_R\bigl(M,\Hom_R(N,P)\bigr),
$$
so $-\otimes_R N$ is left adjoint to $\Hom_R(N,-)$.

::: pf-proof
The isomorphism sends $F:M\otimes_RN\to P$ to $m\mapsto(n\mapsto F(m\otimes n))$, and its inverse sends $G$ to the map induced by the bilinear map $(m,n)\mapsto G(m)(n)$. For a noncommutative ring the same statement holds with $M$ a right $R$-module, $N$ an $(R,S)$-bimodule and $P$ a right $S$-module.
:::

:::

::: pf-step
(b) In representation theory this is Frobenius reciprocity: for $H\le G$, a $\CC[H]$-module $V$ and a $\CC[G]$-module $W$,
$$
\Hom_G(\operatorname{Ind}_H^GV,W)\cong\Hom_H(V,\operatorname{Res}_H^GW).
$$

::: pf-proof
With $\operatorname{Ind}_H^GV=\CC[G]\otimes_{\CC[H]}V$, this is the adjunction of part (a) for the $(\CC[G],\CC[H])$-bimodule $\CC[G]$:
$$
\Hom_{\CC[G]}\bigl(\CC[G]\otimes_{\CC[H]}V,W\bigr)\cong\Hom_{\CC[H]}\bigl(V,\Hom_{\CC[G]}(\CC[G],W)\bigr),
$$
and $\Hom_{\CC[G]}(\CC[G],W)\cong\operatorname{Res}_H^GW$.
:::

:::

:::

:::
