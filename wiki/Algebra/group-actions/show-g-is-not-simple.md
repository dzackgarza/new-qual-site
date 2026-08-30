---
title: Show $G$ is not simple
order: 0
problems:
  topics:
  - Simple Groups
  - Sylow Theory
---

# Show $G$ is not simple

The most frequently asked question in the subject, and it is asked in one form: here is $\size G = n$, produce a proper nontrivial normal subgroup.
Almost every instance is settled by one of the seven arguments below, and the order in which to try them is the order they are listed.

## Read the order first

Factor $n$ and write down $n_p$'s constraints for each prime immediately.
By Sylow 3, for $n = p^k m$ with $p\nmid m$,
\[
n_p \equiv 1 \pmod p, \qquad n_p \divides m
.\]
That pair of conditions is usually enough to force $n_p = 1$ for some $p$, which is the whole problem: a unique Sylow $p\dash$subgroup is normal, because conjugation permutes the Sylow $p\dash$subgroups and there is nowhere else to send it.

Two orders never need any of this:

- $n$ prime: $G$ is cyclic and simple, so the answer is that it *is* simple.
- $n = p^k$ with $k\geq 2$: the class equation forces $Z(G) \neq 1$, and the centre is normal.

## 1. A Sylow count that leaves only $n_p = 1$

Try every prime.
For $n = 20 = 2^2\cdot 5$: $n_5 \equiv 1 \pmod 5$ and $n_5 \divides 4$, so $n_5 = 1$.
Done, without any further work.

This is the first thing to try and it succeeds more often than any other argument.

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
In particular a subgroup of index $2$ is normal, which is the case that comes up most.

[[PR-PADL7]]

## 5. The normalizer of a Sylow subgroup

$n_p = [G : N_G(P)]$, so a Sylow count is a statement about an index, and arguments 3 and 4 apply to $N_G(P)$.
If $n_p = p$ or another small number, the normalizer is a large subgroup, which is often exactly the proper normal subgroup being asked for -- or its core is.

## 6. Two Sylow subgroups meeting nontrivially

For $p^2 \divides \size G$, distinct Sylow $p\dash$subgroups can share a subgroup of order $p$.
Take $P \neq Q$ with $\size{P\intersect Q}$ maximal; then $N_G(P\intersect Q)$ contains both $P$ and $Q$ properly, so it is a large subgroup, and its index is small enough for argument 3.

This is the argument for orders like $n = p^2q$ where element counting is not tight enough.

## 7. The action on the Sylow subgroups

$G$ acts by conjugation on its $n_p$ Sylow $p\dash$subgroups, giving $\rho: G \to S_{n_p}$.
The kernel is normal, so if $G$ is simple then $\rho$ is injective and $\size G \divides n_p!$.
Sylow 2 says the action is transitive, so the kernel is proper whenever $n_p > 1$.

This subsumes argument 3 with $H = N_G(P)$ and is the form to reach for when the index itself is not obviously useful.

## What each argument needs

| Argument | Needs | Gives |
| --- | --- | --- |
| Sylow count | only the factorization of $n$ | $n_p = 1$, hence a normal Sylow |
| element count | Sylows of prime order | some $n_p = 1$ |
| index too small | a subgroup of known index $k$ | $\size G \divides k!$, a contradiction |
| smallest prime index | a subgroup of index the least prime | that subgroup is normal |
| normalizer | $n_p = [G:N_G(P)]$ | a large subgroup to feed the others |
| intersecting Sylows | $p^2 \divides \size G$ | a large normalizer |
| action on Sylows | $n_p > 1$ | $\size G \divides n_p!$ |

## When the answer is that it is simple

$A_n$ for $n\geq 5$, and groups of prime order.
If the order is $60$ and every argument above fails, that is the expected outcome: $A_5$ is the smallest nonabelian simple group, and any simple group of order $60$ is isomorphic to it.
