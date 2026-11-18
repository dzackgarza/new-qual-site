---
schema: qual/card@1
id: P-APAS19J
kind: problem
title: Multiplicity-free isotypic decomposition iff $\mathrm{End}_A V$ is commutative
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card, which is
    correct as it stood. Added: the proof of the two Schur-lemma statements from the
    simplicity of the S_i together with the finiteness and algebraic closure of C, which the
    prose had quoted; and the verification that every A-endomorphism is block diagonal, block
    by block, in both directions (any block-diagonal family is A-linear), so that the
    identification of End_A(V) with the product of matrix algebras is an isomorphism of
    algebras and not only of vector spaces. Not claimed: a retained solution set; the
    provenance names the examination paper only. Statement unchanged.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card, which is
    correct as it stood. Added: the proof of the two Schur-lemma statements from the
    simplicity of the S_i together with the finiteness and algebraic closure of C, which the
    prose had quoted; and the verification that every A-endomorphism is block diagonal, block
    by block, in both directions (any block-diagonal family is A-linear), so that the
    identification of End_A(V) with the product of matrix algebras is an isomorphism of
    algebras and not only of vector spaces. Not claimed: a retained solution set; the
    provenance names the examination paper only. Statement unchanged.
---

::: {.problem}
Let $A$ be a finite-dimensional algebra over $\CC$ and let $(V,\rho)$ be a finite-dimensional representation of $A$.
Show that the isotypic decomposition of $(V,\rho)$ is multiplicity free if and only if $\mathrm{End}_A V$ is commutative.
:::

::: {.solution}
No retained solution set covers this problem: the collection's `provenance` names `assets/attachments/Applied-Algebra-Qual-Spring-2019.pdf`, the examination paper itself, which carries no solutions. The argument below is the card's own and follows the card's previous prose.

Throughout $A$ is a finite-dimensional algebra over $\CC$, $(V,\rho)$ a finite-dimensional $A$-module, and
$$
V\cong\bigoplus_{i=1}^{r}S_i^{\oplus m_i},\qquad m_i\ge1,
$$
its isotypic decomposition, with $S_1,\dots,S_r$ pairwise nonisomorphic simple $A$-modules.

::: pf

::: {.pf-step #schur}
$\operatorname{Hom}_A(S_i,S_j)=0$ for $i\ne j$, and $\operatorname{End}_A(S_i)=\CC\cdot\mathrm{id}$.

::: pf-proof
An $A$-linear map $S_i\to S_j$ with $i\ne j$ has kernel and image that are $A$-submodules; if the map is nonzero then its kernel is $0$ (by simplicity of $S_i$) and its image is $S_j$ (by simplicity of $S_j$), making it an isomorphism, contrary to the choice of the $S_i$. A nonzero endomorphism of $S_i$ likewise has kernel $0$ and image $S_i$, hence is invertible, so $\operatorname{End}_A(S_i)$ is a division algebra finite dimensional over $\CC$ and contains $\CC$ in its centre; a finite-dimensional division algebra over an algebraically closed field is the field, so $\operatorname{End}_A(S_i)=\CC$.

:::

:::

::: {.pf-step #end-algebra}
$\operatorname{End}_A(V)\cong\prod_{i=1}^rM_{m_i}(\CC)$ as $\CC$-algebras.

::: pf-proof
Write $V=\bigoplus_iV_i$ with $V_i=S_i^{\oplus m_i}$. An $A$-linear $f:V\to V$ decomposes into components $f_{ji}:V_i\to V_j$, and by step [](#schur){.pf-ref} $f_{ji}=0$ unless $i=j$, while $f_{ii}$ is an $m_i\times m_i$ matrix with entries in $\End_A(S_i)=\CC$. So $f$ is block diagonal with blocks in $M_{m_i}(\CC)$, and conversely any such block-diagonal family is $A$-linear; composition is matrix multiplication block by block. So the endomorphism algebra is the product of the matrix algebras.

:::

:::

::: {.pf-step #forward}
If all $m_i=1$, then $\operatorname{End}_A(V)\cong\CC^r$ is commutative, so the decomposition is multiplicity free.

::: pf-proof
With $m_i=1$ each factor $M_{m_i}(\CC)$ is $\CC$, and a product of copies of $\CC$ is commutative.

:::

:::

::: {.pf-step #converse}
If some $m_i\ge2$, then $\operatorname{End}_A(V)$ is not commutative, so the decomposition is not multiplicity free.

::: pf-proof
In $M_{m_i}(\CC)$ with $m_i\ge2$ the matrix units $E_{12}$ and $E_{21}$ satisfy $E_{12}E_{21}=E_{11}\ne E_{22}=E_{21}E_{12}$. Embedding $M_{m_i}(\CC)$ as the $i$-th factor of the product of step [](#end-algebra){.pf-ref} exhibits two noncommuting elements of $\operatorname{End}_A(V)$, which is therefore not commutative.

:::

:::

::: {.pf-step #conclusion}
The isotypic decomposition of $V$ is multiplicity free iff $\operatorname{End}_A(V)$ is commutative.

::: pf-proof
If the decomposition is multiplicity free then every $m_i=1$, and step [](#forward){.pf-ref} gives commutativity. If it is not, some $m_i\ge2$ and step [](#converse){.pf-ref} gives noncommutativity. So commutativity of $\operatorname{End}_A(V)$ is equivalent to every $m_i$ being $1$.

:::

:::

:::
:::
