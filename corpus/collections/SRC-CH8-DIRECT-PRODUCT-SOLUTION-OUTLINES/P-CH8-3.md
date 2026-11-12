---
schema: qual/card@1
id: P-CH8-3
kind: problem
title: $G\cong G\oplus\{e_H\}$
classification:
  areas:
    - algebra
  topics:
    - Direct Products
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Gallian, Contemporary Abstract Algebra, seventh edition (2010),
    Chapter 8, External Direct Products, Exercises, exercise 3, printed page
    167 (PDF page 182 of
    tmp/sources/Gallian-Contemporary-Abstract-Algebra-7e.pdf, which is not
    tracked in the repository). The printed exercise reads: Let G be a group with identity e_G and let H be a group with identity e_H. Prove that G is isomorphic to G x {e_H} and that H is isomorphic to {e_G} x H.. The card states exactly this, so no repair was needed.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The retained outline's map g to (g, e_H), its homomorphism check, its kernel computation and its surjectivity are kept verbatim in substance and written as two symmetric steps; the conclusion records the copy-of-each-factor reading.
---

::: {.problem}
Let $G$ be a group with identity $e_{G}$ and let $H$ be a group with identity $e_{H}$. Prove that $G$ is isomorphic to $G \oplus \{e_{H}\}$ and that $H$ is isomorphic to $\{e_{G}\} \oplus H$.
:::

::: {.solution}

Let $G,H$ be groups with identities $e_G,e_H$, and let $G\oplus\{e_H\}$ and
$\{e_G\}\oplus H$ carry the componentwise operations of the external direct
product.

::: pf

::: {.pf-step #first}

$\phi\colon G\to G\oplus\{e_H\}$, $\phi(g)=(g,e_H)$, is an isomorphism.

::: pf-proof

$\phi(gh)=(gh,e_H)=(gh,e_He_H)=(g,e_H)(h,e_H)=\phi(g)\phi(h)$, so $\phi$ is a
homomorphism, using that $e_H$ is idempotent. Its kernel is
$\{g:(g,e_H)=(e_G,e_H)\}=\{e_G\}$, so $\phi$ is injective. It is surjective
because every element of $G\oplus\{e_H\}$ is $(g,e_H)$ for some $g\in G$ by
the definition of the direct product as the set of pairs. An injective and
surjective homomorphism is an isomorphism.

:::

:::

::: {.pf-step #second}

$\psi\colon H\to\{e_G\}\oplus H$, $\psi(h)=(e_G,h)$, is an isomorphism.

::: pf-proof

The same computation with the roles exchanged:
$\psi(hk)=(e_G,hk)=(e_Ge_G,hk)=(e_G,h)(e_G,k)=\psi(h)\psi(k)$; the kernel is
trivial since $(e_G,h)=(e_G,e_H)$ forces $h=e_H$; and every element of
$\{e_G\}\oplus H$ is $(e_G,h)$. Hence $H\cong\{e_G\}\oplus H$.

:::

:::

::: {.pf-step #conclusion}

$G\cong G\oplus\{e_H\}$ and $H\cong\{e_G\}\oplus H$.

::: pf-proof

Steps [](#first){.pf-ref} and [](#second){.pf-ref} exhibit the two
isomorphisms. Note that $G\oplus\{e_H\}$ is a subgroup of $G\oplus H$
isomorphic to $G$, so the external direct product contains a copy of each
factor; this is the observation used later in the chapter to identify internal
direct products with external ones.

:::

:::

:::


:::

::: {.remark}
Certificate. <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/CH8DirectProduct.lean> proves the three assertions of
this exercise: `prod_bot_eq_ker_snd` identifies $G\times\{e\}$ with the kernel of
the second projection, `prod_bot_normal` and `bot_prod_normal` give normality of
$G\times\{e\}$ and $\{e\}\times H$, `quotient_prod_bot_mulEquiv` and
`quotient_bot_prod_mulEquiv` give the quotient isomorphisms onto $H$ and $G$, and
`prod_bot_mulEquiv` and `bot_prod_mulEquiv` give $G\times\{e\}\cong G$ and
$\{e\}\times H\cong H$. No `sorryAx`.
:::
