---
title: Show $G$ is not simple
order: 0
topics:
- Simple Groups
- Sylow Theory
---

# Show $G$ is not simple

To show that a group $G$ is not simple is to exhibit a proper nontrivial normal subgroup. The arguments below use its order, Sylow subgroups, and permutation actions.

## Constraints from the order

The prime factorization of $n$ constrains the number $n_p$ of Sylow $p$-subgroups.
By Sylow 3, for $n = p^k m$ with $p\nmid m$,
\[
n_p \equiv 1 \pmod p, \qquad n_p \divides m
.\]
If these conditions force $n_p = 1$, the unique Sylow $p\dash$subgroup is normal because conjugation permutes the Sylow $p\dash$subgroups.

For prime and prime-power orders:

- $n$ prime: $G$ is cyclic and simple, so the answer is that it *is* simple.
- $n = p^k$ with $k\geq 2$: the class equation forces $Z(G) \neq 1$. If $Z(G)$ is proper, it is the required normal subgroup. Otherwise $G$ is abelian, and a subgroup of order $p$ is proper and normal.

## 1. A Sylow count that leaves only $n_p = 1$

For $n = 20 = 2^2\cdot 5$: $n_5 \equiv 1 \pmod 5$ and $n_5 \divides 4$, so $n_5 = 1$.
The Sylow $5$-subgroup is therefore proper, nontrivial, and normal.

## 2. Counting elements

When no $n_p$ is forced to $1$ individually, count what the Sylows would cost.
Distinct Sylow $p\dash$subgroups of order $p$ meet trivially, so $n_p$ of them contribute $n_p(p-1)$ elements of order $p$.
Sum over the primes; if the total exceeds $n$, some $n_p$ was too large.

For $n = 30$: if $n_5 = 6$ and $n_3 = 10$ then the elements of order $5$ and $3$ already number $6\cdot 4 + 10 \cdot 2 = 44 > 30$.
So at least one of them is $1$.

The counting is exact only when the Sylows intersect trivially, which is automatic for $p$ but not for $p^2$; see argument 6.

## 3. The index of a subgroup is too small

If $G$ is simple and $H \leq G$ has index $k > 1$, then $G$ acts faithfully on the $k$ cosets, so $G$ embeds in $S_k$ and
\[
\size G \divides k!
.\]
Take a subgroup that Sylow guarantees, usually a Sylow $p\dash$subgroup or its normalizer, and check the divisibility.

For $n = 24$: if $n_2 = 3$ then $[G : N_G(P_2)] = 3$, so $\size G = 24$ would have to divide $3! = 6$.

[[PR-5FGA7]]

## 4. Smallest prime index

A subgroup of index equal to the *smallest* prime dividing $\size G$ is automatically normal.
In particular a subgroup of index $2$ is normal.

[[PR-PADL7]]

## 5. The normalizer of a Sylow subgroup

$n_p = [G : N_G(P)]$, so a Sylow count is a statement about an index, and arguments 3 and 4 apply to $N_G(P)$.
If $n_p>1$ and $|G|$ does not divide $n_p!$, the coset action on $G/N_G(P)$ has a proper nontrivial kernel.

## 6. Two Sylow subgroups meeting nontrivially

Suppose distinct Sylow $p\dash$subgroups $P,Q$ have order $p^2$ and intersect in a subgroup $H$ of order $p$. Since $P$ and $Q$ are abelian, both lie in $N_G(H)$, which strictly contains each of them. If $N_G(H)=G$, then $H$ is normal. Otherwise its index gives a coset action to which argument 3 applies.

## 7. The action on the Sylow subgroups

$G$ acts by conjugation on its $n_p$ Sylow $p\dash$subgroups, giving $\rho: G \to S_{n_p}$.
For $n_p>1$, the kernel is proper and normal, so if $G$ is simple then $\rho$ is injective and $\size G \divides n_p!$.
Sylow 2 says the action is transitive, so the kernel is proper whenever $n_p > 1$.

This is argument 3 with $H = N_G(P)$: the Sylow subgroups correspond to cosets of the normalizer.

## What each argument needs

| Argument | Needs | Gives |
| --- | --- | --- |
| Sylow count | only the factorization of $n$ | $n_p = 1$, hence a normal Sylow |
| element count | Sylows of prime order | some $n_p = 1$ |
| index too small | a subgroup of known index $k$ | $\size G \divides k!$, a contradiction |
| smallest prime index | a subgroup of index the least prime | that subgroup is normal |
| normalizer | $n_p = [G:N_G(P)]$ | a large subgroup to feed the others |
| intersecting Sylows | Sylow subgroups of order $p^2$ meeting in order $p$ | a normalizer containing both |
| action on Sylows | $n_p > 1$ | $\size G \divides n_p!$ |

## When the answer is that it is simple

$A_n$ for $n\geq 5$, and groups of prime order.
$A_5$ is the smallest nonabelian simple group, and any simple group of order $60$ is isomorphic to it.
