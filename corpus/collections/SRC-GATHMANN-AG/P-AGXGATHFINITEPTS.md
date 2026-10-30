---
schema: qual/card@1
id: P-AGXGATHFINITEPTS
kind: problem
title: Finite point sets in $\AA^n$ as the zero locus of $n$ polynomials
classification:
  areas:
  - algebraic-geometry
  topics:
  - Affine Varieties
  - Lagrange Interpolation
  - Zero Loci
relations: []
review: draft
---

::: {.problem}
Prove that every affine variety $X\subset \AA^n/k$ consisting of only finitely many points can be written as the zero locus of $n$ polynomials.

> Hint: use interpolation.
> It is useful to assume at first that all points in $X$ have different $x_1\dash$coordinates.
:::

::: {.solution}
Let $k$ be the ground field, which is algebraically closed and in particular infinite. Let $X=\theset{\mathbf{p}_1,\dots,\mathbf{p}_d}$ with the $\mathbf{p}_j$ distinct and $\mathbf{p}_j=(p_j^1,\dots,p_j^n)$. If $d=0$, then $X=V(1)$, a zero locus of $n$ copies of the constant $1$; so assume $d\geq1$.

::: pf

::: {.pf-step #reduction}
It suffices to treat the case where $p_1^1,\dots,p_d^1$ are pairwise distinct.

::: pf-proof

::: {.pf-step #coord-change}
If $\phi\colon\AA^n\to\AA^n$ is an invertible linear map and $\phi(X)=V(g_1,\dots,g_n)$, then $X=V(g_1\circ\phi,\dots,g_n\circ\phi)$ is a zero locus of $n$ polynomials.

::: pf-proof
A point $\mathbf{q}$ satisfies $g_k(\phi(\mathbf{q}))=0$ for all $k$ exactly when $\phi(\mathbf{q})\in\phi(X)$, that is, when $\mathbf{q}\in X$, since $\phi$ is bijective. Each $g_k\circ\phi$ is a polynomial because $\phi$ is linear.
:::

:::

::: {.pf-step #distinct-first}
There is such a $\phi$ for which the first coordinates of the points $\phi(\mathbf{p}_j)$ are pairwise distinct.

::: pf-proof
For $j\neq l$, the vector $\mathbf{p}_j-\mathbf{p}_l$ is nonzero, so $H_{jl}\coloneqq\theset{\lambda\in k^n\st \lambda\cdot(\mathbf{p}_j-\mathbf{p}_l)=0}$ is a proper linear subspace of $k^n$. Over the infinite field $k$, a finite union of proper subspaces is not all of $k^n$, so there is $\lambda\notin\Union_{j\neq l}H_{jl}$; in particular $\lambda\neq0$. Extend $\lambda$ to a basis $\lambda,\mu_2,\dots,\mu_n$ of $k^n$ and put $\phi(\mathbf{v})\coloneqq(\lambda\cdot\mathbf{v},\mu_2\cdot\mathbf{v},\dots,\mu_n\cdot\mathbf{v})$, which is invertible. The first coordinates $\lambda\cdot\mathbf{p}_j$ are pairwise distinct by the choice of $\lambda$.
:::

:::

::: pf-qed
Apply the distinct case to $\phi(X)$ with $\phi$ from step [](#distinct-first){.pf-ref}, and transport the result back by step [](#coord-change){.pf-ref}.
:::

:::

:::

::: {.pf-step}
If $p_1^1,\dots,p_d^1$ are pairwise distinct, then $X=V(f_1,\dots,f_n)$, where
$$
f_1\coloneqq\prod_{j=1}^d(x_1-p_j^1),
\qquad
f_k\coloneqq \tilde f_k(x_1)-x_k\quad(2\leq k\leq n),
$$
and $\tilde f_k\in k[t]$ is the Lagrange interpolating polynomial
$$
\tilde f_k(t)\coloneqq\sum_{j=1}^d p_j^k\prod_{\substack{1\leq m\leq d\\ m\neq j}}\frac{t-p_m^1}{p_j^1-p_m^1}
.$$

::: pf-proof

::: {.pf-step #interp}
Each $\tilde f_k$ is a polynomial of degree at most $d-1$ with $\tilde f_k(p_l^1)=p_l^k$ for all $l$.

::: pf-proof
The denominators are nonzero because the $p_m^1$ are distinct, and each product has $d-1$ linear factors. At $t=p_l^1$, every product with $j\neq l$ contains the factor $t-p_l^1=0$, and the product with $j=l$ equals $1$, so $\tilde f_k(p_l^1)=p_l^k$.
:::

:::

::: {.pf-step #forward}
$X\subseteq V(f_1,\dots,f_n)$.

::: pf-proof
At $\mathbf{p}_l$, the product $f_1(\mathbf{p}_l)$ contains the factor $p_l^1-p_l^1=0$, and $f_k(\mathbf{p}_l)=\tilde f_k(p_l^1)-p_l^k=0$ by step [](#interp){.pf-ref}.
:::

:::

::: {.pf-step #backward}
$V(f_1,\dots,f_n)\subseteq X$.

::: pf-proof
Let $\mathbf{q}=(q^1,\dots,q^n)\in V(f_1,\dots,f_n)$. From $f_1(\mathbf{q})=0$, some factor vanishes, so $q^1=p_j^1$ for some $j$. For $2\leq k\leq n$, $f_k(\mathbf{q})=0$ gives $q^k=\tilde f_k(q^1)=\tilde f_k(p_j^1)=p_j^k$ by step [](#interp){.pf-ref}. Hence $\mathbf{q}=\mathbf{p}_j\in X$.
:::

:::

:::

:::

:::
:::
