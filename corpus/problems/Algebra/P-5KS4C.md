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

::: problem
Let $K$ be a field of characteristic $0$, let $f\in K[x]$ be irreducible of degree $n\ge5$, and let $F$ be the splitting field of $f$ over $K$. Assume
\[
\Gal(F/K)\cong S_n.
\]
Let $u\in F$ be a root of $f$.

Show that there is no radical extension field $E/K$ such that
\[
K\subset K(u)\subset E.
\]
:::

::: {.solution}
Because $f$ is irreducible and $u$ is a root, the minimal polynomial of $u$ over $K$ is $f$. Hence the normal closure of the simple extension
\[
K(u)/K
\]
is exactly the splitting field $F$ of $f$.

A standard solvability-by-radicals theorem says that a finite separable extension $M/K$ in characteristic $0$ is contained in a radical extension of $K$ only if the Galois group of the normal closure of $M/K$ is solvable.

Apply this with
\[
M=K(u).
\]
If there were a radical extension $E/K$ with
\[
K\subset K(u)\subset E,
\]
then the Galois group of the normal closure of $K(u)/K$ would be solvable. But that normal closure is $F$, so this would force
\[
\Gal(F/K)\cong S_n
\]
to be solvable.

For $n\ge5$, the symmetric group $S_n$ is not solvable: its normal subgroup $A_n$ is nonabelian simple, so the derived series cannot terminate at the identity.
This contradiction proves that no such radical extension $E$ exists.
:::
