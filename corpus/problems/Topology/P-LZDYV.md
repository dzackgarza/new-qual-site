---
schema: qual/card@1
id: P-LZDYV
kind: problem
title: van Kampen's theorem, and $\pi_1$ of glued tori, the Klein bottle, and wedges
classification:
  areas:
  - topology
  topics:
  - van Kampen
  - Fundamental Group
  - Surfaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
(a) State the Seifert–van Kampen Theorem.
(b) Calculate the fundamental group of the space obtained by taking two copies of the torus $T = S^1 \times S^1$ and gluing them along a circle $S^1 \times \{p\}$.
(c) Calculate the fundamental group of the Klein bottle $K$.
(d) Calculate the fundamental group of the wedge sum $T^2 \vee S^1 = (S^1 \times S^1) \vee S^1$.
(e) Calculate the fundamental group of the wedge sum $T^2 \vee \mathbb{RP}^2$.
:::

::: solution
**Goal:** Apply the Seifert–van Kampen theorem to compute fundamental groups of glued surfaces and wedge sums.

<1>1. Part (a): Statement of the Seifert–van Kampen Theorem:
    *Proof:*
    <2>1. Let $X = U \cup V$ where $U, V \subseteq X$ are open, path-connected subsets whose intersection $U \cap V$ is non-empty and path-connected, containing a basepoint $x_0 \in U \cap V$.
    <2>2. Let $j_U: \pi_1(U \cap V, x_0) \to \pi_1(U, x_0)$ and $j_V: \pi_1(U \cap V, x_0) \to \pi_1(V, x_0)$ be the homomorphisms induced by inclusion maps.
    <2>3. **Theorem:** The fundamental group $\pi_1(X, x_0)$ is isomorphic to the **amalgamated free product** (pushout in the category of groups):
        $$\pi_1(X, x_0) \cong \pi_1(U, x_0) *_{\pi_1(U \cap V, x_0)} \pi_1(V, x_0) \cong \frac{\pi_1(U, x_0) * \pi_1(V, x_0)}{\langle j_U(\gamma) j_V(\gamma)^{-1} \mid \gamma \in \pi_1(U \cap V, x_0) \rangle}.$$

<1>2. Part (b): Two tori glued along a circle $S^1 \times \{p\}$:
    *Proof:*
    <2>1. Let $T_1, T_2$ be two tori with $\pi_1(T_1) = \langle a_1, b_1 \mid [a_1, b_1] = 1 \rangle \cong \mathbb{Z}^2$ and $\pi_1(T_2) = \langle a_2, b_2 \mid [a_2, b_2] = 1 \rangle \cong \mathbb{Z}^2$.
    <2>2. The gluing circle $C = S^1 \times \{p\}$ corresponds to the loop $a_1$ in $T_1$ and $a_2$ in $T_2$, with $\pi_1(C) \cong \mathbb{Z} = \langle c \rangle$.
    <2>3. By van Kampen's Theorem, the amalgamated free product is:
        $$\pi_1(T_1 \cup_C T_2) \cong \pi_1(T_1) *_{\pi_1(C)} \pi_1(T_2) = \langle a_1, b_1, a_2, b_2 \mid [a_1, b_1] = 1, [a_2, b_2] = 1, a_1 = a_2 \rangle.$$
    <2>4. Setting $a = a_1 = a_2$, this simplifies to:
        $$\pi_1(X) \cong \langle a, b_1, b_2 \mid [a, b_1] = 1, [a, b_2] = 1 \rangle \cong \mathbb{Z} *_{\mathbb{Z}} (\mathbb{Z} \times \mathbb{Z}) \cong \mathbb{Z} \times (\mathbb{Z} * \mathbb{Z}) = \mathbb{Z} \times F_2.$$

<1>3. Part (c): Fundamental Group of the Klein Bottle:
    *Proof:*
    <2>1. The Klein bottle $K$ has standard 2-cell polygon presentation with boundary word $a b a^{-1} b$.
    <2>2. The 1-skeleton is $S^1 \vee S^1$ with $\pi_1(K^1) = \langle a, b \rangle$.
    <2>3. Attaching the 2-cell yields the relation $a b a^{-1} b = 1 \iff a b a^{-1} = b^{-1}$.
    <2>4. Thus:
        $$\pi_1(K) = \langle a, b \mid a b a^{-1} = b^{-1} \rangle \cong \mathbb{Z} \rtimes \mathbb{Z}.$$

<1>4. Part (d): Wedge Sum $T^2 \vee S^1$:
    *Proof:*
    <2>1. For wedge sums of path-connected, locally contractible spaces, van Kampen's theorem gives the bare free product:
        $$\pi_1(X \vee Y) \cong \pi_1(X) * \pi_1(Y).$$
    <2>2. For $T^2 \vee S^1$, $\pi_1(T^2) \cong \mathbb{Z}^2 = \langle a, b \mid [a, b] = 1 \rangle$ and $\pi_1(S^1) \cong \mathbb{Z} = \langle c \rangle$.
    <2>3. Therefore:
        $$\pi_1(T^2 \vee S^1) \cong \mathbb{Z}^2 * \mathbb{Z} = \langle a, b, c \mid [a, b] = 1 \rangle.$$

<1>5. Part (e): Wedge Sum $T^2 \vee \mathbb{RP}^2$:
    *Proof:*
    <2>1. We have $\pi_1(T^2) \cong \mathbb{Z}^2$ and $\pi_1(\mathbb{RP}^2) \cong \mathbb{Z}_2 = \langle d \mid d^2 = 1 \rangle$.
    <2>2. By the free product formula for wedge sums:
        $$\pi_1(T^2 \vee \mathbb{RP}^2) \cong \mathbb{Z}^2 * \mathbb{Z}_2 = \langle a, b, d \mid [a, b] = 1, d^2 = 1 \rangle.$$

<1>6. Conclusion:
    The fundamental groups are: (b) $\mathbb{Z} \times F_2$, (c) $\mathbb{Z} \rtimes \mathbb{Z}$, (d) $\mathbb{Z}^2 * \mathbb{Z}$, and (e) $\mathbb{Z}^2 * \mathbb{Z}_2$. Q.E.D.
:::
