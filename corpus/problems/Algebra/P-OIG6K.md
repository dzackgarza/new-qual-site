---
schema: qual/card@1
id: P-OIG6K
kind: problem
title: An irreducible cubic with Galois group not in $A_3$ has Galois group $S_3$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Classification
  - Permutations
relations: []
review: draft
---

::: {.problem}
Let $f\in F[x]$ be an irreducible separable cubic. If its Galois group is not contained in $A_3$, prove that its Galois group is $S_3$.
:::

::: {.solution}
Let $L$ be the splitting field of $f$, and regard $G=\Gal(L/F)$ as a subgroup of $S_3$ through its action on the three distinct roots of $f$.

::: pf

::: {.pf-step #contains-a3}

$A_3\le G$.

::: pf-proof

Because $f$ is irreducible, $G$ acts transitively on its three roots, so $3$ divides $\abs{G}$ by the orbit-stabilizer theorem. By Cauchy's theorem $G$ contains an element of order $3$, which generates $A_3$, the unique subgroup of order $3$ in $S_3$.

:::

:::

::: pf-step

$G=S_3$.

::: pf-proof

By step [](#contains-a3){.pf-ref} and Lagrange's theorem, $\abs{G}\in\{3,6\}$, so $G=A_3$ or $G=S_3$. By hypothesis $G\not\subseteq A_3$.

:::

:::

:::

:::
