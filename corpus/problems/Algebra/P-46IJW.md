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

::: pf

::: {.pf-step #aw-rings}
A ring $R$ is semisimple Artinian if and only if
$$
R\cong \prod_{i=1}^r M_{n_i}(D_i),
$$
where each $D_i$ is a division ring and each $n_i\ge1$. The factors are unique up to permutation and isomorphism of the division rings.

::: pf-proof
This is the Artin--Wedderburn theorem.
:::

:::

::: pf-step
The number $r$ is the number of isomorphism classes of simple left $R$-modules $S_1,\ldots,S_r$, and
$$
R\cong \bigoplus_{i=1}^r S_i^{\oplus n_i},\qquad \operatorname{End}_R(S_i)\cong D_i^{\mathrm{op}}.
$$

::: pf-proof
For the factor $M_{n_i}(D_i)$, the unique simple left module up to isomorphism is the column module $S_i=D_i^{n_i}$, and $M_{n_i}(D_i)$ is the direct sum of its $n_i$ columns. A module endomorphism of $D_i^{n_i}$ commutes with all matrices, so it is right multiplication by an element of $D_i$; composition reverses the order of these right multiplications, which gives $D_i^{\mathrm{op}}$.
:::

:::

::: {.pf-step #division-algebra}
If $k$ is algebraically closed, every finite-dimensional division $k$-algebra is $k$.

::: pf-proof
For $a$ in such a division algebra, the subalgebra $k[a]$ is finite-dimensional, so $a$ is algebraic over $k$. The ring $k[a]$ is a subring of a division ring, hence a domain, so the minimal polynomial of $a$ is irreducible; over the algebraically closed field $k$ it is linear, hence $a\in k$.
:::

:::

::: {.pf-step #aw-algebras}
A finite-dimensional semisimple algebra $A$ over an algebraically closed field $k$ satisfies
$$
A\cong \prod_{i=1}^r M_{n_i}(k).
$$

::: pf-proof
By step [](#aw-rings){.pf-ref}, $A\cong\prod_i M_{n_i}(D_i)$, and each $D_i$ is a finite-dimensional division $k$-algebra, so $D_i=k$ by step [](#division-algebra){.pf-ref}.
:::

:::

::: pf-step
For a finite group $G$,
$$
\CC[G]\cong \prod_i M_{d_i}(\CC),
\qquad \cardinality{G}=\sum_i d_i^2.
$$

::: pf-proof
By Maschke's theorem $\CC[G]$ is semisimple, so step [](#aw-algebras){.pf-ref} applies with $k=\CC$. Comparing $\CC$-dimensions gives $\cardinality{G}=\sum_i d_i^2$.
:::

:::

:::

:::
