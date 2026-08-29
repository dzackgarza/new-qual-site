---
schema: qual/card@1
id: P-PSAET
kind: problem
title: Orders of $\GL_n(\FF_p)$ and $\SL_n(\FF_p)$
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
  - Finite Fields
  - Determinants
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Determine the orders $|\operatorname{GL}_n(\mathbb{F}_p)|$ and $|\operatorname{SL}_n(\mathbb{F}_p)|$ for any prime $p$ and integer $n \ge 1$.
:::

::: solution
**Goal:** Compute the orders $|\operatorname{GL}_n(\mathbb{F}_p)|$ and $|\operatorname{SL}_n(\mathbb{F}_p)|$.

<1>1. Computation of $|\operatorname{GL}_n(\mathbb{F}_p)|$ by basis counting:
    *Proof:*
    <2>1. An $n \times n$ matrix $A \in M_n(\mathbb{F}_p)$ is in $\operatorname{GL}_n(\mathbb{F}_p)$ if and only if its columns $(v_1, v_2, \dots, v_n)$ form an ordered basis of the vector space $\mathbb{F}_p^n$.
    <2>2. We count the number of ways to choose these columns sequentially such that each is linearly independent of the preceding ones:
        - **Column 1 ($v_1$):** Can be any non-zero vector in $\mathbb{F}_p^n$. Since $|\mathbb{F}_p^n| = p^n$, there are $p^n - 1$ choices.
        - **Column 2 ($v_2$):** Must not lie in $\operatorname{span}_{\mathbb{F}_p}\{v_1\}$, which has size $p^1 = p$. So there are $p^n - p$ choices.
        - **Column 3 ($v_3$):** Must not lie in $\operatorname{span}_{\mathbb{F}_p}\{v_1, v_2\}$, which has size $p^2$. So there are $p^n - p^2$ choices.
        - **Column $k$ ($v_k$):** Must not lie in $\operatorname{span}_{\mathbb{F}_p}\{v_1, \dots, v_{k-1}\}$, which has size $p^{k-1}$. So there are $p^n - p^{k-1}$ choices.
    <2>3. By the multiplication principle:
        $$|\operatorname{GL}_n(\mathbb{F}_p)| = \prod_{k=0}^{n-1} (p^n - p^k) = (p^n - 1)(p^n - p)(p^n - p^2)\cdots(p^n - p^{n-1}).$$
    <2>4. Factoring out powers of $p$:
        $$|\operatorname{GL}_n(\mathbb{F}_p)| = p^{\frac{n(n-1)}{2}} \prod_{i=1}^n (p^i - 1).$$

<1>2. Computation of $|\operatorname{SL}_n(\mathbb{F}_p)|$ via the First Isomorphism Theorem:
    *Proof:*
    <2>1. Consider the determinant map:
        $$\det: \operatorname{GL}_n(\mathbb{F}_p) \to \mathbb{F}_p^\times.$$
    <2>2. **$\det$ is a group homomorphism:** $\det(AB) = \det(A)\det(B)$.
    <2>3. **$\det$ is surjective:** For any $c \in \mathbb{F}_p^\times$, the diagonal matrix $\operatorname{diag}(c, 1, 1, \dots, 1) \in \operatorname{GL}_n(\mathbb{F}_p)$ has determinant $c$.
    <2>4. The kernel is by definition the special linear group:
        $$\ker(\det) = \operatorname{SL}_n(\mathbb{F}_p).$$
    <2>5. By the First Isomorphism Theorem for groups:
        $$\operatorname{GL}_n(\mathbb{F}_p) / \operatorname{SL}_n(\mathbb{F}_p) \cong \mathbb{F}_p^\times.$$
    <2>6. Since $|\mathbb{F}_p^\times| = p - 1$, by Lagrange's theorem:
        $$|\operatorname{SL}_n(\mathbb{F}_p)| = \frac{|\operatorname{GL}_n(\mathbb{F}_p)|}{|\mathbb{F}_p^\times|} = \frac{|\operatorname{GL}_n(\mathbb{F}_p)|}{p-1}.$$
    <2>7. Substituting the product formula:
        $$|\operatorname{SL}_n(\mathbb{F}_p)| = \frac{\prod_{k=0}^{n-1} (p^n - p^k)}{p-1} = p^{\frac{n(n-1)}{2}} (p^n - 1)(p^{n-1} - 1)\cdots(p^2 - 1).$$

<1>3. Conclusion:
    $|\operatorname{GL}_n(\mathbb{F}_p)| = \prod_{k=0}^{n-1} (p^n - p^k)$ and $|\operatorname{SL}_n(\mathbb{F}_p)| = \frac{1}{p-1}\prod_{k=0}^{n-1}(p^n - p^k)$. Q.E.D.
:::
