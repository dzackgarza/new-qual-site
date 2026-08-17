---
schema: qual/card@1
id: P-B6EUH
kind: problem
title: Suppose the group $G$ acts on the set $X$ . Show that the stabilizers of...
classification:
  areas:
  - algebra
  topics:
  - orbit-stabilizer
  - conjugacy
  - burnside-s-lemma
relations: []
review: draft
solved: true
---

::: problem
(a) Suppose the group $G$ acts on the set $X$ . Show that the stabilizers of elements in the same orbit are conjugate.

(b) Let $G$ be a finite group and let $H$ be a proper subgroup. Show that the union of the conjugates of $H$ is strictly smaller than $G$, i.e.
    $$
    \union_{g\in G} gHg\inv \subsetneq G
    $$

(c) Suppose $G$ is a finite group acting transitively on a set $S$ with at least 2 elements. Show that there is an element of $G$ with no fixed points in $S$.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**(a) Conjugacy of stabilizers in the same orbit:**
Let $x, y \in X$ lie in the same orbit, so $y = g \cdot x$ for some $g \in G$.
Let $G_x = \{h \in G \mid h \cdot x = x\}$ and $G_y = \{h \in G \mid h \cdot y = y\}$.
For any $h \in G_y$:
$$
h \cdot (g \cdot x) = g \cdot x \iff (g^{-1} h g) \cdot x = x \iff g^{-1} h g \in G_x \iff h \in g G_x g^{-1}.
$$
Thus $G_y = g G_x g^{-1}$, so the stabilizers $G_x$ and $G_y$ are conjugate in $G$.

**(b) Proper subgroup conjugates cannot cover $G$:**
Let $H < G$ be a proper subgroup with $[G : H] = k \geq 2$.
The number of distinct conjugate subgroups $g H g^{-1}$ is $[G : N_G(H)] \leq [G : H] = k$.
Each conjugate subgroup has order $|H|$ and contains the identity element $e$.
Counting elements in the union:
$$
\left| \bigcup_{g \in G} g H g^{-1} \right| \leq 1 + \sum_{g H g^{-1}} (|H| - 1) \leq 1 + [G:H](|H| - 1) = 1 + |G| - [G:H].
$$
Since $H$ is proper, $[G : H] \geq 2$, so:
$$
\left| \bigcup_{g \in G} g H g^{-1} \right| \leq |G| - 1 < |G|.
$$
Therefore, $\bigcup_{g \in G} g H g^{-1} \subsetneq G$.

**(c) Existence of a fixed-point-free element in transitive actions:**
Pick any $s_0 \in S$, and let $H = G_{s_0}$ be its stabilizer.
Since the action is transitive, the orbit of $s_0$ is the entire set $S$, so by the Orbit-Stabilizer Theorem:
$$
|S| = [G : G_{s_0}] = [G : H].
$$
Since $|S| \geq 2$, $[G : H] \geq 2$, so $H < G$ is a proper subgroup.
By part (a), for any $s \in S$, the stabilizer $G_s$ is conjugate to $H = G_{s_0}$, so every stabilizer is of the form $g H g^{-1}$ for some $g \in G$.
An element $g \in G$ has a fixed point in $S$ if and only if $g \in G_s$ for some $s \in S$, which means:
$$
\{g \in G \mid g \text{ fixes at least one point in } S\} = \bigcup_{s \in S} G_s = \bigcup_{g \in G} g H g^{-1}.
$$
By part (b), this union is strictly smaller than $G$.
Therefore, there exists at least one element $g \in G \setminus \bigcup_{s \in S} G_s$, which fixes no points in $S$.
:::
