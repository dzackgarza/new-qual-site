---
schema: qual/card@1
id: P-WUWUT
kind: problem
title: Hungerford 2.1.10
classification:
  areas:
  - algebra
  topics:
  - Abelian Groups
  - Free Modules
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
(a) Show that the additive group of rationals $(\mathbb{Q}, +)$ is not finitely generated.

(b) Show that $(\mathbb{Q}, +)$ is not a free abelian group.

(c) Conclude that the statement "every torsion-free abelian group is free" is false if the hypothesis "finitely generated" is omitted.
:::

::: solution
**Goal:** Prove that $(\mathbb{Q}, +)$ is not finitely generated in (a), not free in (b), and serves as an infinitely generated counterexample to the freeness of torsion-free abelian groups in (c).

<1>1. Part (a): $\mathbb{Q}$ is not finitely generated as an abelian group.
    *Proof:*
    <2>1. Suppose for contradiction that $(\mathbb{Q}, +)$ is finitely generated:
    $$\mathbb{Q} = \left\langle \frac{a_1}{b_1}, \frac{a_2}{b_2}, \dots, \frac{a_k}{b_k} \right\rangle,$$
    where $a_i \in \mathbb{Z}$ and $b_i \in \mathbb{Z}^+$ for each $i \in \{1, \dots, k\}$.
    <2>2. Let $B = \prod_{i=1}^k b_i \in \mathbb{Z}^+$ be the product of all denominators.
    <2>3. Every element $x \in \langle \frac{a_1}{b_1}, \dots, \frac{a_k}{b_k} \rangle$ can be written as an integer linear combination:
    $$x = \sum_{i=1}^k c_i \frac{a_i}{b_i} = \frac{1}{B} \sum_{i=1}^k c_i a_i \left(\prod_{j \ne i} b_j\right) \in \frac{1}{B}\mathbb{Z}.$$
    <2>4. Thus the assumption implies $\mathbb{Q} \subseteq \frac{1}{B}\mathbb{Z}$.
    <2>5. Choose a prime number $p > B$.
    <2>6. The rational number $\frac{1}{p} \in \mathbb{Q}$.
    <2>7. If $\frac{1}{p} \in \frac{1}{B}\mathbb{Z}$, there exists an integer $m \in \mathbb{Z}$ such that $\frac{1}{p} = \frac{m}{B}$, which implies $B = m p$.
    <2>8. This means $p \mid B$, which contradicts $p > B \ge 1$.
    <2>9. Thus $\frac{1}{p} \notin \frac{1}{B}\mathbb{Z}$, so $\mathbb{Q}$ cannot be finitely generated.

<1>2. Part (b): $\mathbb{Q}$ is not a free abelian group.
    *Proof:*
    <2>1. Suppose for contradiction that $(\mathbb{Q}, +)$ is a free abelian group with basis $\mathcal{B} \subset \mathbb{Q}$.
    <2>2. If $|\mathcal{B}| = 1$, then $\mathbb{Q} \cong \mathbb{Z}$, so $\mathbb{Q}$ is cyclic, which contradicts <1>1.
    <2>3. If $|\mathcal{B}| \ge 2$, choose two distinct basis elements $x, y \in \mathcal{B}$.
    <2>4. Write $x = \frac{a}{b}$ and $y = \frac{c}{d}$ with non-zero integers $a, b, c, d \in \mathbb{Z} \setminus \{0\}$.
    <2>5. Consider the non-trivial $\mathbb{Z}$-linear combination:
    $$(b c) x - (a d) y = (b c) \left(\frac{a}{b}\right) - (a d) \left(\frac{c}{d}\right) = a c - a c = 0.$$
    <2>6. Since $a, b, c, d \ne 0$, the integer coefficients $b c \ne 0$ and $-a d \ne 0$ are non-zero.
    <2>7. This non-trivial relation contradicts the linear independence of the basis $\mathcal{B}$ over $\mathbb{Z}$.
    <2>8. Thus $(\mathbb{Q}, +)$ is not a free abelian group.

<1>3. Part (c): Indispensability of the finite generation hypothesis.
    *Proof:*
    <2>1. The group $(\mathbb{Q}, +)$ is torsion-free: for any $n \in \mathbb{Z} \setminus \{0\}$ and $\frac{a}{b} \in \mathbb{Q}$, $n \cdot \frac{a}{b} = \frac{n a}{b} = 0 \implies n a = 0 \implies a = 0 \implies \frac{a}{b} = 0$.
    <2>2. By Part (b), $(\mathbb{Q}, +)$ is not free.
    <2>3. Therefore, "every torsion-free abelian group is free" is false in general, and the hypothesis of finite generation is essential.

<1>4. Conclusion:
    *Proof:*
    $(\mathbb{Q}, +)$ is neither finitely generated nor free, despite being torsion-free.
:::
