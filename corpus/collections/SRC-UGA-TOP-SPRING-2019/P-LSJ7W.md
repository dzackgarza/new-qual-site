---
schema: qual/card@1
id: P-LSJ7W
kind: problem
title: Homeomorphism of $T^2$ induced by $SL(2, \mathbb{Z})$ and $H_1$ of the mapping torus $T_A^3$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Quotient Spaces
  - Manifolds
relations: []
review: draft
---

::: problem
(a) Consider the 2-torus as the quotient space
$$
T^2 = \mathbb{R}^2 / \sim \quad \text{where } (x, y) \sim (x + m, y + n) \text{ for } m, n \in \mathbb{Z},
$$
and let $A \in \operatorname{SL}(2, \mathbb{Z})$ be a $2 \times 2$ matrix with integer entries such that $\det A = 1$.
Prove that the linear action of $A$ on $\mathbb{R}^2$ descends to induce a well-defined homeomorphism $\bar{f}_A: T^2 \to T^2$.

(b) Using this homeomorphism $\bar{f}_A$, define the mapping torus
$$
T_A^3 = (T^2 \times \mathbb{R}) / \sim \quad \text{where } (p, t) \sim (\bar{f}_A(p), t + 1).
$$
Compute $H_1(T_A^3; \mathbb{Z})$ for $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.
:::

::: solution
**Goal:** Prove well-definedness and invertibility of the induced map $\bar{f}_A$ in (a), and compute $H_1(T_A^3; \mathbb{Z})$ using the Mayer–Vietoris sequence (and fundamental group abelianization) for the mapping torus in (b).

<1>1. Part (a): Well-definedness and continuity of $\bar{f}_A$.
    *Proof:*
    <2>1. Let $q: \mathbb{R}^2 \to T^2 = \mathbb{R}^2/\mathbb{Z}^2$ be the canonical quotient projection.
    <2>2. Define the linear map $f_A: \mathbb{R}^2 \to \mathbb{R}^2$ by $f_A(v) = A v$. Because $f_A$ is linear, it is continuous.
    <2>3. Let $v, v' \in \mathbb{R}^2$ be equivalent, so $v' = v + w$ for some $w \in \mathbb{Z}^2$.
    <2>4. Compute the image:
    $$f_A(v') = A(v + w) = A v + A w.$$
    <2>5. Since $A \in \operatorname{SL}(2, \mathbb{Z})$, all entries of $A$ are integers, so $A w \in \mathbb{Z}^2$ whenever $w \in \mathbb{Z}^2$.
    <2>6. Thus $q(f_A(v')) = q(A v + A w) = q(A v) = q(f_A(v))$.
    <2>7. By the universal property of quotient spaces, $f_A$ descends to a unique continuous map $\bar{f}_A: T^2 \to T^2$ satisfying $\bar{f}_A(q(v)) = q(A v)$.

<1>2. Part (a): $\bar{f}_A$ is a homeomorphism.
    *Proof:*
    <2>1. Since $\det A = 1$, the matrix $A$ is invertible in $M_{2 \times 2}(\mathbb{Z})$.
    <2>2. By Cramer's rule, $A^{-1} = \frac{1}{\det A} \operatorname{adj}(A) = \operatorname{adj}(A)$ has integer entries and $\det(A^{-1}) = 1$, so $A^{-1} \in \operatorname{SL}(2, \mathbb{Z})$.
    <2>3. By <1>1, $A^{-1}$ descends to a continuous map $\bar{f}_{A^{-1}}: T^2 \to T^2$.
    <2>4. For every $[v] \in T^2$:
    $$\bar{f}_{A^{-1}}(\bar{f}_A([v])) = [A^{-1} A v] = [v], \quad \bar{f}_A(\bar{f}_{A^{-1}}([v])) = [A A^{-1} v] = [v].$$
    <2>5. Thus $\bar{f}_A$ is bijective with continuous inverse $(\bar{f}_A)^{-1} = \bar{f}_{A^{-1}}$, so $\bar{f}_A$ is a homeomorphism.

<1>3. Part (b): Mayer–Vietoris sequence of the mapping torus.
    *Proof:*
    <2>1. The space $T_A^3$ is the mapping torus of the homeomorphism $\bar{f}_A: T^2 \to T^2$.
    <2>2. The Mayer–Vietoris sequence for the mapping torus of a space $X$ yields:
    $$\cdots \to H_1(X) \xrightarrow{I - A_*} H_1(X) \xrightarrow{i_*} H_1(T_A^3) \xrightarrow{\partial_*} H_0(X) \xrightarrow{I - A_*} H_0(X) \to 0.$$
    <2>3. For $X = T^2$:
        - $H_0(T^2) \cong \mathbb{Z}$, and $A_* = \operatorname{id}_{\mathbb{Z}}$ on $H_0$, so $I - A_* = 0$ on $H_0(T^2)$.
        - $H_1(T^2) \cong \mathbb{Z}^2$, with canonical basis corresponding to the fundamental circles of $\mathbb{R}^2/\mathbb{Z}^2$.
    <2>4. The exact sequence reduces to:
    $$0 \to \operatorname{coker}(I - A_*) \to H_1(T_A^3) \to \ker(I - A_*|_{H_0}) \to 0.$$
    <2>5. Since $\ker(I - A_*|_{H_0}) = H_0(T^2) \cong \mathbb{Z}$ is a free abelian group, the short exact sequence splits:
    $$H_1(T_A^3) \cong \operatorname{coker}(I - A_*) \oplus \mathbb{Z}.$$

<1>4. Part (b): Computation of $\operatorname{coker}(I - A_*)$ and $H_1(T_A^3)$.
    *Proof:*
    <2>1. The action on $H_1(T^2) \cong \mathbb{Z}^2$ is given by multiplication by $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.
    <2>2. Compute the matrix $I - A$:
    $$I - A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} - \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 0 & 0 \end{pmatrix}.$$
    <2>3. The image of $I - A: \mathbb{Z}^2 \to \mathbb{Z}^2$ is:
    $$\operatorname{Im}(I - A) = \left\{ \begin{pmatrix} 0 & -1 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} u \\ v \end{pmatrix} \;\middle|\; u, v \in \mathbb{Z} \right\} = \left\{ \begin{pmatrix} -v \\ 0 \end{pmatrix} \;\middle|\; v \in \mathbb{Z} \right\} = \mathbb{Z} \begin{pmatrix} 1 \\ 0 \end{pmatrix} \oplus \{0\}.$$
    <2>4. The cokernel is the quotient:
    $$\operatorname{coker}(I - A_*) = \mathbb{Z}^2 / (\mathbb{Z} \oplus 0) \cong \mathbb{Z}.$$
    <2>5. Combining with the split exact sequence from <1>3:
    $$H_1(T_A^3; \mathbb{Z}) \cong \mathbb{Z} \oplus \mathbb{Z} = \mathbb{Z}^2.$$

<1>5. Conclusion:
    *Proof:*
    $A \in \operatorname{SL}(2, \mathbb{Z})$ descends to a homeomorphism of $T^2$, and $H_1(T_A^3; \mathbb{Z}) \cong \mathbb{Z}^2$.
:::
