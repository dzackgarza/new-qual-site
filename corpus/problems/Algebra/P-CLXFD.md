---
schema: qual/card@1
id: P-CLXFD
kind: problem
title: Galois groups of irreducible cubics
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Classification
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
What are the Galois groups of irreducible cubics?
:::

::: {.solution}
Let $F$ be a field of characteristic not $2$, let $f\in F[x]$ be an irreducible separable cubic with roots $r_1,r_2,r_3$ in a splitting field $L$, and let $G=\Gal(L/F)$ act on the roots.
Put $\delta=(r_1-r_2)(r_1-r_3)(r_2-r_3)$ and $\Delta(f)=\delta^2\in F$.

<1>1. $G$ is a transitive subgroup of $S_3$, so $G=A_3\cong\ZZ/3\ZZ$ or $G=S_3$.

::: {.proof}
$G$ acts faithfully on the roots, and transitively since $f$ is irreducible.
A transitive subgroup of $S_3$ has order divisible by $3$ by orbit-stabilizer, so it is $A_3$ or $S_3$.
:::

<1>2. $G\le A_3$ if and only if $\Delta(f)$ is a square in $F$.

::: {.proof}
Each $\sigma\in G$ satisfies $\sigma(\delta)=\operatorname{sgn}(\sigma)\delta$.
Since $f$ is separable, $\delta\neq0$, and since $\operatorname{char}F\neq2$, $-\delta\neq\delta$.
So $\delta$ is fixed by $G$, that is $\delta\in F$, exactly when $G$ consists of even permutations; and $\Delta(f)$ is a square in $F$ exactly when $\delta\in F$.
:::

<1>3. Q.E.D.

::: {.proof}
By steps <1>1 and <1>2, $G\cong\ZZ/3\ZZ$ when $\Delta(f)$ is a square in $F$, and $G\cong S_3$ otherwise.
:::
:::
