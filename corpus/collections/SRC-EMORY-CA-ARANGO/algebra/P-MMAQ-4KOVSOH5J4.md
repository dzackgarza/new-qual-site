---
schema: qual/card@1
id: P-MMAQ-4KOVSOH5J4
kind: problem
title: No finite group is the union of conjugates of a proper subgroup; a transitive
  action on more than one point has a fixed-point-free element
classification:
  areas:
  - algebra
  topics:
  - Groups
  - Group Actions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let $G$ be a finite group.

1. Prove that if $H < G$ is a proper subgroup, then $G$ is not the union of conjugates of $H$.

2. Suppose that $G$ acts transitively on a set $X$ with $|X| > 1$.
   Prove that there exists an element of $G$ with no fixed points in $X$.
:::

::: {.solution}
**Goal.** (1) A finite group is not a union of conjugates of a proper subgroup. (2) A transitive action on $|X| > 1$ points has a fixed-point-free element.

<1>1. (1) $G \neq \bigcup_{g \in G} gHg^{-1}$ for $H < G$ proper.
<2>1. The number of distinct conjugates of $H$ is $[G : N_G(H)] \le [G : H]$.
Proof: the conjugates of $H$ are indexed by $G/N_G(H)$, and $N_G(H) \supseteq H$, so $[G : N_G(H)] \le [G : H]$.
<2>2. Each conjugate has $|H|$ elements, and all contain the identity.
Proof: $|gHg^{-1}| = |H|$, and $1 \in gHg^{-1}$ for all $g$.
<2>3. Hence $\abs{\bigcup_g gHg^{-1}} \le 1 + [G:H](|H| - 1) = 1 + |G| - [G:H] < |G|$.
Proof: the union has at most $1 + (\text{number of conjugates})(|H| - 1)$ elements (counting the identity once), and $[G:H] > 1$ since $H$ is proper.
<2>4. Hence the union is a proper subset of $G$.
Proof: it has fewer than $|G|$ elements.

<1>2. (2) A transitive action on $|X| > 1$ has a fixed-point-free element.
<2>1. Suppose every $g \in G$ fixes some point of $X$.
Proof: assume for contradiction.
<2>2. Then $G = \bigcup_{x \in X} G_x$, where $G_x$ is the stabilizer of $x$.
Proof: every element fixes some point, so every element lies in some stabilizer.
<2>3. The stabilizers $G_x$ are all conjugate (since the action is transitive).
Proof: $G_{gx} = g G_x g^{-1}$.
<2>4. Hence $G$ is a union of conjugates of the proper subgroup $G_x$ (proper since $|X| > 1$ and the action is transitive).
Proof: $G_x$ is proper because the orbit of $x$ is all of $X$ with $|X| > 1$, so $G_x \neq G$.
<2>5. This contradicts <1>1.
Proof: <1>1 says $G$ is not a union of conjugates of a proper subgroup.

<1>3. Q.E.D.
Proof: <1>1 proves (1); <1>2 proves (2).
:::
