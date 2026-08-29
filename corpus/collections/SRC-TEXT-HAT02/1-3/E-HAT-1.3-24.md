---
schema: qual/card@1
id: E-HAT-1.3-24
kind: exercise
title: "Covering spaces from subgroups of deck transformation groups"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

Given a covering space action of a group $G$ on a path-connected, locally path-connected space $X$, then each subgroup $H \subset G$ determines a composition of covering spaces $X \to X/H \to X/G$.
Show:

(a) Every path-connected covering space between $X$ and $X/G$ is isomorphic to $X/H$ for some subgroup $H \subset G$.

(b) Two such covering spaces $X/H_1$ and $X/H_2$ of $X/G$ are isomorphic if $H_1$ and $H_2$ are conjugate subgroups of $G$.

(c) The covering space $X/H \to X/G$ is normal if $H$ is a normal subgroup of $G$, in which case the group of deck transformations of this cover is $G/H$.

::: {.solution}
**(a).**

<1>1. Let $p : Y \to X/G$ be a path-connected covering space, and choose a basepoint $y_0 \in Y$ with $p(y_0) = x_0$.
Proof: setup.

<1>2. Since $X \to X/G$ is the universal cover (a covering space action of $G$ on a simply-connected $X$), there is a lift $\tilde p : X \to Y$ of the covering $X \to X/G$ through $p$.
Proof: the universal property of the universal cover (lifting criterion).

<1>3. The deck transformation group of $X \to X/G$ is $G$, and the subgroup $H = p_*(\pi_1(Y))$ (or equivalently the stabilizer of the lift) acts on $X$ with quotient $Y$.
Proof: covering space theory; $Y \cong X/H$ where $H$ is the subgroup of $G$ corresponding to the subgroup $p_*(\pi_1(Y)) \le \pi_1(X/G) = G$.

<1>4. Hence $Y \cong X/H$ for some subgroup $H \le G$.
Proof: <1>3.

**(b).**

<1>1. $X/H_1$ and $X/H_2$ are isomorphic as covering spaces of $X/G$ iff $H_1$ and $H_2$ are conjugate in $G$.
Proof: two subgroups give isomorphic covers iff they are conjugate (the isomorphism is induced by a deck transformation of $X$ conjugating one subgroup to the other).

<1>2. Hence the claim.
Proof: <1>1.

**(c).**

<1>1. The cover $X/H \to X/G$ is normal iff $H$ is normal in $G$.
Proof: a covering is normal iff the corresponding subgroup is normal in the fundamental group.

<1>2. If $H \trianglelefteq G$, the deck transformation group of $X/H \to X/G$ is $N_G(H)/H = G/H$.
Proof: the deck transformations of $X/H \to X/G$ are the elements of $G$ normalizing $H$, modulo $H$; when $H$ is normal, $N_G(H) = G$.

<1>3. Q.E.D.
Proof: <1>4 (a), <1>2 (b), <1>2 (c).
:::
