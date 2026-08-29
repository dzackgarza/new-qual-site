---
schema: qual/card@1
id: P-24CMJ
kind: problem
title: $\pi_1(S^1\vee S^1)$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - van Kampen
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Compute the fundamental group $\pi_1(S^1 \vee S^1, x_0)$ of the wedge sum of two circles (the figure eight space).
:::

::: solution
**Goal:** Prove that $\pi_1(S^1 \vee S^1, x_0) \cong \mathbb{Z} * \mathbb{Z} = F_2$, the free group on two generators, using the Seifert–van Kampen theorem.

<1>1. Setting up the open cover for the Seifert–van Kampen Theorem:
    *Proof:*
    <2>1. Let $X = S_a^1 \vee S_b^1$ with basepoint $x_0$ being the wedge point.
    <2>2. Let $p_a \in S_a^1 \setminus \{x_0\}$ and $p_b \in S_b^1 \setminus \{x_0\}$ be points distinct from the basepoint.
    <2>3. Define open sets:
        - $U = X \setminus \{p_b\} = S_a^1 \vee (S_b^1 \setminus \{p_b\})$.
        - $V = X \setminus \{p_a\} = (S_a^1 \setminus \{p_a\}) \vee S_b^1$.
    <2>4. Then $U \cup V = X$, and both $U, V$ are open in $X$.

<1>2. Homotopy types of $U, V$, and $U \cap V$:
    *Proof:*
    <2>1. The open arc $S_b^1 \setminus \{p_b\}$ is homeomorphic to an open interval, hence contractible to the wedge point $x_0$.
    <2>2. Thus $U \simeq S_a^1$, so $\pi_1(U, x_0) \cong \pi_1(S_a^1) \cong \mathbb{Z} = \langle a \rangle$.
    <2>3. Similarly, $V \simeq S_b^1$, so $\pi_1(V, x_0) \cong \pi_1(S_b^1) \cong \mathbb{Z} = \langle b \rangle$.
    <2>4. The intersection is $U \cap V = (S_a^1 \setminus \{p_a\}) \vee (S_b^1 \setminus \{p_b\})$, which is the union of two open intervals meeting at $x_0$.
    <2>5. Thus $U \cap V$ is contractible ($\pi_1(U \cap V, x_0) = \{e\}$).

<1>3. Application of the Seifert–van Kampen Theorem:
    *Proof:*
    <2>1. Since $U, V$, and $U \cap V$ are open and path-connected containing $x_0$, the Seifert–van Kampen Theorem applies:
        $$\pi_1(X, x_0) \cong \pi_1(U, x_0) *_{\pi_1(U \cap V, x_0)} \pi_1(V, x_0).$$
    <2>2. Because the amalgamated subgroup is trivial ($\pi_1(U \cap V, x_0) = \{e\}$), the amalgamated free product is simply the free product of groups:
        $$\pi_1(S^1 \vee S^1, x_0) \cong \pi_1(U, x_0) * \pi_1(V, x_0) \cong \mathbb{Z} * \mathbb{Z} \cong F_2 = \langle a, b \mid \varnothing \rangle.$$

<1>4. Conclusion:
    $\pi_1(S^1 \vee S^1) \cong \mathbb{Z} * \mathbb{Z} = F_2$. Q.E.D.
:::
