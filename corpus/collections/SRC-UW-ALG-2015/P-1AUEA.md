---
schema: qual/card@1
id: P-1AUEA
kind: problem
title: Finitely generated projective modules over a Noetherian local ring are free
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Commutative Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement read from the card in `corpus/collections/SRC-UW-ALG-2015`; it is the standard theorem
    and no correction is claimed. The references used in the solution — Nakayama's lemma and the
    behaviour of projective modules — are Atiyah--Macdonald, *Introduction to Commutative Algebra*,
    Proposition 2.5 and its corollary (Nakayama) together with the projective-module definition of
    Chapter 2; no repository-local source text is involved.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    Proved in the standard way, with Nakayama's lemma proved rather than quoted: lift a $k$-basis of
    $P/\mathfrak mP$ to a surjection $R^r\to P$; split it by projectivity; the split sequence stays
    exact after tensoring with $k=R/\mathfrak m$, which forces $K/\mathfrak mK=0$; $K$ is finitely
    generated because $R$ is Noetherian, so Nakayama gives $K=0$. Every hypothesis is used: finite
    generation for Nakayama on $P/\operatorname{im}\varphi$, projectivity for the splitting,
    Noetherian for the finite generation of $K$. Nothing is left in outline.
---

::: {.problem}
Prove that every finitely generated projective module over a commutative noetherian local ring is free.
:::

::: {.solution}

Let $(R,\mathfrak m)$ be a commutative Noetherian local ring, $k=R/\mathfrak m$ its residue field, and $P$ a finitely generated projective $R$-module.

::: pf

::: {.pf-step #s1}

Nakayama's lemma: if $M$ is a finitely generated $R$-module with $M=\mathfrak mM$, then $M=0$.

::: pf-proof

Let $m_1,\dots,m_n$ generate $M$. Since $M=\mathfrak mM$, there are $a_{ij}\in\mathfrak m$ with $m_i=\sum_ja_{ij}m_j$, so the column vector $m=(m_i)$ satisfies $(I-A)m=0$ for $A=(a_{ij})$. Every entry of $A$ lies in $\mathfrak m$, so $\det(I-A)\equiv\det I=1 \pmod{\mathfrak m}$; as $\mathfrak m$ is the unique maximal ideal (the ring is local), $\det(I-A)\notin\mathfrak m$ is a unit. Multiplying $(I-A)m=0$ by the adjugate matrix gives $\det(I-A)\,m=0$, hence $m_i=0$ for every $i$.

:::

:::

::: {.pf-step #s2}

There is $r\ge0$ and a surjection $\varphi:R^r\to P$.

::: pf-proof

$P/\mathfrak mP$ is a finite-dimensional $k$-vector space, being a quotient of the finite-dimensional space $P/\mathfrak mP$ with $P$ finitely generated. Let $\bar v_1,\dots,\bar v_r$ be a $k$-basis and choose lifts $v_i\in P$; define $\varphi:R^r\to P$ by $e_i\mapsto v_i$.

Tensoring with $k$ gives $\bar\varphi:k^r\to P/\mathfrak mP$, which is an isomorphism, hence surjective. Therefore $P=\operatorname{im}\varphi+\mathfrak m P$. The module $P/\operatorname{im}\varphi$ is finitely generated and satisfies $P/\operatorname{im}\varphi=\mathfrak m\,(P/\operatorname{im}\varphi)$, so it vanishes by step [](#s1){.pf-ref}; that is, $\varphi$ is surjective.

:::

:::

::: {.pf-step #s3}

$\varphi$ splits, so $R^r\cong P\oplus K$ with $K=\ker\varphi$, and $K/\mathfrak mK=0$.

::: pf-proof

Since $P$ is projective and $\varphi$ is surjective, there is $s:P\to R^r$ with $\varphi\circ s=\mathrm{id}_P$; hence $R^r=\ker\varphi\oplus\operatorname{im}s$ and $\operatorname{im}s\cong P$, so $R^r\cong K\oplus P$ with $K=\ker\varphi$.

The sequence $0\to K\to R^r\to P\to 0$ is split exact, and additive functors preserve split exactness, so tensoring with $k$ gives the exact sequence
$$
0\longrightarrow K/\mathfrak mK\longrightarrow k^r\longrightarrow P/\mathfrak mP\longrightarrow0 .
$$
Comparing dimensions over $k$ and using $\dim_kP/\mathfrak mP=r$ from step [](#s2){.pf-ref}, we get $\dim_kK/\mathfrak mK=r-r=0$, so $K=\mathfrak mK$.

:::

:::

::: {.pf-step #s4}

$K=0$, hence $P\cong R^r$ is free.

::: pf-proof

Because $R$ is Noetherian and $K$ is a submodule of the finitely generated module $R^r$, $K$ is finitely generated. Combined with $K=\mathfrak mK$ from step [](#s3){.pf-ref}, Nakayama's lemma (step [](#s1){.pf-ref}) gives $K=0$. Then $R^r\cong P\oplus0\cong P$, so $P$ is free of rank $r$.

:::

:::

:::

:::
