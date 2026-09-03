---
schema: qual/card@1
id: E-HAT-1.3-20
kind: problem
title: "Nonnormal covering spaces of the Klein bottle"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: exercise
Construct nonnormal covering spaces of the Klein bottle by a Klein bottle and by a torus.
:::

::: solution
**Goal:** Construct explicit non-normal covering spaces of the Klein bottle $K$ whose total spaces are a Klein bottle and a torus, by finding corresponding non-normal subgroups of $\pi_1(K)$.

<1>1. Presentation and algebraic structure of $\pi_1(K)$:
    *Proof:*
    <2>1. The fundamental group of the Klein bottle has the presentation
    $$\pi_1(K) = \langle a, b \mid a b a^{-1} = b^{-1} \rangle.$$
    <2>2. Every element $g \in \pi_1(K)$ can be written uniquely in normal form as $g = a^m b^n$ for $m, n \in \mathbb{Z}$.
    <2>3. Group multiplication follows the semidirect product rule $(a^m b^n)(a^p b^q) = a^{m+p} b^{(-1)^p n + q}$.
    <2>4. Conjugation of generators:
    $$b a b^{-1} = a (a^{-1} b a) b^{-1} = a b b^{-1} = a b^{-2} \quad \text{and} \quad a b a^{-1} = b^{-1}.$$

<1>2. Non-normal covering of $K$ by a Klein bottle:
    *Proof:*
    <2>1. Define the subgroup $H_K = \langle a, b^3 \rangle \le \pi_1(K)$.
    <2>2. The elements of $H_K$ are precisely $\{a^m b^{3n} : m, n \in \mathbb{Z}\}$.
    <2>3. The generators satisfy $a (b^3) a^{-1} = (a b a^{-1})^3 = (b^{-1})^3 = (b^3)^{-1}$, so
    $$H_K \cong \langle a, b^3 \mid a (b^3) a^{-1} = (b^3)^{-1} \rangle \cong \pi_1(K).$$
    <2>4. Since $H_K \cong \pi_1(K)$, the corresponding connected covering space $\widetilde{K}$ has $\pi_1(\widetilde{K}) \cong \pi_1(K)$, so $\widetilde{K}$ is a Klein bottle.
    <2>5. The index is $[\pi_1(K) : H_K] = 3$, so $\widetilde{K} \to K$ is a 3-sheeted covering.
    <2>6. Non-normality check: Conjugate the generator $a \in H_K$ by $b \in \pi_1(K)$:
    $$b a b^{-1} = a b^{-2}.$$
    <2>7. The element $a b^{-2}$ has $b$-exponent $-2$. Since $-2 \not\equiv 0 \pmod 3$, $a b^{-2} \notin H_K$.
    <2>8. Thus $b H_K b^{-1} \neq H_K$, so $H_K$ is not a normal subgroup of $\pi_1(K)$, and the 3-sheeted Klein bottle cover is non-normal.

<1>3. Non-normal covering of $K$ by a torus:
    *Proof:*
    <2>1. Define the subgroup $H_T = \langle a^2 b, b^3 \rangle \le \pi_1(K)$.
    <2>2. The generators commute:
    $$(a^2 b) b^3 (a^2 b)^{-1} = a^2 b^4 b^{-1} a^{-2} = a^2 b^3 a^{-2} = (a^2 b a^{-2})^3 = (b^{(-1)^2})^3 = b^3.$$
    <2>3. Thus $H_T \cong \mathbb{Z}^2$, so the covering space $\widetilde{T}$ is a closed, connected, orientable surface with $\pi_1(\widetilde{T}) \cong \mathbb{Z}^2$, which is the torus $T^2$.
    <2>4. The elements of $H_T$ are precisely $\{(a^2 b)^m (b^3)^n = a^{2m} b^{m + 3n} : m, n \in \mathbb{Z}\}$.
    <2>5. The index is $[\pi_1(K) : H_T] = 6$, so $\widetilde{T} \to K$ is a 6-sheeted covering.
    <2>6. Non-normality check: Conjugate the generator $a^2 b \in H_T$ by $a \in \pi_1(K)$:
    $$a (a^2 b) a^{-1} = a^2 (a b a^{-1}) = a^2 b^{-1}.$$
    <2>7. In the form $a^{2m} b^{m + 3n}$, the element $a^2 b^{-1}$ requires $m = 1$ and $1 + 3n = -1 \implies 3n = -2$, which has no integer solution $n \in \mathbb{Z}$.
    <2>8. Thus $a (a^2 b) a^{-1} = a^2 b^{-1} \notin H_T$, so $a H_T a^{-1} \neq H_T$.
    <2>9. Therefore $H_T$ is not a normal subgroup of $\pi_1(K)$, and the 6-sheeted torus cover is non-normal.

<1>4. Conclusion:
    *Proof:*
    The subgroup $H_K = \langle a, b^3 \rangle$ gives a 3-sheeted non-normal Klein bottle covering space, and $H_T = \langle a^2 b, b^3 \rangle$ gives a 6-sheeted non-normal torus covering space.
:::
