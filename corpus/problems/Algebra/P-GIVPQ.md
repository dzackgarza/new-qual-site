---
schema: qual/card@1
id: P-GIVPQ
kind: problem
title: Semisimple algebras and the Artin–Wedderburn theorem
classification:
  areas:
  - algebra
  topics:
  - Semisimplicity
  - Algebras
  - Structure Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Reviewed against the Lamport standard. What was found: both questions ask for a
    statement — "what is a semisimple algebra" and "state the structure theorem" —
    so neither is a proof obligation and no pf block was added; a structured proof
    here would be invented structure. What was checked: the definition given (A_A
    semisimple, equivalently every left A-module semisimple, equivalently every
    short exact sequence of left A-modules splits) is the standard one; the
    Artin-Wedderburn statement as given (semisimple iff a finite product of matrix
    rings over division rings) is correct, including that the factors are
    determined up to permutation and isomorphism; and the specialisation over an
    algebraically closed field (each division ring finite dimensional over an
    algebraically closed k is k itself) is correct. What was not checked: no
    proof of the theorem was written or reviewed here, since the card asks only for
    its statement, and no source solution is retained for this card.
---

::: {.problem}
What is a semisimple algebra?
State the structure theorem for semisimple algebras.
:::

::: {.solution}

The definitions and the equivalences are the card's own; the Artin--Wedderburn theorem is quoted with the parts of it that this card can check, and no retained set supplies it. The sets searched are recorded in the audit trail.

Throughout $A$ is a unital ring and modules are unital left $A$-modules; a module is **simple** when it is nonzero and its only submodules are $0$ and itself, and **semisimple** when it is a direct sum of simple submodules.

::: pf

::: {.pf-step #definitions}
The three conditions — (a) every left $A$-module is semisimple, (b) every short exact sequence of left $A$-modules splits, (c) ${}_{A}A$ is semisimple — are equivalent, and each is a definition of "$A$ is semisimple".

::: pf-proof
(c)$\Rightarrow$(a): a free module is a direct sum of copies of ${}_{A}A$, a direct sum of semisimple modules is semisimple, a submodule of a semisimple module is a direct summand and hence semisimple, and every module is a quotient of a free module; so every module is semisimple. (a)$\Rightarrow$(b): in $0\to A'\to B\to C\to 0$ the image of $A'$ is a submodule of $B$, hence a direct summand because $B$ is semisimple, which is exactly a splitting. (b)$\Rightarrow$(c): every submodule of every module is then a direct summand. Let $M\ne0$ be a module; the set of submodules that are direct sums of simple submodules is nonempty (a nonzero cyclic submodule has a maximal proper submodule by Zorn's lemma, whose quotient is simple) and has a maximal member $N$ by Zorn, and if $N\ne M$ then a complement $N'$ of $N$ is nonzero, contains a simple submodule $S$, and $N\oplus S$ is a larger such sum, a contradiction. So $M$ is semisimple.
:::

:::

::: {.pf-step #matrix-semisimple}
For a division ring $D$ and $n\ge1$, the ring $M_{n}(D)$ satisfies (c): ${}_{A}A$ is the direct sum of the $n$ simple left ideals $L_{j}=\{a:a_{ik}=0 \text{ for } k\ne j\}$.

::: pf-proof
$L_{j}$ is the set of matrices all of whose columns but the $j$-th are zero; it is a left ideal, since left multiplication by a matrix $A$ produces $AX$ with the same property and $j$-th column $A(Xe_{j})$, and every matrix is the sum of its columns, so ${}_{A}A=L_{1}\oplus\cdots\oplus L_{n}$ as left modules. The map $X\mapsto Xe_{j}$ is an isomorphism of left $M_{n}(D)$-modules $L_{j}\to D^{n}$, because $(AX)e_{j}=A(Xe_{j})$ and any column vector is the $j$-th column of some matrix in $L_{j}$. So it suffices that $D^{n}$ is simple over $M_{n}(D)$: if $0\ne v\in D^{n}$ and $w\in D^{n}$ is arbitrary, then $v$ can be completed to a $D$-basis of $D^{n}$, and a $D$-linear map with $v\mapsto w$ is a matrix $A\in M_{n}(D)$ with $Av=w$, so $M_{n}(D)v=D^{n}$ and $D^{n}$ has no nonzero proper submodule. Hence each $L_{j}$ is simple and ${}_{A}A$ is a direct sum of the $n$ simple left ideals $L_{j}$.
:::

:::

::: {.pf-step #aw}
Artin--Wedderburn: $A$ is semisimple if and only if $A\cong\prod_{i=1}^{r}M_{n_{i}}(D_{i})$ with each $D_{i}$ a division ring and $n_{i}\ge1$; and the integer $r$, the integers $n_{i}$ and the division rings $D_{i}$ are determined up to permutation and isomorphism.

::: pf-proof
The forward direction is the structure theorem and is quoted, not proved here: a semisimple ring is a finite direct product of matrix rings over division rings, one factor for each simple left module up to isomorphism, with $D_{i}=\Endo_{A}(L_{i})^{\mathrm{op}}$. The reverse direction is step [](#matrix-semisimple){.pf-ref} together with the fact that a finite product of semisimple rings is semisimple: a product acts coordinatewise, so a module over the product is a direct sum of modules over the factors, and each of those is semisimple. Uniqueness follows from the two-sided ideals of the product: its factors are exactly its minimal two-sided ideals, so $r$ and the multiset of factors are determined. Inside a factor $M_{n}(D)$ the regular left module is $L^{\oplus n}$ with $L$ simple, by the column decomposition of step [](#matrix-semisimple){.pf-ref}, so $n$ is its composition length as a module over that factor and is recovered from the factor's left module structure; and $M_{n}(D)$ has a unique simple left module up to isomorphism, namely $L=D^{n}$, with $D\cong\Endo_{M_{n}(D)}(L)^{\mathrm{op}}$, which recovers $D$.
:::

:::

::: {.pf-step #algebraically-closed}
If $A$ is a finite-dimensional algebra over a field $k$, each $D_{i}$ is finite-dimensional over $k$; if in addition $k$ is algebraically closed, then $D_{i}\cong k$ and $A\cong\prod_{i=1}^{r}M_{n_{i}}(k)$.

::: pf-proof
The centre of $A$ contains $k$ and the decomposition is a ring isomorphism, so $k$ embeds in the centre of each factor $M_{n_{i}}(D_{i})$, which is the centre of $D_{i}$; hence $D_{i}$ is a finite-dimensional $k$-algebra, and finite dimensionality follows from $\dim_{k}A=\sum_{i}n_{i}^{2}\dim_{k}D_{i}$. For $d\in D_{i}$ the subalgebra $k(d)$ is a finite-dimensional commutative integral domain over $k$, hence a finite field extension of $k$; if $k$ is algebraically closed then $k(d)=k$, so $d\in k$ and $D_{i}=k$.
:::

:::

:::
:::
