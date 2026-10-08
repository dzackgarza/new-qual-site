---
schema: qual/card@1
id: P-AGXGATHRANKONE
kind: problem
title: The variety of $2\times 3$ matrices of rank at most one
classification:
  areas:
  - algebraic-geometry
  topics:
  - Determinantal Varieties
  - Irreducibility
  - Dimension
relations: []
review: draft
---

::: {.problem}
Define
\[
X \da \ts{M \in \mat(2\times 3, k) \st \rk M \leq 1} \subseteq \AA^6/k
.\]

Show that $X$ is an irreducible variety, and find its dimension.
:::

::: {.solution}
Write a matrix as
\[
M=\begin{pmatrix}x&y&z\\a&b&c\end{pmatrix},
\]
and assume $k$ is a field. For $1\leq i\leq2$ and $1\leq j\leq3$, denote the matrix entry by $m_{ij}$ and put $U_{ij}=X\cap D(m_{ij})$.

<1>1. The locus $X$ is closed in $\mathbb A_k^6$.

::: {.proof}
A matrix of size $2\times3$ has rank at most one precisely when each of its three minors of size two vanishes. Therefore
\[
X=V(xb-ya,\;xc-za,\;yc-zb).
\]
The minors are polynomial functions on $\mathbb A_k^6$, so their common zero locus is closed.
:::

<1>2. The variety $X$ is irreducible.

::: {.proof}
Consider the morphism
\[
\mu:\mathbb A_k^2\times\mathbb A_k^3\longrightarrow X,
\qquad
(u,v)\longmapsto uv^{T},
\]
where $u$ is a column vector and $v$ a column vector of lengths two and three, respectively. Every matrix of rank at most one is an outer product: a nonzero rank-one matrix is a nonzero column times its row of coefficients, and the zero matrix is obtained when $u=0$. Thus $\mu$ is surjective on geometric points. After any extension to an algebraic closure the same factorization holds, so the image is dense in $X$. Since the affine space $\mathbb A_k^5$ is irreducible, its continuous image has irreducible closure. Therefore $X$ is irreducible.
:::

<1>3. Each $U_{ij}$ is isomorphic to $\mathbb G_{m,k}\times\mathbb A_k^3$.

::: {.proof}
It suffices, by permuting rows and columns, to treat $U_{11}$, on which $x\neq0$. The equations in step <1>1 imply
\[
b=\frac{ay}{x},\qquad c=\frac{az}{x}.
\]
Conversely, these formulas make all three minors vanish. Hence the morphisms
\[
(x,y,z,a)\longmapsto
\begin{pmatrix}x&y&z\\a&ay/x&az/x\end{pmatrix}
\quad\text{and}\quad
M\longmapsto(x,y,z,a)
\]
are mutually inverse between $\mathbb G_{m,k}\times\mathbb A_k^3$ and $U_{11}$. They are regular because $x$ is invertible on these loci. Permuting entries proves the claim for every $U_{ij}$.
:::

<1>4. The dimension of $X$ is
\[
\boxed{\dim X=4}.
\]

::: {.proof}
By step <1>3, the nonempty open set $U_{11}$ is isomorphic to $\operatorname{Spec}k[x,x^{-1},y,z,a]$, whose dimension is four. By step <1>2, $X$ is an irreducible variety of finite type over $k$. Every nonempty open subset of an irreducible finite-type variety over a field has the same dimension as the variety. Thus $\dim X=\dim U_{11}=4$.
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>2 and <1>4 establish irreducibility and dimension four, respectively.
:::
:::
