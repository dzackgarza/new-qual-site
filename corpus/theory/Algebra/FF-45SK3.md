---
schema: qual/card@1
id: FF-45SK3
kind: fact
title: Nakayama's lemma for a local ring
prompts:
- What is Nakayama's lemma for a local ring?
classification:
  areas:
  - algebra
  topics:
  - Nakayama's Lemma
  - Local Rings
  - Modules
relations: []
review: draft
---

::: {.fact}
Let $(R,\mfm)$ be a [[D-TGB4R|local ring]] with residue field $k=R/\mfm$, and let $M$ be a finitely generated $R$-module.
Elements $m_1,\ldots,m_n\in M$ generate $M$ if and only if their images span the $k$-vector space $M/\mfm M$.
Consequently, a generating set of $M$ is minimal under inclusion if and only if its image is a $k$-basis of $M/\mfm M$, and every minimal generating set of $M$ has $\dim_k M/\mfm M$ elements.

If $(m_1,\ldots,m_n)$ and $(m_1',\ldots,m_n')$ are minimal generating sets of $M$, then there is $P\in\GL_n(R)$ with $m_i'=\sum_jP_{ij}m_j$ for every $i$.
:::

::: {.proof}
If the images of $m_1,\ldots,m_n$ span $M/\mfm M$, let $N=Rm_1+\cdots+Rm_n$.
Then $M=N+\mfm M$, so $\mfm(M/N)=M/N$, and $M/N=0$ by [[FF-NREXC|Nakayama's lemma]], since $M/N$ is finitely generated and $\mfm=J(R)$.
The converse is immediate.

If the image of a generating set is linearly dependent, some element has image in the span of the images of the others, and those others still generate $M$ by the first part; if the image is a basis, no proper subset has spanning image.

For the last claim, write $m_i'=\sum_jP_{ij}m_j$ and $m_j=\sum_lQ_{jl}m_l'$ with $P,Q\in\Mat_n(R)$.
Reducing modulo $\mfm$, the matrices $\overline P$ and $\overline Q$ are the change-of-basis matrices between two bases of $M/\mfm M$, so $\overline P\,\overline Q=I$.
Hence $\det P\notin\mfm$, so $\det P$ is a unit of $R$ and $P\in\GL_n(R)$.
:::
