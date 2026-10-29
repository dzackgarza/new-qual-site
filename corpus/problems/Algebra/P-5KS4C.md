---
schema: qual/card@1
id: P-5KS4C
kind: problem
title: A root field with normal closure of Galois group $S_n$ is not contained in a radical extension
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Galois Theory
  - Permutations
relations: []
review: draft
---

::: {.problem}
Let $K$ be a field of characteristic $0$, let $f\in K[x]$ be irreducible of degree $n\ge5$, and let $F$ be the splitting field of $f$ over $K$. Assume
$$
\Gal(F/K)\cong S_n.
$$
Let $u\in F$ be a root of $f$.

Show that there is no radical extension field $E/K$ such that
$$
K\subset K(u)\subset E.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #normal-closure}
The normal closure of $K(u)/K$ is $F$.

::: pf-proof
Because $f$ is irreducible and $f(u)=0$, the minimal polynomial of $u$ over $K$ is a scalar multiple of $f$. The normal closure of $K(u)/K$ is the splitting field of that minimal polynomial, which is $F$.
:::

:::

::: {.pf-step #sn-not-solvable}
$S_n$ is not solvable for $n\ge5$.

::: pf-proof
Its normal subgroup $A_n$ is nonabelian simple, so the derived series of $S_n$ stops at $A_n$ and never reaches the identity.
:::

:::

::: pf-step
No radical extension $E/K$ satisfies $K\subset K(u)\subset E$.

::: pf-proof
By Galois's theorem on solvability by radicals, a finite extension $M/K$ in characteristic $0$ lies in a radical extension of $K$ only if the Galois group of the normal closure of $M/K$ is solvable. For $M=K(u)$, step [](#normal-closure){.pf-ref} identifies that group with $\Gal(F/K)\cong S_n$, which is not solvable by step [](#sn-not-solvable){.pf-ref}.
:::

:::

:::

:::
