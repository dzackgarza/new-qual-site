---
schema: qual/card@1
id: P-46IJW
kind: problem
title: Artin–Wedderburn theorem
classification:
  areas:
  - algebra
  topics:
  - Semisimplicity
  - Rings
  - Structure Theorem
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
State and explain the Artin–Wedderburn Structure Theorem for semisimple Artinian rings and finite-dimensional semisimple algebras.
:::

::: {.solution}
The Artin--Wedderburn theorem says that a ring $R$ is semisimple Artinian if and only if
\[
R\cong \prod_{i=1}^r M_{n_i}(D_i),
\]
where each $D_i$ is a division ring and each $n_i\ge1$. The factors are unique up to permutation and isomorphism of the division rings.

For the factor $M_{n_i}(D_i)$, the unique simple left module up to isomorphism is the column module $D_i^{n_i}$. Thus the number $r$ is the number of isomorphism classes of simple left $R$-modules, and as a left module
\[
R\cong \bigoplus_{i=1}^r S_i^{\oplus n_i}.
\]
Moreover
\[
\operatorname{End}_R(S_i)\cong D_i^{\mathrm{op}}.
\]

If $A$ is a finite-dimensional semisimple algebra over an algebraically closed field $k$, then every finite-dimensional division $k$-algebra is $k$: for $a$ in such a division algebra, the subalgebra $k[a]$ is finite-dimensional, so $a$ is algebraic over $k$; its minimal polynomial over the algebraically closed field $k$ is linear, hence $a\in k$. Therefore
\[
A\cong \prod_{i=1}^r M_{n_i}(k).
\]
For example, Maschke's theorem gives, for a finite group $G$ over $\mathbb C$,
\[
\mathbb C[G]\cong \prod_i M_{d_i}(\mathbb C),
\qquad |G|=\sum_i d_i^2.
\]
:::
