---
schema: qual/card@1
id: P-N27XI
kind: problem
title: $Z(R)\cong Z(M_n(R))$ via $r\mapsto rI_n$
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Matrices
  - Isomorphism Theorems
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $R$ be a ring with identity $1 \ne 0$, and let $M_n(R)$ be the ring of $n \times n$ matrices over $R$ ($n \ge 1$).
Prove that the center of the matrix ring $M_n(R)$ consists precisely of scalar matrices $r I_n$ where $r \in Z(R)$, and hence:
$$Z(M_n(R)) \cong Z(R) \quad \text{via the ring isomorphism } r \mapsto r I_n.$$
:::

::: solution
**Goal:** Prove that $Z(M_n(R)) = \{r I_n \mid r \in Z(R)\}$ and that $\phi: Z(R) \xrightarrow{\sim} Z(M_n(R))$ given by $\phi(r) = r I_n$ is a ring isomorphism.

<1>1. Setting and Standard Matrix Units:
    *Proof:*
    <2>1. Let $E_{i, j} \in M_n(R)$ denote the elementary matrix unit with $1$ in the $(i, j)$-entry and $0$ elsewhere.
    <2>2. The standard multiplication rule for matrix units is:
        $$E_{i, j} E_{k, l} = \delta_{j, k} E_{i, l} = \begin{cases} E_{i, l} & \text{if } j = k, \\ 0 & \text{if } j \ne k. \end{cases}$$
    <2>3. Let $A = (a_{i, j}) \in Z(M_n(R))$ be any matrix in the center of $M_n(R)$.
    <2>4. By definition of the center, $A M = M A$ for **all** matrices $M \in M_n(R)$. In particular, $A$ must commute with every elementary matrix unit $E_{i, j}$ ($1 \le i, j \le n$).

<1>2. Proof that $A$ is a Scalar Matrix ($A = r I_n$):
    *Proof:*
    <2>1. Fix distinct indices $i \ne j$.
    <2>2. We compute the $(i, i)$-entry of $A E_{i, j}$ and $E_{i, j} A$:
        - The $(k, l)$-entry of $A E_{i, j}$ is $\sum_m a_{k, m} (E_{i, j})_{m, l} = a_{k, i} \delta_{j, l}$.
          In particular, for $k = i$ and $l = j$, the $(i, j)$-entry of $A E_{i, j}$ is $a_{i, i}$.
        - The $(k, l)$-entry of $E_{i, j} A$ is $\sum_m (E_{i, j})_{k, m} a_{m, l} = \delta_{k, i} a_{j, l}$.
          In particular, for $k = i$ and $l = j$, the $(i, j)$-entry of $E_{i, j} A$ is $a_{j, j}$.
    <2>3. Since $A E_{i, j} = E_{i, j} A$, equating the $(i, j)$-entries gives:
        $$a_{i, i} = a_{j, j} \quad \text{for all } 1 \le i, j \le n.$$
        Thus all diagonal entries are equal to a common element $r \coloneqq a_{1, 1} \in R$.
    <2>4. Now check the $(i, i)$-entry of both products $A E_{i, j}$ and $E_{i, j} A$ for $i \ne j$:
        - The $(i, i)$-entry of $A E_{i, j}$ is $0$ (since $j \ne i$).
        - The $(i, i)$-entry of $E_{i, j} A$ is $a_{j, i}$.
        - Equating them gives $a_{j, i} = 0$ for all $i \ne j$.
    <2>5. Therefore, all off-diagonal entries vanish, and $A = r I_n$ is a scalar matrix.

<1>3. Proof that the Scalar $r \in Z(R)$:
    *Proof:*
    <2>1. For any element $x \in R$, consider the scalar matrix $x I_n \in M_n(R)$ (or the matrix with $x$ in the $(1, 1)$ spot).
    <2>2. Since $A = r I_n \in Z(M_n(R))$, $A (x E_{1, 1}) = (x E_{1, 1}) A$.
    <2>3. This evaluates to $(r x) E_{1, 1} = (x r) E_{1, 1}$, which implies:
        $$r x = x r \quad \text{for all } x \in R.$$
    <2>4. Thus $r \in Z(R)$.

<1>4. Ring Isomorphism:
    *Proof:*
    <2>1. Define $\phi: Z(R) \to Z(M_n(R))$ by $\phi(r) = r I_n$.
    <2>2. **Homomorphism:** $\phi(r + s) = (r + s)I_n = r I_n + s I_n$, $\phi(r s) = (r s) I_n = (r I_n)(s I_n)$, and $\phi(1) = I_n$.
    <2>3. **Injective:** If $\phi(r) = 0$, then $r I_n = 0 \implies r = 0$, so $\ker\phi = \{0\}$.
    <2>4. **Surjective:** By Steps <1>2 and <1>3, every $A \in Z(M_n(R))$ has the form $A = r I_n = \phi(r)$ for some $r \in Z(R)$.
    <2>5. Therefore $\phi$ is a ring isomorphism, and $Z(M_n(R)) \cong Z(R)$.

<1>5. Conclusion:
    The center of $M_n(R)$ consists precisely of scalar matrices $r I_n$ with $r \in Z(R)$, and $Z(M_n(R)) \cong Z(R)$. Q.E.D.
:::
