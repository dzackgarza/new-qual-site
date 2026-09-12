---
schema: qual/card@1
id: P-ALGS15A
kind: problem
title: Groups of order $p^2 q^2$ with $p>q$ are solvable
classification:
  areas:
  - algebra
  topics:
  - Group Theory
  - Classification
  - Sylow Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
Let $G$ be a group of order $p^2 q^2$, where $p$ and $q$ are primes with $p > q$.

(a) Prove that either $|G| = 36$ or else $G$ has a normal Sylow $p$-subgroup.

(b) Prove that $G$ is solvable.
(Hint: when $|G| = 36$, consider the action of $G$ on the left cosets of a Sylow $3$-subgroup).
:::

::: {.solution}
<1>1. Let $n_p$ be the number of Sylow $p$-subgroups of $G$.
By Sylow's theorems,
\[
n_p\equiv 1\pmod p,
\qquad
n_p\mid q^2.
\]
Thus $n_p\in\{1,q,q^2\}$.
::: {.proof}
The number of Sylow $p$-subgroups divides the $p$-free part $q^2$ of $|G|$ and is congruent to $1$ modulo $p$.
:::

<1>2. The case $n_p=q$ is impossible because $q<p$ and $q\equiv1\pmod p$ cannot hold.
If $n_p=q^2>1$, then
\[
p\mid q^2-1=(q-1)(q+1).
\]
Since $p>q$, we cannot have $p\mid q-1$, so $p\mid q+1$.
Hence $p\le q+1$, and therefore $p=q+1$.
The only consecutive primes are then $q=2$ and $p=3$.
::: {.proof}
Because $p>q$, divisibility $p\mid q+1$ forces $q<p\le q+1$, hence $p=q+1$.
Two consecutive integers larger than $2$ cannot both be prime, so $q=2$ and $p=3$.
:::

<1>3. Therefore either $n_p=1$, in which case the Sylow $p$-subgroup is normal, or $(p,q)=(3,2)$ and
\[
|G|=3^2 2^2=36.
\]
::: {.proof}
This exhausts the possibilities in <1>1 and <1>2.
:::

<1>4. Suppose first that $G$ has a normal Sylow $p$-subgroup $P$.
Then $P$ has order $p^2$ and $G/P$ has order $q^2$, so both are abelian.
Hence $G$ is solvable.
::: {.proof}
Every group of prime-square order is abelian.
Since $1\triangleleft P\triangleleft G$ has abelian factors $P$ and $G/P$, it is a solvable series.
:::

<1>5. It remains to treat $|G|=36$.
Let $P$ be a Sylow $3$-subgroup.
Since $[G:P]=4$, the left action of $G$ on $G/P$ gives a homomorphism
\[
\rho:G\longrightarrow S_4.
\]
Let $K=\ker\rho$.
::: {.proof}
The action on the four left cosets of $P$ is a permutation representation of degree $4$.
:::

<1>6. The kernel $K$ is contained in $P$, so $K$ is a $3$-group and hence solvable.
The quotient $G/K\cong\rho(G)$ is a subgroup of $S_4$, hence is solvable.
Therefore $G$ is solvable.
::: {.proof}
An element in the kernel fixes the coset $P$, so it lies in $P$; thus $K\le P$.
Finite $p$-groups are solvable.
Also $S_4$ is solvable, and every subgroup of a solvable group is solvable.
Finally, an extension of a solvable group by a solvable group is solvable.
:::

<1>7. Thus every group of order $p^2q^2$ with $p>q$ is solvable.
::: {.proof}
Combine <1>4 with the exceptional case handled in <1>5--<1>6.
:::
:::
