---
schema: qual/card@1
id: P-5AS2X
kind: problem
title: Hungerford 7.1.3
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Matrices
  - Rings
relations: []
review: draft
---

::: problem
Let $R$ be a ring with identity $1_R \ne 0$, and let $M_n(R)$ be the ring of $n \times n$ matrices over $R$ ($n \ge 1$).

(a) Show that the center of the ring $M_n(R)$ consists precisely of scalar matrices of the form $r I_n$ where $r \in Z(R)$ is in the center of $R$.

(b) Show that $Z(M_n(R)) \cong Z(R)$ as rings.
:::

::: solution
**Goal:** Compute the center $Z(M_n(R)) = \{r I_n : r \in Z(R)\}$ in (a), and establish the ring isomorphism $Z(M_n(R)) \cong Z(R)$ in (b).

<1>1. Matrix units and their algebraic relations:
    *Proof:*
    <2>1. For $1 \le i, j \le n$, let $E_{i, j} \in M_n(R)$ denote the elementary matrix unit having $1_R$ in the $(i, j)$ position and $0$ in all other entries.
    <2>2. The product of matrix units satisfies:
    $$(E_{i, j} E_{k, \ell})_{p, q} = \sum_{m=1}^n (E_{i, j})_{p, m} (E_{k, \ell})_{m, q} = \delta_{p, i} \delta_{j, k} \delta_{\ell, q} = \delta_{j, k} (E_{i, \ell})_{p, q}.$$
    Thus $E_{i, j} E_{k, \ell} = \delta_{j, k} E_{i, \ell}$, where $\delta_{j, k}$ is the Kronecker delta.

<1>2. Part (a): Central matrices are scalar matrices.
    *Proof:*
    <2>1. Let $A = (a_{i, j}) \in Z(M_n(R))$.
    <2>2. Then $A$ commutes with every matrix unit: $A E_{i, j} = E_{i, j} A$ for all $1 \le i, j \le n$.
    <2>3. Compute the $(k, \ell)$ entry of $A E_{i, j}$:
    $$(A E_{i, j})_{k, \ell} = \sum_{m=1}^n a_{k, m} (E_{i, j})_{m, \ell} = a_{k, i} \delta_{j, \ell}.$$
    <2>4. Compute the $(k, \ell)$ entry of $E_{i, j} A$:
    $$(E_{i, j} A)_{k, \ell} = \sum_{m=1}^n (E_{i, j})_{k, m} a_{m, \ell} = \delta_{k, i} a_{j, \ell}.$$
    <2>5. Setting $k = i$ and $\ell = j$, we obtain $a_{i, i} = a_{j, j}$. Since this holds for all $i, j \in \{1, \dots, n\}$, all diagonal entries of $A$ are equal to some common element $r \in R$:
    $$a_{1, 1} = a_{2, 2} = \cdots = a_{n, n} = r.$$
    <2>6. Setting $k \ne i$ and $\ell = j$, the equality becomes $a_{k, i} = 0$. Since $k \ne i$ was arbitrary, all off-diagonal entries of $A$ are zero.
    <2>7. Thus $A = r I_n$ is a scalar matrix.

<1>3. Part (a): The scalar $r$ belongs to $Z(R)$.
    *Proof:*
    <2>1. For any element $s \in R$, consider the scalar matrix $s I_n \in M_n(R)$.
    <2>2. Since $A = r I_n \in Z(M_n(R))$, $A$ commutes with $s I_n$:
    $$(r s) I_n = (r I_n)(s I_n) = (s I_n)(r I_n) = (s r) I_n.$$
    <2>3. Comparing the $(1, 1)$ entry yields $r s = s r$ for all $s \in R$.
    <2>4. Thus $r \in Z(R)$.
    <2>5. Conversely, if $r \in Z(R)$, then for any matrix $B = (b_{i, j}) \in M_n(R)$:
    $$(r I_n B)_{i, j} = r b_{i, j} = b_{i, j} r = (B (r I_n))_{i, j},$$
    so $r I_n \in Z(M_n(R))$.
    <2>6. Therefore $Z(M_n(R)) = \{r I_n : r \in Z(R)\}$.

<1>4. Part (b): Ring isomorphism $Z(M_n(R)) \cong Z(R)$.
    *Proof:*
    <2>1. Define the map $\Phi: Z(R) \to Z(M_n(R))$ by $\Phi(r) = r I_n$.
    <2>2. Ring homomorphism: For all $r_1, r_2 \in Z(R)$:
    $$\Phi(r_1 + r_2) = (r_1 + r_2) I_n = r_1 I_n + r_2 I_n = \Phi(r_1) + \Phi(r_2),$$
    $$\Phi(r_1 r_2) = (r_1 r_2) I_n = (r_1 I_n)(r_2 I_n) = \Phi(r_1) \Phi(r_2),$$
    $$\Phi(1_R) = 1_R I_n = I_n.$$
    <2>3. Injectivity: If $\Phi(r) = 0$, then $r I_n = 0$, so $r = 0$. Thus $\ker \Phi = \{0\}$.
    <2>4. Surjectivity: By Part (a), every matrix in $Z(M_n(R))$ is of the form $r I_n = \Phi(r)$ for some $r \in Z(R)$.
    <2>5. Therefore $\Phi$ is a ring isomorphism, so $Z(M_n(R)) \cong Z(R)$.

<1>5. Conclusion:
    *Proof:*
    The center of $M_n(R)$ consists of central scalar matrices and is ring-isomorphic to $Z(R)$.
:::
