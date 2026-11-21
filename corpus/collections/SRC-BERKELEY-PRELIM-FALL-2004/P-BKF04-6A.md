---
schema: qual/card@1
id: P-BKF04-6A
kind: problem
title: A congruence condition on square-free $n$ forcing every group of order $n$ to be abelian
classification:
  areas: [prelim]
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the Sylow normalizer count forcing each Sylow subgroup
    normal, the normal products $Q_{i}$ and their cyclic quotients, and the injection into the product of
    the cyclic groups of prime order. No retained solution set covers this exercise (the collection retains
    the examination, not solutions), so the argument is the card's own; the index computation and the final
    order count were checked for this pass.
---

::: {.problem}
Let $n$ be a square-free positive integer (i.e., $n=1$ or $n$ is prime or $n$ is a product of distinct primes). Assume that for every product of primes $pq_1\cdots q_r$ dividing $n$, with $r>0$, we have $q_1\cdots q_r\not\equiv1\pmod p$. Prove that every group $G$ of order $n$ is abelian.
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own, and the index computation below was checked for this pass. Throughout $n$ is square-free, so $n=p_{1}\cdots p_{k}$ is a product of distinct primes, and the hypothesis says that no product $q_{1}\cdots q_{r}$ with $r>0$ of primes with $pq_{1}\cdots q_{r}\mid n$ is congruent to $1$ modulo $p$.

::: pf

::: {.pf-step #sylow-normal}
For each prime $p\mid n$, a Sylow $p$-subgroup $P$ of $G$ is normal.

::: pf-proof
Let $N=N_{G}(P)$. By Sylow's theorem the number of Sylow $p$-subgroups is $[G:N]$ and satisfies $[G:N]\equiv1\pmod p$. Since $P\subseteq N$, the index $[G:N]$ divides $[G:P]=n/p$, which is a product $q_{1}\cdots q_{r}$ of primes different from $p$ because $n$ is square-free; the hypothesis then forces $r=0$, that is $[G:N]=1$ and $N=G$. So $P$ is normal in $G$.
:::

:::

::: {.pf-step #products}
For each $i$ the product $Q_{i}$ of the Sylow subgroups $P_{j}$ with $j\ne i$ is a normal subgroup of order $n/p_{i}$.

::: pf-proof
By step [](#sylow-normal){.pf-ref} every $P_{j}$ is normal. Normal subgroups whose orders are pairwise coprime commute elementwise — if $x\in P_{j}$ and $y\in P_{l}$ with $j\ne l$ then $xyx^{-1}y^{-1}\in P_{j}\cap P_{l}=\{1\}$ — so the product $Q_{i}$ is a direct product, is normal as a product of normal subgroups, and its order is the product $\prod_{j\ne i}p_{j}=n/p_{i}$.
:::

:::

::: {.pf-step #quotients}
$G/Q_{i}$ is cyclic of order $p_{i}$, so there is a surjective homomorphism $\phi_{i}:G\to\ZZ/p_{i}\ZZ$ for each $i$.

::: pf-proof
By step [](#products){.pf-ref} the quotient $G/Q_{i}$ has order $n/(n/p_{i})=p_{i}$, and a group of prime order is cyclic. Composing the quotient map with an isomorphism onto $\ZZ/p_{i}\ZZ$ gives the surjection $\phi_{i}$.
:::

:::

::: {.pf-step}
$G$ is abelian.

::: pf-proof
Combine the $\phi_{i}$ into $\phi:G\to\prod_{i}\ZZ/p_{i}\ZZ$, $g\mapsto(\phi_{i}(g))_{i}$, a homomorphism because each $\phi_{i}$ is. Let $K=\ker\phi$. Each $\phi_{i}$ is surjective and factors through $G/K$, so the image of $G/K$ under the induced map is all of $\ZZ/p_{i}\ZZ$ and $p_{i}$ divides $\abs{G/K}$; since $\abs{G/K}$ also divides $\abs{G}=n=p_{1}\cdots p_{k}$, it equals $n$ and $K$ is trivial. So $\phi$ is injective, and the two finite groups have the same order $\prod_{i}p_{i}=n$; hence $\phi$ is an isomorphism and $G\cong\prod_{i}\ZZ/p_{i}\ZZ$ is abelian, as claimed.
:::

:::

:::
:::
