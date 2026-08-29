---
schema: qual/card@1
id: E-AMD-JNN3C5JP
kind: exercise
title: Groups of order $p^2$ are abelian
classification:
  areas:
  - algebra
  topics:
  - Classification
  - p-Groups
  - Abelian Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Show that every group of order $p^2$ is abelian and classify them.
:::

::: solution
**Goal:** Prove that every group $G$ of order $p^2$ ($p$ prime) is abelian and classify all such groups up to isomorphism.

<1>1. Non-triviality of the center $Z(G)$:
    *Proof:*
    <2>1. By the class equation for $G$:
        $$|G| = |Z(G)| + \sum_{i=1}^k [G : C_G(x_i)],$$
        where $x_1, \dots, x_k$ are representatives of the non-central conjugacy classes.
    <2>2. For each $x_i \notin Z(G)$, the centralizer satisfies $Z(G) \le C_G(x_i) \lneq G$, so $[G : C_G(x_i)] = p$.
    <2>3. Because $p \mid |G|$ and $p \mid [G : C_G(x_i)]$ for all $i$, $p$ must divide $|Z(G)|$.
    <2>4. By Lagrange's Theorem, $|Z(G)|$ divides $|G| = p^2$, so $|Z(G)| \in \{p, p^2\}$.

<1>2. Proof that $G$ is abelian ($|Z(G)| = p^2$):
    *Proof:*
    <2>1. Suppose for contradiction that $|Z(G)| = p$.
    <2>2. Then $|G / Z(G)| = p^2 / p = p$.
    <2>3. Any group of prime order is cyclic, so $G / Z(G) = \langle g Z(G) \rangle$ for some $g \in G$.
    <2>4. Every $x, y \in G$ can be written as $x = g^a z_1$ and $y = g^b z_2$ for $a, b \in \mathbb{Z}$ and $z_1, z_2 \in Z(G)$.
    <2>5. Computing the product:
        $$x y = (g^a z_1)(g^b z_2) = g^{a+b} z_1 z_2 = g^{b+a} z_2 z_1 = (g^b z_2)(g^a z_1) = y x.$$
    <2>6. Thus $G$ is abelian, which forces $Z(G) = G$ and $|Z(G)| = p^2$, a contradiction.
    <2>7. Therefore $|Z(G)| = p^2$, so $Z(G) = G$, meaning $G$ is abelian.

<1>3. Classification of groups of order $p^2$:
    *Proof:*
    <2>1. By Lagrange's Theorem, every non-identity element of $G$ has order $p$ or $p^2$.
    <2>2. **Case 1 (Contains element of order $p^2$):** If there exists $x \in G$ with $|x| = p^2$, then $G = \langle x \rangle \cong \mathbb{Z}_{p^2}$ is cyclic.
    <2>3. **Case 2 (All non-identity elements have order $p$):** If every $x \in G \setminus \{e\}$ has order $p$, choose $x \in G \setminus \{e\}$ and $y \in G \setminus \langle x \rangle$.
        Then $\langle x \rangle \cap \langle y \rangle = \{e\}$, and $|\langle x \rangle \langle y \rangle| = p \cdot p = p^2 = |G|$.
        Since $G$ is abelian, $G \cong \langle x \rangle \times \langle y \rangle \cong \mathbb{Z}_p \times \mathbb{Z}_p$.

<1>4. Conclusion:
    Every group of order $p^2$ is abelian, and up to isomorphism the only such groups are:
    $$\mathbb{Z}_{p^2} \quad \text{and} \quad \mathbb{Z}_p \times \mathbb{Z}_p.$$
    Q.E.D.
:::
