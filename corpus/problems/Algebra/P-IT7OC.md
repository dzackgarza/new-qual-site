---
schema: qual/card@1
id: P-IT7OC
kind: problem
title: A subgroup that meets every conjugacy class is the whole group
classification:
  areas:
  - algebra
  topics:
  - Conjugacy
  - Cosets and Lagrange
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $G$ be a finite group and let $H \le G$ be a subgroup.
Prove that if $H$ meets every conjugacy class of $G$ (i.e. $\bigcup_{g \in G} g H g^{-1} = G$), then $H = G$ (Jordan's Theorem on permutation groups).
:::

::: solution
**Goal:** Prove that a proper subgroup $H \lneq G$ of a finite group cannot meet every conjugacy class of $G$, and therefore $\bigcup_{g \in G} g H g^{-1} = G \implies H = G$.

<1>1. Union of Conjugates of $H$:
    *Proof:*
    <2>1. Let $H \le G$ be a subgroup of a finite group $G$, and let $n = [G : H]$ be the index of $H$.
    <2>2. The distinct conjugates of $H$ in $G$ are indexed by the cosets of the normalizer $N_G(H)$:
        - The number of distinct conjugates is $k = [G : N_G(H)]$.
        - Since $H \le N_G(H)$, we have $k = [G : N_G(H)] \le [G : H] = n$.
    <2>3. Each conjugate $g H g^{-1}$ contains $|H|$ elements, and all conjugates share at least the identity element $e \in \bigcap_{g \in G} g H g^{-1}$.
    <2>4. The number of non-identity elements in the union $\bigcup_{g \in G} g H g^{-1}$ satisfies the union bound:
        $$\left| \bigcup_{g \in G} (g H g^{-1} \setminus \{e\}) \right| \le \sum_{g N_G(H)} |g H g^{-1} \setminus \{e\}| = k (|H| - 1).$$
    <2>5. Adding the identity element back in gives:
        $$\left| \bigcup_{g \in G} g H g^{-1} \right| \le 1 + k (|H| - 1) \le 1 + [G : H](|H| - 1).$$

<1>2. Strict Inequality for Proper Subgroups ($H \lneq G$):
    *Proof:*
    <2>1. Suppose $H$ is a proper subgroup of $G$, so $[G : H] = n \ge 2$.
    <2>2. Expanding the upper bound:
        $$1 + [G : H](|H| - 1) = 1 + [G : H]|H| - [G : H] = 1 + |G| - [G : H] = |G| - ([G : H] - 1).$$
    <2>3. Since $[G : H] \ge 2$, we have $[G : H] - 1 \ge 1 > 0$, which strictly implies:
        $$\left| \bigcup_{g \in G} g H g^{-1} \right| \le |G| - ([G : H] - 1) < |G|.$$
    <2>4. Thus, the union of all conjugates of a proper subgroup $H \lneq G$ cannot cover all of $G$:
        $$\bigcup_{g \in G} g H g^{-1} \subsetneq G.$$

<1>3. Alternative Formulation via Burnside's Lemma (Jordan's Theorem):
    *Proof:*
    <2>1. Consider the transitive action of $G$ on the coset space $X = G/H$ of size $n = [G : H] \ge 2$.
    <2>2. A group element $g \in G$ fixes a coset $x H \iff x^{-1} g x \in H \iff g \in x H x^{-1}$.
    <2>3. Thus $g \in \bigcup_{x \in G} x H x^{-1} \iff \operatorname{Fix}(g) \ne \varnothing$.
    <2>4. By **Burnside's Lemma** (Orbit-Counting Theorem), the average number of fixed points is the number of orbits:
        $$\frac{1}{|G|} \sum_{g \in G} |\operatorname{Fix}(g)| = |\text{Orbits}| = 1.$$
    <2>5. The identity $e$ fixes all $n \ge 2$ points: $|\operatorname{Fix}(e)| = n \ge 2$.
    <2>6. For the average over all $|G|$ elements to equal 1, there must exist at least one element $g_0 \in G$ with $|\operatorname{Fix}(g_0)| = 0$ (a **derangement**).
    <2>7. A derangement $g_0$ fixes no coset, so $g_0 \notin \bigcup_{x \in G} x H x^{-1}$.
    <2>8. Thus the conjugacy class of $g_0$ does not intersect $H$.

<1>4. Conclusion:
    If $H$ meets every conjugacy class, $H$ cannot be a proper subgroup, so $H = G$. Q.E.D.
:::
