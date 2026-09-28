---
title: Show $G$ is not simple
order: 0
topics:
- Simple Groups
- Sylow Theory
---

# Show $G$ is not simple

Throughout, $G$ is a finite group of order $n$, $p$ is a prime, $n = p^k m$ with $p\notdivides m$, and $n_p$ is the number of Sylow $p$-subgroups of $G$.

## Constraints from the order

By Sylow's third theorem,
$$
n_p \equiv 1 \pmod p, \qquad n_p \divides m.
$$
If $n_p = 1$, the unique Sylow $p$-subgroup $P$ is normal: for $g\in G$, $gPg\inv$ is again a Sylow $p$-subgroup, so $gPg\inv = P$.

Groups of prime-power order:

- If $n$ is prime, $G$ is cyclic and simple.

- If $n = p^k$ with $k\geq 2$, then $Z(G) \neq 1$ by the class equation.
  If $Z(G)\neq G$, then $Z(G)$ is a proper nontrivial normal subgroup; if $Z(G)=G$, then $G$ is abelian and every subgroup of order $p$ is proper, nontrivial, and normal.

## A Sylow count with $n_p = 1$

If the only divisor of $m$ congruent to $1$ modulo $p$ is $1$, then $n_p=1$ and the Sylow $p$-subgroup is normal.

::: {.example}
For $n = 20 = 2^2\cdot 5$: $n_5 \equiv 1 \pmod 5$ and $n_5 \divides 4$, so $n_5 = 1$.
:::

## Counting elements

Distinct subgroups of prime order $p$ intersect trivially, so if the Sylow $p$-subgroups have order $p$, they contain $n_p(p-1)$ elements of order $p$.
If the sum of these counts over several primes exceeds $n$, then some $n_p$ is smaller than assumed.
Sylow subgroups of order $p^2$ can intersect in a subgroup of order $p$, and then this count does not apply; see [[algebra/group-actions/show-g-is-not-simple#Two Sylow subgroups meeting nontrivially|Two Sylow subgroups meeting nontrivially]].

::: {.example}
For $n = 30$: if $n_5 = 6$ and $n_3 = 10$, then $G$ has $6\cdot 4 + 10 \cdot 2 = 44 > 30$ elements of order $5$ or $3$.
Hence $n_5 = 1$ or $n_3 = 1$.
:::

## A subgroup of small index

If $G$ is simple and $H < G$ has index $k > 1$, then the action of $G$ on the $k$ left cosets of $H$ has kernel a proper normal subgroup, hence trivial, so $G$ embeds in $S_k$ and
$$
\size G \divides k!.
$$
The subgroup $H$ can be a Sylow subgroup or the normalizer $N_G(P)$ of a Sylow subgroup $P$.

::: {.example}
For $n = 24$: if $n_2 = 3$, then $[G : N_G(P)] = 3$ for a Sylow $2$-subgroup $P$, and $24 \notdivides 3! = 6$, so $G$ is not simple.
If $n_2 = 1$, the Sylow $2$-subgroup is normal.
:::

[[PR-5FGA7]]

## Index the smallest prime

If $H \leq G$ has index $q$, the smallest prime dividing $\size G$, then $H$ is normal in $G$.
In particular, a subgroup of index $2$ is normal.

[[PR-PADL7]]

## The normalizer of a Sylow subgroup

For a Sylow $p$-subgroup $P$, orbit-stabilizer for the conjugation action on the Sylow $p$-subgroups gives $n_p = [G : N_G(P)]$.
Hence a bound on $n_p$ is a bound on the index of the subgroup $N_G(P)$, to which [[algebra/group-actions/show-g-is-not-simple#A subgroup of small index|A subgroup of small index]] and [[algebra/group-actions/show-g-is-not-simple#Index the smallest prime|Index the smallest prime]] apply.

## Two Sylow subgroups meeting nontrivially

Suppose the Sylow $p$-subgroups have order $p^2$ and two of them, $P \neq Q$, satisfy $\size{P\intersect Q} = p$.
Groups of order $p^2$ are abelian, so $D \da P\intersect Q$ is normal in both $P$ and $Q$, and $N_G(D)$ contains the subgroup $\langle P, Q\rangle$, whose order is a multiple of $p^2$ greater than $p^2$.
Hence $[G:N_G(D)]$ is a proper divisor of $m$, and either $N_G(D) = G$, so that $D$ is a proper nontrivial normal subgroup, or $[G:N_G(D)]$ is small enough for [[algebra/group-actions/show-g-is-not-simple#A subgroup of small index|A subgroup of small index]]. If instead any two distinct Sylow $p$-subgroups intersect trivially, [[algebra/group-actions/show-g-is-not-simple#Counting elements|Counting elements]] applies with $n_p(p^2-1)$ nonidentity elements.

## The action on the Sylow subgroups

$G$ acts by conjugation on its $n_p$ Sylow $p$-subgroups, giving a homomorphism $\rho\colon G \to S_{n_p}$.
By Sylow's second theorem the action is transitive, so $\ker\rho$ is a proper normal subgroup when $n_p > 1$.
If $G$ is simple and $n_p>1$, then $\rho$ is injective and $\size G \divides n_p!$.
This is the action of $G$ on the cosets of $N_G(P)$.

## Arguments and conclusions

| Argument | Input | Conclusion |
| --- | --- | --- |
| Sylow count | the factorization of $n$ | $n_p = 1$, so a Sylow $p$-subgroup is normal |
| element count | Sylow subgroups of prime order | some $n_p = 1$ |
| small index | a proper subgroup of index $k$ | $G$ simple implies $\size G \divides k!$ |
| smallest prime index | a subgroup of index the least prime dividing $n$ | that subgroup is normal |
| normalizer | $n_p = [G:N_G(P)]$ | a subgroup of index $n_p$ |
| intersecting Sylow subgroups | $\size{P\intersect Q} = p$ for Sylow subgroups of order $p^2$ | a subgroup $N_G(P\intersect Q)$ of index a proper divisor of $m$ |
| action on Sylow subgroups | $n_p > 1$ | $G$ simple implies $\size G \divides n_p!$ |

## Simple groups

The groups of prime order and the alternating groups $A_n$ for $n\geq 5$ are simple.
The group $A_5$ of order $60$ is the smallest nonabelian simple group, and every simple group of order $60$ is isomorphic to $A_5$.
