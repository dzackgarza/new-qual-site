---
schema: qual/card@1
id: P-EMAG5
kind: problem
title: "Quotient by center cyclic implies abelian, and p-groups have center"
classification:
  areas:
  - algebra
  topics:
  - Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
(a) Let $G$ be a group, and $Z(G)$ the center of $G$.
Prove that if $G/Z(G)$ is cyclic, then $G$ is abelian.

(b) Prove that a group of order $p^n$, where $p$ is a prime and $n \geq 1$, has non-trivial center.

(c) Prove that a group of order $p^2$ must be abelian.
:::

::: {.solution}
**Part (a).**

<1>1. Let $G/Z(G) = \langle gZ(G) \rangle$ be cyclic.
Proof: hypothesis.

<1>2. Every element of $G$ is of the form $g^k z$ for some $k \in \ZZ$ and $z \in Z(G)$.
Proof: the cosets of $Z(G)$ are the powers of $gZ(G)$.

<1>3. Any two elements $g^k z_1$ and $g^\ell z_2$ commute.
Proof: $(g^k z_1)(g^\ell z_2) = g^{k+\ell} z_1 z_2 = (g^\ell z_2)(g^k z_1)$, since $z_1, z_2$ are central and powers of $g$ commute.

<1>4. Hence $G$ is abelian.
Proof: <1>2 and <1>3.

**Part (b).**

<1>1. The class equation gives $|G| = |Z(G)| + \sum [G : C_G(g_i)]$, where the sum is over representatives of the non-central conjugacy classes.
Proof: class equation.

<1>2. Each $[G : C_G(g_i)]$ is divisible by $p$.
Proof: for a non-central $g_i$, $C_G(g_i) \neq G$, so $[G : C_G(g_i)] > 1$ divides $|G| = p^n$, hence is a power of $p$ greater than $1$.

<1>3. Hence $p \mid |Z(G)|$.
Proof: $|G| = p^n$ and each term in the sum is divisible by $p$, so $|Z(G)| = |G| - \sum [G : C_G(g_i)]$ is divisible by $p$.

<1>4. Therefore $Z(G) \neq 1$.
Proof: $|Z(G)| \ge p > 1$.

**Part (c).**

<1>1. $Z(G) \neq 1$ by part (b).
Proof: <1>4 of part (b).

<1>2. $|Z(G)| \in \{p, p^2\}$.
Proof: $Z(G)$ is a subgroup of $G$ of order dividing $p^2$, and it is nontrivial.

<1>3. If $|Z(G)| = p^2$, then $G = Z(G)$ is abelian.
Proof: $Z(G) \subseteq G$ and $|Z(G)| = |G|$.

<1>4. If $|Z(G)| = p$, then $G/Z(G)$ has order $p$, hence is cyclic.
Proof: a group of prime order is cyclic.

<1>5. Hence $G$ is abelian by part (a).
Proof: <1>4 and part (a).

<1>6. Q.E.D.
Proof: <1>3 and <1>5 cover both cases.
:::
