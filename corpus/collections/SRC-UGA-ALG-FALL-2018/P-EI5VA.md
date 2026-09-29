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

::: {.problem}
(a) Suppose the group $G$ acts on a set $X$. Show that the stabilizers of elements in the same orbit are conjugate: for any $x \in X$ and $g \in G$, $G_{g \cdot x} = g G_x g^{-1}$.

(b) Let $G$ be a finite group and let $H < G$ be a proper subgroup. Show that the union of all conjugates of $H$ is strictly smaller than $G$:
$$
\bigcup_{g \in G} g H g^{-1} \subsetneq G.
$$

(c) Suppose a finite group $G$ acts transitively on a set $S$ with $|S| \ge 2$. Show that there exists an element $g \in G$ having no fixed points in $S$ (i.e. $g \cdot s \ne s$ for all $s \in S$).
:::

::: {.solution}
**Goal:** Prove conjugacy of stabilizers in (a), prove that conjugates of a proper subgroup do not cover $G$ in (b), and deduce the existence of a fixed-point-free element (derangement) for transitive actions in (c).

::: pf

::: pf-step
Part (a): Conjugacy of stabilizers in an orbit.

::: pf-proof

::: pf-step
Let $x \in X$ and $g \in G$, and let $y = g \cdot x \in X$.
:::

::: pf-step
An element $h \in G$ stabilizes $y$ if and only if $h \cdot y = y$.
:::

::: pf-step
Substituting $y = g \cdot x$:
$$h \cdot (g \cdot x) = g \cdot x \iff (g^{-1} h g) \cdot x = x \iff g^{-1} h g \in G_x.$$
:::

::: pf-step
Multiplying on the left by $g$ and on the right by $g^{-1}$:
$$g^{-1} h g \in G_x \iff h \in g G_x g^{-1}.$$
:::

::: pf-step
Therefore $G_y = G_{g \cdot x} = g G_x g^{-1}$.
:::

:::

:::

::: pf-step
Part (b): Conjugates of a proper subgroup do not cover $G$.

::: pf-proof

::: pf-step
Let $N_G(H) = \{g \in G : g H g^{-1} = H\}$ be the normalizer of $H$ in $G$.
:::

::: pf-step
The distinct conjugates of $H$ in $G$ are parameterized by the cosets of $N_G(H)$, so there are precisely $k = [G : N_G(H)]$ distinct conjugates $H_1, H_2, \dots, H_k$.
:::

::: pf-step
Since $H \le N_G(H) \le G$, by the tower law of indices $[G : H] = [G : N_G(H)] [N_G(H) : H] \ge [G : N_G(H)] = k$.
:::

::: pf-step
Every conjugate $g H g^{-1}$ contains the identity element $e$.
:::

::: pf-step
Each of the $k$ distinct conjugates contains $|H| - 1$ non-identity elements.
:::

::: pf-step
Bound the size of the union of all conjugates:
$$\left| \bigcup_{g \in G} g H g^{-1} \right| = \left| \{e\} \cup \bigcup_{i=1}^k (H_i \setminus \{e\}) \right| \le 1 + \sum_{i=1}^k (|H_i| - 1) = 1 + k (|H| - 1).$$
:::

::: pf-step
Since $k \le [G : H]$, we have
$$\left| \bigcup_{g \in G} g H g^{-1} \right| \le 1 + [G : H](|H| - 1) = 1 + [G : H]|H| - [G : H] = |G| + 1 - [G : H].$$
:::

::: pf-step
Since $H$ is a proper subgroup ($H \ne G$), the index $[G : H] \ge 2$.
:::

::: pf-step
Thus:
$$\left| \bigcup_{g \in G} g H g^{-1} \right| \le |G| + 1 - [G : H] \le |G| - 1 < |G|.$$
:::

::: pf-step
Therefore $\bigcup_{g \in G} g H g^{-1} \subsetneq G$.
:::

:::

:::

::: pf-step
Part (c): Transitive actions on $|S| \ge 2$ have a fixed-point-free element.

::: pf-proof

::: pf-step
Method 1 (via Part (b)):

::: pf-proof

::: pf-step
Choose an arbitrary point $s_0 \in S$, and let $H = G_{s_0} \le G$ be its stabilizer.
:::

::: pf-step
By the Orbit-Stabilizer Theorem, since the action is transitive, $[G : H] = |G \cdot s_0| = |S| \ge 2$.
:::

::: pf-step
Thus $H$ is a proper subgroup of $G$.
:::

::: pf-step
By Part (a), every stabilizer is of the form $G_{g \cdot s_0} = g H g^{-1}$.
:::

::: pf-step
An element $g \in G$ fixes at least one point $s \in S$ if and only if $g \in G_s = h H h^{-1}$ for some $h \in G$.
:::

::: pf-step
Thus the set of elements in $G$ that fix at least one point of $S$ is precisely $\bigcup_{h \in G} h H h^{-1}$.
:::

::: pf-step
By Part (b), $\bigcup_{h \in G} h H h^{-1} \subsetneq G$.
:::

::: pf-step
Therefore there exists an element $g \in G \setminus \bigcup_{h \in G} h H h^{-1}$, which fixes no points of $S$.
:::

:::

:::

::: pf-step
Method 2 (via Burnside's Lemma):

::: pf-proof

::: pf-step
Let $X^g = \{s \in S : g \cdot s = s\}$ denote the fixed point set of $g \in G$.
:::

::: pf-step
By Burnside's Lemma, the number of orbits is the average number of fixed points:
$$1 = \frac{1}{|G|} \sum_{g \in G} |X^g| \implies |G| = \sum_{g \in G} |X^g| = |X^e| + \sum_{g \ne e} |X^g|.$$
:::

::: pf-step
Since the identity fixes all of $S$, $|X^e| = |S| \ge 2$.
:::

::: pf-step
If every $g \ne e$ had at least one fixed point ($|X^g| \ge 1$), then
$$\sum_{g \in G} |X^g| = |X^e| + \sum_{g \ne e} |X^g| \ge 2 + (|G| - 1) = |G| + 1,$$
a contradiction.
:::

::: pf-step
Thus there exists at least one $g \in G$ with $|X^g| = 0$.
:::

:::

:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
Stabilizers in an orbit are conjugate, conjugates of a proper subgroup cannot cover a finite group, and transitive actions on sets of size $\ge 2$ always contain derangements.
:::

:::

:::
:::
