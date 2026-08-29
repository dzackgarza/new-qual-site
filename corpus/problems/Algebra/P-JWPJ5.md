---
schema: qual/card@1
id: P-JWPJ5
kind: problem
title: Number of irreducible representations of $S_n$
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Partitions
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
(1) How many non-isomorphic irreducible complex representations does the symmetric group $S_n$ have?
(2) What classical function in mathematics does this number equal, and how are the irreducible representations explicitly indexed?
:::

::: solution
**Goal:** Prove that the number of irreducible representations of $S_n$ equals the number of integer partitions $p(n)$, and describe their construction via Young diagrams and Specht modules.

<1>1. General Character Theory and Conjugacy Classes:
    *Proof:*
    <2>1. By fundamental character theory of finite groups, the number of distinct isomorphism classes of irreducible complex representations of a finite group $G$ is equal to the **number of conjugacy classes** of $G$:
        $$|\operatorname{Irr}(G)| = |\operatorname{Cl}(G)|.$$

<1>2. Conjugacy Classes in the Symmetric Group $S_n$:
    *Proof:*
    <2>1. Two permutations $\sigma, \tau \in S_n$ are conjugate in $S_n$ ($\tau = \rho \sigma \rho^{-1}$) if and only if they have the same **cycle type**.
    <2>2. The cycle type of a permutation $\sigma \in S_n$ decomposed into disjoint cycles of lengths $\lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_k \ge 1$ forms an **integer partition** of $n$:
        $$\lambda = (\lambda_1, \lambda_2, \dots, \lambda_k) \vdash n, \qquad \sum_{i=1}^k \lambda_i = n.$$
    <2>3. Therefore, the conjugacy classes of $S_n$ are in bijective correspondence with the integer partitions of $n$.

<1>3. Relation to the Integer Partition Function $p(n)$:
    *Proof:*
    <2>1. The number of irreducible representations of $S_n$ is precisely given by Euler's **partition function** $p(n)$:
        $$|\operatorname{Irr}(S_n)| = p(n).$$
    <2>2. The partition function $p(n)$ has the famous generating function (Euler's product formula):
        $$\sum_{n=0}^\infty p(n) q^n = \prod_{k=1}^\infty \frac{1}{1 - q^k} = 1 + q + 2q^2 + 3q^3 + 5q^4 + 7q^5 + 11q^6 + \cdots$$
    <2>3. For example:
        - $S_1$: $p(1) = 1$ irrep.
        - $S_2$: $p(2) = 2$ irreps (Trivial, Sign).
        - $S_3$: $p(3) = 3$ irreps (Trivial, Sign, Standard 2D).
        - $S_4$: $p(4) = 5$ irreps (Trivial, Sign, Standard 3D, Sign $\otimes$ Standard 3D, 2D).
        - $S_5$: $p(5) = 7$ irreps.

<1>4. Young Diagrams and Specht Modules:
    *Proof:*
    <2>1. In the representation theory of $S_n$, each partition $\lambda \vdash n$ corresponds to a **Young diagram** $Y_\lambda$.
    <2>2. The corresponding irreducible representation is the **Specht module** $S^\lambda$.
    <2>3. The dimension of $S^\lambda$ is computed by the **Hook Length Formula**:
        $$\dim(S^\lambda) = \frac{n!}{\prod_{(i, j) \in Y_\lambda} h(i, j)}.$$

<1>5. Conclusion:
    $S_n$ has exactly $p(n)$ irreducible representations (where $p(n)$ is Euler's integer partition function), indexed by Young diagrams/partitions $\lambda \vdash n$. Q.E.D.
:::
