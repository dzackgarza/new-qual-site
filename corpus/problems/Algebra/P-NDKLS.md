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
What are the irreducible representations of finite abelian groups over $\CC$?
Prove that every irreducible representation is 1-dimensional, and describe the dual group $\widehat{G} \cong G$.
:::

::: {.solution}
Let $G$ be a finite abelian group and $\widehat G=\Hom(G,\CC^\times)$, a group under pointwise multiplication.

::: pf

::: {.pf-step #dim}
Every irreducible complex representation $(\rho,V)$ of $G$ is one-dimensional.

::: pf-proof
For each $g\in G$, $\rho(g)$ commutes with every $\rho(h)$ because $G$ is abelian, so $\rho(g)$ is a $G$-endomorphism of $V$, and Schur's lemma makes it a scalar.
Then every line in $V$ is $G$-stable, and irreducibility forces $\dim_{\CC}V=1$.
:::

:::

::: pf-step
The irreducible representations of $G$ are, up to isomorphism, exactly the elements of $\widehat G$, and their values are roots of unity.

::: pf-proof
By step [](#dim){.pf-ref}, an irreducible representation is a homomorphism $G\to\GL_1(\CC)=\CC^\times$, and isomorphic one-dimensional representations are equal homomorphisms.
If $g^n=e$, then $\chi(g)^n=1$.
:::

:::

::: pf-step
$\widehat G\cong G$.

::: pf-proof
For a cyclic group $C_n=\langle g\rangle$, a character is determined by $\chi(g)$, which may be any $n$-th root of unity, so $\widehat{C_n}\cong\mu_n\cong C_n$.
A character of a product is the product of its restrictions to the factors, so $\widehat{A\times B}\cong\widehat A\times\widehat B$.
Writing $G\cong C_{n_1}\times\cdots\times C_{n_r}$ gives $\widehat G\cong\widehat{C_{n_1}}\times\cdots\times\widehat{C_{n_r}}\cong G$.
:::

:::

:::

:::

::: {.remark}
The isomorphism $\widehat G\cong G$ depends on the choice of a decomposition and of generators; the evaluation map $G\to\widehat{\widehat G}$ is a canonical isomorphism.
:::
