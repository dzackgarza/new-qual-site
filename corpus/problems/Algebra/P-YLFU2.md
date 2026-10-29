---
schema: qual/card@1
id: P-YLFU2
kind: problem
title: 'Structure theorem for finitely generated modules over a PID: invariant factors
  and elementary divisors'
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Modules
  - Principal Ideal Domains
relations: []
review: draft
---

::: {.problem}
State and prove the structure theorem for finitely generated modules over a PID, in both invariant-factor and elementary-divisor form.
:::

::: {.solution}
Let $R$ be a PID with fraction field $K$, and let $M$ be a finitely generated $R$-module.

::: pf

::: {.pf-step #invariant}
(Invariant factors) $M\cong R^r\oplus\bigoplus_{i=1}^s R/(d_i)$ with $d_1\mid d_2\mid\cdots\mid d_s$, each $d_i$ nonzero and not a unit.

::: pf-proof
Choose a surjection $R^n\to M$ with kernel $N$.
Over a PID a submodule of $R^n$ is free of rank at most $n$, so $N$ is free; let $A$ be the matrix of $N\hookrightarrow R^n$ in chosen bases.
By the Smith normal form over a PID there are invertible $U,V$ with $UAV=\diag(d_1,\ldots,d_t,0,\ldots,0)$ and $d_1\mid\cdots\mid d_t$.
In the new bases $M\cong R^n/\operatorname{im}A\cong R^{n-t}\oplus\bigoplus_{i\le t}R/(d_i)$; dropping the zero summands with $d_i$ a unit gives the claim.
:::

:::

::: {.pf-step #elementary}
(Elementary divisors) $M\cong R^r\oplus\bigoplus_j R/(p_j^{e_j})$ with $p_j$ prime elements, not necessarily distinct, and $e_j\ge1$.
Conversely, elementary divisors determine invariant factors.

::: pf-proof
For $d=u\prod_kp_k^{e_k}$ with distinct primes $p_k$, the ideals $(p_k^{e_k})$ are pairwise comaximal, so the Chinese remainder theorem gives $R/(d)\cong\bigoplus_kR/(p_k^{e_k})$; apply this to each summand in step [](#invariant){.pf-ref}.
Conversely, list the powers of each prime in nondecreasing order, aligned on the right and padded with $1$; the product of the $j$-th column from the right is the $j$-th largest invariant factor, and these satisfy the divisibility chain.
:::

:::

::: pf-step
$r$ and the elementary divisors, hence by step [](#elementary){.pf-ref} the invariant factors up to units, are determined by $M$.

::: pf-proof
$r=\dim_K(M\otimes_RK)$, because the torsion summands vanish after tensoring with $K$.
The torsion submodule $T$ of $M$ is the sum of the cyclic torsion summands, and for a prime $p$ its $p$-primary part $T_p$ is the sum of the summands $R/(p^e)$.
For $k\ge0$, $p^kT_p/p^{k+1}T_p$ is a vector space over $R/(p)$ whose dimension is the number of summands $R/(p^e)$ with $e>k$.
These numbers, for all $k$, determine how many summands $R/(p^e)$ occur for each $e$.
:::

:::

:::

:::
