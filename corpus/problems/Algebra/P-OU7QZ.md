---
schema: qual/card@1
id: P-OU7QZ
kind: problem
title: The Galois group of an irreducible quintic with two non-real roots is $S_5$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Permutations
  - Polynomials
relations: []
review: draft
---

::: {.problem}
Let $f\in \QQ[x]$ be an irreducible quintic with exactly two non-real roots. Prove that its Galois group over $\QQ$ is $S_5$.
:::

::: {.solution}
Let $L$ be the splitting field of $f$, and regard $G=\Gal(L/\QQ)$ as a subgroup of $S_5$ through its action on the five distinct roots of $f$.

::: pf

::: {.pf-step #five-cycle}

$G$ contains a $5$-cycle.

::: pf-proof

Because $f$ is irreducible, $G$ acts transitively on the roots, so $5\mid\abs{G}$. By Cauchy's theorem $G$ contains an element of order $5$, and an element of order $5$ in $S_5$ is a $5$-cycle.

:::

:::

::: {.pf-step #transposition}

$G$ contains a transposition.

::: pf-proof

Complex conjugation restricts to an automorphism of $L$. It fixes the three real roots and swaps the two non-real roots, which are conjugate because $f$ has rational coefficients.

:::

:::

::: pf-step

$G=S_5$.

::: pf-proof

Let $\sigma$ be the $5$-cycle of step [](#five-cycle){.pf-ref} and $\tau=(a\ b)$ the transposition of step [](#transposition){.pf-ref}. Since $\sigma$ generates a transitive cyclic group of prime order, some power $\sigma^k$ is a $5$-cycle with $\sigma^k(a)=b$. Labelling the roots so that $\sigma^k=(1\ 2\ 3\ 4\ 5)$ and $\tau=(1\ 2)$, conjugation by powers of $\sigma^k$ gives $(2\ 3)$, $(3\ 4)$ and $(4\ 5)$ in $G$. The adjacent transpositions $(i\ i{+}1)$ generate $S_5$.

:::

:::

:::

:::
