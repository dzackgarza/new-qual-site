---
schema: qual/card@1
id: P-TOPF20E
kind: problem
title: "No retraction of S^n x S^n onto the coordinate axes union"
classification:
  areas:
  - topology
  topics:
  - Retracts
  - Cohomology
  - Spheres
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
For $n \geq 1$, take a point $p \in S^n$ and consider the subspace $A = \{(x, y) \in S^n \times S^n \mid x = p \text{ or } y = p\}$ of $S^n \times S^n$.
Show that there does not exist a retraction of $S^n \times S^n$ to $A$.
:::

::: solution
**Goal:** Prove that for $n \ge 1$, there exists no retraction $r: S^n \times S^n \to A$, where $A = (S^n \times \{p\}) \cup (\{p\} \times S^n) \subset S^n \times S^n$.

<1>1. Algebraic properties of a retraction on cohomology rings:
    *Proof:*
    <2>1. Suppose for contradiction that there exists a continuous map $r: S^n \times S^n \to A$ such that $r \circ i = \operatorname{id}_A$, where $i: A \hookrightarrow S^n \times S^n$ is the subspace inclusion.
    <2>2. The induced map on cohomology rings $r^*: H^*(A; \mathbb{Z}) \to H^*(S^n \times S^n; \mathbb{Z})$ is a graded ring homomorphism satisfying
    $$i^* \circ r^* = (r \circ i)^* = (\operatorname{id}_A)^* = \operatorname{id}_{H^*(A; \mathbb{Z})}.$$
    <2>3. In particular, $r^*$ is an injective ring homomorphism, and $r^*(\alpha \smile \beta) = r^*(\alpha) \smile r^*(\beta)$ for all $\alpha, \beta \in H^*(A; \mathbb{Z})$.

<1>2. Cohomology ring structure of the wedge sum $A \cong S^n \vee S^n$:
    *Proof:*
    <2>1. The subspace $A = (S^n \times \{p\}) \cup (\{p\} \times S^n)$ intersects at the single basepoint $(p, p)$, so $A$ is homeomorphic to the wedge sum $S^n \vee S^n$.
    <2>2. The cohomology groups of $A$ are:
    $$H^k(A; \mathbb{Z}) \cong \begin{cases} \mathbb{Z} & k = 0, \\ \mathbb{Z}\alpha \oplus \mathbb{Z}\beta & k = n, \\ 0 & \text{otherwise}, \end{cases}$$
    where $\alpha, \beta \in H^n(A; \mathbb{Z})$ are the generator classes corresponding to the two sphere summands $S^n \times \{p\}$ and $\{p\} \times S^n$.
    <2>3. Because $H^{2n}(A; \mathbb{Z}) = 0$, the cup product of the two degree-$n$ classes vanishes identically:
    $$\alpha \smile \beta = 0 \in H^{2n}(A; \mathbb{Z}).$$

<1>3. Cohomology ring structure of the product $S^n \times S^n$:
    *Proof:*
    <2>1. By the Künneth formula for cohomology rings:
    $$H^*(S^n \times S^n; \mathbb{Z}) \cong H^*(S^n; \mathbb{Z}) \otimes_\mathbb{Z} H^*(S^n; \mathbb{Z}) \cong \frac{\mathbb{Z}[a, b]}{(a^2, b^2, ab - (-1)^n ba)},$$
    where $a = \pi_1^*(\iota_{S^n}) \in H^n(S^n \times S^n; \mathbb{Z})$ and $b = \pi_2^*(\iota_{S^n}) \in H^n(S^n \times S^n; \mathbb{Z})$.
    <2>2. In degree $2n$, the cup product $a \smile b$ generates the top cohomology group:
    $$H^{2n}(S^n \times S^n; \mathbb{Z}) = \mathbb{Z}(a \smile b) \cong \mathbb{Z} \neq 0.$$

<1>4. Identification of the pullback generators:
    *Proof:*
    <2>1. Restricting the product generators $a, b$ to $A$ via $i^*$:
    $$i^*(a) = \alpha, \qquad i^*(b) = \beta.$$
    <2>2. Thus $i^*: H^n(S^n \times S^n; \mathbb{Z}) \to H^n(A; \mathbb{Z})$ is an isomorphism.
    <2>3. Since $i^* \circ r^* = \operatorname{id}_{H^*(A)}$, the unique preimages under $i^*$ satisfy:
    $$r^*(\alpha) = a, \qquad r^*(\beta) = b.$$

<1>5. Contradiction from the ring homomorphism property:
    *Proof:*
    <2>1. Applying the ring homomorphism $r^*$ to the cup product $\alpha \smile \beta$:
    $$r^*(\alpha \smile \beta) = r^*(0) = 0 \in H^{2n}(S^n \times S^n; \mathbb{Z}).$$
    <2>2. On the other hand, since $r^*$ preserves cup products:
    $$r^*(\alpha \smile \beta) = r^*(\alpha) \smile r^*(\beta) = a \smile b \neq 0 \in H^{2n}(S^n \times S^n; \mathbb{Z}).$$
    <2>3. This gives the contradiction $0 = a \smile b \neq 0$.

<1>6. Conclusion:
    *Proof:*
    No continuous retraction $r: S^n \times S^n \to A$ exists for any $n \ge 1$.
:::
