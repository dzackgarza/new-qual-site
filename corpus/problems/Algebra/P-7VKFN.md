---
schema: qual/card@1
id: P-7VKFN
kind: problem
title: The quaternion group and the number of elements of each order
classification:
  areas:
  - algebra
  topics:
  - Groups
  - Group Presentations
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
What is the quaternion group $Q_8$? Give its presentation and list the number of elements of each order.
:::

::: solution
**Goal:** Define the quaternion group $Q_8$ and count its elements by order.

<1>1. Definition and Presentation:
    *Proof:*
    <2>1. The **quaternion group** $Q_8$ is a non-abelian group of order 8, defined by the presentation:
        $$Q_8 = \langle -1, i, j, k \mid (-1)^2 = 1, \, i^2 = j^2 = k^2 = ijk = -1 \rangle.$$
    <2>2. As a set, $Q_8 = \{1, -1, i, -i, j, -j, k, -k\}$.
    <2>3. Multiplication rules:
        - $(-1) x = x (-1) = -x$ for all $x \in Q_8$.
        - $i j = k = -ji$, \quad $j k = i = -kj$, \quad $k i = j = -ik$.
    <2>4. Matrix representation: $Q_8$ can be embedded into $\operatorname{SU}(2) \subset \operatorname{GL}_2(\mathbb{C})$ via Pauli matrices:
        $$1 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \quad -1 = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}, \quad i = \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix}, \quad j = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}, \quad k = \begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix}.$$

<1>2. Number of elements of each order:
    *Proof:*
    <2>1. By Lagrange's Theorem, the order of any element $g \in Q_8$ must divide $|Q_8| = 8$, so $\operatorname{ord}(g) \in \{1, 2, 4, 8\}$.
    <2>2. **Order 1:** Exactly 1 element: the identity $1$.
    <2>3. **Order 2:** Exactly 1 element: $-1$ (since $(-1)^2 = 1$ and $-1 \ne 1$).
        *(Note: every other non-identity element squares to $-1 \ne 1$, so there are no other elements of order 2)*.
    <2>4. **Order 4:** Exactly 6 elements: $\{\pm i, \pm j, \pm k\}$.
        - $(\pm i)^2 = -1 \implies (\pm i)^4 = (-1)^2 = 1$, so $\operatorname{ord}(\pm i) = 4$.
        - $(\pm j)^2 = -1 \implies (\pm j)^4 = (-1)^2 = 1$, so $\operatorname{ord}(\pm j) = 4$.
        - $(\pm k)^2 = -1 \implies (\pm k)^4 = (-1)^2 = 1$, so $\operatorname{ord}(\pm k) = 4$.
    <2>5. **Order 8:** 0 elements (since $Q_8$ is not cyclic, $\exp(Q_8) = 4$).

<1>3. Summary Table:
    $$\begin{array}{|c|c|c|}
    \hline
    \text{Order } d & \text{Number of elements} & \text{Elements} \\
    \hline
    1 & 1 & \{1\} \\
    2 & 1 & \{-1\} \\
    4 & 6 & \{i, -i, j, -j, k, -k\} \\
    \hline
    \text{Total} & 8 & Q_8 \\
    \hline
    \end{array}$$

<1>4. Distinctive Property (Comparison with $D_4$):
    *Proof:*
    <2>1. $Q_8$ is the unique group of order 8 with a unique involution (single element of order 2).
    <2>2. In contrast, the dihedral group $D_4$ of order 8 has 5 elements of order 2 and 2 elements of order 4.
    <2>3. Every subgroup of $Q_8$ is normal: the subgroups are $\{1\}$, $\langle -1 \rangle \cong \mathbb{Z}_2$, $\langle i \rangle \cong \mathbb{Z}_4$, $\langle j \rangle \cong \mathbb{Z}_4$, $\langle k \rangle \cong \mathbb{Z}_4$, and $Q_8$ (a Hamiltonian group).

<1>5. Conclusion:
    $Q_8$ has 1 element of order 1, 1 element of order 2, and 6 elements of order 4. Q.E.D.
:::
