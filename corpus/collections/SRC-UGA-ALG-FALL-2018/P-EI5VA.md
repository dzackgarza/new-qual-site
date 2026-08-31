---
schema: qual/card@1
id: P-EI5VA
kind: problem
title: Stabilizers in an orbit are conjugate, conjugates of a proper subgroup do not
  cover $G$, and a transitive action on two or more points has a fixed-point-free
  element
classification:
  areas:
  - algebra
  topics:
  - Orbit-Stabilizer
  - Conjugacy
  - Burnside's Lemma
relations: []
review: draft
---

::: problem
(a) Suppose the group $G$ acts on a set $X$. Show that the stabilizers of elements in the same orbit are conjugate: for any $x \in X$ and $g \in G$, $G_{g \cdot x} = g G_x g^{-1}$.

(b) Let $G$ be a finite group and let $H < G$ be a proper subgroup. Show that the union of all conjugates of $H$ is strictly smaller than $G$:
$$
\bigcup_{g \in G} g H g^{-1} \subsetneq G.
$$

(c) Suppose a finite group $G$ acts transitively on a set $S$ with $|S| \ge 2$. Show that there exists an element $g \in G$ having no fixed points in $S$ (i.e. $g \cdot s \ne s$ for all $s \in S$).
:::

::: solution
**Goal:** Prove conjugacy of stabilizers in (a), prove that conjugates of a proper subgroup do not cover $G$ in (b), and deduce the existence of a fixed-point-free element (derangement) for transitive actions in (c).

<1>1. Part (a): Conjugacy of stabilizers in an orbit.
::: {.proof}
    <2>1. Let $x \in X$ and $g \in G$, and let $y = g \cdot x \in X$.
    <2>2. An element $h \in G$ stabilizes $y$ if and only if $h \cdot y = y$.
    <2>3. Substituting $y = g \cdot x$:
    $$h \cdot (g \cdot x) = g \cdot x \iff (g^{-1} h g) \cdot x = x \iff g^{-1} h g \in G_x.$$
    <2>4. Multiplying on the left by $g$ and on the right by $g^{-1}$:
    $$g^{-1} h g \in G_x \iff h \in g G_x g^{-1}.$$
    <2>5. Therefore $G_y = G_{g \cdot x} = g G_x g^{-1}$.

:::

<1>2. Part (b): Conjugates of a proper subgroup do not cover $G$.
::: {.proof}
    <2>1. Let $N_G(H) = \{g \in G : g H g^{-1} = H\}$ be the normalizer of $H$ in $G$.
    <2>2. The distinct conjugates of $H$ in $G$ are parameterized by the cosets of $N_G(H)$, so there are precisely $k = [G : N_G(H)]$ distinct conjugates $H_1, H_2, \dots, H_k$.
    <2>3. Since $H \le N_G(H) \le G$, by the tower law of indices $[G : H] = [G : N_G(H)] [N_G(H) : H] \ge [G : N_G(H)] = k$.
    <2>4. Every conjugate $g H g^{-1}$ contains the identity element $e$.
    <2>5. Each of the $k$ distinct conjugates contains $|H| - 1$ non-identity elements.
    <2>6. Bound the size of the union of all conjugates:
    $$\left| \bigcup_{g \in G} g H g^{-1} \right| = \left| \{e\} \cup \bigcup_{i=1}^k (H_i \setminus \{e\}) \right| \le 1 + \sum_{i=1}^k (|H_i| - 1) = 1 + k (|H| - 1).$$
    <2>7. Since $k \le [G : H]$, we have
    $$\left| \bigcup_{g \in G} g H g^{-1} \right| \le 1 + [G : H](|H| - 1) = 1 + [G : H]|H| - [G : H] = |G| + 1 - [G : H].$$
    <2>8. Since $H$ is a proper subgroup ($H \ne G$), the index $[G : H] \ge 2$.
    <2>9. Thus:
    $$\left| \bigcup_{g \in G} g H g^{-1} \right| \le |G| + 1 - [G : H] \le |G| - 1 < |G|.$$
    <2>10. Therefore $\bigcup_{g \in G} g H g^{-1} \subsetneq G$.

:::

<1>3. Part (c): Transitive actions on $|S| \ge 2$ have a fixed-point-free element.
::: {.proof}
    <2>1. Method 1 (via Part (b)):
        <3>1. Choose an arbitrary point $s_0 \in S$, and let $H = G_{s_0} \le G$ be its stabilizer.
        <3>2. By the Orbit-Stabilizer Theorem, since the action is transitive, $[G : H] = |G \cdot s_0| = |S| \ge 2$.
        <3>3. Thus $H$ is a proper subgroup of $G$.
        <3>4. By Part (a), every stabilizer is of the form $G_{g \cdot s_0} = g H g^{-1}$.
        <3>5. An element $g \in G$ fixes at least one point $s \in S$ if and only if $g \in G_s = h H h^{-1}$ for some $h \in G$.
        <3>6. Thus the set of elements in $G$ that fix at least one point of $S$ is precisely $\bigcup_{h \in G} h H h^{-1}$.
        <3>7. By Part (b), $\bigcup_{h \in G} h H h^{-1} \subsetneq G$.
        <3>8. Therefore there exists an element $g \in G \setminus \bigcup_{h \in G} h H h^{-1}$, which fixes no points of $S$.
    <2>2. Method 2 (via Burnside's Lemma):
        <3>1. Let $X^g = \{s \in S : g \cdot s = s\}$ denote the fixed point set of $g \in G$.
        <3>2. By Burnside's Lemma, the number of orbits is the average number of fixed points:
        $$1 = \frac{1}{|G|} \sum_{g \in G} |X^g| \implies |G| = \sum_{g \in G} |X^g| = |X^e| + \sum_{g \ne e} |X^g|.$$
        <3>3. Since the identity fixes all of $S$, $|X^e| = |S| \ge 2$.
        <3>4. If every $g \ne e$ had at least one fixed point ($|X^g| \ge 1$), then
        $$\sum_{g \in G} |X^g| = |X^e| + \sum_{g \ne e} |X^g| \ge 2 + (|G| - 1) = |G| + 1,$$
        a contradiction.
        <3>5. Thus there exists at least one $g \in G$ with $|X^g| = 0$.

:::

<1>4. Conclusion:
::: {.proof}
    Stabilizers in an orbit are conjugate, conjugates of a proper subgroup cannot cover a finite group, and transitive actions on sets of size $\ge 2$ always contain derangements.
:::
:::
