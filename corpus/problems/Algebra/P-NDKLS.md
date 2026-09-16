---
schema: qual/card@1
id: P-NDKLS
kind: problem
title: Irreducible representations of finite abelian groups
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Abelian Groups
  - Character Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
What are the irreducible representations of finite abelian groups over $\mathbb{C}$?
Prove that every irreducible representation is 1-dimensional, and describe the dual group $\widehat{G} \cong G$.
:::

::: {.solution}
Let $(\rho,V)$ be an irreducible complex representation of a finite abelian group $G$. For every $g\in G$, the operator $\rho(g)$ commutes with every $\rho(h)$. By Schur's lemma, each $\rho(g)$ is scalar. Hence every one-dimensional subspace of $V$ is $G$-stable, so irreducibility forces $\dim_{\mathbb C}V=1$.

Thus the irreducible representations are exactly the characters
\[
\widehat G=\operatorname{Hom}(G,\mathbb C^\times),
\]
with pointwise multiplication. Because $G$ is finite, all character values are roots of unity.

For $C_n=\langle g\rangle$, a character is determined by the choice of $\chi(g)$ among the $n$th roots of unity, so $\widehat{C_n}\cong C_n$. If
\[
G\cong C_{n_1}\times\cdots\times C_{n_r},
\]
then
\[
\widehat G\cong \widehat{C_{n_1}}\times\cdots\times\widehat{C_{n_r}}\cong G.
\]
This isomorphism with $G$ is noncanonical; the evaluation map $G\to\widehat{\widehat G}$ is canonical.
:::
