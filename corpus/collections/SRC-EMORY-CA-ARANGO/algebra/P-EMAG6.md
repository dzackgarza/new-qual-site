---
schema: qual/card@1
id: P-EMAG6
kind: problem
title: "Union of conjugates and fixed-point-free elements"
classification:
  areas:
  - algebra
  topics:
  - Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: problem
Let $G$ be a finite group.

(a) Prove that if $H < G$ is a proper subgroup, then $G$ is not the union of conjugates of $H$.

(b) Suppose that $G$ acts transitively on a set $X$ with $|X| > 1$.
Prove that there exists an element of $G$ with no fixed points in $X$.
:::

::: solution
**Goal:** Prove that a finite group cannot be written as the union of conjugates of a proper subgroup, and deduce that any transitive action on a set of size $> 1$ admits a fixed-point-free element (derangement).

<1>1. Part (a): If $H < G$ is a proper subgroup of a finite group $G$, then $\bigcup_{g \in G} gHg^{-1} \subsetneq G$.
    *Proof:*
    <2>1. Let $N = N_G(H)$ be the normalizer of $H$ in $G$. The distinct conjugates of $H$ in $G$ are in bijection with the left cosets of $N$ in $G$, so the number of distinct conjugate subgroups is $k = [G : N]$.
    <2>2. Since $H \subseteq N \subseteq G$, Lagrange's Theorem implies $[G : N] \le [G : H]$.
    <2>3. Each conjugate $gHg^{-1}$ has order $|H|$ and contains the identity element $e$.
    <2>4. The union $\bigcup_{g \in G} gHg^{-1}$ is the union of the $k$ distinct conjugate subgroups:
        $$\left|\bigcup_{g \in G} gHg^{-1}\right| = \left| \{e\} \cup \bigcup_{i=1}^k (g_i H g_i^{-1} \setminus \{e\}) \right| \le 1 + \sum_{i=1}^k |g_i H g_i^{-1} \setminus \{e\}| = 1 + k(|H| - 1).$$
    <2>5. Substituting $k \le [G : H] = \frac{|G|}{|H|}$ yields:
        $$\left|\bigcup_{g \in G} gHg^{-1}\right| \le 1 + [G : H](|H| - 1) = 1 + |G| - [G : H].$$
    <2>6. Since $H$ is a proper subgroup, $[G : H] \ge 2$, hence:
        $$\left|\bigcup_{g \in G} gHg^{-1}\right| \le |G| - 1 < |G|.$$
    <2>7. Therefore, $\bigcup_{g \in G} gHg^{-1} \neq G$.

<1>2. Part (b): If $G$ acts transitively on $X$ with $|X| > 1$, there exists $g \in G$ with no fixed points on $X$.
    *Proof:*
    <2>1. Fix an element $x_0 \in X$ and let $H = G_{x_0} = \{g \in G : g \cdot x_0 = x_0\}$ be the stabilizer of $x_0$.
    <2>2. By the Orbit-Stabilizer Theorem, $[G : H] = |G \cdot x_0| = |X| > 1$, so $H$ is a proper subgroup of $G$.
    <2>3. For any $x \in X$, transitivity provides some $g \in G$ such that $x = g \cdot x_0$. The stabilizer of $x$ is:
        $$G_x = G_{g \cdot x_0} = g G_{x_0} g^{-1} = g H g^{-1}.$$
    <2>4. An element $g \in G$ has at least one fixed point in $X$ if and only if $g \in G_x$ for some $x \in X$, which holds if and only if $g \in \bigcup_{x \in X} G_x = \bigcup_{g \in G} g H g^{-1}$.
    <2>5. By <1>1, $\bigcup_{g \in G} g H g^{-1} \subsetneq G$, so there exists $g \in G$ such that $g \notin \bigcup_{x \in X} G_x$.
    <2>6. This element $g$ fixes no point in $X$. Q.E.D.
:::
