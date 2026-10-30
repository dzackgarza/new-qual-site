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
$$
X \coloneqq \theset{M \in \Mat(2\times 3, k) \st \rank M \leq 1} \subseteq \AA^6/k
.$$

Show that $X$ is an irreducible variety, and find its dimension.
:::

::: {.solution}
Write a point of $\AA^6$ as the matrix
$$
M=\begin{bmatrix} x & y & z \\ a & b & c \end{bmatrix}.
$$

::: pf

::: {.pf-step #closed}
$X=V(xb-ya,\ yc-zb,\ xc-za)$, so $X$ is closed in $\AA^6$.

::: pf-proof
The rank of a matrix is the largest order of a nonzero minor.
Hence $\rank M\le 1$ exactly when every $2\times 2$ minor of $M$ vanishes, and the $2\times2$ minors of $M$ are the three displayed polynomials.
:::

:::

::: {.pf-step #image}
$X$ is the image of the morphism
$$
\Phi:\AA^2\times\AA^3\to\AA^6,\qquad (u,v)\mapsto u\,v^{T},
$$
where $u\in k^2$ and $v\in k^3$ are columns.

::: pf-proof
Each entry of $u\,v^T$ is a product $u_iv_j$, so $\Phi$ is a morphism.
Every column of $u\,v^T$ is a multiple of $u$, so $\rank u\,v^T\le1$ and $\Phi$ maps into $X$.
Conversely, let $\rank M\le1$.
If $M=0$, then $M=\Phi(0,0)$.
Otherwise the column space of $M$ is spanned by one nonzero vector $u$, so the $j$-th column of $M$ is $v_ju$ for some $v_j\in k$, and $M=\Phi(u,v)$ with $v=(v_1,v_2,v_3)^T$.
:::

:::

::: {.pf-step #irreducible}
$X$ is an irreducible variety.

::: pf-proof
The space $\AA^2\times\AA^3=\AA^5$ is irreducible because $k[t_1,\dots,t_5]$ is a domain.
A morphism is continuous in the Zariski topology, and the continuous image of an irreducible space is irreducible.
By step [](#image){.pf-ref}, $X=\Phi(\AA^5)$ is irreducible, and by step [](#closed){.pf-ref} it is closed in $\AA^6$.
:::

:::

::: {.pf-step #chart}
The open subset $X_x\coloneqq X\cap D(x)$ of $X$ is isomorphic to the open subset $D(x)$ of $\AA^4$ with coordinates $x,y,z,a$.

::: pf-proof
Let $\pi:X_x\to D(x)\subseteq\AA^4$ forget $b$ and $c$, and define
$$
\sigma:D(x)\to\AA^6,\qquad (x,y,z,a)\mapsto \qty{x,y,z,a,\tfrac{ay}{x},\tfrac{az}{x}},
$$
which is a morphism because $x$ is invertible on $D(x)$.
The point $\sigma(x,y,z,a)$ lies in $X$: its minors are $x\cdot\frac{ay}{x}-ya=0$, $y\cdot\frac{az}{x}-z\cdot\frac{ay}{x}=0$ and $x\cdot\frac{az}{x}-za=0$.
So $\sigma$ maps into $X_x$, and $\pi\circ\sigma=\id$.
On $X_x$ the equations $xb=ya$ and $xc=za$ give $b=ay/x$ and $c=az/x$, so $\sigma\circ\pi=\id$.
:::

:::

::: pf-step
$\dim X=\boxed{4}$.

::: pf-proof
The set $X_x$ is nonempty, since it contains the matrix with $x=1$ and all other entries $0$.
A nonempty open subset of an irreducible variety has the same dimension as the variety.
By step [](#irreducible){.pf-ref}, $X$ is irreducible, so $\dim X=\dim X_x$.
By step [](#chart){.pf-ref}, $X_x\cong D(x)$, a nonempty open subset of the irreducible variety $\AA^4$, so $\dim X_x=\dim\AA^4=4$.
:::

:::

:::
:::
