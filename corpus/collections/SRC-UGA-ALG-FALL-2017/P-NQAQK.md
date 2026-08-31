---
schema: qual/card@1
id: P-NQAQK
kind: problem
title: $F[x]$-modules of linear operators, similarity, and simplicity in dimension
  $2$
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Semisimplicity
  - Linear Algebra
relations: []
review: draft
---

::: problem
Let $F$ be a field and let $V$ and $W$ be vector spaces over $F$. Make $V$ and $W$ into $F[x]$-modules via linear operators $T \in \operatorname{End}_F(V)$ and $S \in \operatorname{End}_F(W)$ by defining $x \cdot v = T(v)$ for all $v \in V$ and $x \cdot w = S(w)$ for all $w \in W$. Denote the resulting $F[x]$-modules by $V_T$ and $W_S$ respectively.

(a) Show that an $F[x]$-module homomorphism from $V_T$ to $W_S$ consists of an $F$-linear transformation $R: V \to W$ such that $R T = S R$.

(b) Show that $V_T \cong W_S$ as $F[x]$-modules if and only if there is an $F$-linear isomorphism $P: V \to W$ such that $T = P^{-1} S P$.

(c) Recall that a module $M$ is *simple* (or irreducible) if $M \ne \{0\}$ and its only submodules are $\{0\}$ and $M$. Suppose that $\dim_F V = 2$. Give an example of $F$ and $T$ with $V_T$ simple.

(d) Assume $F$ is algebraically closed. Prove that if $\dim_F V = 2$, then $V_T$ is never simple.
:::

::: solution
**Goal:** Characterize module homomorphisms and isomorphisms for polynomial modules $V_T$, and analyze simplicity via invariant subspaces and eigenvalues.

<1>1. Part (a): $F[x]$-module homomorphisms correspond to intertwining linear maps ($R T = S R$).
::: {.proof}
    <2>1. Forward direction ($\implies$):
        - Let $\varphi: V_T \to W_S$ be an $F[x]$-module homomorphism.
        - Since $F \subset F[x]$, $\varphi(c v) = c \varphi(v)$ for all $c \in F$ and $\varphi(v_1 + v_2) = \varphi(v_1) + \varphi(v_2)$, so $\varphi$ is an $F$-linear transformation $R: V \to W$.
        - Module compatibility on $x$ gives $\varphi(x \cdot v) = x \cdot \varphi(v)$.
        - Since $x \cdot v = T(v)$ and $x \cdot \varphi(v) = S(\varphi(v))$, this means $R(T(v)) = S(R(v))$ for all $v \in V$.
        - Thus $R T = S R$.
    <2>2. Reverse direction ($\impliedby$):
        - Let $R: V \to W$ be an $F$-linear transformation such that $R T = S R$.
        - By induction, $R T^k = S^k R$ for all $k \ge 0$.
        - Let $p(x) = \sum_{k=0}^d a_k x^k \in F[x]$ be any polynomial.
        - For any $v \in V$:
        $$R(p(x) \cdot v) = R\left( \sum_{k=0}^d a_k T^k(v) \right) = \sum_{k=0}^d a_k R(T^k(v)) = \sum_{k=0}^d a_k S^k(R(v)) = p(x) \cdot R(v).$$
        - Together with additivity, $R$ is an $F[x]$-module homomorphism.

:::

<1>2. Part (b): $V_T \cong W_S \iff T = P^{-1} S P$ for an $F$-linear isomorphism $P$.
::: {.proof}
    <2>1. An $F[x]$-module isomorphism is a bijective $F[x]$-module homomorphism.
    <2>2. By Part (a), a map $P: V_T \to W_S$ is an $F[x]$-module homomorphism if and only if $P: V \to W$ is $F$-linear and $P T = S P$.
    <2>3. A map between vector spaces is a bijective module homomorphism if and only if it is an $F$-linear isomorphism whose inverse is also compatible.
    <2>4. If $P$ is invertible, multiplying $P T = S P$ on the left by $P^{-1}$ gives $T = P^{-1} S P$.
    <2>5. Conversely, if $P: V \to W$ is an $F$-linear isomorphism with $T = P^{-1} S P$, then $P T = S P$, so $P$ is an $F[x]$-module isomorphism.

:::

<1>3. Part (c): Example of a simple $V_T$ of dimension 2 over $\mathbb{R}$.
::: {.proof}
    <2>1. Let $F = \mathbb{R}$, $V = \mathbb{R}^2$, and let $T: \mathbb{R}^2 \to \mathbb{R}^2$ be given by the matrix
    $$T = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}.$$
    <2>2. Submodules of $V_T$ are precisely the $T$-invariant $\mathbb{R}$-subspaces of $\mathbb{R}^2$.
    <2>3. If $V_T$ had a proper non-trivial submodule $U$, then $\dim_{\mathbb{R}} U = 1$.
    <2>4. A 1-dimensional $T$-invariant subspace is spanned by an eigenvector of $T$.
    <2>5. The characteristic polynomial of $T$ is
    $$\chi_T(x) = \det(x I - T) = \det \begin{pmatrix} x & 1 \\ -1 & x \end{pmatrix} = x^2 + 1.$$
    <2>6. Since $x^2 + 1$ has no real roots, $T$ has no real eigenvalues, and therefore no 1-dimensional $T$-invariant subspaces.
    <2>7. Thus the only $T$-invariant subspaces of $\mathbb{R}^2$ are $\{0\}$ and $\mathbb{R}^2$, so $V_T$ is simple.

:::

<1>4. Part (d): Over an algebraically closed field $F$, $V_T$ is never simple when $\dim_F V = 2$.
::: {.proof}
    <2>1. Let $F$ be algebraically closed and $\dim_F V = 2$.
    <2>2. The characteristic polynomial $\chi_T(x) = \det(x I - T) \in F[x]$ has degree 2.
    <2>3. Because $F$ is algebraically closed, $\chi_T(x)$ has at least one root $\lambda \in F$.
    <2>4. The root $\lambda$ is an eigenvalue of $T$, so there exists a non-zero eigenvector $v \in V \setminus \{0\}$ such that $T(v) = \lambda v$.
    <2>5. Define the 1-dimensional subspace $U = \operatorname{span}_F(v) \subset V$.
    <2>6. For any $u = c v \in U$ ($c \in F$), $T(u) = c T(v) = c \lambda v = (\lambda c) v \in U$.
    <2>7. Thus $U$ is a $T$-invariant subspace, hence an $F[x]$-submodule of $V_T$.
    <2>8. Since $\dim_F U = 1$ and $\dim_F V = 2$, $\{0\} \subsetneq U \subsetneq V_T$, so $U$ is a proper non-trivial submodule.
    <2>9. Therefore $V_T$ is not simple.

:::

<1>5. Conclusion:
::: {.proof}
    $F[x]$-homomorphisms intertwine operators, isomorphisms correspond to similarity, $90^\circ$ rotation on $\mathbb{R}^2$ gives a simple module, and over algebraically closed fields existence of eigenvalues prevents simplicity in dimension 2.
:::
:::
